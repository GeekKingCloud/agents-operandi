# Assistant Operations Repository Instructions

This example assumes the top-level kit directories are available next to the copied root `AGENTS.md`. When reading this example in-place, use the top-level kit paths:

- `../../instructions/personal-assistant.md` for owner-facing behavior
- `../../instructions/ops-and-automation.md` for cron/services/scripts
- `../../instructions/security-and-privacy.md` before touching channels, credentials, logs, or user data
- `../../rubrics/agent-harness-eval.md` before changing prompts, evals, or assistant policy

All generic checks must be safe on a fresh clone: no real sends, no production cron registration, no gateway restarts, and no credential reads unless a live opt-in is explicit.
