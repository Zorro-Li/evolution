# x-creator-openai-newsroom

Use this skill to track `@OpenAINewsroom`, official OpenAI newsroom posts, adoption metrics, ChatGPT Images 2.0 usage, Codex non-developer positioning, consumer usage narratives, Stargate, compute infrastructure, and OpenAI corporate communications.

## Capture Workflow

1. Open `https://x.com/OpenAINewsroom` in Safari through Computer Use.
2. Capture profile metadata, official links, visible posts, quoted accounts, link cards, images, methodology caveats, and usage metrics.
3. Classify posts as `adoption_metric`, `consumer_usage_data`, `user_workflow_amplification`, `codex_positioning`, `infrastructure_story`, `policy_comms`, or `corporate_update`.
4. Preserve source URL, date, metrics, quoted user, OpenAI product name, caveat text, link-card target, and visible engagement.
5. Convert each post into a product, market, policy, or Jarvis operating implication.

## Extraction Fields

- Product signal: ChatGPT, ChatGPT Images 2.0, Codex, OpenAI Platform.
- Metrics: growth percentage, daily-user composition, geography, demographic inference, engagement.
- Method caveats: anonymized data, first-name inference, sample scope, visible image caption.
- Use cases: education, visual storytelling, brand kits, daily work, docs, slides, spreadsheets, research, planning.
- Corporate narrative: Stargate, compute capacity, Abilene, Texas, skilled trades, local investment, responsible infrastructure.
- Source graph: `@OpenAI`, quoted users, openai.com/news, openai.com infrastructure posts.

## Output Format

Return:

| Field | Content |
|---|---|
| Source | post URL and capture surface |
| Newsroom signal | metric/use-case/corporate/infrastructure/policy signal |
| Evidence | metric, quote, media clue, link card, or methodology caveat |
| Product implication | adoption, audience, workflow, market, or positioning implication |
| Jarvis implication | local workflow test, dashboard metric, skill idea, or monitoring hook |
| Watch graph | accounts, products, links, and terms to track |

## Watch Graph

- `@OpenAINewsroom`
- `@OpenAI`
- `@ChatGPTapp`
- `@OpenAIDevs`
- `openai.com/news`
- ChatGPT Images 2.0
- Codex
- Stargate
- Abilene, Texas
- compute infrastructure
- image-generation usage
- demographic methodology caveats

## Failure Modes

- Treating Newsroom as a duplicate of `@OpenAI` and missing adoption metrics.
- Saving demographic claims without preserving methodology caveats.
- Tracking quoted examples without extracting why OpenAI amplified them.
- Reading Stargate only as infrastructure PR and missing capex, labor, regional, and policy signals.
- Keeping Codex inside developer-only framing after official newsroom positions it for ChatGPT users.

