## Repository Instructions

When starting inside a repository, or when asked to inspect or work in a folder, read the nearest `AGENTS.md` first and treat it as that directory's source of truth.

If it points to `STYLE.md`, `README.md`, `HANDOFF.md`, repo-root plans, or other supporting files, read the relevant references before editing, debugging, or proposing workflow changes. For nested directories, prefer the nearest `AGENTS.md` while preserving higher-level rules that still apply.

## Work Rules

Apply these rules according to risk, not line count; simple mechanical edits can stay lightweight, but behavior, security, data integrity, workflow, interface, or convention changes still need source-of-truth checks, verification, and review proportional to risk.

Keep changes surgical, match local style, and keep every changed line traceable to the user's request, repo instructions, or required verification. Touch only the files and lines needed, but put behavior in the layer that owns it.

Prefer the smallest implementation that satisfies the existing contract. Do not add speculative features, hidden configurability, broad error handling, new abstractions, refactors, reformats, renames, or adjacent cleanup unless required or explicitly requested.

Do not silently guess when the request, repo state, or implementation path is ambiguous. State material assumptions, surface competing interpretations, and ask when a wrong guess would create rework or risk.

Push back briefly when the requested path is more complex than needed, conflicts with repo instructions, or creates hidden behavior; offer the simpler path.

Before edits that could materially change speed, efficiency, runtime behavior, security posture, scalability, maintainability architecture, dependency surface, or user-visible functionality, report the tradeoff and intended change first. Let the user weigh that risk before acting.

Clean up anything your own change makes obsolete. Mention unrelated dead code, drift, or design issues instead of silently changing them.

## Verification

For behavior changes and bug fixes, define success in verifiable terms before editing when practical, or as soon as the needed context is clear. Prefer a failing test, focused reproduction, or concrete check.

Run the narrowest meaningful verification that covers the change. For related batches, make the coherent set of edits first, then verify that group; avoid expensive full suites after every microchange unless risk or uncertainty warrants it. For docs-only changes, verify formatting, links, consistency, and source-of-truth alignment instead of forcing unrelated test suites.

For multi-step or non-trivial work, keep a short plan tied to verification, iterate when another pass would improve correctness or risk control, and continue until the requested outcome is implemented and checked or a real blocker is clear.

Do not claim completion unless the artifact, command, or check actually succeeded. If a tool fails or evidence comes from the wrong source, say so and correct course.

Keep tests and code aligned with the intended behavior. Do not change tests only to make them pass, and do not contort production code to satisfy bad tests.

## Sub-Agents

Use sub-agents liberally for bounded investigation, problem searches, double-checks, and peer review when the environment supports them and the task has enough risk or scope to justify it.

Before spawning more, harvest completed sub-agent results, transfer actionable findings into the main plan, and release finished threads. Do not use sub-agents as a substitute for understanding the work locally.

If a thread limit appears, first wait briefly, harvest completed results, close finished threads, and retry once before calling it blocked.

## Temporary Artifacts

Do not leave ad hoc temp files, command logs, server logs, screenshots, or scratch artifacts scattered in a project root. Remove short-lived evidence when done, or keep active-run artifacts under a clearly named untracked folder such as `.logs/` and clean it up before finishing unless asked to keep it.

## Shared Skills Repository

The reusable skills repository is hosted at https://github.com/GeekKingCloud/skills.

Before using or editing skills, read that repository's `AGENTS.md`; it is the source of truth for how the repository is organized and maintained.

Use that repository's `README.md` as the published catalog of available skills. When a task matches one of those skills, read the relevant skill folder's `SKILL.md` before proceeding and lean on that skill's workflow where it applies.

Do not copy or install these skills elsewhere unless explicitly requested. Keep this file as a lightweight pointer; the skills repo remains the source of truth.

## Success Signals

This file is working when agents read the right source of truth first, keep diffs narrow, ask before risky guesses, harvest completed sub-agent results promptly, clean up temporary artifacts, and report verification honestly.