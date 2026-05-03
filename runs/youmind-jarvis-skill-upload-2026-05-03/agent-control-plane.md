# Agent 控制平面拆解

ID: `agent-control-plane`

## Description

把 Codex/Jarvis/远程 Agent 系统拆成身份、权限、队列、审批、日志、成本、回调和失败处理。适合做本地 Jarvis、Telegram/微信远程执行和企业 Agent。

## Sources

- `memory/operating_state.md`
- `AGENTS.md`
- `runs/x-creator-watch/2026-05-03/03_skill_distillation.md`
- `runs/manxis-leads-2026-05-03/README.md`

## Instruction

# Agent 控制平面拆解

你的目标是把一个“能跑任务的 Agent”升级成可运营、可审计、可控风险的系统。

## 输入
- 入口：聊天、Telegram、微信、Web、CLI、定时任务。
- 执行器：Codex、Claude Code、脚本、浏览器、MCP、后台 worker。
- 动作风险：读文件、写文件、发消息、上传、删除、付费、登录、调用 API。
- 身份权限：用户、管理员、自动化、外部触发。

## 工作流
1. 画链路：chat entry -> gateway -> queue -> local agent -> codex execution -> callback -> memory update。
2. 定义任务 schema：目标、上下文、权限、验收标准、输出路径、回调方式。
3. 定义 approval tiers：无需确认、预批准、行动时确认、用户手动完成。
4. 记录审计字段：actor、task_id、tool、command、cost、status、error、artifact。
5. 加入队列和锁：防止重复执行、冲突写入、共享资源踩踏。
6. 设计失败处理：重试、降级、暂停、告警、人工接管。
7. 把稳定经验写入 Jarvis memory / GBrain / AGENTS.md。

## 输出格式
```markdown
## Agent Control Plane
- Entry:
- Queue schema:
- Worker:
- Permissions:
- Approval tiers:
- Audit logs:
- Failure handling:
- Memory update:
- Smallest test:
```

## 验收
- 每个高风险动作有确认策略。
- 每个任务有 artifact 和状态回写。
- 最小样例能 `worker --once` 跑通。
