# 来源台账与证据分级

研究日期：2026-11-19。主题入口：https://x.com/bruc3van/status/2115963644811116732

原始 X 页面通过公开网页抓取遇到 403；可读的原帖镜像：https://instalker.org/bruc3van/status/2115963644811116732 。该作者本人随后说明部分引用链接显示不完整。因此本仓库**不声称已逐条核验八篇原始 X 帖**。下表说明实际读取的内容、转述链及 Skill 如何使用，供后续更正。

证据等级：`A` 作者署名的完整原文/文章可读（通过镜像亦标明）；`B` 作者文本的转载/转推或原文片段可读；`C` 仅汇总推文转述；`D` 本仓库自主工程推论。此分级衡量**可追溯性**，不代表观点的科学真实性。

| 作者 | 证据等级 | 核验范围 | 具体来源 | Skill 取用与限度 |
|---|---|---|---|---|
| @Kubai087 枯白 | B | 已找到作者署名、被转推的 #004 内容（嵌套圆角、连续曲率及适用的 CSS）；原始 X URL 仍无法直接读取 | [作者转推全文](https://xitter.gq/tuttihq) · [汇总帖](https://instalker.org/bruc3van/status/2115963644811116732) | 几何一致性和条件支持的连续圆角；不是强制公式 |
| @ZaynHao | B | 10 条 UI 设计提示词，可读转推全文 | [转推镜像](https://teapaw.org/aaras_v) · [整理摘要](https://inspirationworld.ai/zh-cn/prompts/zaynhao-ten-ui-polish-prompts) | 文案、色阶、对齐、边框、动效、字号、决策点、阴影；均属条件性建议 |
| @ianneo_ai 伊恩 | B | 作者关于 Gleb 案例“颜色留给内容”的转述/账号榜单摘录 | [作者摘要/摘录](https://xbangdan.com/account/ianneo_ai/) | 降低 chrome 视觉噪声；适用于内容优先界面，**非所有页面必须黑白灰** |
| @dingyi 丁一 | B | AI slop 特征清单转载，内含原帖链接 | [转载清单](https://2libra.com/post/frontend/hCmF2gG?commentId=b0eb2575-41a6-4967-9a6c-410252ee9a0f) · [原帖](https://x.com/dingyi/status/2115790005423734818) | 作为反模式检查，不把某个字体/配色本身定性为差 |
| @Xian0063 弦 | A（镜像） | 文章正文中 8 条原则、5 个 Skill 介绍及注明示例不是实际 Skill 运行的免责声明 | [署名全文](https://teapaw.org/Xian0063/article/2114306504778256445) | 目标与任务先行、拆解不复制、小步迭代、真实反馈 |
| @yanliudreamer | B/C | 10 个组件工具库文章存在的确认；可直接核对的项目仅部分，例如 Spline | [作者主页镜像](https://teapawt.org/yanliudreamer) · [汇总帖](https://instalker.org/bruc3van/status/2115963644811116732) | 有目的地查找可靠组件与素材库；**不伪造完整十项清单** |
| @ricouii RicoUI | B | 作者关于中文字体加载、字体栈、字体子集和 CDN 风险的完整转推文本 | [可读转推](https://teapaw.org/x_czyt/reposts) | 本地化字体栈、不同平台测试、长中文标题回归 |
| @remixdesigner | C | Bruce 只概述 Apple Preview 图标在 Clear 模式增加层级的个案，未找到原始案例正文 | [汇总帖](https://instalker.org/bruc3van/status/2115963644811116732) | 图标不应只缩放同一资产，应检验浅/深/透明背景的可辨识度；属本仓库归纳 |

## 与工程/无障碍规范的独立交叉核验

- [Agent Skills 官方规范](https://agentskills.io/specification)：`SKILL.md` frontmatter 与按需加载资源。
- [Radix Colors Scale](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale)：色阶用途；不代表所有项目必须使用 Radix。
- [MDN corner-shape](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)：`superellipse()` 支持和 `border-radius` 关系；渐进增强且要浏览器兼容性检查。
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)：文本对比、键盘、焦点和界面状态等约束；设计师偏好不能豁免。

## 原创性与署名规则

本 Skill 是对多个公开讨论的**原创流程化归纳**，不是复制作者的提示词全文，也不宣称获得其背书。只保留必要的短摘要和可追踪 URL，不随仓库分发第三方截图、文章全文、图标或字体。若原始帖出现勘误，维护者应更新此台账、具体规则及变更日志。

## v0.2.0 的方法参考（不同于上文 X 来源）

2026-11-19 读取了以下公开仓库 README，用于**工作流分工**，不用于硬性审美打分，也不代表获得其作者认可：

- [oil-oil/oil-ui](https://github.com/oil-oil/oil-ui)：单一明确视觉方向、需要时多个真正不同方向、真实浏览器截图迭代。
- [rgranet/designlint-skill](https://github.com/rgranet/designlint-skill)：在编码前明确用户和设计决策，审计已有界面时主动批评。
- [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)：观察现有 token 和 DOM 视觉语言的线索，必须与项目正式设计系统对照。
- [uxuiprinciples/agent-skills](https://github.com/uxuiprinciples/agent-skills)：UX smells、界面评估和用户流程检查的拆分方式。

这些项目本身的评分/榜单、Star 数和许可证不构成本 Skill 的质量证据；v0.2.0 未复制其原始代码或截图。 
