# 四阶段教学演练：原创阅读工作台

> **证据性质：仓库自有演示，不是真实网站盲测。** 原始材料是 [刻意设置反模式的页面](anti-pattern.html) 和 [手动修订后的页面](revised.html)；两者由项目构造，**不代表 AI Agent 自主提出并实施了这些修改**。早先的 Chromium 截图和任务冒烟来自 [已保存的历史检查记录](screenshots/browser-smoke-results.json)，不是本次 Skill v0.2.2 的新真实项目实验。有关原始改版推理见 [case-study.md](case-study.md)。

这个演练说明如何使用 [四阶段提示词](../skills/ui-craft-guard/references/prompt-recipes.md)，并明确每个步骤能够证明什么、不能证明什么。

## ① 自主诊断（audit）

**任务与范围**：快速保存文章标题并浏览阅读清单；材料是两份原创 HTML，重点关注主任务和关键交互。若没有浏览器工具，能力为 `partial`，不能说自己完成了交互测试。

从仓库根目录运行源码启发式扫描：

```bash
python3 scripts/audit_ui.py examples/anti-pattern.html --format markdown
python3 scripts/audit_ui.py examples/revised.html --format markdown
```

审计报告应该：
- 分别给 FLOOR、STRUCTURE、TASTE、POLISH 检查覆盖状态。静态源码不能替代浏览器的可读性、焦点和任务结果。
- 从 visual_quality、usability、design_identity 三个独立维度解释发现；没有品牌 brief 时不能凭空发明品牌策略。
- 将扫描器的 `H01`、`A01` 等**启发式信号编号**与 Rulebook 的 **`rule_id`** 区分。比如“缺乏依据的渐变”可讨论 `C03`，但是否要修改仍需产品意图与真实页面观察。
- 同一条规则可以对应多个独立 `finding_id`，也可以合理决定 `retain` 或 `investigate`。

**本阶段没有本轮新生成的完整三维审计 JSON，也没有真实用户数据**。不要伪称已经运行过一个完整的 v0.2.2 Agent 自主审计。

## ② 根因与设计决策（audit 后续分析）

对照 [原有教学案例中的问题与决定](case-study.md)，尝试分组：装饰优先于阅读任务、缺少主操作、细节系统不一致、表单反馈/键盘风险。写出每组的反对解释：

- 对含渐变的首页，不是“紫色有罪”，而是问能否从产品定位解释它的价值。
- 对卡片圆角，不只读 CSS 数值，应看渲染后的边缘关系。
- 对表单问题，静态分析是线索，用户实际操作与反馈才更有说服力。

没有清晰证据的美学调整可以维持 `investigate`；不要为了给方案凑三种方向。

## ③ 执行改进（redesign，只有授权时）

演示仓库已经提供一份 [修订版页面](revised.html)，可以作为学习和前后比较的**样本**。它不是这份文档当场执行的代码修改。真实项目需要在批准范围后记录文件差异、原任务和状态回归，保留有效的原有选择。

## ④ 批判性对比（compare）

仓库现存材料：

| 证据 | 可复查资源 | 证明范围 |
|---|---|---|
| 早期浏览器报告 | [browser-smoke-results.json](screenshots/browser-smoke-results.json) | Chromium 的 375/768/1280 宽度下，修订演示页的横向溢出、提交反馈和键盘首焦点 |
| 旧版截图 | [anti-pattern-desktop.png](screenshots/anti-pattern-desktop.png) | 旧版在指定桌面视口的可见表现 |
| 新版移动截图 | [revised-mobile.png](screenshots/revised-mobile.png) | 新版移动端在截图时的可见表现 |
| 新版桌面截图 | [revised-desktop.png](screenshots/revised-desktop.png) | 新版桌面端在截图时的可见表现 |

可以依据截图、代码与历史测试作**有限的前后比较**，不能由此推断真实用户满意度、全面 WCAG 合规、跨浏览器表现或所有数据状态的正确性。同一 Agent 对自己改版的分析属于批判性自检，不能宣称为独立红队。

## 复现与后续真实验收

```bash
python3 scripts/validate_skill.py
python3 scripts/validate_report.py examples/audit-cases/*.json
python3 -m unittest discover -s tests -v
# 如已额外安装 Playwright + Chromium，可选择运行本项目的演示冒烟检查：
python3 scripts/visual_smoke.py
```

**真实网站盲测：未完成。** 下一步需要的证据是选择一个经授权的真实网站，记录事前问题、盲审输出（含误报和保留项）、经批准的改动、同条件复查与独立评审。只有完成这些，才能对实际 Skill 的审美判断能力形成更强结论。
