# Code Review Rubric

Use this rubric for PRs, diffs, modules, and implementation plans.

## Critical questions

- Does the change implement the requested behavior and no surprising extra behavior?
- Can it fail safely?
- Are secrets, credentials, user data, and permissions handled correctly?
- Are tests or checks meaningful and close to the changed behavior?
- Does the code live in the right layer?
- Does it preserve existing contracts and migration paths?
- Is the naming clear enough for the next maintainer?

## Severity guide

- **Critical:** exploitable security issue, data loss, broken production path, credential exposure.
- **High:** likely correctness failure, unsafe default, missing auth/permission boundary, untested destructive operation.
- **Medium:** maintainability or reliability issue likely to cause bugs soon.
- **Low:** minor clarity, style, or coverage gap.
- **Nit:** optional polish.

## Approval bar

Approve only when Critical/High/Medium issues are fixed, accepted by the owner, or clearly out of scope with a documented blocker.
