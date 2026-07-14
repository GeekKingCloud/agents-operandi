# Implementation Finish Workflow

Use this only after requested code behavior works and before final verification, commit, or handoff. It is a personal development finish policy: leave the task-owned surface as the smallest clear, conventional implementation of the real requirement without turning cleanup into another project. Do not load or run it for development work that did not create or materially change an implementation.

## Bound the Pass

- Start with the task contract and task diff, including staged, unstaged, and relevant untracked work created for the task.
- Read the complete affected files and only the immediate owners or consumers needed to judge a concrete cleanup candidate.
- Keep changes within the request and directly affected flow. Report worthwhile adjacent cleanup instead of silently expanding scope.
- Preserve unrelated work and generated, vendored, dependency, lock, build, cache, and coverage output unless the task explicitly owns it.
- For a tiny change, one deliberate diff read may be the whole pass. Match effort to risk and change size.

## Remove Unjustified Machinery

Ask what current contract, repeated concept, risk, or readability need pays for every added or materially changed layer.

- Remove one-use helpers, wrappers, indirection, configuration, and abstractions when they make current behavior harder to follow without owning a durable concept or boundary.
- Collapse speculative options, fallbacks, compatibility paths, and defensive branches that serve imagined requirements rather than a supported caller or demonstrated failure mode.
- Prefer established repository conventions and helpers over new local machinery.
- Keep domain structure that names real concepts or makes a high-touch surface easier to maintain. Fewer files or lines are not automatically simpler.

Never remove authentication, authorization, validation at trust boundaries, output escaping, data-integrity checks, meaningful error handling, required observability, or other safety controls merely because they look verbose. Remove duplicate internal guards only when every supported entry point and the invariant's lifetime are affirmatively understood.

## Keep Tests and Explanations Durable

- Keep tests that protect observable behavior, business rules, regressions, security boundaries, integration contracts, or stable interfaces.
- Reconsider task-created tests that only lock in private structure, incidental call order, temporary scaffolding, or non-contract prose. Do not weaken a valid test merely because the implementation fails it.
- Do not build elaborate permanent test infrastructure for trivial or intentionally temporary behavior when a focused check is more honest; repository-required gates and durable coverage for important risk still apply.
- Remove comments that narrate obvious code, justify the agent's process, apologize, or preserve implementation archaeology. Keep comments that explain non-obvious invariants or external constraints.
- Remove temporary probes, abandoned alternatives, stale task-created TODOs, and files made obsolete by the final implementation.

## Preserve Contracts, Then Verify

Trace visible consumers before removing a public interface, persisted shape, migration bridge, compatibility layer, configuration key, or integration behavior. Stop before cleanup would change requested behavior, weaken security or recovery, become an architectural rewrite, or remove plausible external or stored-data support without evidence.

After cleanup, review the final diff, run the narrowest checks that prove the contract, run broader repository gates when required, and recheck status for residue. Any later code or test change invalidates intersecting proof: return here as needed and rerun every affected check before claiming completion.
