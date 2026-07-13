# AGENTS

This repository is the public backup of my working preferences for coding agents and adjacent assistants. It is built for how I work. It is not a generic starter kit, a copy-this-repo onboarding system, or an attempt to make one configuration suit everyone.

The root `AGENTS.md` is the small, predictable entry point. It contains the durable rules that should be visible every time and routes task-specific work to focused files that agents load only when relevant. Reusable procedures live in [GeekKingCloud/skills](https://github.com/GeekKingCloud/skills) instead of being copied here as competing rubrics.

## Structure

| Path | Responsibility |
| --- | --- |
| `AGENTS.md` | Core preferences, task contract, routing, skill policy, and authority boundary. |
| `instructions/development.md` | Software work, testing, Git practices, and AutoDev experiments. |
| `instructions/skills.md` | First-class use of the GeekKingCloud skill toolbelt. |
| `instructions/research.md` | Source hierarchy and evidence-backed synthesis. |
| `instructions/computer-use.md` | Browsers, GUIs, terminals, filesystems, and media. |
| `instructions/operations.md` | Automation, services, long-running jobs, and safe repair. |
| `instructions/personal-assistant.md` | Owner-facing communication and autonomy boundaries. |
| `instructions/security-and-privacy.md` | Secrets, permissions, publishing, and private data. |
| `workflows/subagents.md` | Purposeful roles, debate structure, dispatch, and integration. |
| `workflows/verification.md` | Checks, proof states, provenance, and evidence boundaries. |
| `workflows/handoff.md` | Restart-safe state and exact work-location reporting. |
| `workflows/repository-guidance.md` | Ownership split for `AGENTS.md`, `CONTEXT.md`, `STYLE.md`, and related files. |
| `templates/TASK-BRIEF.md` | Durable task control state when a brief helps. |
| `templates/PLAN.md` | Verification-linked plan for multi-step work. |
| `templates/HANDOFF.md` | Restart-safe location, state, proof, and next action. |
| `scripts/check-agents.py` | Structural, reference, and public-repository privacy checks. |

This shape follows the useful part of the [AGENTS.md convention](https://agents.md/): a predictable agent entry point with repository-specific guidance. The extra files are an explicit routing system; agents do not automatically load arbitrary linked Markdown, so the root says what to read and when.

## Design Choices

- Personal preferences beat broad portability. Public visibility lets others borrow ideas, but does not weaken my defaults.
- The root remains compact. Detailed software, research, computer-use, operational, and assistant preferences live with their owning task type.
- Skills own reusable procedures and review machinery. This repository says which procedures I expect agents to use; it does not duplicate them.
- Sub-agents need a reason to exist. Roles such as proposer, skeptic, goal steward, verifier, and specialist create useful tension and evidence instead of parallel noise.
- A capable coding agent working directly in its native harness is the default development loop. `lumber-hack`, `atoshell`, and `g8ldfish` remain useful experiments for durable decomposition, ticket state, and parallel execution when those costs are justified.
- Local work is easy to authorize and inspect. Remote publication always requires a specific request.

## Editing This Repository

Use commit `0e98352`—the original single-file baseline—as a semantic regression oracle, not as a reason to preserve old structure. Any new file must earn its place by owning guidance that is both useful and expensive to load on every task.

Run the repository checks after changes:

```powershell
python scripts/check-agents.py
git diff --check
```

The checker is a structural and policy smoke guard: it rejects the old generic-kit directories, broken or escaping local links, missing high-value policy markers, and common secret or private-home-path patterns. Substring markers catch accidental deletion, not semantic correctness; a human or Roast review still decides whether the guidance reflects how I work.
