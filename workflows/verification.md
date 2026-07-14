# Verification Workflow

Verification turns confidence into evidence.

## Choose the narrowest meaningful check

Start with the check closest to the changed behavior:

- targeted unit/integration test
- reproduction script
- linter/typechecker/formatter
- build command
- dry-run or fixture execution
- config validation
- health check
- static link/reference check
- source-backed manual review

Broaden only when the changed surface is shared, risky, or likely to affect unrelated areas.

## Verification cadence

Verification has a cost, so match its cadence to the evidence needed. During a coherent implementation batch, prefer the smallest reliable test case, filter, reproduction, or focused check that can falsify the changed behavior. Do not default to an entire test file or suite after every small fix when a narrower check proves the same claim. Use the smallest affected file or group when tighter isolation is unavailable or would be misleading.

Keep logical commit boundaries separate from broad-suite cadence. Accumulate related fixes and run broader intersecting checks once the batch is stable, at a meaningful integration, handoff, review, delivery, or risk checkpoint. When a broad run fails, iterate on the failing subset and rerun the broader check once the affected batch is stable instead of repeating it after every repair.

When an interruption is imminent, make an already-authorized safety-checkpoint push first and record pending proof rather than risking the accumulated commits while a broad gate runs. Complete the broader gates on resume before claiming readiness or delivery.

Cost never overrides proof. Shared fixtures, cross-cutting behavior, security-sensitive changes, or repository-required final gates may justify earlier or repeated broad verification. Rerun a check whenever later work intersects the behavior or evidence it established.

## Evidence rules

- Run checks from the correct repository/root/environment.
- Capture real command names and pass/fail status.
- If a command fails due to setup, fix safe local drift once before escalating.
- If a check is skipped, state why and what would be needed to run it.
- Do not claim success from stale output or the wrong branch.

## Proof states and provenance

For substantial work, label final claims instead of reporting one blended outcome. Separate:

- **Verified:** a current-run check directly proved it.
- **Inferred:** it follows from evidence but was not directly checked.
- **Not checked:** no evidence either way.
- **Blocked:** a check was attempted but access, permissions, or the environment prevented it.
- **Next proof needed:** the narrowest check that would settle an open claim.

When freshness matters, such as reruns, releases, generated artifacts, or anything previously verified, also label evidence provenance: fresh, reused, summary-derived, local-only, reviewer-backed, or user-accepted. An exit code, a local pass, or a reviewer's agreement is not delivery proof; name what proves the actual goal and what only proved an intermediate step.

## Docs-only work

Docs-only changes still need verification:

- file references exist
- links are plausible and current where checkable
- examples are syntactically coherent
- private data is absent
- root docs and supporting docs do not contradict each other

## Negative checks

For harnesses and regression tests, prove the check can fail when practical. A test that cannot fail is decoration.

## Adversarial completion pass

Before calling substantial work complete, ask what the current checks do not prove, what the change might accidentally permit, which old behavior could regress, and whether a narrower implementation would meet the same acceptance criteria. If this reveals implementation cleanup, return to the [implementation finish workflow](implementation-finish.md), make the change, and rerun every affected check before carrying proof forward.
