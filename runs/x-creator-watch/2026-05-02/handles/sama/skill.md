# Skill Draft: AI Leadership Signal Watcher

Use this skill when tracking leadership accounts such as `@sama`, frontier AI lab executives, founder accounts, and product-strategy voices whose short posts influence model, product, and community interpretation.

## Inputs

- X handle
- visible posts and quote-tweets
- model names and mode names
- linked research or blog surfaces
- release-event or community-demand references
- engagement metrics when visible

## Workflow

1. Capture the visible profile batch from Safari / Computer Use.
2. Split posts into:
   - leadership product philosophy
   - model usage hint
   - research amplification
   - launch or community-demand signal
   - personal culture post
3. Normalize each high-signal item into:
   - source URL
   - claim
   - model or product surface
   - evidence type
   - local test or monitoring action
4. Convert the batch into user actions:
   - test named models and modes locally
   - add research links to source tracking
   - watch launch-event demand and community feedback
   - turn command-like posts into reproducible product-culture tests
5. Produce a ranked brief with the claims that should change the user's monitoring queue.

## Output Template

```md
# AI Leadership Signal Brief

## Leadership Claims
| URL | Claim | Product surface | Action |
|---|---|---|---|

## Model/Mode Tests
- <model or mode>: <local test>

## Research Links
- <URL>: <why it matters>

## Community Signals
- <signal>: <interpretation>
```

## Failure Modes

- Treating every personal post as product signal.
- Missing a model or mode name hidden in short casual copy.
- Saving the claim without creating a local test.
- Ignoring quote-tweeted researchers and linked blogs.
