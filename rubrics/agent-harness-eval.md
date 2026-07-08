# Agent Harness Eval Rubric

Use this rubric for prompt, policy, skill, assistant-behavior, MCP/tool, cron, channel, and eval-harness changes.

## Core checks

A good agent harness or regression eval:

- encodes a real failure mode or durable behavior contract
- evaluates behavior, not just exact phrasing
- is side-effect free by default
- uses synthetic fixtures and fake recipients/accounts
- avoids reading real secrets, sessions, memories, logs, or host-local config
- does not send live email/chat messages, register cron jobs, restart gateways, or mutate production state unless explicitly in a live opt-in tier
- is wired into a normal check path or clearly documented as manual
- proves it can fail usefully through a negative mutation, fixture, or documented failure mode
- reports concise human-readable failures

## Risk questions

- Could running this on a fresh clone surprise the user?
- Could artifacts leak private context?
- Could a model-as-judge drift make the gate flaky?
- Does the eval create false confidence by checking for words rather than outcomes?
- Are live tests clearly separated from static/offline tests?

## Grade caps

- Live side effects by default cap at **D**.
- Secret or private data in fixtures caps at **F** until removed.
- No meaningful failure mode caps at **C** because the eval is probably decoration.
