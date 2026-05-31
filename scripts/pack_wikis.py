#!/usr/bin/env python3
"""Create one zip package per wiki and one all-in-one package."""
from pathlib import Path
import zipfile, shutil

ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "packs"
WIKIS = ROOT / "wikis"
SKIP_DIRS = {"__pycache__", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
SKIP_SUFFIXES = {".pyc", ".pyo"}
SKIP_FILES = {".DS_Store", "Thumbs.db"}


def should_package(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if path.suffix in SKIP_SUFFIXES:
        return False
    if path.name in SKIP_FILES:
        return False
    return True


def zip_dir(src: Path, out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(src.rglob('*')):
            if p.is_file() and should_package(p):
                zf.write(p, p.relative_to(src.parent))


def main():
    PACKS.mkdir(exist_ok=True)
    for wiki in sorted(WIKIS.iterdir()):
        if wiki.is_dir():
            out = PACKS / f"{wiki.name}.zip"
            zip_dir(wiki, out)
            print(f"packed {out.relative_to(ROOT)}")
    out = PACKS / "agent-wiki-hub-all.zip"
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zf:
        for folder in ['wikis', 'registry', 'scripts', 'codex-skills', 'docs', '.github']:
            src = ROOT / folder
            if src.exists():
                for p in sorted(src.rglob('*')):
                    if p.is_file() and should_package(p):
                        zf.write(p, p.relative_to(ROOT))
        for name in ['README.md', 'AGENTS.md', 'CODEX_BUILD_PROMPT.md']:
            p = ROOT / name
            if p.exists():
                zf.write(p, p.relative_to(ROOT))
    print(f"packed {out.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
