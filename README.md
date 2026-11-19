# UI Craft Guard

**一个面向 AI 编程代理的 UI 审计、设计判断与改进 Skill。** 适合“不知道网页哪里有问题”、改版前的自主诊断、设计系统复查、新页面设计与前后版本验收。

它不是把所有界面统一改成某种风格的“去 AI 味”美化器；目标是**理解产品任务 → 找到真实问题 → 给出可追溯的判断 → 保留有效设计 → 验证修改是否值得**。没有依据时允许 `investigate`，合理的设计允许 `retain`。

> 当前 Skill：**v0.2.2** · [入口与权威执行规范](skills/ui-craft-guard/SKILL.md) · [版本历史](CHANGELOG.md) · [测试证据与限制](VALIDATION.md)  
> GitHub 公开不代表已安装或加载到本地客户端。

## 核心方法

**四层审计是完整骨架，三个维度是独立评价视角，证据和设计意图决定行动。** 三者不是相互替代的版本。

| 四层审计（v0.1.0 保留） | 关注点 |
|---|---|
| **FLOOR** | 功能、可读性、焦点、无障碍与异常反馈 |
| **STRUCTURE** | 信息层级、任务入口、导航、结构与响应式 |
| **TASTE** | 产品和品牌适配、视觉系统、缺乏依据的模板惯性 |
| **POLISH** | 排版、对齐、圆角、图标、状态与动效细节 |

再分别评价 **视觉质量 `visual_quality`、使用体验 `usability`、设计个性 `design_identity`**；不合成虚假的 UI 总分。

每层都需说明已检查还是未检查；**无问题 ≠ 未检查**。每条发现绑定 `finding_id`（本次发现）、`rule_id`（原规则/项目特有规则）及 Evidence ID，再选择 `change / retain / investigate`。数据契约和判断门槛以 [证据协议](skills/ui-craft-guard/references/evidence-protocol.md) 为准。

## 30 秒开始：网站有问题，但不知道是什么

已安装 Skill 且代理具备项目访问权限时，在网站项目中输入：

```text
请加载 ui-craft-guard，使用 audit 模式自主诊断当前网站。
我不知道有哪些问题，请先理解产品目标、现有代码和设计规范；
有浏览器能力时查看真实页面并测试主要用户任务。
检查 FLOOR、STRUCTURE、TASTE、POLISH 四层覆盖情况，
再分别评价视觉质量、使用体验和设计个性。
每个重要发现提供 finding_id、rule_id、Evidence ID、
最强反证、根因、优先级和 change/retain/investigate 决策；
明确哪些设计值得保留。不能验证的写明缺口。本轮不改代码。
```

**完整可复制话术与场景选择：** [Prompt Recipes · 四阶段工作手册](skills/ui-craft-guard/references/prompt-recipes.md)。

## 用在整个设计周期

| 使用阶段 | 推荐 Skill 模式 | 目标 |
|---|---|---|
| ① 自主诊断 | `audit` | 找未知问题、四层覆盖、三维评价、证据与优先级 |
| ② 设计推演 | `audit` 的后续分析 | 聚类根因、比较方案及代价，不写代码 |
| ③ 实施改进 | `redesign` | 仅按已确认范围修改、记录 diff 与回归 |
| ④ 批判性复查 | `compare` | 不预设新版更好，报告改善、退化与未知 |

**四阶段是建议的用户工作流，不是四个新模式。** Skill 保留 `audit / redesign / build / compare` 四种模式；新界面用 `build`。同一个 Agent 自我复查不是独立红队测试；需要独立性时用新的会话或另一个评审者。

## 安装与更新

复制的是**完整** `skills/ui-craft-guard/`（含 `SKILL.md`、`VERSION`、`references/`、`templates/`、`scripts/`），不是单独的入口文件。

Mac 用户可在浏览器 [下载 main.zip](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/archive/refs/heads/main.zip)，解压后**进入解压的仓库根目录**，再执行：

```bash
cd "$HOME/Downloads/ui-craft-guard-main"
bash scripts/update_user_skills.sh
```

如果解压目录被自动加了后缀，请用实际路径。更新脚本不通过 Git 下载，会备份旧版并更新三个用户级目录：`~/.dsh/skills/`、`~/.agents/skills/`、`~/.claude/skills/`。客户端需重新加载，且应实际检查能否读取 `VERSION`，不能只凭目录存在就称“已加载”。详见 [安装与验证](PUBLISH.md)。

## 示例、验证与限制

- [可复现的四阶段教学演练](examples/workflow-walkthrough.md)：以仓库原创页面演示从诊断到复查，**不是**真实客户网站的盲测。
- [原创建模前后对比](examples/case-study.md) · [浏览器历史检查记录](examples/screenshots/browser-smoke-results.json)
- [合成决策契约案例](examples/audit-cases)：验证“保留品牌渐变 / 保留高效后台 / 不忽略表单故障”的合约逻辑，**不是**真实用户研究。
- [验证历史](VALIDATION.md) · [可选工具的能力边界](skills/ui-craft-guard/references/tool-matrix.md)

```bash
python3 scripts/validate_skill.py
python3 scripts/validate_report.py examples/audit-cases/*.json
python3 -m unittest discover -s tests -v
```

静态扫描和 JSON 合约检查无法判断真实审美，也不构成 WCAG 认证；没有浏览器与用户任务测试时必须注明“未验证”。

## 贡献与许可

项目的文档采用**单一职责 / 单一权威来源**：执行规范在 `SKILL.md`，规则在 [Rulebook](skills/ui-craft-guard/references/design-principles.md)，证据契约在 [evidence-protocol](skills/ui-craft-guard/references/evidence-protocol.md)，可复制话术在 [prompt-recipes](skills/ui-craft-guard/references/prompt-recipes.md)，实际复现材料在 `examples/`。README 只提供索引和一次快速启动，不重复维护完整流程。

[贡献与文档维护准则](CONTRIBUTING.md) · [来源台账](skills/ui-craft-guard/references/source-ledger.md) · [MIT License](LICENSE)
