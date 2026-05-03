# Agent 记忆与上下文边界拆解

ID: `agent-memory-context`

## Description

拆解 Agent 记忆、跨会话上下文、local-first 数据、终端状态恢复和上下文安全。用于设计 Jarvis/GBrain/ManXis 的记忆系统。

## Sources

- `runs/x-creator-watch/2026-05-02/handles/wey_gu/skill.md`
- `runs/x-creator-watch/2026-05-02/handles/nicbstme/skill.md`
- `memory/operating_state.md`

## Instruction

# Agent 记忆与上下文边界拆解

你的目标是判断一个 Agent 系统应该记住什么、忘掉什么、如何恢复、如何保护。

## 输入
- Agent 类型：coding、research、browser、workflow、chat、terminal。
- 上下文来源：文件、聊天、工具输出、日志、GBrain、记忆库、外部 app。
- 风险：隐私、过期信息、错记、跨用户污染、prompt injection、成本膨胀。

## 工作流
1. 分层：session memory、project memory、long-term profile、tool state、external knowledge。
2. 判断保留价值：下次是否能减少重复解释、提高质量、降低风险或节省成本。
3. 判断安全边界：敏感数据、账号、密钥、身份、医疗/财务/法律内容。
4. 设计恢复机制：thread summary、task ledger、GBrain slug、terminal snapshot、artifact path。
5. 设计遗忘机制：过期、低信心、错误纠正、用户撤销、敏感材料本地化。
6. 输出上下文预算：哪些进 prompt，哪些进检索，哪些只存本地。

## 输出格式
```markdown
## Context Boundary Plan
- Memory layers:
- Keep:
- Retrieve:
- Drop:
- Sensitive boundaries:
- Refresh triggers:
- Recovery path:
- Cost impact:
```

## 验收
- 每条记忆有用途、来源和更新条件。
- 敏感材料默认本地化。
- 长任务恢复能从 artifact path 和 task ledger 接上。
