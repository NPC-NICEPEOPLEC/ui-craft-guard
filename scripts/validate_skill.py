#!/usr/bin/env python3
"""Check portable Agent Skills packaging and required documentation."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/ui-craft-guard/SKILL.md"
REQUIRED = [
    "README.md", "LICENSE", "CHANGELOG.md", ".github/workflows/ci.yml",
    "skills/ui-craft-guard/references/source-ledger.md",
    "skills/ui-craft-guard/references/design-principles.md",
    "skills/ui-craft-guard/references/geometry-typography.md",
    "skills/ui-craft-guard/references/chinese-ui.md",
    "skills/ui-craft-guard/references/interaction-accessibility.md",
    "skills/ui-craft-guard/references/prompt-recipes.md",
    "skills/ui-craft-guard/references/evidence-protocol.md",
    "skills/ui-craft-guard/references/design-intent.md",
    "skills/ui-craft-guard/references/tool-matrix.md",
    "skills/ui-craft-guard/templates/AUDIT_REPORT.md",
    "skills/ui-craft-guard/templates/DESIGN_DECISIONS.md",
    "scripts/validate_report.py", "tests/test_report_contract.py", "tests/test_packaging.py",
    "skills/ui-craft-guard/scripts/audit_ui.py",
    "skills/ui-craft-guard/scripts/validate_report.py",
    "examples/audit-cases/brand-gradient.json",
    "examples/audit-cases/efficient-dashboard.json",
    "examples/audit-cases/broken-submit.json",
    "examples/anti-pattern.html", "examples/revised.html", "examples/case-study.md",
    "scripts/audit_ui.py", "scripts/visual_smoke.py", "scripts/install.sh", "tests/test_audit.py",
]


def validate() -> list[str]:
    errors = [f"Missing: {name}" for name in REQUIRED if not (ROOT / name).is_file()]
    if not SKILL.is_file():
        return errors + ["Missing SKILL.md"]
    data = SKILL.read_text(encoding="utf-8")
    if not data.startswith("---\n") or "\n---\n" not in data[4:]:
        errors.append("SKILL.md needs YAML frontmatter")
    else:
        fm = data.split("\n---\n", 1)[0][4:]
        if not re.search(r"(?m)^name: ui-craft-guard\s*$", fm):
            errors.append("Invalid skill name")
        if not re.search(r"(?m)^description:\s*(?:\S|>)", fm):
            errors.append("Description missing")
    for ref in re.findall(r"\]\((references/[^)]+|templates/[^)]+)\)", data):
        if not (SKILL.parent / ref).is_file():
            errors.append(f"Broken SKILL.md reference: {ref}")
    ledger = ROOT / "skills/ui-craft-guard/references/source-ledger.md"
    if ledger.is_file():
        txt = ledger.read_text(encoding="utf-8")
        for handle in ("Kubai087", "ZaynHao", "ianneo_ai", "dingyi", "Xian0063",
                       "yanliudreamer", "ricouii", "remixdesigner"):
            if handle not in txt:
                errors.append(f"Missing provenance for {handle}")
    # Standalone installations copy only skills/ui-craft-guard: keep runtime tools in sync.
    for script in ("audit_ui.py", "validate_report.py"):
        original = ROOT / "scripts" / script
        portable = SKILL.parent / "scripts" / script
        if original.is_file() and portable.is_file() and original.read_bytes() != portable.read_bytes():
            errors.append(f"Runtime copy is stale: {script}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("FAIL\n" + "\n".join(problems))
        sys.exit(1)
    print("PASS: frontmatter, references, source coverage and file inventory")
