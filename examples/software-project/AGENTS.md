# Repository Instructions

Read `CONTEXT.md` for architecture and `STYLE.md` for conventions before non-trivial changes.

## Commands

- Install: `pnpm install`
- Test focused package: `pnpm test --filter <package>`
- Lint: `pnpm lint`

## Workflow

Use a generate/evaluate/repair loop for feature and bug work. Add or update tests for behavior changes. Keep public APIs stable unless the issue requests a breaking change.
