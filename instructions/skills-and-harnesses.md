# Skills and Harness Instructions

Use this file for reusable skills, prompt libraries, evals, agent policies, MCP/tool wrappers, and assistant-behavior harnesses.

## Skills

A good skill is procedural memory, not a diary entry. It should include:

- when to use it
- prerequisites and required tools
- exact steps or decision points
- pitfalls and repair notes
- verification commands or acceptance criteria
- linked references, scripts, or templates when useful

Keep skills generic unless they explicitly belong to one identity or private environment.

## Optional companion skills

This kit should remain usable without any external skill repository. Optional external skill libraries may complement this file, but they are not dependencies. Use this repository's guidance by default.

If the user or project explicitly opts into an external skill library, load only the specific procedure needed for the task. Do not fetch, install, vendor, or require external skills without explicit opt-in. If an optional external skill is unavailable, do not mention it unless the user specifically asked to use that skill or its absence materially changes the result.

The GeekKingCloud skills repository is one example of an optional companion source:

- https://github.com/GeekKingCloud/skills

Useful skills to look for when available and opted in:

- **Crucible** and **Roast** together for release-hardening loops: generate a focused change, review it strictly, repair concrete findings, and verify again.
- **Handoff** for restart-safe state transfer between agents, machines, SSH sessions, or context windows.
- **Find** for locating prior context, decisions, examples, or collaboration history before asking a human to repeat it.
- **Feedback** for reviewing previous agent work and turning collaboration history into process improvements.

Use domain assessment skills, such as SEO readiness, agent readiness, or accessibility readiness, only when the target artifact has that surface. They are optional gates, not default requirements.

## Prompt and policy changes

Treat prompt changes as behavior changes. Before editing:

- state the behavior being changed
- identify the failure mode or user correction motivating it
- keep the wording small and durable
- avoid overfitting to one transcript or one model's quirks
- add or update a regression check when the behavior is important

## Evals and harnesses

Default to static/offline checks for generic agent behavior. Live tests that send messages, register cron jobs, hit production services, or read credentials must be opt-in and clearly labeled.

A useful eval should:

- encode a real failure mode
- assert behavior, not exact prose, unless exact output is the contract
- use synthetic fixtures
- avoid secrets and host-local state
- be runnable on a fresh clone when possible
- prove it can fail with a negative mutation or fixture

## MCP and tool surfaces

Document:

- what the tool can access
- what actions are read-only vs mutating
- required credentials and safe storage location
- rate limits, cost, and external side effects
- dry-run or sandbox mode
- smoke test and rollback path
