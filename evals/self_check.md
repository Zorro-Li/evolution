# Self-Check

Before claiming this Jarvis layer is ready, verify:

- `python3 jarvis.py status` runs.
- `python3 jarvis.py self-check` passes.
- `python3 jarvis.py reflect` writes a reflection and proposal.
- `python3 scripts/evolve_self_memory.py --print-summary` writes self-memory files.
- `python3 jarvis.py auto-review --repo /path/to/git/repo --dry-run` builds a Codex review command.
- `AGENTS.md` contains the voice, identity, load order, and evolution loop.
- Memory files contain a current profile, durable rules, operating state, and lessons.
