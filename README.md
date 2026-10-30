# AI Skill Library

An agent-agnostic, version-controlled library of independently usable AI skills.

## Principles
- One skill = one folder. Every skill has **SKILL.md** (procedure) and **HOW_TO_USE.md** (when to use, expected result, limitations).
- Canonical skills do not depend on Claude, Codex, a model provider, or a framework.
- Agent-specific install paths are adapters, not sources of truth.
- Inspect and test imported skills before executing any included scripts. GitHub visibility does not grant redistribution rights.
- Updating the library does **not** automatically update existing projects.

## Layout
```text
skills/
  visual-design/{SKILL.md,HOW_TO_USE.md}
  microinteractions/{SKILL.md,HOW_TO_USE.md}
  visual-qa/{SKILL.md,HOW_TO_USE.md}
community/            # reviewed, licensed third-party imports only
inbox/                # candidate references; never execute blindly
templates/skill/      # template for new independent skills
scripts/              # validation and opt-in installation
registry.json         # status and provenance metadata
```

## Quick use
Review a skill's `HOW_TO_USE.md`, then ask an AI coding agent to follow its `SKILL.md` against your project. Alternatively install skills locally:

```bash
python3 scripts/validate.py
python3 scripts/install.py --target /path/to/project --agent codex --dry-run
python3 scripts/install.py --target /path/to/project --agent codex
# Claude Code: --agent claude
```

The installer refuses to overwrite an existing skill unless `--overwrite` is explicitly provided. Keep project-specific decisions in the project rather than hardcoding them into shared skills.

## Adding skills
Copy `templates/skill/` into `skills/<unique-name>/`; fill out both files, add a registry entry, validate, review licensing/security and test on a disposable project. Use `community/` only for reviewed redistribution-compatible imports. Record the upstream URL and license for third-party material.

## Security
Treat third-party SKILL.md and any referenced scripts as untrusted instructions. Inspect commands, credential access, network calls and dependency installation before use; scope permissions to the task and avoid automatic execution.
