---
name: ancestral-agent-workflow
description: >
  Use this skill to execute coding, research, documentation, automation, refactor,
  migration, production-config, or GitHub publishing tasks with the
  "老祖宗 Agent 工作法": plan before edits, check dependencies first, record
  decisions in /ai-docs, verify with tests, protect secrets, pause on unknown
  APIs, warn before high-risk actions, and provide rollback paths. Trigger when
  the user asks for 老祖宗工作法, agent workflow discipline, reusable execution
  rules, safer Codex work, task planning, verification, docs-first changes, or
  publishing an implementation with durable notes.
---

# Ancestral Agent Workflow

## Core Contract

Execute like a careful local agent: understand context, plan, inspect dependencies, make the smallest useful change, document key decisions, verify, and leave a recovery path.

## Start Every Task

1. Read local instructions: `AGENTS.md`, relevant README files, local docs, tests, and recent implementation patterns.
2. State a short plan before editing.
3. Define acceptance criteria: what must be true when the task is complete.
4. Check "粮草": dependencies, environment variables, startup commands, test commands, formatter/linter/build commands.
5. Identify risk class:
   - Low: docs, small helper, narrow bug fix.
   - Medium: user-facing behavior, shared module, schema, dependency.
   - High: deletion, migration, auth, payments, production config, secrets, data, infra, irreversible operation.

## Mandatory Rules

Use the full rulebook in [references/rulebook.md](references/rulebook.md).

High-level rules:
- **谋定而后动**: plan first, then edit.
- **好记性不如烂笔头**: write decisions, risks, and key changes to `/ai-docs/`; when that path is unavailable, use the repo-local `ai-docs/`.
- **知之为知之**: pause and state the gap when an API, field, dependency, credential, schema, or production fact is uncertain.
- **三思而后行**: warn before deletion, refactor, migration, production config, credential, or data changes.
- **兵马未动，粮草先行**: check dependency and verification commands before implementation.
- **有则改之**: self-check and run the smallest reliable validation after changes.
- **留得青山在**: include rollback for high-risk changes.

## Execution Workflow

1. **Context pass**
   - Read local docs and code before designing.
   - Search with `rg` or `rg --files`.
   - Inspect existing tests and commands.

2. **Plan**
   - Keep the plan small and executable.
   - Include acceptance criteria.
   - Call out high-risk steps and rollback.

3. **Document**
   - Create or update an `/ai-docs/` note for substantial tasks.
   - Use [references/doc-template.md](references/doc-template.md).

4. **Implement**
   - Follow existing architecture and style.
   - Prefer the smallest complete version.
   - Keep unrelated findings in the docs or task list.

5. **Verify**
   - Run project formatter/linter/test/build when available.
   - Use the smallest reliable command for narrow changes.
   - State verified commands and any remaining gaps.

6. **Publish**
   - For GitHub work, inspect `git status`, stage only intended files, commit with a scoped message, push branch, and create PR when tooling is available.
   - Use [references/github-publish.md](references/github-publish.md).

## Output Format

For implementation tasks, finish with:

```markdown
完成：<what changed>
验证：<commands and results>
记录：<ai-docs path>
发布：<branch/commit/PR or blocker>
回滚：<rollback path for risky changes>
```

For planning-only tasks, finish with:

```markdown
计划：<steps>
验收标准：<criteria>
风险：<risk notes>
建议下一步：<one concrete action>
```
