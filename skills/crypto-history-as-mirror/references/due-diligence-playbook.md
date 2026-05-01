# Due Diligence Playbook

## Fast Mode: 15-Minute Historical Triage

Use when the user asks "这个能不能碰", "像不像 rug", or "这个盘好坏".

Output:

```markdown
结论：<long-cycle / infra / PvP / bubble / custody risk / rug setup / avoid>
历史类比：<2-3 analogs>
核心风险：<one sentence>
证据缺口：<what must be checked>
建议：<research / watch / avoid / tiny experimental size / exit-first>
```

Checklist:

1. Identify asset type.
2. Check chain, contract, official links.
3. Read tokenomics and unlocks.
4. Check LP depth and owner.
5. Check admin powers.
6. Check payer behind yield.
7. Check team/VC/KOL distribution path.
8. Match historical analog.

## Deep Mode: Full "以史为鉴" Report

Use when the user asks for a detailed report, knowledge-base entry, investment memo, or project teardown.

Template:

```markdown
# <Project> 以史为鉴分析

## 结论
<one paragraph>

## 一、历史位置
- Era:
- Plate type:
- Closest analogs:
- PDF anchors:

## 二、兴起条件
- New primitive:
- Liquidity venue:
- Narrative:
- Participant class:
- Distribution machine:

## 三、衰落条件
- Supply pressure:
- Control risk:
- Yield payer:
- Liquidity exit:
- Regulatory/custody surface:

## 四、链上与市场证据
| Dimension | Evidence | Reading | Confidence |
|---|---|---|---|

## 五、以史为鉴判断
- Historical lesson:
- Current match:
- Key difference:
- Evidence to record:
- Stop condition:

## 六、决策
- Participate:
- Size:
- Exit:
- Review:
- Invalidation:
```

## Evidence Standard

Use this hierarchy:

1. Chain data: contract source, events, balances, holders, admin calls.
2. Market data: DEX liquidity, CEX order book, 30-day volume, funding, liquidations.
3. Project docs: tokenomics, unlocks, governance, architecture.
4. Security docs: audits, bug bounty, timelock, multisig, incident history.
5. Social data: X, Telegram, Discord, GitHub, forum, community complaints.
6. Historical analogs: PDF page anchors and known cycle patterns.

## Common Verdicts

### Long-Cycle Asset

Use when:
- The asset has survived multiple cycles.
- Self-custody and liquidity are mature.
- Demand exists beyond short-term incentives.
- Narrative has historical depth and user base.

Main risks:
- Macro liquidity, regulation, custody mistakes, concentration, leverage cycles.

### Infrastructure Bet

Use when:
- The project sells blockspace, security, data, execution, settlement, custody, or developer tools.
- Usage can be measured independently of token emissions.
- Token captures value through fees, staking, collateral, or governance with actual demand.

Main risks:
- Weak token value capture, VC unlocks, competing infra, overfunded narrative.

### PvP Speculation

Use when:
- Rules are visible.
- Liquidity and attention are rising.
- The user can define a short holding period.
- Upside comes from timing rather than fundamentals.

Main risks:
- Fast rotation, insider wallets, thin LP, social manipulation.

### Reflexive Bubble

Use when:
- Price validates narrative and narrative validates price.
- Yield, points, or social status bring in users.
- Exit liquidity depends on continued attention.

Main risks:
- Volume collapse, unlocks, reward reduction, narrative migration.

### Custody Risk

Use when:
- User assets sit inside an exchange, bridge, lending desk, vault, or opaque manager.
- Withdrawals, reserves, or asset segregation are unclear.

Main risks:
- Freeze, insolvency, legal seizure, rehypothecation, bridge hack.

### Rug Setup

Use when:
- Direct control path exists.
- LP is thin or controlled.
- Supply is insider-heavy.
- Yield lacks a payer.
- Marketing replaces usage.

Main risks:
- Sudden liquidity pull, mint, tax change, blacklist, migration, team dump.

## Saving A Knowledge Entry

When asked to persist research, save under:

`/ai-docs/crypto/<project-or-topic>.md`

Minimum sections:

- Date and analyst
- Source links
- Contract addresses
- Historical analogs
- Evidence table
- Verdict
- Open questions
- Review date
