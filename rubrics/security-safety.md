# Security and Safety Rubric

Use this rubric for any change that touches permissions, data, external services, automation, or user-visible channels.

## Check surfaces

- secrets and credentials
- auth/authz/session handling
- user/tenant data boundaries
- untrusted input into shell, SQL, file paths, templates, URLs, deserializers, eval-like APIs, regexes, or redirects
- logging, traces, errors, and generated artifacts
- dependency/install hooks
- destructive commands and rollback
- public posting, messaging, or email sends
- cost and rate limits

## Safe defaults

- read-only before mutating
- dry-run before live run
- fake fixtures before real data
- least privilege credentials
- explicit owner approval for risky side effects
- sanitized reports

## Findings

Every finding needs evidence, impact, and a concrete fix. Do not bury security issues under style feedback.
