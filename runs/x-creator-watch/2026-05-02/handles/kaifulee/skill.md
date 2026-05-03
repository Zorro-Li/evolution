# Skill Draft: Enterprise AI Agent Strategy Watcher

Use this skill when tracking AI executives and enterprise-agent companies such as `@kaifulee`, `@01ai_yi`, and accounts discussing open model adoption, multi-agent systems, China/US AI strategy, or enterprise AI deployment.

## Inputs

- X handle
- visible posts and retweets
- company links
- media interviews
- hiring posts
- quoted or retweeted ecosystem accounts
- engagement metrics when visible

## Workflow

1. Capture the visible account batch from Safari / Computer Use.
2. Split posts into:
   - executive strategy
   - enterprise-agent GTM
   - open ecosystem thesis
   - multi-agent workflow claim
   - hiring and delivery-model signal
   - author or worldview signal
3. Normalize each item into:
   - source URL
   - strategic claim
   - company/product surface
   - enterprise use case
   - delivery implication
   - local Jarvis relevance
4. Convert the signal into local action:
   - add company and partner accounts to the watch graph
   - translate hiring roles into operating capabilities
   - map multi-agent claims to Jarvis modules
   - track open-model adoption and safety framing
5. Produce a brief that ranks enterprise-agent strategy signals by practical implementation value.

## Output Template

```md
# Enterprise AI Agent Strategy Brief

## Company Direction
<direction>

## Evidence Table
| URL | Type | Signal | Enterprise implication | Local Jarvis action |
|---|---|---|---|---|

## Delivery Model Inferred From Hiring
- <capability>: <evidence>

## Multi-Agent Architecture Notes
- <note>
```

## Failure Modes

- Treating executive media posts as generic publicity.
- Missing hiring posts as evidence of delivery strategy.
- Saving multi-agent claims without mapping them to local architecture.
- Ignoring open-ecosystem safety framing.
