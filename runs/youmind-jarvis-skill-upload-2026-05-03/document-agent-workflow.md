# 文档 Agent 工作流拆解

ID: `document-agent-workflow`

## Description

把 PDF、OCR、表格、图表、合同、报告等复杂文档处理成 parse/extract/index/retrieve/action/eval 流程，要求字段有来源、置信度和验收样例。

## Sources

- `runs/x-creator-watch/2026-05-03/03_skill_distillation.md`

## Instruction

# 文档 Agent 工作流拆解

你的目标是让 Agent 稳定处理复杂文档，而不是只做一次性总结。

## 输入
- 文档集合和文件类型。
- 下游任务：问答、抽取、审计、报告、比较、入库、自动操作。
- 输出 schema。
- 失败模式：版式、表格、图表、手写、引用、跨页字段、OCR 噪音。
- eval 样本和指标。

## 工作流
1. 判断文档领域和下游 Agent 任务。
2. 拆成 parse、extract、index、retrieve、action、eval 六段。
3. 选择解析方式：本地 parser、LlamaParse、OCR、MCP、SDK 或人工校验。
4. 为每个字段定义 schema、source anchor、confidence。
5. 建小型 eval set，覆盖代表性失败样本。
6. 输出结构化结果，并附页码、引用和置信度。
7. 验证样本：字段完整率、引用准确率、错误类型、人工复核点。

## 输出格式
```markdown
## Document Workflow
- Domain:
- Files:
- Parse strategy:
- Extraction schema:
- Retrieval/index plan:
- Agent action:
- Eval cases:
- Failure modes:
- Next automation:
```

## 验收
- 每个抽取字段都有来源位置或置信度。
- benchmark claim 有样本量和失败维度。
- 新文档可复用同一流程。
