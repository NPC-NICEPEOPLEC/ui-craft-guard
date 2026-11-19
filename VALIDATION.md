# UI Craft Guard 验收记录（2026-11-19）

## GitHub 公开同步：已验证

- 仓库： https://github.com/NPC-NICEPEOPLEC/ui-craft-guard
- 权限：PUBLIC；默认分支：`main`。
- Skill 主入口：`skills/ui-craft-guard/SKILL.md`。
- v0.1.0 最初参考文件为 6 份；v0.2.0 扩展为 `references/` 9 份、`templates/` 2 份，均已加入远端。
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
- **v0.2.0 真实验收完成**：PR [#1](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/pull/1) 已合并到 `main`；合并提交 [2d3150e](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/commit/2d3150ef6fb376b7d75a6b6f9435d09ab7e3ab82)。
- 合并后 `main` 的 [skill-validation #44481809467](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/actions/runs/44481809467) **success**：Skill 入口/引用校验、3 组 JSON 合约案例、17 项 Python 单元测试均通过（已读取实际 job logs）。
- [PR 检查 #44481769156](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/actions/runs/44481769156) 也 success；远端 v0.2 Skill 目录包含 `SKILL.md`、3 个新增参考文档、2 份模板与 2 份内置运行脚本。
- **尚未验证**用户个人 Mac 中的三处技能目录升级、ChatGPT 私人 Plugin 的安装和真实站点的自动化设计评估；不能将示例合约通过等同实站审美评审。

- v0.2.0 可移植性：Skill 目录内自带两份运行脚本，安装器支持 dsh/codex/claude 三种目录，且不覆盖已存在 Skill；真实 CI 检查见对应版本提交记录。

## v0.2.1 兼容性补丁的验收边界

- 变更内容：独立 finding_id/rule_id、FLOOR/STRUCTURE/TASTE/POLISH 覆盖记录、完整 README 定位与离线 ZIP 用户级安装器。
- 旧版 0.2.0 JSON 仍使用原有字段的兼容读取路径；新格式 0.2.1 将由 CI 的结构测试验证。
- **实际部署回执**：PR [#2](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/pull/2) 已合并；main 合并提交 [3eab43e](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/commit/3eab43e959b1819d247b33fffdc6368f37350394)。
- **合并后的 GitHub Actions 成功**：[skill-validation #44491350215](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/actions/runs/44491350215)，实际 job logs 显示 24 项 Python 单元测试通过、3 组 JSON 合约案例 PASS、Skill 格式及引用校验 PASS。
- **远端回读**：`skills/ui-craft-guard/VERSION` 为 `0.2.1`；`SKILL.md`、四层覆盖协议、Rulebook、报告模板、便携验证脚本和离线更新器均存在。
- **仍待实际确认**：用户 Mac 中三套技能位置是否已更新、客户端是否重新加载，以及此 Skill 在真实项目上的审计质量；本次合成案例和 CI 不能证明这些事项。
