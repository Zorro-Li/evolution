# X Creator Watch Automation

Purpose: daily use Safari with the logged-in X account `soro` to inspect the following list, identify AI and US-market creators, archive accessible tweets/posts, analyze each creator, distill repeatable workflows into skills, and save reusable knowledge to GBrain.

Primary skill: `/Users/lizongru/.codex/skills/x-creator-distiller/SKILL.md`

Daily operating path:

1. Use the 6551 API capture script as the primary data path:
   `python3 scripts/x_6551_capture.py --registry runs/x-creator-watch/2026-05-02/00_following_registry.md --categories AI_CORE,US_STOCKS_MACRO --limit <N>`
2. Use Computer Use with Safari for logged-in X access when following-list refresh, pinned posts, images, videos, article previews, or API gaps need verification.
3. Start from the following list for the `soro` account.
4. Process a realistic daily batch of unprocessed creators.
5. Store outputs under `runs/x-creator-watch/YYYY-MM-DD/`.
6. Install high-value creator skills under `/Users/lizongru/.codex/skills/x-creator-<handle>/`.
7. Save compact reusable synthesis to GBrain.
8. Publish completed deconstruction outputs to GitHub:
   `python3 scripts/publish_x_deconstruction_to_github.py --run-dir runs/x-creator-watch/YYYY-MM-DD`
9. Record Jarvis observation and report blockers.

GitHub publishing policy:

- Default upload includes run-level Markdown/CSV reports and per-handle `profile.md`, `analysis.md`, and `skill.md`.
- Default upload excludes raw tweet/API archives under `raw/`.
- Use `--include-raw` only when the destination repo is appropriate for raw public tweet/API exports.
- The publisher stages only X creator deconstruction artifacts and related automation scripts, so unrelated local changes stay out of the commit.

6551 API notes:

- `TWITTER_TOKEN` must be set in the environment.
- `twitter_user_info` is used for profile snapshots.
- `twitter_search` with `fromUser` is used for recent tweets.
- `twitter_user_tweets` currently returns a paid-plan gate on this token.
- A public following-list endpoint was not available in the local 6551 skill; use the existing registry as the seed and Safari for following-list refreshes.

Escalation:

- For X API, payment, credit-card, API-key, identity-verification, or account-approval steps, stop on the official page in Safari.
- Send `zongru001103@gmail.com` an email with the page URL, reason, required action, and local run path.
- Store the same escalation note in the run folder.

Quality bar:

- Every claim has a source URL or local raw-file pointer.
- Every creator report answers what they do, where they are strong, and how the user can reuse their method.
- Every generated skill contains trigger, inputs, workflow, output, and validation.
- Public-facing Markdown uses original synthesis, links, metadata, and short source anchors.
