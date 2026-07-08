# Plan Quality Rubric

Use this rubric for implementation plans, migration plans, and multi-agent work queues.

## A strong plan includes

- goal and non-goals
- current context and assumptions
- exact files or surfaces likely to change
- bite-sized ordered tasks
- verification for each meaningful task
- rollback or recovery notes for risky changes
- privacy/security considerations
- open questions that genuinely affect implementation

## Red flags

- vague tasks such as "improve architecture"
- no verification commands or acceptance criteria
- hidden dependency on private context
- broad rewrites without a reason
- no sequencing for migrations or data changes
- no owner decision points for risky actions

## Approval bar

The implementer should be able to start without guessing. If they must infer file paths, test commands, or success criteria for core work, the plan is incomplete.
