#!/usr/bin/env python3
"""Validate the *structure* and evidence gates of v0.2.0 (legacy) and v0.2.1 UI audit JSON reports.

This cannot prove a screenshot, test result or brand intent is true.
Standard library only. All findings remain subject to actual review.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DIMENSIONS = {"visual_quality", "usability", "design_identity"}
LAYERS = {"FLOOR", "STRUCTURE", "TASTE", "POLISH"}
KINDS = {"screenshot", "source_code", "task_test", "browser_run",
         "static_scan", "brief", "brand_asset", "user_research"}
STATUSES = {"observed", "inferred", "unavailable"}
DECISIONS = {"change", "retain", "investigate"}
PRIORITIES = {"P0", "P1", "P2", "P3"}
CAPABILITIES = {"full", "partial", "limited"}
IDENTITY_SOURCES = {"brief", "brand_asset", "user_research"}


def rulebook_ids() -> set[str]:
    """Read the original v0.1 rulebook in repo or portable Skill install."""
    base = Path(__file__).resolve().parent.parent
    options = (
        base / "skills/ui-craft-guard/references/design-principles.md",
        base / "references/design-principles.md",
    )
    for path in options:
        if path.is_file():
            return set(re.findall(r"(?m)^\|\s*([A-Z]\d{2})\s*\|", path.read_text(encoding="utf-8")))
    return set()


def filled(value):
    return isinstance(value, str) and bool(value.strip())


def validate(report: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(report, dict):
        return ["root: expected JSON object"]
    version = report.get("schema_version")
    if version not in {"0.2.0", "0.2.1"}:
        errors.append("schema_version: expected 0.2.0 (legacy) or 0.2.1")
    strict = version == "0.2.1"
    if "overall_score" in report or "ui_quality_score" in report:
        errors.append("overall_score: aggregate UI quality score is forbidden")
    for field in ("project", "mode", "capability"):
        if not filled(report.get(field)):
            errors.append(f"{field}: required nonempty string")
    if report.get("mode") not in {"audit", "redesign", "build", "compare"}:
        errors.append("mode: unrecognized")
    if report.get("capability") not in CAPABILITIES:
        errors.append("capability: expected full, partial or limited")

    raw_evidence = report.get("evidence")
    if not isinstance(raw_evidence, list):
        errors.append("evidence: expected list")
        raw_evidence = []
    evidence: dict[str, dict] = {}
    for index, item in enumerate(raw_evidence):
        where = f"evidence[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where}: expected object")
            continue
        eid = item.get("id")
        if not filled(eid):
            errors.append(f"{where}.id: missing")
            continue
        if eid in evidence:
            errors.append(f"{where}.id: duplicate {eid}")
            continue
        evidence[eid] = item
        if item.get("kind") not in KINDS:
            errors.append(f"{where}.kind: unsupported")
        if item.get("status") not in STATUSES:
            errors.append(f"{where}.status: unsupported")
        if item.get("status") == "observed":
            if not filled(item.get("locator")):
                errors.append(f"{where}.locator: observed evidence needs location")
            if not filled(item.get("detail")):
                errors.append(f"{where}.detail: observed evidence needs reproducible detail")

    def refs(item: dict, field: str, where: str, require: bool = False) -> list[dict]:
        value = item.get(field, [])
        if not isinstance(value, list) or any(not filled(x) for x in value):
            errors.append(f"{where}.{field}: expected list of evidence IDs")
            return []
        if require and not value:
            errors.append(f"{where}.{field}: cannot be empty")
        missing = [x for x in value if x not in evidence]
        for x in missing:
            errors.append(f"{where}.{field}: unknown evidence ID {x}")
        return [evidence[x] for x in value if x in evidence]

    dims = report.get("dimensions")
    if not isinstance(dims, dict):
        errors.append("dimensions: expected object")
        dims = {}
    if set(dims) != DIMENSIONS:
        errors.append("dimensions: must independently contain visual_quality, usability, design_identity")
    for key in DIMENSIONS:
        where = f"dimensions.{key}"
        item = dims.get(key)
        if not isinstance(item, dict):
            errors.append(f"{where}: missing or not an object")
            continue
        status = item.get("status")
        if status not in {"supported", "hypothesis", "not_assessed"}:
            errors.append(f"{where}.status: unsupported")
        if not filled(item.get("summary")):
            errors.append(f"{where}.summary: required")
        sources = refs(item, "evidence_ids", where)
        if status == "supported" and not any(e.get("status") == "observed" for e in sources):
            errors.append(f"{where}: supported requires observed evidence")
        if status == "not_assessed" and not filled(item.get("limitations")):
            errors.append(f"{where}.limitations: explain why not assessed")

    # Layers are coverage categories, not mandatory counts of defects.
    coverage = report.get("layer_coverage")
    if strict:
        if not isinstance(coverage, dict) or set(coverage) != LAYERS:
            errors.append("layer_coverage: must explicitly include FLOOR, STRUCTURE, TASTE, POLISH")
            coverage = {}
        for layer in LAYERS:
            entry = coverage.get(layer)
            where = f"layer_coverage.{layer}"
            if not isinstance(entry, dict):
                errors.append(f"{where}: missing coverage record")
                continue
            state = entry.get("status")
            if state not in {"assessed", "not_assessed"}:
                errors.append(f"{where}.status: expected assessed or not_assessed")
            if not filled(entry.get("summary")):
                errors.append(f"{where}.summary: required")
            refs_found = refs(entry, "evidence_ids", where)
            if state == "assessed" and not any(e.get("status") == "observed" for e in refs_found):
                errors.append(f"{where}: assessed requires observed evidence")
            if state == "not_assessed" and not filled(entry.get("limitations")):
                errors.append(f"{where}.limitations: explain what was not checked")
    else:
        coverage = {}

    known_rules = rulebook_ids() if strict else set()
    if strict and not known_rules:
        errors.append("rulebook: design-principles.md not found or has no declared IDs")

    findings = report.get("findings")
    if not isinstance(findings, list):
        errors.append("findings: expected list")
        findings = []
    ids: set[str] = set()
    for index, item in enumerate(findings):
        where = f"findings[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where}: expected object")
            continue
        fid = item.get("finding_id") if strict else item.get("finding_id", item.get("id"))
        if not filled(fid):
            errors.append(f"{where}.finding_id: missing")
        elif fid in ids:
            errors.append(f"{where}.finding_id: duplicate")
        else:
            ids.add(fid)
        if strict:
            if "id" in item:
                errors.append(f"{where}: use finding_id instead of legacy id")
            rid = item.get("rule_id")
            if not filled(rid):
                errors.append(f"{where}.rule_id: required")
            elif rid not in known_rules and not re.fullmatch(r"PROJECT:[a-z0-9][a-z0-9-]*", rid):
                errors.append(f"{where}.rule_id: unknown rule; use rulebook ID or PROJECT:slug")
            if filled(rid) and fid == rid:
                errors.append(f"{where}: finding_id and rule_id must identify different concepts")
        dim = item.get("dimension")
        if dim not in DIMENSIONS:
            errors.append(f"{where}.dimension: unsupported")
        layer = item.get("layer")
        if layer not in LAYERS:
            errors.append(f"{where}.layer: unsupported")
        if strict and layer in LAYERS:
            state = coverage.get(layer, {}).get("status") if isinstance(coverage.get(layer), dict) else None
            if state != "assessed":
                errors.append(f"{where}: a finding requires its layer_coverage to be assessed")
        decision = item.get("decision")
        if decision not in DECISIONS:
            errors.append(f"{where}.decision: unsupported")
        if item.get("priority") not in PRIORITIES:
            errors.append(f"{where}.priority: unsupported")
        for field in ("location", "observation", "impact", "alternative_explanation", "recheck"):
            if not filled(item.get(field)):
                errors.append(f"{where}.{field}: required")
        sources = refs(item, "evidence_ids", where, require=True)
        observed = [e for e in sources if e.get("status") == "observed"]
        if dim in dims and isinstance(dims[dim], dict) and dims[dim].get("status") == "not_assessed":
            errors.append(f"{where}: cannot make a finding for an unassessed dimension")
        if decision == "change":
            if not observed:
                errors.append(f"{where}: change needs direct observed evidence")
            if not any(e.get("kind") != "static_scan" for e in observed):
                errors.append(f"{where}: static scan alone cannot authorize change")
            if dim == "design_identity" and not any(
                e.get("kind") in IDENTITY_SOURCES for e in observed
            ):
                errors.append(f"{where}: identity change requires observed product/brand/user intent")
            if not filled(item.get("minimal_change")):
                errors.append(f"{where}.minimal_change: required for change")
            if dim in dims and isinstance(dims[dim], dict) and dims[dim].get("status") != "supported":
                errors.append(f"{where}: change requires supported dimension")
        elif decision == "retain" and not observed:
            errors.append(f"{where}: retain needs observed evidence, otherwise investigate")
        if item.get("task_failure") is True:
            if not any(e.get("kind") == "task_test" and e.get("status") == "observed" for e in sources):
                errors.append(f"{where}: task_failure needs actual observed task_test")
            if decision == "retain":
                errors.append(f"{where}: cannot retain a reproduced task failure")

    retained = report.get("retained")
    if not isinstance(retained, list):
        errors.append("retained: expected list")
        retained = []
    for index, item in enumerate(retained):
        where = f"retained[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where}: expected object")
            continue
        for field in ("choice", "reason"):
            if not filled(item.get(field)):
                errors.append(f"{where}.{field}: required")
        refs(item, "evidence_ids", where, require=True)
    if not retained and any(
        isinstance(dims.get(k), dict) and dims[k].get("status") == "supported"
        for k in DIMENSIONS
    ):
        errors.append("retained: state at least one preserved choice when any dimension is supported")

    if not isinstance(report.get("unverified"), list) or any(
        not filled(x) for x in report.get("unverified", []) if isinstance(report.get("unverified"), list)
    ):
        errors.append("unverified: expected list of nonempty strings")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+", type=Path, help="one or more audit JSON reports")
    args = parser.parse_args()
    failed = False
    for path in args.reports:
        try:
            report = json.loads(path.read_text(encoding="utf-8"))
            errors = validate(report)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors = [str(exc)]
        print(f"{'PASS' if not errors else 'FAIL'} {path}")
        for err in errors:
            print(f"  - {err}")
        failed |= bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
