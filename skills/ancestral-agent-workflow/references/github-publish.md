# GitHub Publish Workflow

Use when the user asks to publish changes to GitHub.

## Preconditions

1. Inspect state:

```bash
git status --short
git branch --show-current
git remote -v
```

2. Identify intended scope.
3. Check GitHub path:
   - `gh --version`
   - `gh auth status`
   - Git SSH remote push access via `git push`

## Branch Rule

When starting from `main` or `master`, create:

```text
codex/<short-task-slug>
```

## Staging Rule

Stage explicit files:

```bash
git add <file1> <file2> <dir/>
```

Use full worktree staging only when the whole tree belongs to the task.

## Commit Rule

Use a terse scoped message:

```text
Add ancestral agent workflow skill
```

## Validation Rule

Run task-specific checks before committing when feasible. For skills:

```bash
python3 /Users/lizongru/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>
```

## Push Rule

```bash
git push -u origin $(git branch --show-current)
```

## PR Rule

Use `gh pr create --draft` when `gh` exists and is authenticated. When `gh` is unavailable, push the branch and report the branch URL or remote branch name.

## Rollback

For a pushed branch:

```bash
git revert <commit>
git push
```

For an unpublished local commit:

```bash
git reset --soft HEAD~1
```

Run destructive rollback only after explicit user approval.
