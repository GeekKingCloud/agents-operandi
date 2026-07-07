# AGENTS Instruction Kit

This repository is a reusable instruction kit for AI coding agents and adjacent assistants. It starts with `AGENTS.md` as the predictable entry point, then routes deeper tasks to focused supporting files.

`AGENTS.md` is intentionally short enough to be read every time. The rest of the kit is opt-in context for work that needs it: coding, review, research, personal-assistant behavior, operations, computer use, skills, harnesses, privacy, verification, handoff, and repository documentation.

## Why this shape

The public AGENTS.md convention treats `AGENTS.md` as a README for agents: a dedicated place for build steps, tests, conventions, and workflow guidance that would clutter a human README.

This kit keeps those lessons portable:

- **One predictable entry point:** agents should read the nearest `AGENTS.md` first.
- **Focused supporting docs:** heavy guidance lives in small files loaded only when relevant.
- **Repo-local truth:** downstream projects can copy only the pieces they need.
- **No private assumptions:** examples are synthetic and should not contain credentials, routing IDs, personal memory, or host-local paths.

## File map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Universal entry point and routing table. |
| `instructions/` | Task-type guidance: coding, review, research, assistant behavior, operations, skills/harnesses, computer use, security/privacy. |
| `workflows/` | Reusable process loops: generate/evaluate/repair, verification, subagents, handoff/state, repository docs. |
| `rubrics/` | Review and eval rubrics that can be applied to plans, code, harnesses, and safety-sensitive changes. |
| `templates/` | Copyable starter files for downstream projects. |
| `examples/` | Small example layouts showing how to use the kit. |
| `scripts/check-agents-kit.py` | Static validation for this repository's structure and privacy hygiene. |

## Adoption patterns

### Minimal project

Copy the downstream starter, not this repository's maintainer entry point:

```text
templates/AGENTS.md -> AGENTS.md
```

Use this when the project is small and does not need the full instruction-kit tree.

### Software project

Copy:

```text
templates/AGENTS.md -> AGENTS.md
templates/CONTEXT.md -> CONTEXT.md
templates/STYLE.md -> STYLE.md
```

Then add project-specific setup/test commands and coding conventions. Keep `CONTEXT.md` for why the project exists and `STYLE.md` for what good work looks like.

### Agent-heavy or operations project

Copy the starter root file plus relevant modules:

```text
templates/AGENTS.md -> AGENTS.md
instructions/coding.md
instructions/ops-and-automation.md
instructions/security-and-privacy.md
workflows/generate-evaluate-repair.md
workflows/verification.md
rubrics/security-safety.md
```

Add `instructions/personal-assistant.md` and `rubrics/agent-harness-eval.md` when the repo controls prompts, channels, cron jobs, assistants, MCP servers, evals, or other live agent behavior.

## Companion resources

This kit is self-contained and does not require any external skill library. Teams that already use reusable procedure libraries can treat them as optional companions; one example is https://github.com/GeekKingCloud/skills.

External skills should never be required for adopting this AGENTS kit. See `instructions/skills-and-harnesses.md` for scoped guidance on using optional companion skills when a project or user explicitly opts in.

## Editing this repo

Useful reference point:

- https://agents.md/ for the cross-agent `AGENTS.md` convention.

1. Read `AGENTS.md`.
2. Keep root guidance short and route task-specific detail into supporting files.
3. Keep examples synthetic.
4. Run:

```bash
python3 scripts/check-agents-kit.py
git diff --check
```

5. If you change the structure, update this README and the static check in the same PR.

## What not to put here

- Secrets, tokens, private keys, OAuth state, local databases, session logs, or routing IDs.
- Personal memory or host-local assistant facts.
- Tool-specific commands that are only true on one private machine.
- Long generated transcripts or temporary agent work papers.
- Exact-output goldens for inherently flexible agent behavior unless there is a deterministic contract.
