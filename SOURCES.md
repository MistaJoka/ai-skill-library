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
