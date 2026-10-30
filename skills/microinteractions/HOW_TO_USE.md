# How to use: Microinteractions

## When to use
Use when clicks, saves, drag/drop, loading or failures lack clear feedback, or interactions feel abrupt.

## How to invoke
Ask your agent: "Read `skills/microinteractions/SKILL.md` and apply it to [specific view or flow]. Preserve existing functionality, use the current stack, and report changes and checks."

## Expected results
Feedback linked to real state transitions; loading, success and failure states distinguishable; reduced-motion preference honored.

## Where it does not do well
Avoid animation for its own sake, fake completion signals, blocking animations, or changes that impair keyboard or touch operation. Requires actual state signals from the application.

## Prerequisites
Access to project files and clear target behavior; screenshots/browser tools are needed for visual verification claims.

## Acceptance check
Confirm the requested view or interaction works as before, improvements are inspectable, accessibility constraints are preserved, and all unverified checks are labeled.
