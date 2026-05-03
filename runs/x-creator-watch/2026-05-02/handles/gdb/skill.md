# Skill Draft: Codex Adoption Signal Watcher

Use this skill when tracking OpenAI leadership accounts such as `@gdb`, Codex community posts, OpenAI Developers posts, and user examples that show how Codex is being used in real workflows.

## Inputs

- X handle
- visible posts and quote-tweets
- quoted user accounts
- feature terms such as `/goal`, Computer Use, CLI, app commands, plugins, and project config
- engagement metrics when visible

## Workflow

1. Capture the visible leadership batch from Safari / Computer Use.
2. Mark each item as:
   - founder amplification
   - official developer signal
   - user workflow proof
   - community tool or add-on
   - product feature vocabulary
3. Normalize each post into:
   - source URL
   - quoted account
   - Codex feature or surface
   - user job-to-be-done
   - engagement signal
   - local Jarvis relevance
4. Convert each signal into a local action:
   - test the feature
   - add the quoted builder to the watch list
   - create a short workflow recipe
   - update a Codex/Jarvis operating rule
5. Produce a brief that ranks signals by product direction and local implementation value.

## Output Template

```md
# Codex Adoption Signal Brief

## Current Product Direction
<direction>

## High-Signal Posts
| URL | Quoted account | Feature | Workflow proof | Local action |
|---|---|---|---|---|

## Watch Graph Additions
- <account>: <reason>

## Local Jarvis Tests
1. <test>
2. <test>
3. <test>
```

## Failure Modes

- Treating founder quote-tweets as casual reposts.
- Missing the quoted user as the real source of workflow evidence.
- Saving product vocabulary without mapping it to a local test.
- Tracking engagement counts without ranking implementation relevance.
