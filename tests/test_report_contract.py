"""Data-contract tests. These do not simulate an LLM's visual judgment."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_report", ROOT / "scripts/validate_report.py")
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def fixture(name):
    return json.loads((ROOT / "examples/audit-cases" / name).read_text(encoding="utf-8"))


class AuditContractTests(unittest.TestCase):
    def test_three_contrasting_cases_are_structurally_valid(self):
        for case in ("brand-gradient.json", "efficient-dashboard.json", "broken-submit.json"):
            with self.subTest(case=case):
                self.assertEqual(checker.validate(fixture(case)), [])

    def test_brand_gradient_is_not_automatically_changed(self):
        report = fixture("brand-gradient.json")
        identity = [f for f in report["findings"] if f["dimension"] == "design_identity"]
        self.assertTrue(identity)
        self.assertEqual({f["decision"] for f in identity}, {"retain"})

    def test_minimal_dashboard_is_retained(self):
        report = fixture("efficient-dashboard.json")
        self.assertEqual({f["decision"] for f in report["findings"]}, {"retain"})

    def test_beautiful_page_cannot_hide_observed_blocking_failure(self):
        report = fixture("broken-submit.json")
        broken = next(f for f in report["findings"] if f.get("task_failure"))
        self.assertEqual(broken["decision"], "change")
        self.assertEqual(broken["priority"], "P0")
        broken["decision"] = "retain"
        self.assertTrue(any("cannot retain a reproduced task failure" in e
                            for e in checker.validate(report)))

    def test_change_rejects_inference_only(self):
        report = fixture("broken-submit.json")
        test = next(e for e in report["evidence"] if e["id"] == "E-TASK")
        test["status"] = "inferred"
        next(e for e in report["evidence"] if e["id"] == "E-CODE")["status"] = "inferred"
        errors = checker.validate(report)
        self.assertTrue(any("change needs direct observed evidence" in e for e in errors))

    def test_brand_redesign_needs_actual_brand_context(self):
        report = fixture("brand-gradient.json")
        issue = report["findings"][0]
        issue["decision"] = "change"
        issue["minimal_change"] = "Replace gradient"
        issue["evidence_ids"] = ["E-SCREEN"]
        errors = checker.validate(report)
        self.assertTrue(any("identity change requires observed product/brand/user intent" in e
                            for e in errors))

    def test_nonexistent_evidence_is_rejected(self):
        report = fixture("efficient-dashboard.json")
        report["findings"][0]["evidence_ids"].append("E-GHOST")
        self.assertTrue(any("unknown evidence ID" in e for e in checker.validate(report)))

    def test_dimension_not_assessed_cannot_host_findings(self):
        report = fixture("brand-gradient.json")
        report["findings"][0]["dimension"] = "usability"
        errors = checker.validate(report)
        self.assertTrue(any("unassessed dimension" in e for e in errors))

    def test_aggregate_scores_forbidden(self):
        report = fixture("efficient-dashboard.json")
        report["overall_score"] = 98
        self.assertTrue(any("aggregate UI quality score" in e
                            for e in checker.validate(report)))

    def test_all_four_layers_must_be_reported(self):
        report = fixture("brand-gradient.json")
        self.assertEqual(set(report["layer_coverage"]), checker.LAYERS)
        del report["layer_coverage"]["FLOOR"]
        self.assertTrue(any("layer_coverage" in e for e in checker.validate(report)))

    def test_assessed_layer_requires_real_evidence_reference(self):
        report = fixture("efficient-dashboard.json")
        report["layer_coverage"]["POLISH"]["status"] = "assessed"
        errors = checker.validate(report)
        self.assertTrue(any("assessed requires observed evidence" in e for e in errors))

    def test_unassessed_layer_cannot_have_findings(self):
        report = fixture("brand-gradient.json")
        report["findings"][0]["layer"] = "STRUCTURE"
        errors = checker.validate(report)
        self.assertTrue(any("requires its layer_coverage to be assessed" in e for e in errors))

    def test_finding_id_and_rule_id_are_distinct(self):
        report = fixture("brand-gradient.json")
        finding = report["findings"][0]
        self.assertNotEqual(finding["finding_id"], finding["rule_id"])
        self.assertEqual(finding["rule_id"], "G02")
        del finding["rule_id"]
        self.assertTrue(any("rule_id: required" in e for e in checker.validate(report)))

    def test_only_known_or_namespaced_project_rules(self):
        report = fixture("broken-submit.json")
        f = report["findings"][0]
        f["rule_id"] = "MADE-UP"
        self.assertTrue(any("rule_id: unknown" in e for e in checker.validate(report)))
        f["rule_id"] = "PROJECT:submit-handler"
        self.assertEqual(checker.validate(report), [])

    def test_v020_schema_stays_backward_compatible(self):
        report = fixture("brand-gradient.json")
        report["schema_version"] = "0.2.0"
        del report["layer_coverage"]
        for finding in report["findings"]:
            finding["id"] = finding.pop("finding_id")
            del finding["rule_id"]
        self.assertEqual(checker.validate(report), [])

    def test_static_scan_alone_not_permission_to_change(self):
        report = fixture("broken-submit.json")
        bad = next(f for f in report["findings"] if f.get("task_failure"))
        bad["task_failure"] = False
        report["evidence"].append({"id": "E-SCAN", "kind": "static_scan",
                                   "status": "observed", "locator": "style.css:2",
                                   "detail": "heuristic match"})
        bad["evidence_ids"] = ["E-SCAN"]
        errors = checker.validate(report)
        self.assertTrue(any("static scan alone" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
