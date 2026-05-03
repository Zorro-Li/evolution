# Skill Distillation - 2026-05-03

## @llama_index: Document-Agent Workflow Builder

### Trigger

Use when the task involves messy documents, PDFs, OCR, RAG quality, document extraction, LlamaParse, LlamaCloud, document MCP, or benchmark design for document agents.

### Inputs

- Document set and file types.
- Target workflow or vertical.
- Desired output schema.
- Known failure modes: layout, tables, charts, handwriting, citations, confidence.
- Evaluation sample and acceptance metrics.

### Steps

1. Classify the document domain and downstream agent task.
2. Define parse/extract/index/retrieve/action stages.
3. Choose a parser or API surface: local parser, LlamaParse, LlamaCloud, MCP, or SDK.
4. Create a small eval set with representative failure cases.
5. Run extraction into a structured schema.
6. Attach citations, confidence, and page anchors.
7. Validate outputs against task-specific checks.
8. Package the workflow as a local reusable skill.

### Output

```markdown
## Document Workflow
- Domain:
- Files:
- Parse strategy:
- Extraction schema:
- Retrieval/index plan:
- Agent action:
- Eval cases:
- Failure modes:
- Next automation:
```

### Validation

- Every extracted field has source location or confidence.
- Every benchmark claim has sample size and failure dimensions.
- The final workflow can run on a new document without changing the core steps.

Installed skill: `/Users/lizongru/.codex/skills/x-creator-llama-index/SKILL.md`

## @PortkeyAI: Production AI Control Plane

### Trigger

Use when designing production LLM/agent infrastructure, gateways, policy enforcement, budget controls, agent security, observability, governance, or approval boundaries.

### Inputs

- Agents and tools in scope.
- Sensitive actions and approval tiers.
- Model/provider list.
- User identity and permission model.
- Cost and rate limits.
- Logging, audit, and retention requirements.

### Steps

1. Map every model/tool call through a gateway/control-plane layer.
2. Define allowed actions, blocked actions, and confirmation tiers.
3. Add logging for request, actor, tool, cost, outcome, and error.
4. Add policy checks before tool execution.
5. Add fallback routing for provider failure or rate limits.
6. Add spend and usage views for operators.
7. Add incident review notes for risky or failed actions.
8. Promote stable policy lessons into Jarvis rules.

### Output

```markdown
## AI Control Plane Design
- Actors:
- Tools:
- Policies:
- Approvals:
- Logs:
- Cost controls:
- Fallbacks:
- Security risks:
- Verification command:
```

### Validation

- Each privileged action has actor, approval state, and audit record.
- Each model/tool route has fallback behavior.
- Each budget rule has observable counters.

Installed skill: `/Users/lizongru/.codex/skills/x-creator-portkeyai/SKILL.md`

## @helicone_ai: Open LLMOps Gateway

### Trigger

Use when building or reviewing an LLM app that needs multi-provider access, OpenAI-compatible routing, observability, prompt/version tracking, session/user analytics, cost tracking, or open-source LLMOps.

### Inputs

- Existing model API surface.
- Provider list and model names.
- Logging fields.
- Session/user identifiers.
- Prompt templates.
- Cost and latency targets.
- Local/self-hosted requirements.

### Steps

1. Preserve an OpenAI-compatible client interface where feasible.
2. Route requests through a gateway endpoint.
3. Log request, response, model, latency, cost, user/session, prompt version, and error.
4. Add fallback and provider-routing logic.
5. Add dashboards for usage, cost, sessions, prompts, and failures.
6. Add a replay/debug workflow for failed requests.
7. Keep self-host/open-source options visible for trust.
8. Evaluate internal agents by work class and workload share.

### Output

```markdown
## LLMOps Gateway Plan
- Client interface:
- Gateway endpoint:
- Providers:
- Observability fields:
- Routing/fallback:
- Debug workflow:
- Dashboard:
- Open-source/self-host stance:
```

### Validation

- A single request can be traced from user/session to model/provider to final output.
- Failures generate useful debug records.
- Provider changes do not require application-layer rewrites.

Installed skill: `/Users/lizongru/.codex/skills/x-creator-helicone-ai/SKILL.md`

## @geekbb: Codex State Maintenance

### Trigger

Use when Codex feels slow after heavy use, when `.codex/sessions/`, long JSONL chats, worktrees, logs, stale project config, or long-lived dev processes may be adding local drag.

### Inputs

- Codex home path and current workspace path.
- Current Codex running state.
- Active repo chats that still need continuity.
- Size/age thresholds for sessions, worktrees, logs, and config.
- Desired mode: report-only, backup-only, or apply.

### Steps

1. Run a read-only report first: session sizes, archive size, stale worktrees, log size, config candidates, and heavy dev processes.
2. Identify important old repo chats that still need continuity.
3. Generate handoff docs and reactivation prompts for those chats.
4. Back up local Codex metadata before any apply step.
5. Archive stale sessions, worktrees, and logs with manifests and restore paths.
6. Prune stale config/project references after backup.
7. Run the read-only report again and compare results.
8. Add a weekly report-only reminder for heavy users.

### Output

```markdown
## Codex State Report
- Active session size:
- Archived session size:
- Largest session candidates:
- Worktree candidates:
- Log size:
- Config candidates:
- Heavy dev processes:
- Handoff docs needed:
- Safe next action:
- Verification command:
```

### Validation

- The first pass changes no files.
- Important old chats have handoff docs or keep decisions.
- Every apply action has backup, archive path, manifest, and restore route.
- Maintenance runs after Codex is closed or through an explicit wait-for-exit flow.

Installed skill: `/Users/lizongru/.codex/skills/codex-state-maintenance/SKILL.md`
