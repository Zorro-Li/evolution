# Codex 本地状态维护

ID: `codex-state-maintenance`

## Description

把 Codex 长期使用后的聊天、worktree、日志、配置和本地状态膨胀拆成只读体检、handoff、备份、归档、验证和提醒流程。

## Sources

- `runs/x-creator-watch/2026-05-03/handles/geekbb/skill.md`
- `runs/x-creator-watch/2026-05-03/handles/geekbb/profile.md`
- `https://x.com/geekbb/status/2050786115427402050`
- `https://github.com/vibeforge1111/keep-codex-fast`

## Instruction

# Codex 本地状态维护

你的目标是让重度使用后的 Codex 恢复轻量、可恢复、可继续执行的状态。

## 适用场景

- Codex 启动、恢复或切换线程变慢。
- `.codex/sessions/`、JSONL 聊天、worktree、日志或配置持续变大。
- 用户想清理 Codex 本地状态，同时保留重要上下文。
- 用户需要把旧长线程迁移成新线程可接上的 handoff。

## 工作流

1. 先做只读体检：统计 active session、archive、worktree、log、config、Node/dev process。
2. 判断哪些旧线程仍有业务价值：当前项目、未完成目标、近期文件改动、待验收任务。
3. 给重要线程生成 repo-local handoff：目标、完成事项、文件、命令、失败、约束、下一步和 reactivation prompt。
4. 应用前先备份：Codex metadata、配置、需要归档的 session/worktree/log。
5. 采用归档策略：旧 session、stale worktree 和大日志进入 archive，并写 manifest 与恢复路径。
6. 配置修剪只处理失效项目引用、临时路径和明显过期项。
7. 完成后再次运行只读体检，对比体积、候选项和异常。
8. 高频使用者加周度 report-only 提醒，自动化只提醒体检和 handoff。

## 输出格式

```markdown
## Codex State Report
- Active session size:
- Archived session size:
- Largest session candidates:
- Worktree candidates:
- Log size:
- Config candidates:
- Heavy dev processes:
- Handoff docs needed:
- Safe next action:
- Verification command:
```

## 验收

- 第一次运行只读体检。
- 每个重要旧线程有 handoff 或保留决策。
- 每个 apply 动作有 backup、archive、manifest、restore route。
- 应用维护发生在 Codex 关闭后，或明确使用 wait-for-exit。
- 维护后再次体检成功。
