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

## Services

For long-running services, start them with the environment's process manager when available. Verify readiness with a health check or log signal. Clean up temporary servers/watchers when done.

Do not restart or stop a service from inside the active request path if doing so can kill the process producing the current reply. Use an external control plane or ask the owner when needed.
