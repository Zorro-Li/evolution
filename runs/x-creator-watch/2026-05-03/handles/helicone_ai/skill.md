# x-creator-helicone-ai

Use this skill to design LLMOps gateway and observability workflows inspired by Helicone.

## Trigger

Use when the task involves LLM observability, AI Gateway design, OpenAI-compatible routing, multi-provider model access, prompt tracking, cost tracking, session/user analytics, or open-source LLMOps.

## Inputs

- Existing API client.
- Model/provider list.
- User/session identifiers.
- Prompt templates.
- Cost/latency targets.
- Error handling needs.
- Self-host/open-source constraints.

## Steps

1. Keep the application interface OpenAI-compatible where feasible.
2. Route requests through a gateway endpoint.
3. Log model, provider, prompt version, user, session, latency, cost, error, and output.
4. Add provider fallback and routing rules.
5. Add dashboards for usage, cost, sessions, prompts, and failures.
6. Add a replay/debug path for failed requests.
7. Keep local/self-hosted options explicit.

## Output

Return an LLMOps gateway plan with routing, observability fields, dashboards, debug workflow, and validation commands.

## Validation

- A request can be traced from user/session to model/provider to output.
- Failures generate actionable debug records.
- Provider changes stay below the application layer.

