# How to use: Visual QA

## When to use
Use after UI changes, responsive redesigns, animation changes, or before shipping a visually complex feature.

## How to invoke
Ask your agent: "Read `skills/visual-qa/SKILL.md` and apply it to [specific view or flow]. Preserve existing functionality, use the current stack, and report changes and checks."

## Expected results
An inspectable QA report with tested viewports, screenshots or manual observations, failures, severity, and unresolved verification gaps.

## Where it does not do well
Without browser/screenshot access, cannot claim visual inspection. Screenshot comparison alone does not prove behavior, contrast compliance or accessibility.

## Prerequisites
Access to project files and clear target behavior; screenshots/browser tools are needed for visual verification claims.

## Acceptance check
Confirm the requested view or interaction works as before, improvements are inspectable, accessibility constraints are preserved, and all unverified checks are labeled.
