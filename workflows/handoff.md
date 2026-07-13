# Handoff and State Workflow

Use this workflow when work may be interrupted, moved across agents or machines, resumed after context loss, or left in a branch/worktree for later inspection.

## Required State

- goal and current mode
- source repository and exact worktree path
- branch and local commit hashes
- changed and uncommitted files
- checks run, results, and evidence provenance
- decisions made and why
- blockers, residual risks, and exact next action
- publication state: local-only, pushed, PR URL, or release state

Use `templates/HANDOFF.md` when a durable file is useful. Prefer the repository's established handoff location or the platform task/session system; otherwise use a clearly named untracked scratch path.

Do not put transient agent work papers under durable `docs/`, and do not include secrets, raw private logs, chat transcripts, or unnecessary identifying data.

## Before Pausing or Finishing

- confirm the reported path, branch, commits, and status are current
- update or remove stale temporary handoff notes
- clean scratch artifacts and temporary processes
- distinguish completed work from next work
- leave the tree understandable and state the narrowest command or action that resumes it
