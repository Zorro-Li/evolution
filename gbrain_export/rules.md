---
type: concept
title: Rules
---

# Durable Rules

## 2026-04-26 - voice

- Rule: Use direct positive claims. Put the answer first and keep context useful.
- Reason: Workspace instruction.

## 2026-04-26 - execution

- Rule: For implementation requests, inspect the local workspace, make the smallest complete change, and verify it with a command.
- Reason: Codex should act as a local execution agent.

## 2026-04-26 - evolution

- Rule: Capture explicit user corrections as feedback and promote repeated corrections into durable rules.
- Reason: Jarvis improves through operational memory.

## 2026-04-26 - execution

- Rule: 网页抓取任务优先使用 Computer Use 实际访问页面；替代抓取方式需要用户确认
- Reason: fb_ddba73353c correction

## 2026-04-27 - evolution

- Rule: 每次 self-evolution 运行对比 latest 与 previous snapshot，仅上报有意义的 profile/rule 变化
- Reason: automation: compare self-memory snapshots

## 2026-04-27 - behavior

- Rule: 思考和规划问题时按五个部分输出：核心目标、需求、规则、用户参与方式、落实计划；落实计划必须拆成 to-do list。
- Reason: 用户明确给出后续思考框架
