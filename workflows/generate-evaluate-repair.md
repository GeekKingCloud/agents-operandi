# Generate / Evaluate / Repair Workflow

Use this workflow for non-trivial coding, setup, automation, research synthesis, skills, prompt, harness, or assistant-behavior work.

## Loop

1. **Define Done.** Write or infer observable acceptance criteria before calling work complete.
2. **Generate.** Create the smallest useful artifact: patch, draft, plan, script, fixture, eval, or summary.
3. **Evaluate.** Run the narrowest meaningful check: test, lint, typecheck, build, dry-run, health check, diff review, source-backed rubric, or manual inspection.
4. **Repair.** Fix observed failures or gaps. Do not change the check merely to pass unless the check is wrong and the reason is documented. After a repeated or expensive failure, find the root cause and propose the durable prevention — a skill rule, `AGENTS.md` line, template change, or checkpoint — instead of retrying blind.
5. **Repeat.** Continue while each pass reduces risk or uncertainty.
6. **Stop.** Finish when the artifact is verified, or when the remaining blocker needs owner input, credentials, permissions, destructive action, unusual cost, or a product decision.

## Keep it proportional

Do not run a ceremony for simple Q&A, tiny wording changes, or tasks where the user explicitly asked for a rough draft only. Do not run broad expensive suites when a focused check proves the changed behavior.

## Good evaluation examples

| Work | Evaluation |
| --- | --- |
| Bug fix | failing reproduction now passes |
| CLI/script | dry-run or fixture invocation returns expected result |
| Prompt/policy | scenario rubric catches the intended behavior and a negative mutation fails |
| Research | key claims are tied to primary sources or marked uncertain |
| Docs | links, file references, and examples match the repo |
| Ops | health check or status command confirms the target state |

## Report

Final summaries should name the artifact, the checks actually run, the result, and any remaining risk. Do not imply unrun checks passed.
