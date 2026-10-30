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

## Cross-vertical discovery map — 2026-10-30

Status: **discovered, not audited or approved**. These sources are candidate repositories, directories, and upstream references; no imported skills. Review individual file-level licenses, scripts, tool dependencies, benchmark results, and overlap before promotion.

### Creative production
| Focus | Candidate URL | Discovery rationale |
|---|---|---|
| Motion and code-driven animation | https://github.com/VisualxIntelligence/motion-tools-and-skills | Three.js, GSAP, Blender, compositing |
| Game development | https://github.com/minhhoit/gamedev-agent-skills | Godot, Phaser, Bevy, Unreal, Unity workflows |
| Pixel art | https://github.com/with-pebbly/aseprite-ai-artist | Agent-controlled sprites and frame animation; external editor dependency |
| Blender 3D | https://github.com/EL4CTEO/blender-skills | Modeling, materials, rigs and exports; Blender version-sensitive |
| Creative media | https://github.com/calesthio/generative-media-skills | Image/video/audio/voice production; check API costs |
| Motion directories | https://github.com/iart-ai/awesome-motion-skills | Specialized links, not automatically installable collection |
| Manim animation | https://github.com/marcelo-earth/manim-awesome-skills | Math animation discovery; curated links |
| Music production | https://github.com/sb-dev/music-production-skills | Composition through mastering |
| Narrative production | https://github.com/sb-dev/narrative-production-skills | Character/world/continuity workflows |
| Creative writing | https://github.com/jwynia/agent-skills | Interactive fiction and game narrative |
| Manim renderer workflow | https://github.com/awesome-skills/manim-skill | Programmatic explanatory animation |

### Other verticals
| Focus | Candidate URL | Discovery rationale |
|---|---|---|
| Business marketing | https://github.com/coreyhaines31/marketingskills | Specialized SEO and conversion workflows |
| Security | https://github.com/trailofbits/skills | Domain-specific defensive auditing; high scrutiny |
| Context engineering | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering | Local agent memory/context design |
| Cross-vertical collection | https://github.com/seb1n/awesome-ai-agent-skills | Engineering, research, documents, data and operations |
| Legal/compliance discovery | https://github.com/lawve-ai/awesome-legal-skills | Reference directory only; jurisdiction and accuracy constraints |

### Search indexes (discover, never bulk-import)
- https://skills.sh
- https://hotskills.dev
- https://stackscape.org/en/skills/
- https://www.theskillmd.com/

### Capability discovery taxonomy
visual-design; motion-animation; pixel-art; 3d-production; game-development; audio-music; video-production; creative-writing; software-engineering; ai-engineering; data-science; security; automation; research; marketing-sales; finance-risk; education; productivity.

### Review priorities
1. Pixel-art pipelines with real rendered assets and editable sources.
2. Motion design with rendered outputs and repeatable CLI verification.
3. Game-development skills compatible with Godot and portable patterns.
4. Business SEO/analytics skills that add non-native functionality.
5. Context engineering, security and remaining verticals.

**Promotion standard:** do not conflate a GitHub repository with a single skill. Evaluate the exact skill path and upstream revision. Prefer tested quality over popularity, free/local execution where practicable, and one primary capability owner. Preserve alternatives as links, not duplicate files.
