# ManXis Token Audit 样板包

日期：2026-05-03

## 核心产品

ManXis Token Audit 是给长任务 Agent 用户的一次本地诊断交付：读取客户提供的 redacted trace、账单截图、任务描述和最终输出，找出 token 浪费来源，给出 before/after 成本表和可执行 workflow patch。

## 交付对象

| ICP | 成交理由 |
|---|---|
| 高频 Claude Code / Codex / Cursor 用户 | 他们已经有长任务、上下文膨胀、compact、失败重试和账单痛感。 |
| AI automation agency | token 成本会直接影响每个客户项目毛利。 |
| Agent 工具团队 | 他们有真实用户流量和 runtime cost，愿意优化毛利和可靠性。 |
| LLM observability 用户 | Helicone / Langfuse / LangSmith trace 能直接作为 audit 输入。 |

## 输入

| 输入 | 格式 | 最小要求 |
|---|---|---|
| 任务描述 | markdown / text | 目标、工具、模型、期望输出。 |
| trace / logs | JSONL / markdown / screenshots | 至少包含 20 次以上模型或工具调用，或 50k+ tokens。 |
| 成本数据 | billing screenshot / CSV / dashboard export | 至少有单任务 token 或金额估计。 |
| 最终输出 | markdown / PR / report / app link | 用于质量评估。 |
| 隐私约束 | checklist | 标注敏感字段、可处理范围、可公开范围。 |

## 输出

| 输出 | 作用 |
|---|---|
| Token footprint | 标出 input、output、cached、tool-output、retry tokens。 |
| Waste map | 标出重复上下文、冗长工具输出、弱记忆边界、低质量检索、失败重试。 |
| Before/after table | 展示 tokens、cost、runtime、retries、quality risk。 |
| Workflow patch | 给 prompt、memory、retrieval、tool return、routing、compact threshold 的修改建议。 |
| Savings estimate | 按月任务量计算节省金额和可收费空间。 |

## 成功标准

| 指标 | 合格线 |
|---|---|
| 成本下降 | 同类任务目标 30%-80%，按真实 trace 单独判断。 |
| 质量维持 | 输出可用性、事实完整性、任务完成度不下降。 |
| 可解释性 | 每个 savings claim 对应 trace 证据。 |
| 可执行性 | 客户能按 patch 修改自己的 workflow。 |
| 商业信号 | 客户愿意继续给 3-5 个任务或进入 paid pilot。 |

## 文件说明

| 文件 | 用途 |
|---|---|
| `audit_template.md` | 客户交付模板。 |
| `sample_audit.md` | 用本地 Codex/company-research-agent demo 填出的样例。 |
| `metrics.csv` | Token Audit 指标表结构。 |
| `privacy_checklist.md` | 本地/匿名 trace 处理说明。 |
| `pricing.md` | 试点和标准报价。 |
| `example_tasks.md` | 3 个可马上跑 benchmark 的任务。 |

## 直接推荐

第一批先卖 `Local Token Audit`，价格从 $500 pilot 开始。客户给一条真实长任务 trace，ManXis 交付一份成本浪费报告和 workflow patch。
