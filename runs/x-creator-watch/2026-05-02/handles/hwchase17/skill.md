---
name: x-creator-hwchase17
description: Track Harrison Chase, LangChain, LangSmith, agent harnesses, harness engineering, open harnesses, context management, continual learning for AI agents, Deep Agents, create_agent, Browserbase, browser-use agents, and production-agent reliability.
---

# X Creator: Harrison Chase

## Core Use

Use this skill to convert `@hwchase17` posts into agent-infrastructure intelligence: harness design, open agent runtimes, context management, LangChain/LangSmith product direction, Deep Agents, and browser/web subagents.

## Inputs

- `@hwchase17` posts, retweets, quote posts, articles, profile metadata
- linked LangChain/LangSmith/DeepAgents/Browserbase posts
- partner posts from LangChain ecosystem builders
- visible engagement metrics and link-card/article context

## Workflow

1. Capture:
   - URL
   - timestamp label
   - text
   - original/retweet/quote/article status
   - referenced product or partner
   - visible engagement metrics
2. Classify:
   - harness engineering
   - open harness / portability
   - context management
   - continual learning
   - Deep Agents / `create_agent`
   - browser-use agents / web access
   - observability / production reliability
   - hiring / company signal
3. Extract:
   - model layer
   - harness/runtime layer
   - context/memory layer
   - tool/browser layer
   - observability layer
   - partner ecosystem
4. Map to Jarvis:
   - identify local harness design implications
   - turn context-management claims into memory/runtime checks
   - turn browser-agent posts into Computer Use and browser QA experiments
   - turn open-harness claims into portability requirements
5. Write an agent-infrastructure brief with "thesis", "runtime layer", "product signal", "partner graph", and "local experiment".

## Pattern Library

| Pattern | What To Look For | How To Use It |
|---|---|---|
| Harness thesis | "harness", "harness engineering", "open harnesses". | Track LangChain's agent runtime positioning. |
| Layered learning | model, harness, context. | Separate model capability from runtime and memory improvements. |
| Context manager | context-window fill-up, who decides, context policy. | Define explicit context-management rules for local agents. |
| Deep Agents primitive | `create_agent`, DeepAgents, simple harness primitive. | Evaluate API primitives as reusable local-agent building blocks. |
| Browser subagents | Browserbase, search/fetch/browser subagents, web access. | Map to Computer Use, browser automation, and observability tests. |
| Ecosystem proof | retweeted partner examples and conference clips. | Add quoted accounts to watch graph and capture launch timing. |

## Output Template

```md
# Agent Harness Signal

## Source
| URL | Type | Date | Product/partner | Engagement |
|---|---|---|---|---|

## Thesis
<one concise claim>

## Runtime Map
model -> harness -> context -> tools/browser -> observability

## Partner Graph
<accounts, products, and integration surfaces>

## Jarvis Experiment
<local test or design rule>
```

## Failure Modes

- Reading harness posts as naming alone while missing runtime design implications.
- Losing partner accounts that reveal ecosystem adoption.
- Treating model switching as the main portability problem while harness switching carries the deeper lock-in signal.
- Capturing browser-agent announcements without observability and permission boundaries.

