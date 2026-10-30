---
name: visual-design
description: Improve visual hierarchy, spacing, typography, layout and accessible appearance without changing application semantics.
---

# Visual Design

## Objective
Improve visual hierarchy, spacing, typography, layout and accessible appearance without changing application semantics.

## Inputs
Project UI/requirements, existing design conventions, acceptance criteria, available test environment.

## Procedure
1. Inspect the existing UI, tokens, and product constraints.
2. Identify the highest-impact hierarchy or consistency problem.
3. Propose a small set of explicit changes preserving functional behavior.
4. Implement the changes using existing framework conventions.
5. Check small screens, keyboard use, contrast, and regression risk.

## Output contract
A documented design rationale and focused UI changes with consistent tokens, responsive layouts, clear hierarchy, and before/after evidence.

## Guardrails
- Preserve application logic and established design constraints unless explicitly tasked otherwise.
- Do not add new dependencies without need and approval.
- Prefer measurable outcomes and observable evidence over aesthetic claims.
- Report missing tools and unverified checks clearly.

## Usage guide
See [HOW_TO_USE.md](HOW_TO_USE.md).
