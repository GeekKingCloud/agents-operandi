# Operations and Automation Preferences

Use this file for servers, scripts, scheduled jobs, service checks, deployment glue, local infrastructure, and automation around real systems.

## Establish the Live Boundary

Before running or changing automation, identify the target host/profile/environment, credentials involved, external side effects, rollback path, and expected verification signal. Treat unknown automation as potentially live.

Prefer read-only probes, dry-runs, fake profiles, temporary directories, fixtures, and reversible changes. Ask before privileged, destructive, expensive, credentialed, public, privacy-sensitive, or production-impacting repair.

## Repair Loop

1. Inspect the narrowest useful logs, configuration, implementation, and documentation.
2. Identify root cause rather than guessing from the final error.
3. Apply the smallest reversible fix in the layer that owns the fault.
4. Rerun the failed command and verify the service, job, or deliverable state.
5. Report remaining blockers with the exact next action and authority needed.

## Long-Running Work

Define a stall rule before renders, broad scans, migrations, downloads, or generated helper jobs. If the process exceeds the expected window without new evidence, stop waiting silently: inspect the process and artifacts, decide whether a valid partial result exists, and report its state.

After a failed or stuck run, do a root-cause pass before retrying: what stalled, what evidence would have exposed it sooner, and what timeout, checkpoint, or durable instruction prevents recurrence. Known-slow work with predictable progress is exempt when that expectation is stated.

## Services and Scheduled Work

- Use the environment's process manager for long-running services when available; verify readiness with a health check or direct log signal.
- Clean up temporary servers, watchers, pollers, and jobs when the terminal condition is reached.
- Keep scheduled prompts self-contained; future runs must not depend on hidden chat context.
- Sanitize status and failures. Do not leak tokens, private IDs, raw logs, tracebacks, or unnecessary local paths.
- Do not restart or stop a service from inside the active request path when it could kill the process producing the current response. Use an external control plane or ask the owner.
