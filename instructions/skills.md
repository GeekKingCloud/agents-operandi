# Skill Preferences

Use this file whenever a task names or clearly matches a reusable skill, or when substantial work needs a defined review, recovery, assessment, or publication procedure.

## Default Toolbelt

The [GeekKingCloud skills repository](https://github.com/GeekKingCloud/skills) is the default procedure layer for my work. Its `README.md` is the catalog and each skill's complete `SKILL.md` is the source of truth for that workflow.

- Before using or editing the skills repository, read its nearest `AGENTS.md` and treat that as the repository source of truth.
- Inspect the available skill catalog before substantial work.
- If the user names a skill, add it to the plan, read its `SKILL.md` completely, and follow it.
- If the task clearly matches an available skill, say why it applies, read it, and use it without waiting for the user to know its name.
- Read only the references the selected skill routes to, but read required instruction files completely.
- Prefer scripts, templates, and assets supplied by the skill over re-creating them.
- A skill supplies procedure; it does not expand user authority, weaken repository rules, or turn a local task into permission to publish.

Do not copy, install, vendor, or sync skills elsewhere unless the user explicitly requests it. When an expected skill is missing, ask to install or make it available; that request establishes the authority boundary instead of bypassing it.

Do not silently simulate a required reviewer gate or replace it with an improvised weaker workflow. An unrelated missing skill is not a reason to block.

## Preferred Routes

| Need | Preferred skill route |
| --- | --- |
| Substantial implementation or release hardening | Crucible to orchestrate, Roast as the strict evidence-backed gate |
| Blunt code, architecture, plan, or release-risk review | Roast |
| Collaboration-history analysis and durable preference discovery | Feedback |
| Locate a prior coding-agent conversation | Find |
| Pause or transfer unfinished work | Handoff |
| Resume after interruption, crash, or context loss | Recover |
| Publish an authorized local change to GitHub | The GitHub publication/yeet workflow |
| Accessibility, SEO, agent-readiness, security, media, or other specialized work | The matching domain skill |

Use Crucible and Roast proportionally. They are defaults for substantial or high-risk work, not an excuse to wrap trivial questions or mechanical edits in release ceremony.

## Skills, Prompts, and Harnesses

Treat changes to skills, prompts, agent policies, evals, and tool wrappers as behavior changes:

- state the behavior or failure mode being changed
- identify the authoritative source and affected consumers
- keep wording durable rather than overfitting one transcript or model quirk
- add or update a regression check when the behavior is important
- validate that an eval can fail on a realistic negative mutation when practical
- keep generic checks offline and synthetic by default
- require explicit opt-in for live messages, credentials, production services, cron jobs, or external side effects

For MCP and other tool surfaces, document access, read-only versus mutating actions, credential storage, cost/rate limits, side effects, dry-run behavior, smoke proof, and rollback.

## Source-State Discipline

Distinguish source repositories, installed copies, cached plugin versions, generated outputs, and summaries. If the user asks for the latest local skill, inspect the source checkout they identify rather than assuming the installed copy is current. Report the exact source and revision when version choice matters.
