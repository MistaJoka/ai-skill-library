# Utility belt: skill selection and curation

## Mission
Keep the best *tested* skill for each distinct capability, not the most skills. Three targets: **prompt** (improve instructions/outputs), **project** (plan/build/review), **repository** (inspect/modify/verify code). A skill may support only a subset.

## Intake and quality gate
1. Record upstream URL, author, revision, license and permissions. Treat imports as untrusted.
2. Compare candidate inputs, outputs, procedure, scope and failure cases with incumbents.
3. Reject unsafe instructions, exfiltration, unknown redistribution rights and unnecessary privileges before scoring.
4. Test candidate and incumbent against the same representative tasks, environment and acceptance criteria. Save evidence.
5. Decide: **adopt**, **replace**, **merge**, **specialize**, or **reject**. Document reasons and rollback.
6. Document limitations in the skill's own HOW_TO_USE.md and register the capability.

## Deduplication
Exactly one primary owner per capability identifier. Two skills can coexist only with a documented, materially distinct specialization boundary. Similar titles are a review signal, not proof of equivalence. The validator detects declared duplicate capability owners, but semantic duplication still needs review.

## Comparative score (only after hard gates pass)
- Task effectiveness: 30%
- Reliability and verification: 25%
- Security/minimal permissions: 20%
- Portability: 15%
- Maintainability: 10%

No numeric score without test evidence. GitHub stars are not a quality metric.

## Invocation
Classify target **prompt**, **project**, or **repository**; choose mode **advisory**, **execution**, or **verification**. Identify task, constraints, tools and permissions. Find the smallest relevant set of registered skills, read HOW_TO_USE.md, then follow SKILL.md only within authorization. Verify and report gaps. Never silently edit a repo during an advisory request.

## Not yet implemented
Automatic semantic routing, a benchmark harness, and skill performance data. Current registry is metadata, not an intelligent selector.
