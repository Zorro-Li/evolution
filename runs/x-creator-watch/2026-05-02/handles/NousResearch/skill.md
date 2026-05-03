# Skill Distillation: @NousResearch

## Purpose

Use `@NousResearch` as a source for open-source AI lab signals, Hermes Agent releases, agent interface changes, skill ecosystems, MCP support, partner integrations, and training-infrastructure direction.

## Workflow

1. Capture profile, pinned Hermes Agent releases, GitHub release-note links, partner skills, quote-tweets from partner executives, and hiring cards.
2. Classify posts by release, interface change, skill integration, MCP/runtime feature, migration story, training infrastructure, or community library.
3. Extract exact product mechanics: update command, release version, skill capabilities, platform objects, setup requirements, and linked repo/release notes.
4. Map each signal to Jarvis primitives: CLI/runtime, skills, permissions, credentials, file references, MCP server/client, and channel-specific output.
5. Weight partner-validated skills higher than ordinary launch posts.

## Output Template

```markdown
## Nous / Hermes Agent Signal

- Source:
- Release or skill:
- Version:
- Runtime/interface change:
- Skill capabilities:
- Partner validation:
- Jarvis reuse:
```

## Failure Modes

- Treating open-source branding as product adoption.
- Missing setup and credential friction in migration stories.
- Capturing partner names without preserving the actual platform operations exposed to the agent.
