# Skill discovery sources (candidate fishing grounds)

Discovery is **not endorsement**. Evaluate individual skill licensing, security, capabilities and performance before importing. Source popularity is not a benchmark.

| Source | Purpose | URL |
|---|---|---|
| Anthropic skills | Official examples | https://github.com/anthropics/skills |
| OpenAI skills | Codex skills examples | https://github.com/openai/skills |
| skills.sh | Skill discovery and rankings | https://skills.sh |
| Vercel agent skills | Web/frontend specializations | https://github.com/vercel-labs/agent-skills |
| VoltAgent awesome-agent-skills | Broad curated links | https://github.com/VoltAgent/awesome-agent-skills |
| GitHub awesome-copilot | Development instructions and workflows | https://github.com/github/awesome-copilot |
| Agent Skills specification | Portable authoring standard, not a skills collection | https://agentskills.io/specification |

## Intake procedure
1. Save candidate repo URL, path and commit SHA in `inbox/`; record author and per-skill license.
2. Inspect all instructions, referenced scripts and dependencies without running them.
3. Map task inputs/outputs to a capability identifier; check incumbent and near-duplicate skills.
4. Benchmark candidate against incumbent on matched tasks. Log evidence and tools used.
5. Adopt, replace, merge, specialize or reject per [CURATION.md](CURATION.md).
6. For approved skills, require separate `SKILL.md` and `HOW_TO_USE.md`, update registry and run structural validation.

Do not bulk-download and execute marketplace skills.

## Upstream-first inventory policy
- Do not import wholesale from Anthropic or OpenAI official skill collections.
- Check the actual installed skills and built-in capabilities of Claude Code/Codex before claiming overlap.
- Prefer links or upstream installation for unchanged skills; fork separately when maintaining meaningful modifications.
- Add a skill to this repository only when it fills a documented gap, supplies a proven improvement, or provides a distinct portable specialization.
- For local models, audit tool-use, context-length, file access, and instruction-following compatibility instead of assuming a skill written for a hosted coding agent will work.

## Independent specialized candidates (2026-10-29)
These are **leads for review**, not approved imports. Official Anthropic/OpenAI repos remain upstream references, not collection targets.

| Source | Distinct capability to investigate | First comparison / concern |
|---|---|---|
| https://github.com/pbakaus/impeccable | Art direction and UI critique | Compare with visual-design incumbent; license and test pending |
| https://github.com/coreyhaines31/marketingskills | SEO, CRO, analytics and marketing workflows | Distinct business utility; validate claims and license |
| https://github.com/trailofbits/skills | Defensive security research/audits | Review commands and security boundaries individually |
| https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering | Context engineering for local/multi-agent systems | Benchmark against native agent functionality |
| https://github.com/kepano/obsidian-skills | Obsidian vault, Canvas and structured notes | App-specific, optional dependency |
| https://github.com/obra/superpowers | Structured engineering workflows | Likely native-agent overlap; low import priority |

**Policy:** Prefer independent niche skills and demonstrable new capabilities. Upstream links/forks stay outside the canonical library unless a selected, licensed and tested capability earns inclusion. No candidate here has been fully audited or imported.
