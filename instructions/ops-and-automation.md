# Operations and Automation Instructions

Use this file for servers, scripts, cron jobs, service checks, deployment glue, local infrastructure, and automation around real systems.

## Default stance

Treat automation as potentially live. Before running or changing it, identify:

- target host/profile/environment
- credentials or secrets involved
- external side effects
- rollback path
- expected verification signal

Prefer dry-runs, fake HOME/profile dirs, temp directories, and fixture data for generic checks.

## Safe repair

Local drift is often repairable: stale generated config, missing user-level dependencies, broken wrappers, expired caches, or missing local indexes.

Bound repair work:

1. inspect logs/config/docs narrowly
2. apply the smallest reversible fix
3. rerun the failed command
4. verify the service/job/deliverable state
5. report remaining blockers with exact next action

Ask before privileged, destructive, expensive, credentialed, public, or privacy-sensitive repair.

## Cron and background jobs

- Temporary polling jobs must stop after the condition is resolved.
- Script-only cron wrappers should finish quickly or launch a monitored child and report sanitized status.
- Failure messages should be concise and sanitized: no tokens, raw tracebacks, local paths, route IDs, or full logs.
- Keep job prompts self-contained; future runs should not depend on chat context.

## Long-running work

Define a stall rule before starting renders, broad scans, migrations, large downloads, or generated helper scripts: if the process runs longer than the expected window without producing new evidence, stop, inspect processes and artifacts, and report whether a valid partial artifact exists instead of waiting silently.

After a failed or stuck long run, do a root-cause pass before retrying: what stalled, what evidence would have caught it earlier, and what durable rule, timeout, or checkpoint would prevent it. A retry without a diagnosis usually reproduces the failure. Known-slow suites with predictable output are exempt; say which case applies.

## Services

For long-running services, start them with the environment's process manager when available. Verify readiness with a health check or log signal. Clean up temporary servers/watchers when done.

Do not restart or stop a service from inside the active request path if doing so can kill the process producing the current reply. Use an external control plane or ask the owner when needed.
