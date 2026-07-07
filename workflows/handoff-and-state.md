# Handoff and State Workflow

Use this workflow when work may be interrupted, handed to another agent, resumed later, or coordinated across agents.

## What belongs in a handoff

- goal and current branch/path
- files touched or expected to change
- commands/checks already run and results
- decisions made and why
- blockers and exact next action
- risks or areas needing review

Keep handoffs concise and factual. Do not include secrets, raw logs, private chats, or unnecessary local paths.

## Where to store state

Use the repository's established handoff location when it exists. Otherwise use an untracked scratch/handoff path or the platform's task/session system.

Do not put temporary agent work papers in durable project docs unless they are intentionally promoted into project documentation.

## Before finishing

- update or remove temporary handoff notes
- clean scratch artifacts
- summarize verification evidence
- leave the working tree understandable for the next agent
