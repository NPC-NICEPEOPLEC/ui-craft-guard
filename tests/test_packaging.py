"""Installed skill must be self-contained and preserve existing folders."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PortableInstallTests(unittest.TestCase):
    def test_runtime_copies_match_repo_scripts(self):
        for name in ("audit_ui.py", "validate_report.py"):
            with self.subTest(name=name):
                self.assertEqual((ROOT / "scripts" / name).read_bytes(),
                                 (ROOT / "skills/ui-craft-guard/scripts" / name).read_bytes())

    def test_three_client_locations_and_no_overwrite(self):
        for client, subdir in (("dsh", ".dsh"), ("codex", ".agents"), ("claude", ".claude")):
            with self.subTest(client=client), tempfile.TemporaryDirectory() as home:
                cmd = ["bash", str(ROOT / "scripts/install.sh"), client, home]
                first = subprocess.run(cmd, capture_output=True, text=True)
                self.assertEqual(first.returncode, 0, first.stderr)
                installed = Path(home) / subdir / "skills/ui-craft-guard"
                for file in ("SKILL.md", "scripts/audit_ui.py", "scripts/validate_report.py",
                             "references/evidence-protocol.md", "templates/AUDIT_REPORT.md"):
                    self.assertTrue((installed / file).is_file(), file)
                second = subprocess.run(cmd, capture_output=True, text=True)
                self.assertNotEqual(second.returncode, 0, "installer must not overwrite a skill")


if __name__ == "__main__":
    unittest.main()
