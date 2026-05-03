# Skill Distillation: KobeissiLetter

## Trigger

Use this workflow when analyzing `@KobeissiLetter`, global capital-market commentary, macro liquidity posts, ETF flow charts, AI infrastructure flow narratives, energy-price headlines, tech layoff data, Treasury/TGA posts, crypto/gold reserve comparisons, or market-moving geopolitical headlines.

## Inputs

- `@KobeissiLetter` posts, quote posts, charts, profile metadata, and subscription links
- macro metrics: TGA, T-bills, debt, ETF flows, gasoline, layoffs, gold holdings, central-bank comparisons
- tickers, sectors, ETF categories, and asset classes
- visible engagement metrics
- external verification sources: Treasury data, FRED, EIA/AAA, BLS/Challenger, ETF flow providers, company filings, official statements, and primary reports

## Workflow

1. Capture source evidence:
   - post URL and timestamp label
   - visible text
   - chart/image count
   - metric and claimed time window
   - engagement metrics
   - any external link or subscription CTA
2. Classify each post:
   - liquidity / Treasury
   - ETF flow / sector rotation
   - energy / inflation
   - labor / employment
   - crypto / commodity reserves
   - geopolitics / breaking headline
   - policy / regulation
   - performance marketing
3. Extract the market mechanism:
   - what changed
   - size and direction
   - affected asset classes
   - likely timeframe
   - data source to verify
4. Verify before reuse:
   - official dataset or issuer report
   - chart source and date
   - denominator / benchmark
   - whether the post is annualized, rolling, quarterly, or point-in-time
   - whether language is headline alert or durable trend
5. Output a daily macro brief with verified status and open checks.

## Output Template

```md
# Kobeissi Macro Signal Brief

## Top Signals
| Signal | Source URL | Claimed move | Mechanism | Asset classes | Verification target |
|---|---|---|---|---|---|

## Dashboard Updates
- Liquidity:
- AI infrastructure:
- Energy / inflation:
- Labor:
- Cross-asset reserves:
- Policy / geopolitics:

## Verification Notes
- Primary source:
- Time window:
- Benchmark:
- Open checks:
```

## Failure Modes

- Treating a chart caption as a verified dataset.
- Mixing breaking headlines with durable macro trends.
- Missing subscription / performance-marketing context.
- Ignoring denominator, base period, and chart source.
