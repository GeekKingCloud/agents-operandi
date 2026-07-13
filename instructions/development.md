# Development Preferences

Use this file for implementation, debugging, refactoring, tests, repository maintenance, Git work, and development-tool choices.

## Understand Before Editing

- Read the nearest `AGENTS.md` and the relevant `README.md`, `STYLE.md`, `CONTEXT.md`, nested guidance, plans, and test documentation.
- Inspect the actual implementation, recent history, current branch/worktree state, and existing checks. Do not reason only from filenames, summaries, or intended architecture.
- Identify the behavior owner, public contract, local conventions, and narrowest proof of success.
- When the design or API is uncertain, run a bounded spike with a concrete question. Keep throwaway code outside production paths and remove it when the question is answered.

## Implementation Taste

- Make the smallest behavior-owning change that solves the current problem.
- Match local architecture, naming, error handling, dependency choices, and formatting unless changing them is part of the request.
- Preserve public interfaces unless a breaking change is requested and its migration cost is understood.
- Add a helper, module, class, abstraction, or configuration surface only when it owns a real concept, removes demonstrated repetition, or protects an important boundary.
- Avoid defensive code for impossible states, broad catches that hide failures, compatibility shims with no active consumer, and cleanup unrelated to the requested outcome.
- Comment tricky invariants, surprising edge cases, and external constraints. Do not narrate obvious code or preserve stale reasoning.
- Clean up files, branches, scaffolding, flags, and documentation made obsolete by the change; mention unrelated drift instead of silently expanding scope.

## Tests and Verification

When expected behavior is clear, prefer a concrete failing test or reproduction before the fix. Confirm that it fails for the right reason, implement the minimal correction, rerun the focused check, then broaden only when the changed surface warrants it.

If no formal test harness exists, use the closest real proof: typecheck, lint, build, smoke command, fixture, snapshot inspection, dry-run, or source-backed manual verification. Do not change a test merely to make it pass, and do not contort production behavior around a bad assertion.

Commit durable tests when they protect an observable contract, regression, edge case, security boundary, or workflow expectation that could plausibly break again. Do not promote every temporary probe into permanent test scaffolding.

Use `workflows/verification.md` for proof states, provenance, and final claims.

## Git and Work Location

- Inspect `git status`, branch, worktrees, and relevant history before editing.
- Work in the current checkout for small isolated changes when safe. Prefer a dedicated branch and isolated worktree for substantial work, concurrent work, risky experiments, or when another agent may touch the original checkout.
- Local commits are allowed when they create useful checkpoints or a reviewable unit. Include only intended changes and use the repository's commit convention.
- Always report the exact repository or worktree path, branch, local commits, and remaining uncommitted state. Do not leave completed work hidden in an unnamed worktree.
- Never push, create or update a pull request, merge, tag, release, or deploy without specific user authorization for that remote action. Ask when publication would be the useful next step.
- Before any authorized publication, inspect the diff and status, run the relevant checks, and report skipped proof or residual risk honestly.

## Default Development Loop

A capable coding agent working directly in its native harness is the default. It can inspect, plan, implement, verify, review, and iterate without adding orchestration machinery simply because that machinery exists.

Escalate to the AutoDev tools only when durable coordination provides demonstrated value:

| Tool | Owns | Does not own |
| --- | --- | --- |
| [`lumber-hack`](https://github.com/GeekKingCloud/lumber-hack) | Turning current/future state into a durable plan, ticket queue, and execution workflow. | The ticket database or implementation itself. |
| [`atoshell`](https://github.com/GeekKingCloud/atoshell) | Ticket state, dependencies, assignments, comments, and status transitions. | Product specifications, planning judgment, or orchestration policy. |
| [`g8ldfish`](https://github.com/GeekKingCloud/g8ldfish) | Parallel execution and verification of already-defined tickets. “Goldfish” may be used conversationally. | Deciding what should be built or decomposing an undefined goal. |

The full pipeline is experimental, not a default dependency. Use it when durable decomposition, parallel ownership, recovery after interruption, auditability, or coordination across many agents outweighs setup and state-management overhead. Otherwise stay in the native harness.

When evaluating the tools, compare the same representative task through direct agent execution, a Crucible-governed native run, and the full AutoDev pipeline. Judge delivery quality, elapsed effort, recovery, coordination clarity, and proof—not novelty or amount of machinery.

When software work adds or changes agent-facing project documentation, follow `workflows/repository-guidance.md` rather than inventing a second file taxonomy here.
