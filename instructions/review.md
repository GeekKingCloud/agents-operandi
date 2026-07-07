# Review Instructions

Use this file for code review, architecture review, PR review, roast, and release-risk checks.

## Review target

Clarify what is being reviewed:

- entire repository
- changed diff
- specific file/module
- plan
- prompt or harness
- release candidate
- security-sensitive surface

Do not default to a whole-repo review when the user names a directed artifact.

## Finding format

For each major issue, include:

- **Severity:** Critical, High, Medium, Low, or Nit
- **Evidence:** file path, line, command result, or exact observed behavior
- **Impact:** what can break, leak, slow down, confuse, or become hard to maintain
- **Fix direction:** concrete next step

Separate confirmed findings from suspicions and evidence gaps. Do not invent problems to sound thorough.

## Priority order

1. Security and privacy
2. Correctness and data integrity
3. Reliability, failure handling, and idempotency
4. Tests and verification gaps
5. Architecture and ownership boundaries
6. Maintainability, naming, comments, and style

Style findings still need evidence. Prefer "this name lies about the value's role" over "naming is bad."

## Directed artifact reviews

For eval suites, prompts, agent policies, workflows, or harnesses, review whether the artifact catches the failure mode it claims to catch.

Ask:

- Does it test behavior or only check for ceremonial wording?
- Is it side-effect free by default?
- Does it avoid secrets, live channels, production services, and local private state?
- Can it fail usefully on a negative mutation?
- Is it documented and wired into the normal check path?
- What false positives or false negatives remain acceptable?

## Grade

Use a grade only when useful:

- **A:** boringly solid, only minor polish
- **B:** mergeable with manageable debt
- **C:** works but weakly tested or awkwardly structured
- **D:** fragile, risky, or expensive to maintain
- **F:** unsafe, broken, unreviewable, or built on wishful thinking

Security findings cap the grade until fixed.
