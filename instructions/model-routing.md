# Model Routing Instructions

Use this file when an environment supports multiple models or sub-agents and the task benefits from splitting orchestration from execution.

## Orchestrator and workers

- The orchestrator owns task intake, integration, gates, and final judgment; give it the strongest available reasoning/agentic model.
- Workers handle bounded slices; match the model to the task class, not to habit.
- Keep product decisions and release judgment in the orchestrator regardless of worker strength. A strong worker can propose; only the orchestrator accepts.
- Give each worker the dispatch context from `workflows/subagents.md`: target, goal, boundaries, and acceptance criteria. Model choice does not replace a clear brief.

## Matching models to task classes

Route by task class, not by model name:

- Deep implementation, architecture, and tricky debugging go to the strongest tier.
- Domain-specialized work, such as frontend/UI polish, goes to the model the team has found strongest for that domain.
- Mechanical edits, renames, formatting, broad search, and summarization go to a cheaper/faster tier.
- Review and roast gates go to a strong tier; prefer a different model family than the author of the change for independent perspective when available.
- Security review goes to a strong tier, never the cheapest.

When a task mixes classes, route by the riskiest part: a mostly mechanical change with one behavior-owning edit is a behavior change.

Escalation rule: if a cheaper worker fails twice or returns low-confidence output, escalate the model tier instead of retrying the same tier. Repeating the same tier on the same failure burns budget without new evidence.

## Defaults file

Concrete model names go stale quickly; never hardcode them in instructions, workflows, or skills.

- Keep per-environment defaults in a repo-local `MODEL-DEFAULTS.md` copied from `templates/MODEL-DEFAULTS.md`, with a last-verified date.
- Update the defaults file when the environment's model lineup changes, and refresh the last-verified date whenever names are re-checked against provider docs.
- If the defaults file is missing or stale, use the environment's default model and say so in the final report.
- Treat the defaults file as guidance for routing, not as permission: availability, cost limits, and environment policy still apply.

## Verification

- Cross-model outputs are evidence, not truth: the orchestrator verifies worker output against source before integrating.
- Record which model produced which artifact when it affects review independence, especially for review, roast, and security gates.
- If routing choices materially shaped the outcome, such as a degraded tier or a same-family reviewer, state that in the final report so the reader can weigh the evidence.
