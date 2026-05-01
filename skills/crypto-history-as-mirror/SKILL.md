---
name: crypto-history-as-mirror
description: >
  Use this skill for "以史为鉴" crypto analysis: turning Chinese crypto history,
  boom-bust cycles, Bitcoin maximalist writing, exchange failures,
  ICO/NFT/DeFi/meme/rug cases, and the PDF "华语币圈经典 2010-2024" into a reusable
  knowledge base. Trigger when the user asks for crypto history, coin-cycle rise
  and fall, historical analogies for a token/project, old-cycle lessons,
  rug-plate analysis, "好盘/坏盘", Chinese crypto narratives, historical cycle
  positioning, or crypto due diligence by historical analogy.
---

# Crypto History As Mirror

## Core Mission

Use crypto history as a decision engine. Convert a current project into historical analogs, cycle position, incentives, control points, liquidity exits, and concrete operating rules.

For live projects, gather fresh evidence before judging. For historical learning, use the local PDF knowledge base and page anchors.

## Source Stack

- Start with [references/pdf-knowledge-map.md](references/pdf-knowledge-map.md) for the detailed knowledge map of the PDF.
- Use [references/crypto-rise-fall-2010-2024.md](references/crypto-rise-fall-2010-2024.md) for the full rise-fall cycle narrative.
- Use [references/due-diligence-playbook.md](references/due-diligence-playbook.md) for project analysis workflow and output templates.
- For narrow rug scoring, call the companion skill `$crypto-rug-analysis` or reuse its rubric at `/Users/lizongru/.codex/skills/crypto-rug-analysis/references/rug-scorecard.md`.

## Workflow

1. **Name the object**
   - Asset, protocol, exchange, NFT, meme, ICO, DeFi pool, stablecoin, bridge, mining/DePIN, restaking, airdrop, or narrative.

2. **Place it in history**
   - Match it to one or more eras: cypherpunk origin, early mining, exchange custody, blocksize war, ICO, DeFi summer, NFT, L1/meme, restaking/points.
   - Identify the strongest page anchors from the PDF knowledge map.

3. **Find the incentive skeleton**
   - Who pays first, who receives first, who controls rules, who exits first, who becomes exit liquidity.
   - Classify the engine: store-of-value, casino, exchange, fundraising, yield, cultural asset, infrastructure, or social religion.

4. **Apply historical lessons**
   - Use prior cycles as constraints: match analogs, locate cycle stage, map incentives, verify liquidity, and define failure triggers.

5. **Give a verdict**
   - Classify as: long-cycle asset, infrastructure bet, PvP speculation, reflexive bubble, custody risk, rug setup, historical artifact, or avoid.

## Output Format

```markdown
结论：<one-line verdict>

历史位置
- Era:
- Closest analogs:
- PDF anchors:

兴衰逻辑
- Rise driver:
- Peak signal:
- Decline trigger:
- Survivability:

以史为鉴
- 历史教训:
- 今日对应:
- 需要记录的证据:
- Stop condition:

执行建议
- Research:
- Size/participation:
- Exit:
- Review date:
```

## Operating Rules

- Keep historical claims tied to page anchors, public sources, or current evidence.
- Separate "historical rhyme" from "current proof".
- Treat narratives as market structure evidence, then verify liquidity, supply, and control.
- Prefer written ledgers: save key project evidence under `/ai-docs/` when the user asks for durable work.
- Pause when a current API, chain state, contract function, or source cannot be verified.
