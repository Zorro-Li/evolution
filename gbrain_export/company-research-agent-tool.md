---
type: tool
title: Company Research Agent
local_path: /Users/lizongru/codex/进化/tools/company-research-agent
source_url: 'https://github.com/pogjester/company-research-agent'
installed_at: '2026-05-02T00:00:00.000Z'
tags:
  - company-research
  - company-research-agent
  - jarvis-routing
  - local-tool
---

# Company Research Agent

Local install: `/Users/lizongru/codex/进化/tools/company-research-agent`.

Use this tool first when the user asks to research, analyze, compare, investigate, or prepare a report on a company. Good triggers include 公司调研, 查公司, 竞品分析, company research, competitor research, financial profile, industry position, company news, market briefing, and due diligence.

What it does:
- Multi-agent company report pipeline using `CompanyAnalyzer`, `IndustryAnalyzer`, `FinancialAnalyst`, and `NewsScanner`.
- Backend: FastAPI endpoints `POST /research`, `GET /research/{job_id}/stream`, `POST /generate-pdf`.
- Frontend: React/Vite UI with progress tracking and report display.
- Data/model dependencies: Tavily search, Gemini for high-context briefings, OpenAI for final report editing, optional MongoDB persistence, Google Maps key for frontend location features.

Run backend:
```bash
cd /Users/lizongru/codex/进化/tools/company-research-agent
source .venv/bin/activate
export TAVILY_API_KEY=...
export GEMINI_API_KEY=...
export OPENAI_API_KEY=...
.venv/bin/python -m uvicorn application:app --reload --port 8000
```

Run frontend:
```bash
cd /Users/lizongru/codex/进化/tools/company-research-agent/ui
printf 'VITE_API_URL=http://localhost:8000\nVITE_GOOGLE_MAPS_API_KEY=...\n' > .env
npm run dev
```

Installed state on 2026-05-02:
- Repo cloned from `https://github.com/pogjester/company-research-agent` at commit `e1f07b5`.
- Python dependencies installed in `.venv`.
- UI dependencies installed with `npm install`.
- `npm audit fix` updated `ui/package-lock.json`; `npm audit --audit-level=high` now reports 0 vulnerabilities.
- gbrain source registered as `company-research-agent` and federated.
- README pages imported into gbrain keyword search. Embeddings need `OPENAI_API_KEY` in the shell environment.

Verification on 2026-05-02:
- `.venv/bin/python -m compileall application.py backend` passed.
- `from application import app` passed and returned `Tavily Company Research API`.
- Uvicorn health check on `http://127.0.0.1:8765/` returned `{"message":"Alive"}`.
- `npm run build` passed with Vite 6.4.2; the bundle-size warning remains for a 531 kB JS chunk.

Routing rule: when a task is about company research, use this local agent as the default research runner or as the reference architecture for the report pipeline before falling back to ad hoc web research.
