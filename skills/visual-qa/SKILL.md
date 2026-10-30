---
name: visual-qa
description: Check whether a UI change meets its visual requirements without breaking behavior or accessibility.
---

# Visual QA

## Objective
Check whether a UI change meets its visual requirements without breaking behavior or accessibility.

## Inputs
Project UI/requirements, existing design conventions, acceptance criteria, available test environment.

## Procedure
1. Identify target viewports, states and acceptance criteria.
2. Run available build/type/lint/test commands without altering configuration.
3. Inspect relevant screens across sizes and key states when tooling exists.
4. Verify focus, contrast, overflow, reduced motion and error states.
5. Report exact evidence, limitations and regressions; never mark untested checks as passed.

## Output contract
An inspectable QA report with tested viewports, screenshots or manual observations, failures, severity, and unresolved verification gaps.

## Guardrails
- Preserve application logic and established design constraints unless explicitly tasked otherwise.
- Do not add new dependencies without need and approval.
- Prefer measurable outcomes and observable evidence over aesthetic claims.
- Report missing tools and unverified checks clearly.

## Usage guide
See [HOW_TO_USE.md](HOW_TO_USE.md).
