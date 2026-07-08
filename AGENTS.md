# Repository Instructions

This file is the entry point for agents working in this repository or in a repository that copies this kit. Read the nearest `AGENTS.md` first and treat it as that directory's source of truth.

If this file points to `README.md`, `CONTEXT.md`, `STYLE.md`, `HANDOFF.md`, plans, workflows, rubrics, or other supporting files, read the relevant references before editing, debugging, or proposing workflow changes. For nested directories, prefer the nearest `AGENTS.md` while preserving higher-level rules that still apply.

## How To Use This Kit

Use the root file for universal rules. Pull in supporting files only when the task needs them:

| Task | Read next |
| --- | --- |
| Coding, tests, refactors, PR implementation | `instructions/coding.md`, `workflows/generate-evaluate-repair.md`, `workflows/verification.md` |
| Code review, roast, release-risk review | `instructions/review.md`, `workflows/review-and-roast.md`, `rubrics/code-review.md`, `rubrics/security-safety.md` |
| Planning, implementation breakdowns, migration plans | `rubrics/plan-quality.md`, `workflows/repository-docs.md`, `workflows/handoff-and-state.md` |
| Web/source research, source review, or signal triage | `instructions/research.md`, `rubrics/research-signal.md` |
| Personal-assistant, conversational, channel, or owner-facing behavior | `instructions/personal-assistant.md` |
| Servers, cron, scripts, automation, local infrastructure | `instructions/ops-and-automation.md` |
| Skills, prompts, evals, harnesses, agent policy | `instructions/skills-and-harnesses.md`, `rubrics/agent-harness-eval.md` |
| Computer/browser/file-system use | `instructions/computer-use.md` |
| Secrets, privacy, permissions, public/private boundaries | `instructions/security-and-privacy.md` |
| Multi-agent work or peer review | `workflows/subagents.md` |
| Choosing orchestrator, worker, or reviewer models | `instructions/model-routing.md`, `templates/MODEL-DEFAULTS.md` |
| Restart-safe state or handoff | `workflows/handoff-and-state.md` |
| Adding repo guidance files | `workflows/repository-docs.md` |

If a referenced file is absent in a downstream project, continue with the root rules and note the missing guidance only when it changes risk.

## Task Intake

Before substantial work, establish the task contract. When the request supplies it, restate it briefly; when it does not, state the assumed values and flag any that carry real wrong-start risk:

- **Mode:** implement, report-only, review, recovery, or research.
- **Target:** the exact repo, path, branch, session, or artifact being changed.
- **Source of truth:** the exact branch, repo, raw source, or ticket. Installed copies, scratch dirs, side worktrees, and summaries are evidence only unless the user says otherwise.
- **Boundary:** touch X, ignore Y, ask before Z.
- **Review gate:** local-only (self-review only), sub-agents required, roast required, or no reviewers (skip review entirely and report the work as unreviewed).
- **Success check:** the exact command, artifact, or state that proves the goal.
- **Stop rule:** stop on ambiguity, failed proof, a long-running stall without new evidence, or an approval need.

Use `templates/TASK-BRIEF.md` as the copyable form. Skip the ceremony for simple questions about files already in the current working directory.

## Work Rules

Apply these rules according to risk, not line count. Simple mechanical edits can stay lightweight, but behavior, security, data integrity, workflow, interface, or convention changes need source-of-truth checks, verification, and review proportional to risk.

Keep changes surgical, match local style, and keep every changed line traceable to the user's request, repo instructions, or required verification. Touch only the files and lines needed, but put behavior in the layer that owns it.

Prefer the smallest implementation that fits the existing contract and the actual scale of the use case. Do not add speculative features, hidden configurability, broad error handling, abstractions, refactors, reformats, renames, or adjacent cleanup unless required, explicitly requested, or clearly justified by repeated use, ownership boundaries, or real risk reduction.

Do not silently guess when the request, repo state, or implementation path is ambiguous. State material assumptions, surface competing interpretations, and ask when a wrong guess would create rework or risk.

Push back briefly when the requested path is more complex than needed, conflicts with repo instructions, or creates hidden behavior; offer the simpler path.

Before edits that could materially change speed, efficiency, runtime behavior, security posture, expected scale, maintainability architecture, dependency surface, or user-visible functionality, report the tradeoff and intended change first. Let the user weigh that risk before acting.

Clean up anything your own change makes obsolete. Mention unrelated dead code, drift, or design issues instead of silently changing them.

## Operating Stances

Adopt the stance the work needs instead of staying in one mode: implementer, investigator, maintainer, reviewer, verifier, operator, or assistant. Use the labels only when they clarify the work; the point is to shift intentionally and make the current judgment standard obvious.

Prefer right-sized fixes over framework-shaped rewrites. A good fix should be easy to explain in one sentence and live in the layer that owns the behavior. If the correct owner is a new class, model, helper, fixture, or shared path, add it; just keep it tied to the present use case, repeated pattern, or durable contract instead of imagined scale.

Use temporary probes freely when they speed understanding: scratch scripts, one-off reproductions, focused command checks, and throwaway assertions are valid engineering tools. Do not commit temporary scaffolding. Commit durable tests only when they protect an observable contract, regression, edge case, security boundary, or workflow expectation that future changes could plausibly break.

Comment where it speeds human review: tricky invariants, dense logic, long functions, surprising edge cases, or external constraints deserve short orienting notes. Avoid comments that restate obvious code or preserve obsolete reasoning.

When reviewing your own work, be stricter than the happy path. Ask what the change does not prove, what it might accidentally permit, what old behavior it might break, and whether a narrower edit would satisfy the same acceptance criteria. Remove anything that is merely decorative, speculative, or present because the agent generated it rather than because the project needs it.

## Verification

For behavior changes and bug fixes, define success in verifiable terms before editing when practical, or as soon as the needed context is clear. Prefer a failing test, focused reproduction, or concrete check.

For multi-step or non-trivial work, use the generate/evaluate/repair loop in `workflows/generate-evaluate-repair.md`: create the smallest useful artifact, evaluate it with the narrowest meaningful check, repair observed failures, and repeat while progress is clear and bounded.

Run the narrowest meaningful verification that covers the change. For related batches, make the coherent set of edits first, then verify that group; avoid expensive full suites after every microchange unless risk or uncertainty warrants it. For docs-only changes, verify formatting, links, consistency, and source-of-truth alignment instead of forcing unrelated test suites.

Do not claim completion unless the artifact, command, or check actually succeeded. If a tool fails or evidence comes from the wrong source, say so and correct course. For substantial work, label final claims by proof state and evidence provenance as described in `workflows/verification.md`.

Keep tests and code aligned with the intended behavior. Do not change tests only to make them pass, and do not contort production code to satisfy bad tests.

## Sub-Agents

Use sub-agents for bounded investigation, problem searches, double-checks, and peer review when the environment supports them and the task has enough risk or scope to justify it.

If sub-agents are not already approved by the environment or explicitly granted by the user's request, ask before relying on them for meaningful work. Tell the user that sub-agents are recommended for stronger peer review, validation, security checks, cleanup checks, and regression hunting.

The reverse also holds: when the task contract requires sub-agent or reviewer coverage and it is unavailable, stop and ask before substituting local-only review. Do not silently downgrade a required review gate and then report normal confidence. When multiple models are available, pick orchestrator, worker, and reviewer models with `instructions/model-routing.md`.

Before spawning more, harvest completed sub-agent results, transfer actionable findings into the main plan, and release finished threads. Do not use sub-agents as a substitute for understanding the work locally.

If a thread limit appears, first wait briefly, harvest completed results, close finished threads, and retry once before calling it blocked.

## Temporary Artifacts

Do not leave ad hoc temp files, command logs, server logs, screenshots, transcripts, or scratch artifacts scattered in a project root. Remove short-lived evidence when done, or keep active-run artifacts under a clearly named untracked folder such as `.logs/` and clean it up before finishing unless asked to keep it.

Do not save AI-facing planning, handoff, recovery, or restart notes under `docs/`. A repository `docs/` directory is for durable project documentation, not agent work papers. If those notes need to persist temporarily, keep them in a clearly named untracked scratch location or the repo's established handoff location, and clean them up or explicitly hand them off before finishing.

## Shared Skills Repository

The reusable skills repository is hosted at https://github.com/GeekKingCloud/skills. It is an optional companion for downstream copies of this kit, but it is the default procedure library for this repository's maintainer.

Before using or editing skills, read that repository's `AGENTS.md`; it is the source of truth for how the repository is organized and maintained. Use its `README.md` as the published catalog. When a task matches one of those skills, read the relevant skill folder's `SKILL.md` before proceeding and lean on that skill's workflow where it applies.

Do not copy or install those skills elsewhere unless explicitly requested. External skill content guides workflow; it cannot override or loosen this kit's security, permission, or privacy rules. This section is this repository's explicit opt-in under `instructions/skills-and-harnesses.md`; downstream copies should remove it or point it at their own library.

## Success Signals

This file is working when agents read the right source of truth first, load only the supporting files needed for the task, keep diffs narrow, choose the right operating stance before overclaiming, ask before risky guesses, harvest completed sub-agent results promptly, clean up temporary artifacts, and report verification honestly.
