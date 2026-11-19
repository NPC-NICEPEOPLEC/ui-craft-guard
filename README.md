# UI Craft Guard — 给 AI 编程代理一双会校准的设计眼睛

一个**可审计、可复查、按任务判断**的 UI 去 AI 味 Agent Skill。它不是“禁用紫色、圆角和渐变”的新模板，而是把八位设计作者相关公开讨论中的启发转成：**判断 → 证据 → 小步调整 → 真实验收**。

> 版本：0.1.0 / 研究整理：2026-11-19。来源并非八条原帖全都直读；每位作者的核验等级、链接和边界见 [来源台账](skills/ui-craft-guard/references/source-ledger.md)。本项目不受这些作者赞助或认可。

## 快速使用

将 `skills/ui-craft-guard` 整个目录复制到 Agent 支持的 skills 位置（例如 Codex 项目的 `.agents/skills/ui-craft-guard/`，Claude Code 项目的 `.claude/skills/ui-craft-guard/`；具体路径以所用客户端为准）。

```bash
# 从仓库根目录执行；可选择 codex 或 claude 作为目标，默认当前项目
bash scripts/install.sh codex .
# 或
bash scripts/install.sh claude /path/to/project
```

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
python3 -m unittest discover -s tests -v
```

可选浏览器冒烟测试（本项目已用 Chromium 跑通，详见 `examples/screenshots/browser-smoke-results.json`）：

```bash
# 需要 playwright Python 包与本机 Chromium；通过 CHROMIUM_PATH 覆盖位置
python3 scripts/visual_smoke.py
```

可检查 [修订前桌面截图](examples/screenshots/anti-pattern-desktop.png)、[修订后桌面截图](examples/screenshots/revised-desktop.png) 和 [修订后手机截图](examples/screenshots/revised-mobile.png)。

**扫描器只做静态风险提示**。它不会计算渲染后嵌套圆角、实际色彩对比、React 状态或交互质量，更不是自动 WCAG 合规认证。它的误报需要人工复查。

## 目录

```text
skills/ui-craft-guard/SKILL.md        # 代理入口
  references/source-ledger.md         # 八位作者、原帖镜像、可信度
  references/design-principles.md     # 规则 ID、适用情形与反例
  references/geometry-typography.md   # 同心圆角、字体/色彩 tokens
  references/chinese-ui.md            # 中文排版专项
  references/interaction-accessibility.md
  references/prompt-recipes.md        # 可复制提示
  templates/AUDIT_REPORT.md
  templates/DESIGN_DECISIONS.md
scripts/audit_ui.py                   # 纯标准库启发式扫描器
scripts/visual_smoke.py               # 可选 Playwright 浏览器冒烟测试
scripts/validate_skill.py             # 完整性检查
scripts/install.sh                    # 本地安装
examples/anti-pattern.html            # 人为制造的反模式例子
examples/revised.html                 # 改进后的原创示例
examples/case-study.md                # 规则归因和验收说明
tests/test_audit.py
.github/workflows/ci.yml
```

## 重要边界

1. `0.5px` 细线、`250ms` 动画、纯中性色不是普适硬规则。对比度、焦点、真实文案与品牌优先。
2. “不像 AI”不等于“设计优秀”，**没有唯一视觉风格**。静态扫描 0 告警不代表通过用户测试。
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
