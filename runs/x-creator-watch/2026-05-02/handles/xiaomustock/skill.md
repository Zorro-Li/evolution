# Skill Distillation: xiaomustock

## Trigger

Use this workflow when analyzing `@xiaomustock`, AI infrastructure stock commentary, U.S. stock option/ETF implementation, Google TPU supplier chains, memory/DRAM/HBM exposure, MRVL, SNDK, SK Hynix/Samsung access, or public high-conviction trade plans.

## Inputs

- X posts and quote posts from `@xiaomustock`
- tickers, cashtags, ETFs, leveraged ETFs, and options references
- screenshots, earnings-call references, profit math, and event dates
- engagement metrics
- external verification sources: earnings releases, transcripts, SEC filings, ETF holdings, option chain data, and market prices

## Workflow

1. Capture every visible post with URL, timestamp label, text, quote source, tickers, instruments, metrics, and media count.
2. Classify each item as thesis, implementation, risk-control update, event watch, valuation math, access route, or self-review.
3. Extract the trade map:
   - demand driver
   - beneficiary chain
   - ticker or instrument
   - catalyst date or timeline
   - implementation method
   - leverage / options risk
   - evidence source
4. Verify externally:
   - earnings numbers and guidance
   - supplier relationship
   - ETF holdings and decay risk
   - option strategy payoff and assignment risk
   - market cap / valuation math
5. Convert the output into a watch brief with "claim", "source evidence", "verification status", "risk", and "next data point".

## Output Template

```md
# AI Infrastructure Trade Map

## Top Claim
<one sentence>

## Source Evidence
| URL | Date label | Ticker/instrument | Claim | Engagement | Verification target |
|---|---|---|---|---|---|

## Causal Chain
Demand driver -> supplier/profit pool -> tradable instrument -> catalyst -> risk

## Verification Checklist
- Earnings / guidance:
- Transcript / management quote:
- ETF holdings:
- Leverage or options risk:
- Price / valuation:

## Actionable Watch Items
- <ticker/instrument>: <next evidence to verify>
```

## Failure Modes

- Using high-conviction phrasing as confirmed financial truth.
- Collapsing thesis and implementation into one signal.
- Missing leveraged ETF decay, option assignment, and timing risk.
- Treating screenshots as sufficient evidence without filings or transcripts.
