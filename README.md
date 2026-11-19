# UI Craft Guard

**面向 AI 编程代理的 UI 设计审计、改进与验收 Skill。**

它的职责不是把所有网页改成同一种“没有 AI 味”的风格，而是：**理解产品与用户任务，逐层审查真实界面，找出有证据的问题，保留合理设计，并验证修改结果。** “去 AI 味”是审美诊断中的一个应用场景，不是唯一目标，也不是设计标准。

> 当前版本：**v0.2.1** · 2026-11-19 · [SKILL.md](skills/ui-craft-guard/SKILL.md) · [更新记录](CHANGELOG.md) · [实际验收](VALIDATION.md)  
> 便携式 Agent Skill；并非独立运行的网页应用，也不会因为公开 GitHub 仓库而自动安装到任何客户端。

## 它解决什么问题？

适合：网站正在开发，但开发者不知道哪里有问题；页面有“模板感”，却不知道源于布局、内容还是视觉；想修复现有界面但不破坏功能和品牌；需要用截图、代码和用户任务检查某次改版是否真的改善体验。

工作方式是 **发现 → 证据 → 判断 → 最小调整 → 复查**。如果现有设计有明确产品理由，结论可以是“保留，不需要改”。

## 一张图理解审计体系

```text
产品与用户任务、品牌规范、现有界面
                ↓
① 四层审计骨架（来自 v0.1.0，完整保留）
   FLOOR → STRUCTURE → TASTE → POLISH
   每层记录：已检查 / 未检查；不要求每层都找出问题
                ↓
② 三个独立评价维度（v0.2.0 起）
   视觉质量 / 使用体验 / 设计个性与产品定位
   这是评价视角，不替代四层，也不合成一个总分
                ↓
③ 可追溯的证据与设计意图
   finding_id（本次发现）→ rule_id（原始规则）
   ↘ Evidence IDs（截图/源码/真实交互/品牌依据）
                ↓
④ 决策与回归
   change（调整）/ retain（保留）/ investigate（待验证）
   最小变更 → 相同条件复查
```

### ① 四层审计：查什么

| v0.1.0 既有层级 | 检查范围 | 例子 |
|---|---|---|
| **FLOOR** · 基础底线 | 可阅读性、键盘、焦点、对比度、状态与错误反馈 | 表单提交后没有结果 |
| **STRUCTURE** · 页面结构 | 信息优先级、操作入口、内容顺序、布局和响应式 | 手机首屏找不到主要操作 |
| **TASTE** · 设计判断 | 风格与产品的匹配、组件语言、无依据的装饰和模板痕迹 | 视觉强调色竞争，或品牌渐变被误判 |
| **POLISH** · 细节精修 | 字体、基线、图标、内外圆角、微动效及中文混排 | 卡片内外圆角冲突 |

原有 [规则库](skills/ui-craft-guard/references/design-principles.md) 和静态扫描器保留，**没有被三维评价替换**。检查过却没有问题的层级，应该记录“已检查，无明确发现”；没有检查能力时应写明缺口，不假装通过。

### ② 三维评价：怎样解释问题

| 独立维度 | 核心问题 |
|---|---|
| **visual_quality** · 视觉质量 | 当前布局、排版、层级和组件是否清晰、一致、协调？ |
| **usability** · 使用体验 | 用户想做什么，在哪一步遇到阻碍或额外成本？ |
| **design_identity** · 设计个性与定位 | 视觉选择是否有产品和品牌依据；哪些选择应该保留？ |

三维与四层相互交叉。例如“手机表单无法完成”是 `usability × FLOOR`；“品牌渐变其实合理”是 `design_identity × TASTE`，决策可以是 `retain`。不要用一份模糊的“UI 总分”掩盖差异。

### ③ 证据与决策：为什么这样判断

每条发现至少说明 **本次编号 `finding_id`**、**规则来源 `rule_id`**、所属层级、评价维度、Evidence ID、最强合理反证、决策、优先级和复查方法。

`rule_id` 使用原 [v0.1.0 规则表](skills/ui-craft-guard/references/design-principles.md) 中的 ID（如 `G02`、`F02`、`I02`）。如是项目自身规则，写 `PROJECT:slug`；**不能把本次问题编号冒充规则编号，也不能捏造规则来源**。详见 [证据协议](skills/ui-craft-guard/references/evidence-protocol.md) 和 [设计意图与反证](skills/ui-craft-guard/references/design-intent.md)。

## 如何使用

安装并确认客户端已加载 Skill 后，在项目上下文中输入：

```text
请使用 ui-craft-guard 的 audit 模式自主检查当前网站。
我还不知道有哪些问题，请先了解产品、页面、代码和已有品牌规范；
有浏览器能力时实际查看桌面/移动端并重放关键任务。

先逐一核对 FLOOR、STRUCTURE、TASTE、POLISH 四层，
记录已检查、未检查和真实证据；再从视觉质量、使用体验、
设计个性三个维度独立评价。

每条发现给独立 finding_id、原始 rule_id、Evidence ID、
最强反证、change/retain/investigate、优先级与复查方案。
明确指出哪些设计值得保留。本轮只审计，不修改代码。
```

后续可使用四种模式：`audit`（只审计）、`redesign`（保护已有产品的改版）、`build`（从任务和设计意图出发构建）、`compare`（相同条件对比版本）。

[审计模板](skills/ui-craft-guard/templates/AUDIT_REPORT.md) · [设计决策模板](skills/ui-craft-guard/templates/DESIGN_DECISIONS.md) · [更多话术](skills/ui-craft-guard/references/prompt-recipes.md)

## 安装与更新

**需要安装的是完整的 `skills/ui-craft-guard/` 目录，不是单独的 `SKILL.md`。** 它包含规则、模板、`VERSION` 和可独立运行的两个工具脚本。

用户级路径：

```text
~/.dsh/skills/ui-craft-guard/
~/.agents/skills/ui-craft-guard/
~/.claude/skills/ui-craft-guard/
```

从旧版升级到当前版，推荐浏览器下载 [main.zip](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/archive/refs/heads/main.zip)，解压并进入仓库根目录执行：

```bash
bash scripts/update_user_skills.sh
```

脚本**先复制校验，再备份旧版并替换**；不删除其他技能，不依赖 `git clone`。安装后查看三个目录的 `ui-craft-guard/VERSION`，应为 `0.2.1`。重新启动相关客户端再检查是否识别。详细见 [PUBLISH.md](PUBLISH.md)。

项目级**首次安装**可使用 `scripts/install.sh`；该脚本遇到已有目标会拒绝覆盖，不能当升级工具。

## 工具和证据边界

核心脚本仅使用 Python 3 标准库：

```bash
python3 scripts/validate_skill.py
python3 scripts/validate_report.py examples/audit-cases/*.json
python3 -m unittest discover -s tests -v
python3 scripts/audit_ui.py examples/anti-pattern.html --format markdown
```

- `audit_ui.py`：源码启发式扫描，**不是**自动审美评价或作者归因。
- `validate_report.py`：检查规则编号、四层覆盖、证据引用与决策条件；**不核实**截图、品牌研究或任务是否真的执行。兼容旧版 v0.2.0 JSON。
- `visual_smoke.py`：仓库内的可选 Playwright/Chromium 演示；真实项目必须自己定义实际页面和用户任务。
- Lighthouse、axe-core、Storybook、design-extract 等是可选工具或方法参考，**不是已绑定的内置服务**。[工具职责表](skills/ui-craft-guard/references/tool-matrix.md)

[合成反例](examples/audit-cases) 用于验证“品牌渐变保留 / 简洁后台保留 / 关键表单故障修复”的决策协议，**不是**真实商业网站的运行记录。原创演示截图、历史测试与 CI 记录见 [VALIDATION.md](VALIDATION.md)。

## 来源、约束与许可证

设计启发整理自公开讨论和工程实践；不是八篇原始帖子全部直读，也不代表原作者背书。作者、证据等级与核验范围见 [来源台账](skills/ui-craft-guard/references/source-ledger.md)。无障碍要求以 [WCAG 2.2](https://www.w3.org/TR/WCAG22/) 等规范为准。

不得为了“去 AI 味”牺牲用户任务、品牌识别、可访问性与真实数据；不能伪造测试、品牌资产或第三方素材授权。**一个可解释、可验证的“保留”结论同样有价值。**

MIT License · [LICENSE](LICENSE) · [CONTRIBUTING.md](CONTRIBUTING.md)
