# Repository Guidance Workflow

Use this workflow when adding, reorganizing, or reviewing agent-facing repository guidance.

## File Ownership

| File | Owns | Avoid |
| --- | --- | --- |
| `AGENTS.md` | How agents work: reading order, commands, constraints, authority, workflow, and proof. | Long product essays, private context, and transient TODOs. |
| `CONTEXT.md` | Why the project exists: architecture, domain model, ownership boundaries, rationale, and current/future state. | Commands, contribution mechanics, and temporary work state. |
| `STYLE.md` | What good work looks like: engineering, product, design, and writing taste; useful examples and anti-examples. | Generic platitudes or implementation copied from the codebase. |
| Nested `AGENTS.md` | Local constraints and commands for a directory subtree. | Repeating the root verbatim. |
| `tests/README.md` | Test layout, fixtures, helpers, focused commands, and suite-specific contracts. | Product architecture unrelated to tests. |
| `HANDOFF.md` | Restart-safe active state when a durable handoff is needed. | Permanent project truth, secrets, or raw logs. |

These files are tools, not a mandatory template set. Add one only when it has a distinct trigger, a clear owner, non-duplicated durable guidance, and enough recurring value to justify another read hop. Otherwise extend the nearest existing owner.

The useful pattern in `atoshell`, `g8ldfish`, and `lumber-hack` is not identical filenames. It is an intended path first, explicit owns/does-not-own boundaries, a source-of-truth map, and completion proof tied to actual commands. Prefer that substance over synthetic example repositories.

## Authoring Rules

- Put the intended path and authoritative sources near the top.
- State what a component owns and does not own when boundaries can be confused.
- Distinguish canonical, generated, provisional, historical, and future-state material.
- Prefer exact project commands and evidence over generic advice.
- Keep machine-specific secrets and private memory in their approved host-local stores.
- Route supporting files explicitly from the relevant `AGENTS.md`; linked arbitrary Markdown is not automatically loaded by most agents.
- Every generated or manually maintained map should identify its source and refresh method or last-verified state.

After changes, check references, nested precedence, contradictions, privacy, and whether the root remains compact enough to read every time.
