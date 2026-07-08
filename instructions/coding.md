# Coding Instructions

Use this file for implementation, refactoring, bug fixing, and test work.

## Start with the contract

Before editing, identify the behavior owner:

- public API, CLI, UI, worker, cron job, library function, config, docs, or tests
- existing conventions for file layout, naming, dependency use, and error handling
- the narrowest check that proves the requested behavior

Prefer changes that fit the current contract. If the contract is wrong or unclear, state the ambiguity before changing it.

## Implementation stance

- Make the smallest behavior-owning change that solves the current problem.
- Avoid speculative abstraction, hidden configurability, broad rewrites, and unrelated cleanup.
- Add a new helper/module/class only when it owns a real repeated concept or keeps a large/high-touch file from growing worse.
- Keep dependency surface stable unless the dependency is necessary and justified.
- Preserve public interfaces unless the user or issue explicitly asks for a breaking change.

## Testing stance

Use test-driven development when the expected behavior is clear:

1. Write or identify the failing test/reproduction.
2. Run it and confirm the failure is meaningful.
3. Implement the minimal fix.
4. Rerun the focused check.
5. Broaden to the relevant suite when the changed surface warrants it.

If a formal test harness does not exist, use the closest concrete check: typecheck, lint, build, smoke command, fixture script, snapshot inspection, or source-backed manual verification.

Do not change tests merely to make them pass. Align tests and code with the intended behavior.

## Spikes and uncertainty

When the right design or API is unknown, run a spike instead of pretending to know:

- state the question the spike must answer
- keep throwaway code outside the production path
- measure or observe the result directly
- delete or quarantine scratch artifacts before finishing
- convert the learning into a small implementation or plan

## Commits and PRs

Before committing or opening a PR:

- inspect `git status` and `git diff`
- include only intended files
- run the narrowest relevant checks
- summarize real commands/results, not intentions
- mention remaining risks or skipped checks honestly

Use conventional commit style when the repository already does. Do not push directly to protected branches unless the repo owner explicitly says to.
