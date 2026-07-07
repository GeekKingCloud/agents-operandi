# Review and Roast Workflow

Use this workflow for strict review gates and release-readiness passes.

## Steps

1. Define scope: repo, diff, file, plan, prompt, harness, or release candidate.
2. Read local instructions and relevant context.
3. Inspect evidence before judging.
4. Report findings with severity, evidence, impact, and fix direction.
5. Fix actionable Critical/High/Medium findings when in scope.
6. Rerun focused checks or review the patch again.
7. Stop when remaining risks are Low/nit, accepted, or externally blocked.

## Roast stance

Be direct and useful. Critique the artifact, not the person. Security and correctness beat style.

## Release gate

A change is not ready if it has unresolved actionable Critical, High, or Medium findings. If a finding is external or blocked, state the blocker and cap the grade instead of pretending it is resolved.
