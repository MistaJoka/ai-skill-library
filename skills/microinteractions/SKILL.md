---
name: microinteractions
description: Add meaningful, responsive feedback to user actions, state changes and errors.
---

# Microinteractions

## Objective
Add meaningful, responsive feedback to user actions, state changes and errors.

## Inputs
Project UI/requirements, existing design conventions, acceptance criteria, available test environment.

## Procedure
1. Map the user action and real underlying state transition.
2. Define feedback for pending, success and failure.
3. Use minimal animation duration and native interaction semantics.
4. Respect prefers-reduced-motion and cancellation.
5. Test keyboard, touch, asynchronous failure and duplicate actions.

## Output contract
Feedback linked to real state transitions; loading, success and failure states distinguishable; reduced-motion preference honored.

## Guardrails
- Preserve application logic and established design constraints unless explicitly tasked otherwise.
- Do not add new dependencies without need and approval.
- Prefer measurable outcomes and observable evidence over aesthetic claims.
- Report missing tools and unverified checks clearly.

## Usage guide
See [HOW_TO_USE.md](HOW_TO_USE.md).
