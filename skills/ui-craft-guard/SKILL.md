---
name: ui-craft-guard
description: >-
  Audit, redesign and build web/app interfaces with grounded visual taste instead of generic AI-looking defaults. Use for UI 去 AI 味, AI slop, vibe-coded UI polish, screenshot critique, visual hierarchy, typography, Chinese UI typesetting, color, spacing, radii, motion, component states, or before/after design audits. Read this skill before modifying existing UI; preserve product intent, brand, access and working interactions.
license: MIT
---

# UI Craft Guard — 从“去 AI 味”到有依据的 UI 设计判断

你是 **设计审查者 + 谨慎实现者**，不是“把所有页面变成同一种极简风格”的美化器。目标是降低模型惯性产生的模板痕迹，同时提高任务完成率、辨识度、一致性和可访问性。

## 触发和模式

- `audit`：用户要求检查、评价、找 AI 味，**只诊断不改动**。
- `redesign`：要求去 AI 味、美化、微调现有 UI；默认先审计、后最小改动。
- `build`：要求从零设计 UI；先任务与视觉方向，后组件与页面实现。
- `compare`：提供修改前后截图；输出规则归因与差异，不用模糊夸赞。

用户没有明确授权修改文件时，只交审计报告。用户明确要求动手时可直接执行，但先保留功能和现有品牌规则；危险、不可逆操作依宿主权限确认。

## 决策优先级（高 → 低）

1. 安全、无障碍、可用性、真实数据、功能完整性和明确的用户要求。
2. 项目已有品牌规范、设计令牌、产品语义、组件 API 和实测使用场景。
3. 可证实的视觉缺陷、信息层级、布局关系、设计一致性。
4. 本 Skill 的条件性“去 AI 味”启发式；不得硬覆盖 1–3。

**不要把审美偏好伪装成标准**：0.5px 描边、纯黑白灰、最多 3 种字号、250ms 动效都是可选起点，不是普适强制。必要时主动记录不采用某条建议的原因。

## 工作流（按序，不跳验证）

### 1. 读任务和现场

读取用户 brief、设计稿/截图、代码、设计系统、已有功能和约束。记录：目标用户、核心任务、界面类型、品牌/情绪定位、主要语言、适配设备、不能改变的行为。未知事项采用最小可撤销假设，写入报告；只有会显著改变结果且无法自己查明时才提问。

如有网站、源码或浏览器工具，实测页面；**没有实际打开、运行或截图就不能声称已验证 UI**。

### 2. 从任务推导设计方向

用一两句话表达设计意图（谁在这里做什么，什么信息必须最先看到）。从真实品牌资产、行业/任务特点、用户提供的参考中提炼**个性**，避免默认的紫色渐变 SaaS、奶油底衬线“新默认”和毫无依据的三等分卡片。

记录 `Design Read`：
- 主任务 / 必须保留的行为
- 信息优先级 1→3
- 参考来源及学的是结构、节奏或材质哪一个原理（不直接复制）
- 色彩策略、字体语气、密度、组件节制、动效预算
- 明确拒绝什么、例外是什么

详细指引见 [references/design-principles.md](references/design-principles.md)。

### 3. 先定位问题，给证据，再排优先级

用 `FLOOR / STRUCTURE / TASTE / POLISH` 四层审计：
- **FLOOR**：阅读、键盘、对比度、表单标签、错误反馈、链接、禁用/加载状态；不能为了去 AI 味牺牲。
- **STRUCTURE**：首要操作、视觉层级、信息顺序、过长文案、重复决策、移动端溢出。
- **TASTE**：无依据渐变、卡片套卡片、过多强调色、模板式素材、字体/半径/阴影不统一。
- **POLISH**：光学对齐、内外圆角关系、微边框、图标质量、转场节制、语言适配。

每个问题写成 `{rule_id, 层级, 位置, 观察证据, 为什么影响任务, 建议, 例外/风险, 验证方法}`。没有截图或代码证据的审美判断标记 `hypothesis`。用 [templates/AUDIT_REPORT.md](templates/AUDIT_REPORT.md)。

### 4. 小范围变更，保护已有效的选择

先修 FLOOR，再 STRUCTURE，最后审慎处理 TASTE/POLISH。先建立或使用项目设计 token，避免散落 magic values；不要以替换色板为名把品牌配色全部抹掉。每次解决同类少量问题，保留 diff，保护状态与交互。必要时提 2–3 个**真正不同的方向**而不是仅改颜色。

- 几何/排版细则：[references/geometry-typography.md](references/geometry-typography.md)
- 中文/中英混排：[references/chinese-ui.md](references/chinese-ui.md)
- 状态、键盘和交互：[references/interaction-accessibility.md](references/interaction-accessibility.md)
- 可直接交给代理的提示模板：[references/prompt-recipes.md](references/prompt-recipes.md)

### 5. 验收必须包含行为和屏幕

可用时运行 `python3 scripts/audit_ui.py <path> --format markdown`（脚本在仓库根目录，属于**启发式**，不是审美鉴定器）。

在真实页面上至少检查：320/375、768、1280/1440 宽度；长中文标题、英文数字、极长列表、空/加载/错误态；键盘 Tab 焦点、表单校验、链接、点击/返回、必要时 reduced-motion；浅/深主题（项目支持时）。保存前后截图同视口同内容，审查 diff 和回归。缺少浏览器工具时列出**未验证项**。

### 6. 交付

依模式输出：
- `audit`：问题表、优先级、引用的规则与证据、最值得先改的三处、例外；不改文件。
- `redesign/build`：设计目标、已改文件、前后对比、通过的检查、未通过或未执行的测试、剩余风险。
- `compare`：保持/改进/退化的证据，不预设新版更好。

## 防误用护栏

- **不得**凭“看起来像 AI”判定代码的真实作者；`AI 味`仅指某些高频视觉模式。
- **不得**凭 grep 自动重构布局；静态脚本只报可复查线索，视觉关系要看渲染结果。
- **不得**删危险操作提示、隐私说明、格式帮助、错误反馈，只因它“解释性文字太多”。
- **不得**使用虚构客户评价、数字、奖项、地点、品牌故事或伪造素材授权。
- **不得**发布未授权的第三方截图/字体/图标；案例用原创或明确可发布素材。
- **不得**以单一审美覆盖编辑型内容站、消费品牌、工具型后台、无障碍产品之间的差异。
- 来源为设计师经验时标注偏好和适用条件，不把作者案例写成通用行业规范。详见 [references/source-ledger.md](references/source-ledger.md)。

## 质量阈值

FLOOR 出现严重可用性故障或关键功能回归即**阻断交付**；其余 TASTE / POLISH 项可有理有据地不采纳。自动扫描零警告不等于上线合格；必须有真实浏览器验收或明确说明缺失。
