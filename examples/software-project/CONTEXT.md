# Project Context

This example is a web app with a small API and frontend.

- `apps/web` owns routes and UI.
- `packages/api-client` owns API calls.
- `packages/domain` owns shared domain types.

Preserve the boundary: UI code should not duplicate domain validation.
