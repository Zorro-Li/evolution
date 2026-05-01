# `/ai-docs/` Task Note Template

Create one note per substantial task.

Preferred path:

```text
/ai-docs/<topic>/<YYYY-MM-DD>-<task-slug>.md
```

Repo-local fallback:

```text
ai-docs/<topic>/<YYYY-MM-DD>-<task-slug>.md
```

Template:

```markdown
# <Task Title>

Date: <YYYY-MM-DD>
Owner: Codex
Risk: Low / Medium / High

## Goal

<What user wants done.>

## Acceptance Criteria

- <Observable completion condition>
- <Validation command or artifact>

## Context Checked

- <docs/code/tests/commands inspected>

## Plan

1. <step>
2. <step>
3. <step>

## Decisions

- <decision and reason>

## Changes

- <file/path>: <change>

## Risks

- <risk>: <mitigation>

## Validation

```bash
<command>
```

Result:

```text
<summary>
```

## Rollback

- <git revert / config restore / migration rollback / file restore>

## Follow-ups

- <related bug or improvement>
```
