# UI Craft Guard — v0.2.0 三维审计报告

- 项目 / 页面 / commit：
- 审计模式：audit / redesign / build / compare
- 用户与主要任务：
- **证据能力：** full / partial / limited（理由：）
- 设计规范或品牌资产（有 / 无 / 推断，出处：）
- 无法访问的区域与未测行为：

## 一、设计意图（先理解，勿先判错）

产品目标、用户、内容节奏、既有品牌系统：  
设计意图假设与来源：  
可能的替代解释：  
哪些选择已经有效、值得保留：  
反证或使判断改变的证据：

## 二、证据索引（每条可追踪）

| Evidence ID | 类型 / observed or inferred | 位置（路径:行、URL、视口） | 实际观察 / 测试步骤与结果 | 局限 |
|---|---|---|---|---|
| E01 | screenshot / observed | homepage.png, 375×812 | 某段标题被截断 | 无法证明按钮可点击 |
| E02 | task_test / observed | 表单提交 | 重放步骤、预期与实际 | 仅覆盖该输入数据 |

不允许把截图视觉观察写成任务测试通过；未知就写未知。

## 三、三维独立审计（**禁止合并为一个总分**）

### A. 视觉质量 visual_quality
- 结论：supported / hypothesis / not_assessed
- 观察依据、涉及范围与主要问题：
- 已经有效的视觉选择：
- 不确定点与需补充的证据：

### B. 使用体验 usability
- 结论：supported / hypothesis / not_assessed
- 用户目标 / 主要操作路径：
- 实测阻塞、误解或多余决策点（如未运行标记未验证）：
- 可访问性、状态与响应式：
- 未覆盖的用户任务：

### C. 设计个性与产品定位 design_identity
- 结论：supported / hypothesis / not_assessed
- 产品定位来源与当前视觉语言：
- 哪些设计选择支持定位，哪些违背（有证据才下结论）：
- **最强反证/替代解释**，以及可保留的理由：
- 哪些问题只能暂定 hypothesis：

## 四、发现与决策

| ID | 维度 + FLOOR/STRUCTURE/TASTE/POLISH | 位置和 Evidence IDs | 判断与最强反证 | change/retain/investigate | 优先级 | 最小调整及回查方式 |
|---|---|---|---|---|---|---|
| F01 | usability + FLOOR | 表单 / E02 | 点击无效；确认无权限异常 | change | P0 | 修复提交后原路径重放 |
| I01 | design_identity + TASTE | 首屏 / E03 | 品牌色有正式来源，非模板惯性 | retain | P3 | 不改，保留对比检查 |

每条改动采用 **判断 → 证据 → 最小调整 → 复查结果**；审计轮只有计划，不能写“已复查通过”。

## 五、推荐优先级与保留事项

- P0 / P1 / P2 / P3 的依据（影响、范围、改动成本）：
- 最值得先处理的 1–3 项：
- **至少说明一个应保留的选择**；如果页面无法访问，写明为何无法判断。
- 不采用某条“反 AI 味规则”的原因：

## 六、修改与验收（仅在真正实施后填写）

- 实际修改文件 / commit：
- before/after 同数据、同视口截图与测试环境：
- 用户任务重放（预期 / 实际）：
- 已通过：
- 未通过或未执行：
- 回归风险：
- 仍待验证的假设：

## 七、机器可读配套记录（可选但推荐）

按 `examples/audit-cases/` 的 JSON 结构记录核心结论，运行：

```bash
python3 scripts/validate_report.py examples/audit-cases/brand-gradient.json
```

此检查仅验证记录完整度、证据引用和决策前提，不自动裁定审美优劣。
