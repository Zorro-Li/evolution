# Compresr Research Report

## Company Overview
### Core Product/Service
Compresr builds LLM context-compression infrastructure. Its core product is an API and SDK that compress long prompts, documents, retrieved context, and agent histories before they are sent to an LLM.

Public docs list three model paths:
- `espresso_v1`: general-purpose compression for reusable context.
- `latte_v1`: query-specific compression for RAG and Q&A.
- `coldbrew_v1`: chunk-level filtering, referenced in SDK docs.

Compresr also offers Context Gateway, an open-source local proxy for AI agents such as Claude Code, Codex, Cursor, OpenHands, and OpenClaw. It sits between the agent and the model API, compresses conversation history and large tool outputs, and logs compression events.

### Target Market
Primary buyers are developers and engineering teams building:
- AI agents with long tool outputs and growing conversation history.
- RAG systems with large retrieved document payloads.
- Enterprise LLM workflows in finance, healthcare, legal, and other regulated environments.
- Teams spending meaningfully on LLM input tokens and latency-sensitive workloads.

Public positioning is B2B AI infrastructure, developer tools, and enterprise software.

### Business Model
Compresr appears to use a hybrid model:
- Hosted API / SDK: API-key-based access with Python and TypeScript clients.
- Usage-based pricing: official site references per-million-token pricing and $10 free credits on sign-up.
- Enterprise/on-prem: private deployment inside a customer VPC or data center, with volume pricing, dedicated support, custom throughput/latency SLAs, and domain-tuned models.
- Open-source adoption wedge: Context Gateway is open source under Apache-2.0, while Compresr’s compression models appear to remain commercial infrastructure.

Exact public list prices are unclear; the current pricing page points users toward custom/on-prem plans.

### Leadership / Team Signals
YC lists Compresr as founded in 2026, Winter 2026 batch, active, team size 4, San Francisco.

Listed founders:
- Ivan Zakazov, Founder / CEO. YC profile says he previously researched LLM context compression as an EPFL PhD and worked at Microsoft and Philips Research.
- Berke Argin, Founder / CAIO. YC profile cites EPFL CS and previous UBS experience.
- Kamel Charaf, Founder / COO. YC profile cites EPFL Data Science Masters and ex-Bell Labs.
- Oussama Gabouj, Founder / CTO. YC profile cites EPFL DLab and AXA research work focused on efficient ML systems and prompt compression.

LinkedIn lists Compresr as privately held, 2-10 employees, and shows the same four employees.

## Industry Overview
### Market Segment
Compresr sits in LLM inference optimization, context engineering, and agent infrastructure. The buying trigger is clear: long prompts and agent traces increase input-token cost, latency, and accuracy degradation risk.

The market overlaps with:
- Prompt compression.
- RAG context filtering.
- Agent memory/context management.
- AI gateways and observability.
- Model-provider prompt caching.

### Direct Competition
Visible direct and adjacent competitors include:
- Microsoft LLMLingua: open-source prompt compression research and tooling, with LLMLingua, LongLLMLingua, and LLMLingua-2.
- Preduce: prompt-compression API claiming 50%+ token reduction and deterministic output.
- Compresso API: prompt-compression API for OpenAI, Anthropic, Mistral, and other LLM providers.
- Zur-lix: OpenAI/Anthropic-compatible proxy with prompt compression, spend caps, and usage metering.
- PromptFold / Prompt Piper / similar tools: smaller prompt-compression utilities and APIs.
- Model-provider caching: OpenAI and Anthropic prompt caching reduce cost and latency for repeated prompt prefixes.
- AI gateways such as Portkey, LiteLLM, Helicone, and LockLLM: adjacent middleware that can add routing, caching, guardrails, observability, and cost controls.

### Competitive Advantages
Compresr’s strongest public advantages are:
- Focused positioning around LLM-native context compression for agents and RAG.
- Query-aware compression via `latte_v1`, which maps directly to RAG and agent tasks.
- Context Gateway as a practical developer workflow entry point.
- On-prem / VPC deployment option for regulated enterprise use.
- Founder-market fit signals from EPFL, Microsoft, Bell Labs, AXA, UBS, and direct prompt-compression research backgrounds.
- YC W26 backing and current developer traction signals from Product Hunt and GitHub.

Company-published benchmark claims include 10x average compression across 141 FinanceBench questions, 76% cheaper usage, and accuracy moving from 72.3% to 74.5% in the cited setup. Treat these as company-published performance claims until independently replicated.

### Market Challenges
Key challenges:
- Compression trust: developers need confidence that low-frequency details, code identifiers, citations, and edge-case facts survive compression.
- Evaluation burden: customers will want task-specific accuracy tests before placing Compresr in the request path.
- Provider pressure: larger context windows, cheaper tokens, and native prompt caching reduce some cost pain.
- Middleware risk: teams may resist adding another API/proxy between agents and model providers.
- Enterprise security: regulated buyers will require strong data-handling guarantees, on-prem deployment, audit logs, and procurement readiness.
- Open-source alternatives: LLMLingua and other libraries create a credible build-vs-buy path.

## Financial Overview
### Funding & Investors
Compresr is YC Winter 2026 backed. YC’s standard deal is $500,000 total: $125,000 for 7% plus $375,000 on an uncapped MFN SAFE.

Compresr-specific public funding is unclear. Dealroom.co lists Y Combinator as an investor and shows a Jan 2026 $125,000 seed entry, while the full funding field is gated. Public sources reviewed did not show a priced institutional round.

### Revenue / Pricing Signals
Pricing signals:
- Hosted API with API keys.
- $10 free credits on sign-up, no card required, according to the company site.
- Per-million-token pricing referenced on the company site.
- Custom/on-prem plan with VPC deployment, volume pricing, dedicated support, custom SLAs, and domain-tuned models.
- Context Gateway is free/open source on GitHub; commercial value likely comes from compression model usage and enterprise deployments.

Revenue is unclear.

### Commercial Health Signals
Public traction signals as of reviewed May 2026 sources:
- YC W26 active company.
- Team size 4 on YC.
- LinkedIn shows 803 followers and 2-10 employees.
- Context Gateway Product Hunt page shows #4 Day Rank for March 6, 2026 and 226 upvotes.
- GitHub repository shows 586 stars, 49 forks, 55 commits, 13 releases, and latest release `v0.5.3` dated March 18, 2026.
- Product Hunt comments show developer interest around spend caps, Slack notifications, lossy compression concerns, structured output handling, and agent workflow fit.

These are developer-awareness signals. Customer count, ARR, retention, gross margin, and enterprise pipeline remain unclear.

## News
- 2026: YC lists Compresr as a Winter 2026 active company, founded in 2026, with San Francisco location and team size 4.
- March 6, 2026: Context Gateway ranked #4 of the day on Product Hunt.
- March 2026: Product Hunt launch page positioned Context Gateway as a tool to cut latency and token spend for Claude Code, Codex, and OpenClaw by compressing tool output.
- March 18, 2026: GitHub lists Context Gateway release `v0.5.3` as the latest release.
- Current public funding news beyond YC backing is unclear.

## Strategic Read
### Why This Company Matters
Compresr addresses a real infrastructure pain in agentic AI: context grows quickly, tool outputs are verbose, and long contexts can increase cost while reducing model focus. If agents become a standard software interface, context compression can become a core optimization layer next to routing, caching, memory, observability, and guardrails.

The product matters because it targets input-token economics and model quality at the same time. The Context Gateway wedge is especially relevant for coding agents, where file reads, logs, diffs, and search outputs create obvious context bloat.

### Risks / Gaps
- Public revenue and customer proof are unclear.
- Pricing transparency is limited on the current pricing page.
- Compression quality needs workload-specific evidence, especially for code, legal, medical, financial, and compliance use cases.
- Native prompt caching and falling model costs can weaken the standalone ROI story.
- Open-source prompt-compression projects can satisfy technical teams that prefer self-hosted infrastructure.
- Enterprise adoption depends on privacy posture, SLAs, data residency, and operational reliability.

### Questions For Follow-Up
- What is the exact pricing per million compressed tokens?
- What are the current paid customer count, ARR, and token volume?
- Which workloads show the strongest retained-accuracy results after compression?
- How does Compresr evaluate code-heavy tool outputs versus prose-heavy RAG context?
- What data retention and training policies apply to hosted compression?
- Which parts of the stack run on-prem, and which parts call Compresr-hosted services?
- How often does compression remove details that later need recovery?
- What customer benchmarks exist beyond FinanceBench and launch demos?
- What is the roadmap for structured data, JSON, source-code-aware compression, and auditability?

## References
- https://compresr.ai/
- https://compresr.ai/docs/overview
- https://compresr.ai/docs/sdk
- https://compresr.ai/docs/models
- https://compresr.ai/docs/gateway
- https://compresr.ai/pricing
- https://www.ycombinator.com/companies/compresr
- https://www.ycombinator.com/deal/
- https://www.linkedin.com/company/compresr
- https://github.com/Compresr-ai/Context-Gateway
- https://www.producthunt.com/products/context-gateway
- https://app.dealroom.co/companies/compresr
- https://www.microsoft.com/en-us/research/project/llmlingua/
- https://github.com/microsoft/LLMLingua
- https://preduce.dev/
- https://docs.compresso.dev/
- https://zur-lix.com/
- https://platform.openai.com/docs/guides/prompt-caching/overview