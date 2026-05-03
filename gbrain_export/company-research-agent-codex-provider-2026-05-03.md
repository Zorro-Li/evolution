---
type: implementation_note
title: Company Research Agent Codex Provider
updated: '2026-05-03'
tags:
  - codex
  - company-research-agent
  - local-agent
  - manxis
  - no-api-key-mode
---

# Company Research Agent Codex Provider

Modified `/Users/lizongru/codex/进化/tools/company-research-agent` so ManXis/company-research-agent can route model-style prompts through the local Codex CLI.

## Modes

- `MANXIS_RESEARCH_PROVIDER=codex`: direct Codex company research mode. It bypasses the original Tavily/Gemini/OpenAI graph and calls `codex exec --search` to generate the final report.
- `MANXIS_LLM_PROVIDER=codex`: hybrid pipeline mode. Tavily still handles crawl/search/extract, while Codex replaces query generation, briefing generation, report compilation, and markdown cleanup.

## New Files

- `CODEX_PROVIDER.md`
- `backend/providers/codex_provider.py`
- `backend/providers/__init__.py`
- `backend/codex_research.py`

## Verification

- `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m py_compile ...` passed.
- Direct Codex research branch passed with `MANXIS_CODEX_FAKE_RESPONSE`.
- Hybrid query generation passed with `MANXIS_LLM_PROVIDER=codex` and fake response.
- Real `codex exec` probe returned `OK` via `--output-last-message`.

## Tradeoff

The bridge reuses the user's logged-in Codex CLI and keeps API keys out of this app path. Latency follows Codex CLI runtime and can be slower than direct model APIs.
