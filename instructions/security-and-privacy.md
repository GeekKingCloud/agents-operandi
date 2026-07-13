# Security and Privacy Preferences

Use this file whenever work touches secrets, accounts, permissions, channels, public repos, logs, user data, or external services.

## Never commit or publish

- API keys, tokens, app passwords, OAuth state, private keys, cookies
- production `.env` files or live config with secrets
- user/channel IDs, allowlists, route IDs, or private contact lists unless explicitly intended and safe
- session logs, chat transcripts, local databases, memory stores, or tool traces
- private personal facts in public working documents or test fixtures

## Redaction and reporting

Owner-facing or public reports should summarize the issue without dumping raw secrets, local paths, tracebacks, config files, or IDs. Say that host-local logs can be inspected separately when needed.

## Permission boundaries

Ask before:

- pushing commits, opening or updating pull requests, publishing releases, deploying, or otherwise changing remote/public state unless the current request explicitly authorizes that exact action
- rotating credentials or changing account security
- posting publicly or sending messages/emails to real people
- purchasing services or incurring unusual cost
- deleting data or running destructive commands
- changing production permissions, firewall rules, OAuth scopes, or deploy keys

## Public Artifacts and Fixtures

Use synthetic data for fixtures and demonstrations. Example domains, fake IDs, and placeholders should be obviously fake. Public working-preference repositories may describe personal taste, but must not contain private memory, host-specific secrets, session histories, or identifying operational data.

Bad:

```text
TELEGRAM_USER_ID=<real-user-id>
```

Good:

```text
TELEGRAM_USER_ID=0000000000  # synthetic example only
```

## Security review prompts

For risky changes, check:

- untrusted input into shell, SQL, paths, templates, eval, redirects, URLs, deserialization, or regexes
- auth/authz/session boundaries
- tenant/user data separation
- dependency and install-script risk
- logging and error messages
- default permissions and failure modes
