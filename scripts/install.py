#!/usr/bin/env python3
"""Copy canonical skills into a project; refuses overwrites by default."""
from pathlib import Path
import argparse
import shutil
import sys

root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument("--target", required=True, type=Path)
p.add_argument("--agent", choices=("codex", "claude"), required=True)
p.add_argument("--skill", action="append", help="Install only selected skill ID(s)")
p.add_argument("--dry-run", action="store_true")
p.add_argument("--overwrite", action="store_true")
args = p.parse_args()
target = args.target.expanduser().resolve()
if not target.is_dir():
    sys.exit(f"Target directory does not exist: {target}")
destination = target / (".agents/skills" if args.agent == "codex" else ".claude/skills")
available = {d.name: d for d in (root / "skills").iterdir() if d.is_dir()}
selected = args.skill or sorted(available)
unknown = set(selected) - set(available)
if unknown:
    sys.exit(f"Unknown skills: {', '.join(sorted(unknown))}")
if any((destination / name).exists() for name in selected) and not args.overwrite:
    sys.exit("Refusing to overwrite existing skill directory; use --overwrite after review.")
for name in selected:
    output = destination / name
    print(f"{'WOULD INSTALL' if args.dry_run else 'INSTALL'} {name} -> {output}")
    if not args.dry_run:
        if output.exists():
            shutil.rmtree(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(available[name], output)
