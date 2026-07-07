# Repository Documentation Workflow

Use this workflow when adding or reorganizing agent-facing repository guidance.

## Recommended split

| File | Job | Put here | Avoid here |
| --- | --- | --- | --- |
| `AGENTS.md` | How agents operate | setup/test commands, workflow rules, reading order, safety boundaries, PR/verification rules | long product essays, private context, transient TODOs |
| `CONTEXT.md` | Why the project exists | purpose, architecture, domain model, URL/data model, ownership boundaries, rationale | commands, coding style, temporary work notes |
| `STYLE.md` | What good looks like | coding/design/content taste, examples, anti-examples, conventions | actual CSS unless that is the project convention, private preferences |
| `HANDOFF.md` | Current restart-safe state | active branch, files, checks, blockers, next action | secrets, logs, permanent documentation |
| Nested `AGENTS.md` | Local overrides | folder-specific commands and constraints | repeating root guidance verbatim |

## Principles

- Keep `AGENTS.md` predictable and practical.
- Put durable context near the code or docs it explains.
- Do not expose private memory or host-local configuration in public repo guidance.
- Prefer short files with clear ownership over one giant instruction dump.
- Link supporting files from the root entry point so agents know when to load them.

## Verification

After changing repo guidance:

- ensure linked files exist
- check that root and nested instructions do not conflict
- run any static checker or `git diff --check`
- read examples as a fresh agent would and remove ambiguity
