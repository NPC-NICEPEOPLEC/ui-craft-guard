# 可选工具矩阵（不要求全部安装）

| 工具 | 用来获得什么证据 | 典型步骤 | 不能证明 |
|---|---|---|---|
| [Playwright](https://github.com/microsoft/playwright) | 视口截图、任务步骤、焦点与交互回归 | 固定版本、视口、输入与数据 → 重放 → 保存回执 | 审美是否独特、真实用户一定满意 |
| [axe-core](https://github.com/dequelabs/axe-core) | 可检测的可访问性规则违规 | 页面稳定后运行扫描并人工复查 | 全量 WCAG 合规、完整易用性 |
| [Lighthouse](https://github.com/GoogleChrome/lighthouse) | 性能、页面质量与部分无障碍指标 | 固定 URL、运行条件和版本，比较前后 | 视觉品味、真实商业目标实现 |
| [Storybook](https://github.com/storybookjs/storybook) | 组件不同属性、异常/交互状态 | 核对故事覆盖、局部视觉回归 | 整站真实用户任务已完成 |
| [design-extract](https://github.com/Manavarya09/design-extract) | 从已有界面观察 token 与视觉语法的线索 | 对照项目正式设计系统与代码 | 提取出来的任何 token 都天然合理 |
| [oil-ui](https://github.com/oil-oil/oil-ui) | 视觉方向、截图迭代的设计工作流参考 | 看其公开方法，提炼非复制性原则 | 为本站提供唯一最佳视觉方向 |
| [DesignLint](https://github.com/rgranet/designlint-skill) | 设计意图及审计决策参考 | 借鉴先作设计决定再批评的顺序 | 其美学打分可直接成为客观标准 |
| [UX Agent Skills](https://github.com/uxuiprinciples/agent-skills) | UX 启发式、流程检查的分类参考 | 把 UX 问题映射用户任务，核实具体结果 | 无真实用户证据时证明所有人的行为 |

以上是**工具职责划分**，不是内置集成或背书。各工具有单独依赖、权限、许可证；本 Skill 的核心流程和 JSON 合约只要求 Python 标准库。工具未安装时降级到 `partial`/`limited`，如实标明未覆盖。参考项目方法需保留原创转述和来源，不复制其素材、代码或完整提示词。