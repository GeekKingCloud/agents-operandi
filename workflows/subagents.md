# Purposeful Sub-Agent Workflow

Use sub-agents liberally on substantial work when parallel investigation, independent judgment, or focused expertise can improve the result. Do not spawn them merely to create activity: every sub-agent needs a role in the reasoning system.

## Useful Roles

| Role | Contribution | Typical question |
| --- | --- | --- |
| **Proposer** | Develops a concrete approach or implementation slice. | What is the strongest practical solution? |
| **Skeptic** | Challenges assumptions, complexity, and hidden failure modes. | Why might this be wrong or needlessly elaborate? |
| **Goal steward** | Guards the user's intent, boundaries, and acceptance criteria. | Does this still solve the requested problem? |
| **Verifier** | Checks claims against source, behavior, commands, or artifacts. | What is actually proved, and what remains inferred? |
| **Specialist** | Applies relevant domain knowledge to a bounded surface. | What would an expert in this risk area catch? |

Roles are lenses and authority boundaries, not decorative personas. One agent may own a bounded implementation slice; another may be read-only. For difficult decisions, a proposer and skeptic can form a useful debate while the goal steward prevents the argument from drifting away from the user's outcome.

## Dispatch Contract

Give every sub-agent:

- its role and the concrete question it must answer
- exact repository, worktree, paths, revision, or artifact
- relevant source context and assumptions to verify
- scope, ownership, files it may edit, and actions it must not take
- evidence expectations and checks it should run
- required output shape and completion condition

Do not dispatch vague requests such as “review this” or “help with the repo.” Independence comes from a clear lens and fresh judgment, not missing context.

Avoid concurrent edits to the same files unless the workflow explicitly supports reconciliation. Prefer read-only parallel review while one owner integrates, or give workers disjoint file ownership.

## Approval and Required Gates

Follow the active environment and skill policy for sub-agent approval. If approval is required and has not been granted, ask before relying on meaningful delegated work.

When the user, task contract, or selected skill requires reviewer or sub-agent coverage, treat it as a hard gate. If that coverage becomes unavailable, stop and ask whether to wait, abort, or continue in an explicitly degraded local-only mode. Never silently substitute self-review and report normal confidence.

## Model and Provider Routing

Route by responsibility and risk, not a fashionable model name:

- strongest available reasoning/agentic tier for orchestration, architecture, difficult debugging, and final judgment
- domain-matched worker for a bounded specialist task
- faster/cheaper worker for mechanical search or transformation when errors are easy to detect
- strong, preferably independent reviewer for Roast, security, and release gates

Cross-provider routing is also a data-sharing decision. Check privacy and environment policy before sending private code or context to a different provider. If model availability or reviewer independence materially weakens a required gate, report it.

If a lower-cost worker fails twice without producing new evidence, change the model tier, role, brief, or approach instead of repeating the same dispatch.

## Integration

Harvest completed results before spawning replacements. Verify findings against the real source, transfer actionable items into the main plan, and release finished threads.

If a thread limit appears, wait briefly, harvest and close completed threads, then retry once before treating capacity as a blocker.

The orchestrator owns the final decision. Resolve disagreement against the user's goal, source of truth, observed evidence, risk, and simplicity. Do not vote, average opinions, or accept a confident sub-agent summary without checking it.

Final reporting should name the purposeful roles used, what they examined, which findings changed the work, and any required lens that was unavailable.
