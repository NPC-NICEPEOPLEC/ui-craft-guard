"""Documentation roles and examples contracts; structural checks, not an audit-quality oracle."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills/ui-craft-guard"


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class DocumentationContractTests(unittest.TestCase):
    def test_version_is_not_report_schema(self):
        skill_version = read("skills/ui-craft-guard/VERSION").strip()
        self.assertEqual(skill_version, "0.2.2")
        self.assertIn(f"v{skill_version}", read("README.md"))
        self.assertIn(f"## {skill_version}", read("CHANGELOG.md"))
        self.assertIn("schema_version=0.2.1", read("skills/ui-craft-guard/references/prompt-recipes.md"))
        self.assertIn("schema_version=0.2.1", read("skills/ui-craft-guard/SKILL.md"))

    def test_readme_is_entrypoint_not_second_handbook(self):
        readme = read("README.md")
        self.assertIn("四层审计", readme)
        self.assertIn("三个维度", readme)
        self.assertIn("prompt-recipes.md", readme)
        self.assertIn("SKILL.md", readme)
        self.assertIn("examples/workflow-walkthrough.md", readme)
        self.assertEqual(readme.count("```text"), 1, "README should keep one copy-ready quick start")
        self.assertNotIn("## ① 自主诊断", readme)
        self.assertNotIn("## ③ 执行改进", readme)

    def test_four_stages_have_one_copyable_recipe_each(self):
        recipes = read("skills/ui-craft-guard/references/prompt-recipes.md")
        steps = ["① 自主诊断", "② 根因与设计决策", "③ 执行改进", "④ 批判性对比"]
        starts = [recipes.index("## " + step) for step in steps]
        self.assertEqual(starts, sorted(starts))
        for idx, start in enumerate(starts):
            end = starts[idx + 1] if idx < len(starts) - 1 else recipes.index("## 专项话术")
            section = recipes[start:end]
            self.assertEqual(section.count("```text"), 1, steps[idx])
            self.assertIn("```", section)

    def test_modes_and_safety_boundaries_are_preserved(self):
        skill = read("skills/ui-craft-guard/SKILL.md")
        recipes = read("skills/ui-craft-guard/references/prompt-recipes.md")
        for mode in ("audit", "redesign", "build", "compare"):
            self.assertIn(f"`{mode}`", skill)
        for layer in ("FLOOR", "STRUCTURE", "TASTE", "POLISH"):
            self.assertIn(layer, skill)
        for dimension in ("visual_quality", "usability", "design_identity"):
            self.assertIn(dimension, skill)
        for token in ("finding_id", "rule_id", "Evidence", "retain", "investigate"):
            self.assertIn(token, skill)
        self.assertIn("不是新增 Skill 模式", skill)
        self.assertIn("不得宣称为独立红队验收", skill)
        self.assertIn("本轮只审计", recipes)
        self.assertIn("未确认的项目不擅自扩大范围", recipes)

    def test_walkthrough_does_not_claim_real_site_blind_test(self):
        demo = read("examples/workflow-walkthrough.md")
        self.assertIn("不是真实网站盲测", demo)
        self.assertIn("不是本次 Skill v0.2.2 的新真实项目实验", demo)
        self.assertIn("浏览器历史检查记录", demo)
        self.assertIn("未完成", demo)
        self.assertIn("scanner" if "scanner" in demo else "启发式信号编号", demo)

    def test_documentation_links_resolve_locally(self):
        paths = [
            "README.md",
            "CONTRIBUTING.md",
            "PUBLISH.md",
            "skills/ui-craft-guard/SKILL.md",
            "skills/ui-craft-guard/references/prompt-recipes.md",
            "examples/workflow-walkthrough.md",
        ]
        for path in paths:
            text = read(path)
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                resolved = (ROOT / path).parent.joinpath(target)
                with self.subTest(file=path, link=target):
                    self.assertTrue(resolved.exists(), f"Broken relative link: {target} in {path}")


if __name__ == "__main__":
    unittest.main()
