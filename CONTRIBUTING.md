# Contributing · 规则、证据与文档维护

欢迎改进 UI 审计规则、可复核的证据、工具和使用体验。禁止直接复刻第三方文章、上传未授权的截图/字体或编造测试结果；真实产品样本需确认公开授权和隐私边界。

## 一个信息只维护一份权威定义

| 内容的权威来源 | 只负责什么 | 其他文件如何使用 |
|---|---|---|
| `skills/ui-craft-guard/SKILL.md` | 触发方式、`audit / redesign / build / compare`、执行顺序、操作权限、验收原则 | README 简述并链接；提示词仅引用执行规则 |
| `references/design-principles.md` | 原有设计规则、真实 `rule_id` 和适用例外 | 不在提示词中重新发明规则 ID |
| `references/evidence-protocol.md` | 证据种类与门槛、四层覆盖、三维结论和报告 JSON 契约 | 报告模板与示例只消费该契约 |
| `references/prompt-recipes.md` | 场景索引、完整可复制的四阶段话术、专项话术 | README 仅保留**一个**快速启动示例和链接 |
| `templates/` | 实际报告/决策产物格式 | 示例可引用，不能再定义竞争性字段 |
| `examples/` 与 `VALIDATION.md` | 可复现输入、实际检查、失败记录、限制及 CI 回执 | README 可以概括，但不能把合成数据写成实测 |

真实网站测试优先遵守 [盲测协议模板](examples/real-site-evaluation-protocol.md)，结果需同时公布误报、漏报、保留判断和未测试项，不能只展示成功前后截图。

**禁止三份完整工作流并行维护。** 新的执行义务先修改 `SKILL.md` 或相应规范来源；用户话术只说明调用方式；README 只交代项目价值、架构简图、安装和文档入口。若仅新增一个使用场景，优先修改 `prompt-recipes.md`，不必改动所有文件。

## 提交前的变更影响检查

1. **意图和权限**：这是执行规则变更、话术演示、报告契约变更还是工具行为变更？对 `audit` 禁止写入、`redesign` 需用户授权等边界有无冲突？
2. **旧能力兼容**：保留 FLOOR / STRUCTURE / TASTE / POLISH 全部覆盖；三维 `visual_quality / usability / design_identity` 独立；`finding_id / rule_id / Evidence IDs` 分离。未实际检查不能记为 assessed。
3. **避免误判**：允许 `retain` 和 `investigate`；记录最强反证。不要为四层凑缺陷，不将反模板静态匹配当作真实设计缺陷。
4. **证据透明**：案例必须明确标识“构造案例”“原创演示的历史测试”或“真实网站测试”，附可复现步骤、视口、任务及未测项。同一 Agent 自评不能标记成独立红队。
5. **只更新受影响文件**：不把完整版话术塞进 README 或 SKILL；避免复制规则表、测试数据和版本常量。
6. **版本与验收**：`skills/ui-craft-guard/VERSION` 是 Skill 版本来源；`schema_version=0.2.1` 是单独的审计 JSON 契约。若便携 Skill 文件改变应升级 Skill 版本，并记录 CHANGELOG、同步 README；旧 JSON 是否兼容须明确。
7. **测试和回读**：在 PR/合并前执行下面的检查，保留失败及修复记录。合并后重新读取 GitHub `main` 的关键文件和 CI 结果。不能用“准备测试”代替完成记录。

```bash
python3 scripts/validate_skill.py
python3 scripts/validate_report.py examples/audit-cases/*.json
python3 -m unittest discover -s tests -v
```

结构检测只能降低遗漏风险，不证明真实审美判断。外部真实网站的盲测、独立评价与用户行为证据需要另外开展，不能借用合成案例的“observed”。

## 新增设计规则的证据要求

请写清来源链接、作者、可核对范围、规则适用与不适用条件、证据等级、最强反例、原始 `rule_id` 的归属以及可复查步骤。启发式检测还需解释误报率或典型误报原因，不能以工具自动发现代替设计决策。
