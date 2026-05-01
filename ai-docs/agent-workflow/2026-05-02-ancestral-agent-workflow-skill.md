# Ancestral Agent Workflow Skill

Date: 2026-05-02
Owner: Codex
Risk: Medium

## Goal

Create a reusable Skill for the user's "老祖宗 Agent 工作法": applying traditional maxims to AI/Agent execution discipline.

## Acceptance Criteria

- Skill exists under `skills/ancestral-agent-workflow`.
- Skill can be installed locally under `~/.codex/skills/ancestral-agent-workflow`.
- Skill passes `quick_validate.py`.
- Key decisions, risks, and validation are recorded in `ai-docs/`.
- Git changes are scoped and committed on a `codex/` branch.
- GitHub push is attempted and blocker is documented when authentication is unavailable.

## Context Checked

- `AGENTS.md`
- `README.md`
- `git status --short`
- `git remote -v`
- `skill-creator` instructions
- GitHub publish skill guidance

## Plan

1. Create the reusable Skill in the repository.
2. Add rulebook, doc template, GitHub publish workflow, and examples.
3. Install the Skill locally for Codex discovery.
4. Validate the Skill.
5. Commit and push a scoped branch.

## Decisions

- Skill name: `ancestral-agent-workflow`.
- Repository path: `skills/ancestral-agent-workflow`.
- Local install path: `~/.codex/skills/ancestral-agent-workflow`.
- Root `/ai-docs` is read-only in this environment, so the durable task note is stored at repo-local `ai-docs/agent-workflow/`.
- `gh` CLI is unavailable and `GITHUB_TOKEN`/`GH_TOKEN` are absent.
- Git SSH push succeeded after retry.
- GitHub connector can create PRs in principle, but returned 404 for `Zorro-Li/evolution`, so PR creation is blocked by connector repository access.
- User clarified this is separate from the crypto "以史为鉴" Skill. This Skill only covers AI/Agent workflow discipline.

## Risks

- Working tree contains unrelated existing changes. Mitigation: stage only this task's explicit paths.
- High-risk workflow rules can slow simple tasks. Mitigation: Skill uses risk classes and keeps low-risk tasks lightweight.
- Root `/ai-docs` path is unavailable. Mitigation: use repo-local `ai-docs/`.

## Rollback

- Unpublish branch by deleting remote branch after user approval.
- Revert commit with `git revert <commit>`.
- Remove local install with `rm -rf ~/.codex/skills/ancestral-agent-workflow`.

## Validation

```bash
python3 /Users/lizongru/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lizongru/codex/进化/skills/ancestral-agent-workflow
python3 /Users/lizongru/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lizongru/.codex/skills/ancestral-agent-workflow
```

Result:

```text
Skill is valid!
Skill is valid!
```

## Publish Status

Local branch:

```text
codex/separate-history-ancestral-skills
```

Local commit:

```text
See current branch HEAD for the latest amended commit SHA.
```

GitHub push attempt:

```bash
git push -u origin codex/separate-history-ancestral-skills
```

Result:

```text
To github.com:Zorro-Li/evolution.git
 * [new branch]      codex/separate-history-ancestral-skills -> codex/separate-history-ancestral-skills
```

PR status:

```text
GitHub connector returned 404 when creating a PR for Zorro-Li/evolution.
```

Manual PR URL:

```text
https://github.com/Zorro-Li/evolution/compare/main...codex/separate-history-ancestral-skills?expand=1
```
