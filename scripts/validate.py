#!/usr/bin/env python3
"""Validate self-contained skill folders and the library registry (standard library only)."""
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
errors = []
try:
    registry = json.loads((root / "registry.json").read_text())
except (OSError, ValueError) as exc:
    print(f"FAIL: registry.json: {exc}", file=sys.stderr)
    sys.exit(1)
ids = set()
for entry in registry.get("skills", []):
    skill_id = entry.get("id")
    folder = root / entry.get("path", "")
    if not skill_id or skill_id in ids:
        errors.append(f"missing/duplicate skill id: {skill_id}")
    ids.add(skill_id)
    if not folder.is_dir() or folder.parent != root / "skills" or folder.name != skill_id:
        errors.append(f"invalid canonical skill path: {folder}")
        continue
    for filename in ("SKILL.md", "HOW_TO_USE.md"):
        p = folder / filename
        if not p.is_file() or not p.read_text().strip():
            errors.append(f"missing or empty: {p.relative_to(root)}")
    usage = (folder / "HOW_TO_USE.md")
    if usage.is_file():
        text = usage.read_text().lower()
        for section in ("when to use", "expected results", "where it does not do well"):
            if f"## {section}" not in text:
                errors.append(f"{skill_id}: missing section {section}")
for folder in (root / "skills").iterdir():
    if folder.is_dir() and folder.name not in ids:
        errors.append(f"unregistered skill: {folder.name}")
if errors:
    for error in errors: print("FAIL:", error, file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(ids)} registered skills, usage guides and registry structure")
