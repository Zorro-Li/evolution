# Examples

## Coding Task

User:

```text
Use $ancestral-agent-workflow to add OAuth login.
```

Agent behavior:
- Reads auth docs, routes, tests, env examples.
- Plans the smallest OAuth slice.
- Records decisions in `/ai-docs/auth/<date>-oauth-login.md`.
- Checks secrets handling.
- Implements.
- Runs tests/build.
- Gives rollback and validation.

## Refactor Task

User:

```text
Use $ancestral-agent-workflow to refactor the billing module.
```

Agent behavior:
- Classifies risk as high or medium.
- Reads current tests and call sites.
- Proposes phases.
- Starts with behavior-preserving extraction.
- Runs tests after each phase.
- Documents rollback.

## Research Task

User:

```text
Use $ancestral-agent-workflow to research competitors and save a report.
```

Agent behavior:
- Creates evidence ledger.
- Records sources and dates.
- Separates confirmed facts from inference.
- Writes `/ai-docs/research/<date>-competitors.md`.

## GitHub Publish Task

User:

```text
Use $ancestral-agent-workflow and push this to GitHub.
```

Agent behavior:
- Checks `git status`, branch, remote, and auth tooling.
- Creates `codex/<task>` branch from main.
- Stages only intended files.
- Validates.
- Commits.
- Pushes.
- Creates PR when tooling is available.
