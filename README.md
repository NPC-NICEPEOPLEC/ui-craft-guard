# UI Craft Guard — 给 AI 编程代理一双会校准的设计眼睛

一个**可审计、可复查、按任务判断**的 UI 去 AI 味 Agent Skill。它不是“禁用紫色、圆角和渐变”的新模板，而是把八位设计作者相关公开讨论中的启发转成：**判断 → 证据 → 小步调整 → 真实验收**。

> 版本：0.2.0 / 研究整理：2026-11-19。来源并非八条原帖全都直读；每位作者的核验等级、链接和边界见 [来源台账](skills/ui-craft-guard/references/source-ledger.md)。本项目不受这些作者赞助或认可。

## 快速使用

将 `skills/ui-craft-guard` 整个目录复制到 Agent 支持的 skills 位置（例如 Codex 项目的 `.agents/skills/ui-craft-guard/`，Claude Code 项目的 `.claude/skills/ui-craft-guard/`；具体路径以所用客户端为准）。

```bash
# 从仓库根目录执行；可选择 codex 或 claude 作为目标，默认当前项目
bash scripts/install.sh codex .
# 或
bash scripts/install.sh claude /path/to/project
```

如要安装到三个**用户级**技能目录（须在自己的 Mac 终端执行；已存在的同名技能会被拒绝覆盖）：

```bash
bash scripts/install.sh dsh "$HOME"
bash scripts/install.sh codex "$HOME"
bash scripts/install.sh claude "$HOME"
```

v0.2.0 的 `skills/ui-craft-guard/` 目录已**自带运行时脚本** `scripts/audit_ui.py` 和 `scripts/validate_report.py`，所以只复制这一个目录也能使用两种检查器。仓库根目录的同名脚本供项目 CI 使用；测试保证两边一致。
对 AI 说：

```text
使用 ui-craft-guard 的 audit 模式，审查当前页面的 UI AI 味；先给出
问题位置、证据、规则 ID、例外和验证方法，不要修改代码。
```

或者：

```text
使用 ui-craft-guard 的 redesign 模式，保护已有功能和品牌，
先审计再最小修复。请做中文长标题、移动端、空/错态及键盘回归，
提供前后同视口截图；未运行的测试明确列出。
```

## v0.2.0：三层机制 + 三维独立结论

设计 **判断层 → 证据层 → 意图层** 协作，但最终报告分别回答三个问题：

| 独立维度 | 提问 | 支撑证据 |
|---|---|---|
| 视觉质量 `visual_quality` | 哪里存在比例、层级、排版、布局问题？ | 截图、源码、组件状态 |
| 使用体验 `usability` | 哪个用户任务受阻、误解或增加成本？ | 交互任务回放、状态/焦点检查 |
| 设计个性 `design_identity` | 视觉选择为什么符合或违背品牌与产品目标？ | 实际产品 brief、品牌资产、用户研究；没有则标假设 |

每条建议遵循 **判断 → 证据 → 最小调整 → 复查结果**；允许 `retain`（保留）和 `investigate`（待证），不因为紫色、渐变或朴素后台就强制美化。四层 FLOOR/STRUCTURE/TASTE/POLISH 保留，用于归类发现而非替代三维评价。详细约束见 [证据协议](skills/ui-craft-guard/references/evidence-protocol.md)、[设计意图与反证](skills/ui-craft-guard/references/design-intent.md)、[可选工具矩阵](skills/ui-craft-guard/references/tool-matrix.md)。

**第一次使用（不知道哪里有问题时）**：

```text
使用 ui-craft-guard 的 audit 模式检查我的整个网站。先阅读产品目标、
代码与已有品牌规范；具备浏览器时真实打开页面并验证主要任务。
分别审计视觉质量、使用体验、设计个性。所有发现标注 Evidence ID、
能力等级、最强反证、change/retain/investigate 与最小修复方案。
请明确指出哪些现有设计值得保留；本轮只诊断，不修改代码。
```

## 工作机制

- **任务与来源优先**：明确页面的真实目标、用户、语言及品牌约束；保留已有设计系统。
- **四层审计**：`FLOOR` 可用性底线 → `STRUCTURE` 信息与交互 → `TASTE` 模板惯性 → `POLISH` 几何细节。
- **带出处的规则**：源码/截图证据 + ID + 例外；把“设计师经验”与 WCAG 这类规范分开。
- **小步修复**：不把所有页面刷成另一个默认模板；不改无关功能。
- **真实验收**：视口、中文、键盘、加载/错误、长内容与对比截图；若不能浏览器测试必须声明。

## 工具和测试

仅依赖 Python 3 标准库（扫描器运行无需安装依赖）：

```bash
python3 scripts/audit_ui.py examples/anti-pattern.html --format markdown
python3 scripts/audit_ui.py examples/revised.html --format json
python3 scripts/validate_skill.py
python3 scripts/validate_report.py examples/audit-cases/*.json
python3 -m unittest discover -s tests -v
```

可选浏览器冒烟测试（本项目已用 Chromium 跑通，详见 `examples/screenshots/browser-smoke-results.json`）：

```bash
# 需要 playwright Python 包与本机 Chromium；通过 CHROMIUM_PATH 覆盖位置
python3 scripts/visual_smoke.py
```

可检查 [修订前桌面截图](examples/screenshots/anti-pattern-desktop.png)、[修订后桌面截图](examples/screenshots/revised-desktop.png) 和 [修订后手机截图](examples/screenshots/revised-mobile.png)。

**扫描器和 JSON 合约校验都只做有限验证**。它不会计算渲染后嵌套圆角、实际色彩对比、React 状态或交互质量，更不是自动 WCAG 合规认证。它的误报需要人工复查。

## 目录

```text
skills/ui-craft-guard/SKILL.md        # 代理入口
  references/source-ledger.md         # 八位作者、原帖镜像、可信度
  references/design-principles.md     # 规则 ID、适用情形与反例
  references/geometry-typography.md   # 同心圆角、字体/色彩 tokens
  references/chinese-ui.md            # 中文排版专项
  references/interaction-accessibility.md
  references/prompt-recipes.md        # 可复制提示
  references/evidence-protocol.md     # 证据约束与三维独立判断
  references/design-intent.md         # 品牌定位、反证与保留机制
  references/tool-matrix.md           # 可选工具与能力边界
  templates/AUDIT_REPORT.md
  templates/DESIGN_DECISIONS.md
  scripts/audit_ui.py                # 安装后仍可运行的扫描器
  scripts/validate_report.py         # 安装后仍可运行的审计合约校验
scripts/audit_ui.py                   # 纯标准库启发式扫描器
scripts/visual_smoke.py               # 可选 Playwright 浏览器冒烟测试
scripts/validate_skill.py             # 完整性检查
scripts/validate_report.py            # JSON 证据合约校验（非审美评分）
scripts/install.sh                    # 本地安装
examples/anti-pattern.html            # 人为制造的反模式例子
examples/revised.html                 # 改进后的原创示例
examples/case-study.md                # 规则归因和验收说明
examples/audit-cases/*.json           # 3 个对照的决策测试样例
tests/test_audit.py
tests/test_report_contract.py          # 证据门槛、反证与反例测试
tests/test_packaging.py                # 三客户端目录安装与脚本同一性测试
.github/workflows/ci.yml
```

## 重要边界

1. `0.5px` 细线、`250ms` 动画、纯中性色不是普适硬规则。对比度、焦点、真实文案与品牌优先。
2. “不像 AI”不等于“设计优秀”，**没有唯一视觉风格**。静态扫描 0 告警不代表通过用户测试。三维独立评价，未运行不得声称实测；JSON 测试样例是构造数据，不是现场用户研究。
3. 无第三方文章正文、截图或字体捆绑；规则均为原创概括，并保留出处。
4. 本仓库仅是 Skill 和演示，不自动获取网站数据，不调用任何外部 API，也不自动修改用户项目。

## 参考

- [8 位作者入口推文](https://x.com/bruc3van/status/2115963644811116732)（X 可能要求登录）
- [可读镜像及评论](https://instalker.org/bruc3van/status/2115963644811116732)
- [Agent Skills Specification](https://agentskills.io/specification)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Radix Colors](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale)
- [MDN corner-shape](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)

## License

MIT，见 [LICENSE](LICENSE)。欢迎提交具有完整前后截图、规则依据和测试记录的改进。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 本次验证状态

[本地与 GitHub 真实验收记录](VALIDATION.md)；[公开仓库同步、安装与复验说明](PUBLISH.md)。本项目已公开提交并通过格式/测试与 Chromium 截图工作流。GitHub 仓库发布不代表已在个人电脑或 ChatGPT 中安装。
