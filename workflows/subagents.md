# Sub-Agent Workflow

Use sub-agents for parallel search, independent review, security passes, cleanup checks, and alternate design perspectives when the environment supports them.

## Required review gates

When the task contract, skill, or user request requires sub-agent or reviewer coverage, treat that as a hard gate. If sub-agents become unavailable, stop and ask whether to wait, abort, or continue in an explicitly degraded local-only mode. Do not silently substitute local-only review and report normal confidence; a downgraded gate must be named in the final report.

## When to use

Good uses:

- search a large repo for related patterns
- review a plan or diff from a fresh context
- run a security/privacy lens
- compare implementation options
- inspect docs for consistency
- validate an eval or harness design

Poor uses:

- work needing user interaction
- tasks where the sub-agent lacks required secrets or context
- conflicting edits to the same files
- replacing the main agent's understanding or final judgment

## Model selection

When the environment offers multiple models, match them to roles with `instructions/model-routing.md`: strongest tier for orchestration and final judgment, task-matched tiers for workers, and reviewers from a different model family than the author when available.

## Dispatch pattern

Give each sub-agent:

- target repo/path
- exact task goal
- relevant files or context snippets
- what not to edit, if read-only
- output format and acceptance criteria

Harvest results before spawning more. Transfer actionable findings into the main plan, verify them against source, and discard unsupported claims.

## Review lenses

For substantial changes, use multiple lenses when useful:

- implementer/maintainer
- release-risk/roast reviewer
- security/privacy reviewer
- docs/readability reviewer
- operator/user-experience reviewer
- test/eval reviewer

## Final responsibility

Sub-agent summaries are evidence, not truth. The main agent must integrate, verify, and own the final decision.
