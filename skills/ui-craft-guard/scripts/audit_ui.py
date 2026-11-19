#!/usr/bin/env python3
"""A conservative static UI anti-pattern scanner.

Only scans local HTML and CSS source for review-worthy signals. It DOES NOT
render the UI, audit contrast, prove authorship, or certify WCAG compliance.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path

SEVERITIES = {"high": 3, "medium": 2, "low": 1}
EXTS = {".html", ".htm", ".css", ".jsx", ".tsx", ".vue", ".svelte"}


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    file: str
    line: int
    evidence: str
    explanation: str
    review: str


class MarkupSignals(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.issues: list[tuple[str, int, str]] = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        lineno, _ = self.getpos()
        if tag == "a" and d.get("href") in ("#", "", "javascript:void(0)"):
            self.issues.append(("A01", lineno, f"a[href={d.get('href')!r}]"))
        if tag == "img" and "alt" not in d:
            self.issues.append(("A02", lineno, "img missing alt attribute"))
        if tag == "button" and d.get("type") == "submit" and not d.get("aria-label"):
            # This is not automatically a defect; no warning (visible text may name it).
            pass


def make(rid: str, severity: str, path: Path, line: int, evidence: str,
         explanation: str, review: str) -> Finding:
    return Finding(rid, severity, str(path), line, evidence[:160], explanation, review)


def line_number(source: str, offset: int) -> int:
    return source.count("\n", 0, offset) + 1


def scan_source(path: Path) -> list[Finding]:
    source = path.read_text(encoding="utf-8")
    # Strip comments before regex scanning. Preserve line numbers with newlines.
    cleaned = re.sub(r"/\*.*?\*/|<!--.*?-->",
                     lambda m: "\n" * m.group().count("\n"), source, flags=re.S)
    found: list[Finding] = []

    def flag(rid, severity, match, explanation, review):
        found.append(make(rid, severity, path, line_number(cleaned, match.start()),
                          match.group(0).strip(), explanation, review))

    checks = [
        ("H01", "medium", r"(?:linear|radial)-gradient\([^;{}]*?(?:#(?:8b5cf6|6366f1|a855f7)|\b(?:indigo|violet|purple)\b)[^;{}]*?\)",
         "Potential model-default purple gradient.", "Confirm whether brand/meaning warrants it; do not ban gradients globally."),
        ("H02", "medium", r"(?:-webkit-)?background-clip\s*:\s*text\b",
         "Gradient/clipped text may add decoration without information value.", "Review against actual visual identity."),
        ("H03", "low", r"text-transform\s*:\s*uppercase\b",
         "Uppercase micro-label treatment may be habitual template styling.", "Keep when meaningful for navigation or brand voice."),
        ("H04", "medium", r"border-left\s*:\s*[3-9](?:\.\d+)?px\s+solid\b",
         "Thick colored left-border cards can become repetitive UI decoration.", "Keep when the line encodes status, hierarchy, or meaning."),
        ("H05", "medium", r"transition\s*:\s*all\b",
         "Transitioning every CSS property makes motion less intentional.", "Animate only relevant properties; verify reduced motion."),
        ("A03", "high", r"outline\s*:\s*(?:none|0(?:px)?)\b",
         "Removing outlines can hide keyboard focus.", "Check for a visible, equivalent :focus-visible treatment in the rendered UI."),
        ("H06", "low", r"\b(?:lorem ipsum|coming soon|your amazing product)\b",
         "Placeholder or generic copy may be mistaken for real content.", "Replace only with sourced, task-relevant copy; never invent metrics."),
    ]
    for rid, sev, pat, why, review in checks:
        for match in re.finditer(pat, cleaned, flags=re.I | re.S):
            flag(rid, sev, match, why, review)

    sizes = []
    for m in re.finditer(r"font-size\s*:\s*([0-9]+(?:\.[0-9]+)?)px\b", cleaned, flags=re.I):
        px = float(m.group(1))
        sizes.append(px)
        if px < 12:
            flag("T01", "medium", m, "Source uses a font size under the author's suggested 12px review point.",
                 "Not a WCAG pixel minimum; inspect actual legibility and product context.")
    if len(set(sizes)) > 4:
        m = re.search(r"font-size\s*:", cleaned, flags=re.I)
        if m:
            flag("T02", "low", m,
                 f"Found {len(set(sizes))} distinct px font sizes in one source; hierarchy may be fragmented.",
                 "Count across final computed styles; responsive sizes and design tokens can be valid.")

    if path.suffix.lower() in {".html", ".htm"}:
        html = MarkupSignals()
        html.feed(source)
        for rid, lineno, evidence in html.issues:
            if rid == "A01":
                found.append(make(rid, "high", path, lineno, evidence,
                                  "Placeholder anchors usually do not navigate.", "Provide a real destination or use a button for actions."))
            if rid == "A02":
                found.append(make(rid, "medium", path, lineno, evidence,
                                  "Images need an explicit text alternative decision.", "Add meaningful alt text or alt='' for decorative images."))
    return sorted(found, key=lambda f: (-SEVERITIES[f.severity], f.file, f.line, f.rule_id))


def collect(input_path: Path) -> list[Path]:
    if input_path.is_file():
        if input_path.suffix.lower() not in EXTS:
            raise ValueError(f"Unsupported extension: {input_path.suffix}")
        return [input_path]
    if not input_path.is_dir():
        raise ValueError(f"Path not found: {input_path}")
    return sorted(f for f in input_path.rglob("*") if f.is_file() and f.suffix.lower() in EXTS
                  and not any(part in {"node_modules", ".git", "dist", "build"} for part in f.parts))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("path", type=Path, help="A local .html/.css/.tsx file or directory")
    p.add_argument("--format", choices=("markdown", "json"), default="markdown")
    p.add_argument("--fail-on", choices=("high", "medium", "low"),
                   help="Return nonzero if any issue at or above this severity is found")
    args = p.parse_args()
    try:
        paths = collect(args.path)
        if not paths:
            raise ValueError("No supported UI source files found")
        results = [f for path in paths for f in scan_source(path)]
    except (ValueError, UnicodeError, OSError) as exc:
        p.error(str(exc))
    if args.format == "json":
        print(json.dumps({"disclaimer": "Heuristic source scan, not visual/WCAG validation",
                          "files_scanned": len(paths), "findings": [asdict(f) for f in results]},
                         ensure_ascii=False, indent=2))
    else:
        print("# UI Craft Guard — source-only signal scan\n")
        print(f"Scanned {len(paths)} file(s); found {len(results)} review signals.\n")
        print("This does not test rendered layout, focus, contrast, or interactions.\n")
        for f in results:
            print(f"- **{f.severity.upper()} {f.rule_id}** `{f.file}:{f.line}` — {f.explanation}\n"
                  f"  - Evidence: `{f.evidence}`\n  - Review: {f.review}")
        if not results:
            print("No selected static signals found. Manual visual and functional tests still required.")
    if args.fail_on and any(SEVERITIES[f.severity] >= SEVERITIES[args.fail_on] for f in results):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
