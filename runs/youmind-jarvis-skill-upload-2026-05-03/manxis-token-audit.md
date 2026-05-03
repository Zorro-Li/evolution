# ManXis Token Audit

ID: `manxis-token-audit`

## Description

把长任务 Agent trace 拆成 token footprint、waste map、before/after 成本表和 workflow patch。用于验证 ManXis 的付费 pilot。

## Sources

- `runs/manxis-token-audit-pack-2026-05-03/README.md`
- `runs/manxis-leads-2026-05-03/README.md`
- `runs/manxis-company-research-demo-2026-05-03/README.md`

## Instruction

# ManXis Token Audit

你的目标是把一条真实长任务 Agent trace 变成可收费的优化报告。

## 输入
- 任务描述：目标、工具、模型、期望输出。
- trace/log：JSONL、Markdown、截图或 observability export。
- 成本数据：token、金额、耗时、重试次数。
- 最终输出：PR、报告、应用、文档或运行结果。
- 隐私限制：哪些字段需要匿名、保留、删除或本地处理。

## 拆解维度
1. Token footprint：input、output、cached、tool-output、retry。
2. Waste map：重复上下文、冗长工具输出、弱记忆边界、低质量检索、失败重试、cache miss。
3. Quality risk：压缩后可能丢失的事实、代码、引用、边界条件。
4. Workflow patch：prompt、memory、retrieval、tool return、routing、compact threshold。
5. Savings estimate：按月任务量估算节省金额和可收费空间。

## 输出格式
```markdown
# Local Token Audit

## Executive Verdict
## Token Footprint
## Waste Map
## Quality Risks
## Recommended Workflow Patch
## Before / After Estimate
## Evidence Table
## Next Pilot Step
```

## 验收
- 每个 savings claim 对应 trace 证据。
- 报告必须能转化为一条客户可执行修改。
- 首个 pilot 报价从 `$500` 开始。
