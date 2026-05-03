# @geekbb: Codex Local-State Maintenance

## Trigger

Use when Codex feels slow after heavy use, when `.codex/sessions/`, old JSONL chats, worktrees, logs, config entries, or long-lived terminals may be causing local drag, or when the user asks for safe Codex cleanup.

## Inputs

- Codex home path and current workspace path.
- Whether Codex is running.
- Active repo chats that still need continuity.
- Session, worktree, log, and config age/size thresholds.
- User preference for report-only, backup-only, or apply.

## Steps

1. Start with a read-only report of session sizes, archived size, stale worktrees, log size, config candidates, and heavy dev processes.
2. Identify active repo chats that may still matter.
3. For each important active chat, create a repo-local handoff document and reactivation prompt.
4. Back up Codex metadata before any maintenance action.
5. Archive old sessions and stale worktrees into restore-friendly folders.
6. Rotate large logs and prune stale project/config references after backup.
7. Verify with the same read-only report after maintenance.
8. Add a report-only weekly reminder for heavy users when useful.

## Output

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

## Validation

- The first pass changes no files.
- Every important old chat has a handoff or explicit keep decision.
- Every maintenance action has a backup, archive path, manifest, and restore route.
- Apply happens only after Codex is closed or waiting for exit is explicit.

## Failure Modes

- Archiving active repo chats without handoff docs.
- Treating raw size as sufficient evidence without checking continuity value.
- Killing dev processes automatically.
- Publishing backup folders that may contain private local metadata.
