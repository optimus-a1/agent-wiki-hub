#!/usr/bin/env python3
"""Audit generated wiki zip packages for required contents."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
PACKS = ROOT / "packs"
DOCS_OUT = ROOT / "docs" / "PACK_AUDIT.md"
JSON_OUT = ROOT / "registry" / "pack-audit.json"

REQUIRED_WIKI_FILES = ["manifest.yaml", "README.md", "AGENTS.md", "update-log.md"]
REQUIRED_WIKI_DIRS = ["concepts", "rules", "workflows", "cases", "tools", "prompts", "evals", "sources"]
ROOT_REQUIRED_FILES = ["AGENTS.md", "README.md", "CODEX_BUILD_PROMPT.md"]
RISKY_ARCHIVE_NAMES = {
    ".env",
    ".env.local",
    ".npmrc",
    "id_rsa",
    "id_dsa",
    "id_ed25519",
    "credentials",
    "credentials.json",
    "cookie",
    "cookies.txt",
}
SKIP_EXPECTED_DIRS = {"__pycache__", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
SKIP_EXPECTED_SUFFIXES = {".pyc", ".pyo"}
SKIP_EXPECTED_FILES = {".DS_Store", "Thumbs.db"}


def posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def archive_names(path: Path) -> set[str]:
    if not path.exists():
        return set()
    try:
        with zipfile.ZipFile(path) as zf:
            return set(zf.namelist())
    except zipfile.BadZipFile:
        return set()


def archive_valid(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        with zipfile.ZipFile(path) as zf:
            return zf.testzip() is None
    except zipfile.BadZipFile:
        return False


def has_prefix(names: set[str], prefix: str) -> bool:
    return any(name.startswith(prefix) for name in names)


def unsafe_members(names: set[str]) -> list[str]:
    unsafe: list[str] = []
    for name in sorted(names):
        normalized = name.replace("\\", "/")
        parts = [part for part in normalized.split("/") if part]
        basename = parts[-1].casefold() if parts else ""
        if normalized.startswith("/") or ".." in parts or basename in RISKY_ARCHIVE_NAMES:
            unsafe.append(name)
    return unsafe


def should_expect_packaged(path: Path) -> bool:
    if any(part in SKIP_EXPECTED_DIRS for part in path.parts):
        return False
    if path.suffix in SKIP_EXPECTED_SUFFIXES:
        return False
    if path.name in SKIP_EXPECTED_FILES:
        return False
    return True


def add_check(checks: list[dict], check_id: str, passed: bool, evidence: str) -> None:
    checks.append({"check_id": check_id, "passed": passed, "evidence": evidence})


def wiki_ids() -> list[str]:
    if not WIKIS.exists():
        return []
    return sorted(path.name for path in WIKIS.iterdir() if path.is_dir())


def individual_pack_checks(wiki_id: str) -> list[dict]:
    checks: list[dict] = []
    pack = PACKS / f"{wiki_id}.zip"
    names = archive_names(pack)
    add_check(checks, f"{wiki_id}:zip_exists", pack.exists(), posix(pack))
    add_check(checks, f"{wiki_id}:zip_valid", archive_valid(pack), posix(pack))
    add_check(checks, f"{wiki_id}:zip_not_empty", bool(names), f"{len(names)} entries")
    bad_members = unsafe_members(names)
    add_check(checks, f"{wiki_id}:safe_member_names", not bad_members, ", ".join(bad_members[:5]) or "safe")

    for filename in REQUIRED_WIKI_FILES:
        target = f"{wiki_id}/{filename}"
        add_check(checks, f"{wiki_id}:file:{filename}", target in names, target)
    for dirname in REQUIRED_WIKI_DIRS:
        target = f"{wiki_id}/{dirname}/"
        add_check(checks, f"{wiki_id}:directory:{dirname}", has_prefix(names, target), target)
    return checks


def expected_all_in_one_files() -> list[str]:
    expected: list[str] = []
    for filename in ROOT_REQUIRED_FILES:
        if (ROOT / filename).exists():
            expected.append(filename)
    for folder_name in ["registry", "scripts", "docs", "codex-skills", ".github"]:
        folder = ROOT / folder_name
        if not folder.exists():
            continue
        for path in sorted(p for p in folder.rglob("*") if p.is_file()):
            if not should_expect_packaged(path):
                continue
            if path.resolve() in {DOCS_OUT.resolve(), JSON_OUT.resolve()}:
                continue
            expected.append(path.relative_to(ROOT).as_posix())
    return expected


def all_in_one_checks() -> list[dict]:
    checks: list[dict] = []
    pack = PACKS / "agent-wiki-hub-all.zip"
    names = archive_names(pack)
    add_check(checks, "all:zip_exists", pack.exists(), posix(pack))
    add_check(checks, "all:zip_valid", archive_valid(pack), posix(pack))
    add_check(checks, "all:zip_not_empty", bool(names), f"{len(names)} entries")
    bad_members = unsafe_members(names)
    add_check(checks, "all:safe_member_names", not bad_members, ", ".join(bad_members[:5]) or "safe")

    for wiki_id in wiki_ids():
        for filename in REQUIRED_WIKI_FILES:
            target = f"wikis/{wiki_id}/{filename}"
            add_check(checks, f"all:{wiki_id}:file:{filename}", target in names, target)
        for dirname in REQUIRED_WIKI_DIRS:
            target = f"wikis/{wiki_id}/{dirname}/"
            add_check(checks, f"all:{wiki_id}:directory:{dirname}", has_prefix(names, target), target)

    for target in expected_all_in_one_files():
        add_check(checks, f"all:includes:{target}", target in names, target)
    return checks


def audit() -> list[dict]:
    checks: list[dict] = []
    add_check(checks, "packs:directory_exists", PACKS.is_dir(), posix(PACKS))
    for wiki_id in wiki_ids():
        checks.extend(individual_pack_checks(wiki_id))
    checks.extend(all_in_one_checks())
    return checks


def markdown_report(checks: list[dict]) -> str:
    failed = [item for item in checks if not item["passed"]]
    lines = [
        "# Pack Integrity Audit",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Checks: {len(checks)}",
        f"- Passed: {len(checks) - len(failed)}",
        f"- Failed: {len(failed)}",
        "",
        "## Failed Checks",
        "",
    ]
    if failed:
        lines.extend(["| Check | Evidence |", "| --- | --- |"])
        for item in failed:
            lines.append(f"| {item['check_id']} | {item['evidence']} |")
    else:
        lines.append("No package integrity issues found.")

    lines.extend(
        [
            "",
            "## Usage Notes",
            "",
            "- Run `python3 scripts/pack_wikis.py` before this audit so zip files are current.",
            "- Individual wiki packages must contain the standard wiki files and directories.",
            "- The all-in-one package must contain wikis, registry files, scripts, docs, Codex skill files, CI workflow files, and root instructions.",
            "- This audit also checks archive path safety and common secret-like filenames.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    checks = audit()
    failed = [item for item in checks if not item["passed"]]
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(checks), encoding="utf-8")
    JSON_OUT.write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": not failed, "checks": checks}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if failed:
        print("PACK INTEGRITY FAILED")
        for item in failed:
            print(f"- {item['check_id']}: {item['evidence']}")
        return 1
    print(f"PACK INTEGRITY PASSED ({len(checks)} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
