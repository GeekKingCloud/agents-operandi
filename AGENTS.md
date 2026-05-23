# Shared Skills Repository

The reusable skills repository is hosted at https://github.com/GeekKingCloud/skills.

Before using or editing skills, read that repository's `AGENTS.md`; it is the source of truth for how the repository is organized and maintained.

Use that repository's `README.md` as the published catalog of available skills. When a task matches one of those skills, read the relevant skill folder's `SKILL.md` before proceeding and lean on that skill's workflow where it applies.

Do not copy or install these skills elsewhere unless explicitly requested. Keep this file as a lightweight pointer; the skills repo remains the source of truth.

## Repository Instructions

When starting inside a repository, or when asked to inspect or work in a folder, look for the nearest `AGENTS.md` before doing work. Read it first and treat it as the repository's agent-facing source of truth for that directory.

If that `AGENTS.md` points to supporting files such as `STYLE.md`, `README.md`, `HANDOFF.md`, or repo-root plan files, read the relevant referenced files before editing or proposing workflow changes. Lean on those instructions within that directory and any nested scope they define.

If a nested directory has its own `AGENTS.md`, prefer the nearest one for files under that directory, while preserving higher-level instructions that still apply.

## Coding Agent Work Baseline

These guidelines apply to non-trivial coding, review, refactor, debugging, and documentation work. For obvious one-line fixes, use judgment and keep the response lightweight.

### Think Before Coding

Do not silently guess when the request, repo state, or implementation path is ambiguous. State material assumptions, surface competing interpretations, and ask for clarification when a wrong guess would create rework or risk.

Push back when the requested path appears more complex than necessary, conflicts with repo instructions, or would create hidden behavior. Explain the tradeoff briefly and offer the simpler path.

### Simplicity First

Prefer the smallest implementation that satisfies the request and the repo's existing contract. Do not add speculative features, hidden configurability, new abstractions, or broad error handling that is not required by the current behavior.

If a solution becomes larger than the problem warrants, simplify before finishing.

### Surgical Changes

Touch only the files and lines needed for the task. Match existing local style even when another style would be personally preferable.

Do not refactor, reformat, rename, or clean up adjacent code unless it is required for the task or explicitly requested. If unrelated dead code, drift, or design issues are noticed, mention them rather than silently changing them.

Clean up imports, variables, helpers, files, or tests that your own change made obsolete. Do not remove pre-existing dead code unless asked.

Every changed line should trace back to the user's request, repo instructions, or required verification.

Before making edits that could materially change project speed, efficiency, runtime behavior, security posture, scalability, maintainability architecture, dependency surface, or user-visible functionality, report the tradeoff and intended change first. Let the user weigh that risk before acting, even when the change has a plausible security or underlying engineering benefit.

### Parallel Review And Sub-Agents

When the environment supports sub-agents, use them liberally for independent investigation, problem searches, double-checks, and peer review of meaningful changes. Prefer bounded, parallel tasks with clear ownership, such as searching for related failure paths, reviewing a proposed patch, checking tests, or looking for regressions in a specific module.

Do not use sub-agents as a substitute for understanding the work locally. Keep immediate blocking decisions in the main thread, and integrate sub-agent findings critically against the repo's source of truth.

### Iteration Discipline

Loop over analysis, edits, and verification when another pass is likely to tighten correctness, clarity, or risk control. Multiple passes are encouraged for non-trivial work, especially after tests, review findings, or ambiguous behavior.

Do not overthink simple problems. Iteration should tighten the solution, not expand scope, invent speculative concerns, or delay a clear fix.

### Temporary Artifacts And Logs

Do not leave ad hoc temp files, command logs, server logs, screenshots, or generated scratch artifacts scattered in a project root. For short-lived evidence, remove the files once they are no longer needed. When logs or scratch artifacts must remain during an active run, keep them under a clearly named untracked folder such as `untracked.logs/` and clean that folder up before finishing unless the user asks to keep it.
### Goal-Driven Execution

For behavior changes and bug fixes, define success in verifiable terms. Prefer a failing test, focused reproduction, or concrete check before changing code, then run the narrowest meaningful verification afterward.

For multi-step work, use a short plan that pairs each step with its verification. Keep working until the requested outcome is implemented and checked, or clearly report the blocker.

Do not claim that work was completed unless the artifact, command, or verification check actually succeeded. If a tool fails, an attachment is unavailable, or a result was inferred from the wrong source, say that plainly and correct course instead of presenting it as done.

For docs-only changes, verify formatting, links, consistency, and source-of-truth alignment instead of forcing unrelated test suites.

### Test And Code Alignment

Do not change tests only to make them pass. If existing tests no longer match the intended behavior, update them so they still verify the desired functionality and source-of-truth contract.

Do not write awkward production code only to satisfy awkward tests. First decide whether the test expresses the right product or architecture goal, then update code, tests, or both so they align with safe implementation practice and the repository's style.
