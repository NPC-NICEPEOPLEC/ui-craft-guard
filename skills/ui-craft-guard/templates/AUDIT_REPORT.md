# UI Craft Guard — 审计报告模板 v0.2.1

- 项目 / 页面 / commit：
- 模式：audit / redesign / build / compare
- 用户与核心任务：
- 证据能力：full / partial / limited（原因及不可访问部分）：
- 参考品牌规范、现有 Design Tokens 和关键保护项：

## 1. 产品与设计意图

用户 / 产品任务 / 内容优先级 / 现有视觉语言：  
品牌依据与推断（区分真实资料和假设）：  
最强替代解释、保留条件及可能推翻判断的证据：

## 2. 四层审计覆盖（原有 v0.1.0 框架，**必填**）

| 层级 | 覆盖状态 assessed / not_assessed | 查看了什么 / Evidence IDs | 结果（包括已检查但无问题） | 不能判断的部分 |
|---|---|---|---|---|
| FLOOR | | | | |
| STRUCTURE | | | | |
| TASTE | | | | |
| POLISH | | | | |

**注意：** 四层是审计范围，不是必须各找一个缺陷；没发现可写“已检查，暂未发现缺陷”。如果没有真实条件检查某层，就写 `not_assessed` 和限制，不能伪称全部通过。

## 3. 三维独立评价（与四层交叉，不取代四层）

### A. visual_quality / 视觉质量
状态 supported / hypothesis / not_assessed：  
主要观察、优势与不足、关联 Evidence IDs：  
不确定性及下一步：

### B. usability / 使用体验
状态 supported / hypothesis / not_assessed：  
用户任务及实际测试步骤、阻塞或额外操作：  
未执行的交互、键盘/响应式/错误状态：

### C. design_identity / 设计个性与产品定位
状态 supported / hypothesis / not_assessed：  
品牌定位依据、支持定位的设计、可能违背定位的选择：  
最强反证与应该保留的设计：  

## 4. Evidence 索引

| Evidence ID | kind / status（observed、inferred、unavailable） | 精确定位（源码/截图/视口/操作） | 观察或回放结果 | 限制 |
|---|---|---|---|---|
| E01 | screenshot / observed | 375px 首页截图 | 标题发生截断 | 无法证明表单行为 |

未经实际运行，不得填写“任务通过”或“已截图”。

## 5. 发现、规则来源和决策

| finding_id（本次发现） | rule_id（原规则） | dimension + layer | Evidence IDs / 位置 | 判断、反证与影响 | change / retain / investigate | P0–P3 | 最小调整及复查 |
|---|---|---|---|---|---|---|---|
| ISSUE-01 | F02 | visual_quality + STRUCTURE | E01 / 移动端标题 | 文字截断影响理解；复核字体加载 | change | P2 | 修复换行，同视口复查 |
| ISSUE-02 | G02 | design_identity + TASTE | E02 / 品牌首屏 | 渐变有品牌依据，应保留 | retain | P3 | 不改；品牌更新时复查 |

- `finding_id`：本次审计独立编号，例如 ISSUE-01。
- `rule_id`：必须对应 [原规则库](../references/design-principles.md) 已公布的规则，如 G02、F02、I02。项目独有约束使用 `PROJECT:slug`，不得编造规则来源。
- 问题可属于一个层级并被多个维度讨论；报告中的主要维度必须明确。
- 不能用原始规则编号作为本次问题的唯一身份；一个规则可对应多个问题。
- 四层审计覆盖与发现总数**没有强制一对一关系**。

## 6. 保留项、优先级和实施建议

已经合理、不建议修改的选择（有证据）：  
最值得先处理的 1–3 项、预计影响与修改成本：  
尚需调查的假设：  

## 7. 真实修改与回归（只在执行后填写）

文件 / commit / before-after 同视口截图：  
任务重放：预期 / 实际 / 环境：  
已通过、未通过、未执行、残余风险：

## 8. 可选 JSON 合约验证

仓库根目录运行 `python3 scripts/validate_report.py examples/audit-cases/brand-gradient.json`；仅安装 Skill 时运行其自带 `scripts/validate_report.py`。v0.2.1 校验独立 `finding_id` / `rule_id`、四层覆盖和已存在的证据前置条件；v0.2.0 旧 JSON 仍可通过旧格式兼容分支。JSON 检查**不是**审美品质评定，也不核实截图真实性。
