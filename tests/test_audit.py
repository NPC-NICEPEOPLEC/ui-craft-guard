"""Regression tests for heuristic signals (not visual quality tests)."""
import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("audit_ui", ROOT / "scripts/audit_ui.py")
audit = importlib.util.module_from_spec(SPEC)
import sys
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class ScannerTest(unittest.TestCase):
    def test_bad_fixture_has_expected_signals(self):
        reports = audit.scan_source(ROOT / "examples/anti-pattern.html")
        ids = {f.rule_id for f in reports}
        self.assertTrue({"H01", "H02", "H03", "H04", "H05", "T01", "T02", "A01", "A03"}.issubset(ids))

    def test_revised_fixture_removes_targeted_signals(self):
        reports = audit.scan_source(ROOT / "examples/revised.html")
        ids = {f.rule_id for f in reports}
        self.assertFalse(ids.intersection({"H01", "H02", "H03", "H04", "H05", "T01", "A01", "A02", "A03"}))

    def test_no_fake_dead_link_for_real_url(self):
        with tempfile.TemporaryDirectory() as temp:
            file = pathlib.Path(temp) / "page.html"
            file.write_text('<a href="/articles">文章</a><img src="x" alt="">', encoding="utf-8")
            self.assertEqual(audit.scan_source(file), [])

    def test_nonexistent_path_error(self):
        with self.assertRaises(ValueError):
            audit.collect(ROOT / "missing-dir-for-test")

    def test_file_collection(self):
        files = audit.collect(ROOT / "examples")
        self.assertEqual({p.name for p in files}, {"anti-pattern.html", "revised.html"})


if __name__ == "__main__":
    unittest.main()
