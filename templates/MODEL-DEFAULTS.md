# Model Defaults

Environment-specific model routing defaults; edit the rows for your environment. Concrete names below are examples only.

Last verified: <date> — update this date whenever the names are re-checked against provider docs.

| Role / task class | Default | Fallback | Notes |
| --- | --- | --- | --- |
| Orchestration, integration, final judgment | Claude Fable 5 | GPT-5.5 Codex (high reasoning) | strongest available agentic model |
| Frontend / UI implementation | Claude Opus 4.8 | Claude Sonnet 5 | domain preference |
| Backend / general implementation | Claude Sonnet 5 | GPT-5.5 Codex | balance cost and capability |
| Mechanical edits, search, summarization | Claude Haiku 4.5 | any small fast model | cheap tier; escalate after two failures |
| Review / roast gate | GPT-5.5 Codex (high) | Claude Opus 4.8 | prefer different family than the author |
| Security review | Claude Fable 5 | GPT-5.5 Codex (high) | never the cheapest tier |

The example rows reflect the maintainer's July 2026 environment; replace them with the models actually available where this file lives.

## How to use

- Copy this file to the repo root or agent config location as `MODEL-DEFAULTS.md`.
- Route work per `instructions/model-routing.md`; this file only supplies the concrete names.
- Use the fallback when the default is unavailable, rate-limited, or has failed twice on the task.
- Availability, cost limits, and environment policy still override these defaults.

## Refresh rule

This file is a durable index: it must carry a last-verified date, and agents should treat stale entries (over ~2 months old) as suggestions to re-verify, not facts.
