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

## v0.2.0：三层机制、三维结论、四层问题分类

- **审计判断层**：先理解产品任务，独立评价 `visual_quality`（视觉质量）、`usability`（使用体验）、`design_identity`（设计个性与产品定位）。三个维度都要独立说明 observed / hypothesis / not_assessed，**禁止合成 UI 总分**。
- **可验证证据层**：所有发现绑定可追踪 Evidence ID（种类、来源位置、实际观察、验证状态）；工具扫描只是线索。没有实际运行页面或任务，就不声称通过。
- **设计意图层**：先看品牌/用户/内容目标，写设计意图假设、最强反证与保留条件，再决定 `change` / `retain` / `investigate`。**有理由不修改，就是合法且常见的好结果**。
- 原有 `FLOOR / STRUCTURE / TASTE / POLISH` 继续是每个发现的**问题层级**，不替代三个评价维度。审计分类与决策分别记录，避免互相混淆。

完整决策门槛见 [references/evidence-protocol.md](references/evidence-protocol.md)；定位和反证见 [references/design-intent.md](references/design-intent.md)；可选工具的能力边界见 [references/tool-matrix.md](references/tool-matrix.md)。

## 工作流（按序，不跳验证）

### 1. 读任务和现场

读取用户 brief、设计稿/截图、代码、设计系统、已有功能和约束。记录：目标用户、核心任务、界面类型、品牌/情绪定位、主要语言、适配设备、不能改变的行为。未知事项采用最小可撤销假设，写入报告；只有会显著改变结果且无法自己查明时才提问。

如有网站、源码或浏览器工具，实测页面；**没有实际打开、运行或截图就不能声称已验证 UI**。先声明能力等级 `full`（页面、源码、真实任务）/ `partial`（部分源码或静态截图）/ `limited`（仅描述），不可访问区域必须记录。

### 2. 从任务推导设计方向

用一两句话表达设计意图（谁在这里做什么，什么信息必须最先看到）。从真实品牌资产、行业/任务特点、用户提供的参考中提炼**个性**，避免默认的紫色渐变 SaaS、奶油底衬线“新默认”和毫无依据的三等分卡片。

记录 `Design Read`（包含来源、最强合理反证和保留设计）：
- 主任务 / 必须保留的行为
- 信息优先级 1→3
- 参考来源及学的是结构、节奏或材质哪一个原理（不直接复制）
- 色彩策略、字体语气、密度、组件节制、动效预算
- 明确拒绝什么、例外是什么

详细指引见 [references/design-principles.md](references/design-principles.md)。

### 3. 三维独立审计 → 四层归因 → 证据门槛 → 优先级

先分别回答：

- **视觉质量**：具体哪里的信息层级、对齐、排版或响应式存在问题？证据来自哪张截图/哪段源码？
- **使用体验**：谁要做什么任务，阻塞发生在哪一步，是否有实际重放记录？未经执行不能宣称功能失败或通过。
- **设计个性与定位**：视觉选择怎样支持/违背真实产品意图？有哪些替代解释？有品牌证据时允许直接保留；缺资料时先 investigate。

每个发现再归入 `FLOOR / STRUCTURE / TASTE / POLISH` 四层：
- **FLOOR**：阅读、键盘、对比度、表单标签、错误反馈、链接、禁用/加载状态；不能为了去 AI 味牺牲。
- **STRUCTURE**：首要操作、视觉层级、信息顺序、过长文案、重复决策、移动端溢出。
- **TASTE**：无依据渐变、卡片套卡片、过多强调色、模板式素材、字体/半径/阴影不统一。
- **POLISH**：光学对齐、内外圆角关系、微边框、图标质量、转场节制、语言适配。

每个问题写成 `{id, 维度, 层级, 位置, Evidence IDs, 影响, 最强反证, change/retain/investigate, 最小调整, 验证}`。只有真实观察支持的结论才能建议 `change`；仅靠静态反模板扫描不可直接修改。设计个性要修改，必须有实际品牌/用户定位证据；否则先调查。保留项同样需要解释。参见 [templates/AUDIT_REPORT.md](templates/AUDIT_REPORT.md)；可选机器可读记录以本 Skill 目录内的 `scripts/validate_report.py` 校验，但该工具不判断审美真实性。

### 4. 小范围变更，保护已有效的选择

先修 FLOOR，再 STRUCTURE，最后审慎处理 TASTE/POLISH。先建立或使用项目设计 token，避免散落 magic values；不要以替换色板为名把品牌配色全部抹掉。每次解决同类少量问题，保留 diff，保护状态与交互。必要时提 2–3 个**真正不同的方向**而不是仅改颜色。

- 几何/排版细则：[references/geometry-typography.md](references/geometry-typography.md)
- 中文/中英混排：[references/chinese-ui.md](references/chinese-ui.md)
- 状态、键盘和交互：[references/interaction-accessibility.md](references/interaction-accessibility.md)
- 可直接交给代理的提示模板：[references/prompt-recipes.md](references/prompt-recipes.md)

### 5. 验收必须包含行为和屏幕

可用时运行本 Skill 目录内的 `python3 scripts/audit_ui.py <path> --format markdown`（属于**启发式**，不是审美鉴定器）。安装到 `~/.dsh/skills/ui-craft-guard/`、`~/.agents/skills/ui-craft-guard/` 或 `~/.claude/skills/ui-craft-guard/` 后，以对应 Skill 目录为脚本起点；仓库开发可使用仓库根目录的同名脚本。

在真实页面上至少检查：320/375、768、1280/1440 宽度；长中文标题、英文数字、极长列表、空/加载/错误态；键盘 Tab 焦点、表单校验、链接、点击/返回、必要时 reduced-motion；浅/深主题（项目支持时）。保存前后截图同视口同内容，审查 diff 和回归。缺少浏览器工具时列出**未验证项**。

### 6. 交付

始终分开输出三个评价维度，不用一个模糊的设计质量分。注明：证据能力等级、Evidence 索引、每维结论、发现及决策、保留项、需复查事项。

依模式输出：
- `audit`：三维独立结论、证据清单、问题优先级、最值得先改的三处、明确保留项和反证；不改文件。
- `redesign/build`：设计目标、已改文件、前后对比、通过的检查、未通过或未执行的测试、剩余风险。
- `compare`：保持/改进/退化的证据，不预设新版更好。

## 防误用护栏

- **不得**将三个审计维度合成一个虚假的客观总分；缺少反证、品牌依据时不得直接否决设计。
- **不得**凭“看起来像 AI”判定代码的真实作者；`AI 味`仅指某些高频视觉模式。
- **不得**凭 grep 自动重构布局；静态脚本只报可复查线索，视觉关系要看渲染结果。
- **不得**删危险操作提示、隐私说明、格式帮助、错误反馈，只因它“解释性文字太多”。
- **不得**使用虚构客户评价、数字、奖项、地点、品牌故事或伪造素材授权。
- **不得**发布未授权的第三方截图/字体/图标；案例用原创或明确可发布素材。
- **不得**以单一审美覆盖编辑型内容站、消费品牌、工具型后台、无障碍产品之间的差异。
- 来源为设计师经验时标注偏好和适用条件，不把作者案例写成通用行业规范。详见 [references/source-ledger.md](references/source-ledger.md)。

## 质量阈值

FLOOR 出现严重可用性故障或关键功能回归即**阻断交付**；其余 TASTE / POLISH 项可有理有据地不采纳。自动扫描零警告不等于上线合格；必须有真实浏览器验收或明确说明缺失。
