# UI Craft Guard 验收记录（2026-11-19）

## GitHub 公开同步：已验证

- 仓库： https://github.com/NPC-NICEPEOPLEC/ui-craft-guard
- 权限：PUBLIC；默认分支：`main`。
- Skill 主入口：`skills/ui-craft-guard/SKILL.md`。
- 引用依赖：`references/` 6 份、`templates/` 2 份，已全部加入远端。
- 其他：静态扫描器、安装脚本、测试、原创建模的 HTML、截图记录、许可证、贡献指南和工作流均已提交。
- 四张 PNG 截图由 GitHub Actions 使用 Chromium 重新生成并提交到 `main`，不是只放在本地附件中。

## GitHub Actions：实际通过

- [skill-validation 成功记录](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/actions/runs/44470666035)：标准库单测 5 项及 Skill 格式/引用校验通过。
- [screenshot-evidence 成功记录](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/actions/runs/44470666029)：Playwright/Chromium 安装、三个视口的实际操作冒烟测试与截图入库全部通过。
- 截图工作流初次执行在 Ubuntu 26.04 上因 Playwright 系统支持失败；修正到 Ubuntu 24.04 后已复验成功。保留失败历史以便追溯。

## 质量边界

- 静态扫描针对示例故意放置的反模式给出信号；修订页没有命中当前选定信号。
- Chromium 验证宽度：375px、768px、1280px，覆盖横向溢出、表单提交、列表数量变化和键盘焦点。
- **未验证**完整 WCAG AA、屏幕阅读器、多浏览器、多操作系统及真实用户测试；因此不声称全面无障碍合规。
- 本仓库公开同步与本机安装、ChatGPT Plugin 安装是独立事项；**不会因为仓库已公开就自动出现在用户的 ChatGPT/Claude/Codex 技能列表中**。

## 复现

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
python3 scripts/audit_ui.py examples/anti-pattern.html --format markdown
python3 scripts/audit_ui.py examples/revised.html --format markdown
```

本机复制到 `~/.dsh/skills/`、`~/.agents/skills/` 和 `~/.claude/skills/` 的操作说明见 [PUBLISH.md](PUBLISH.md)。

## v0.2.0 验证说明

- 新增三维独立结论、证据协议、设计意图/反证门槛及构造测试案例。
- `scripts/validate_report.py` 只验证审计 JSON 的结构和证据前置条件，不验证真实品牌、截图、UX 或用户研究。
- 三组 JSON 案例是**合成测试输入**，其中的“observed”仅指测试场景内的假设证据，绝不是对具体网站运行的事实陈述。
- v0.1.0 的截图与 Playwright 冒烟测试作为历史事实保留；不能冒充已验证新版设计判断能力。
- 2026-11-19 的 v0.2 CI 与远端发布证据，须以实际 workflow run/commit 记录为准；未运行前不标记通过。

- v0.2.0 可移植性：Skill 目录内自带两份运行脚本，安装器支持 dsh/codex/claude 三种目录，且不覆盖已存在 Skill；真实 CI 检查见对应版本提交记录。
