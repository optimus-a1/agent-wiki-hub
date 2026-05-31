#!/usr/bin/env python3
"""Audit local Markdown links and internal path references."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS_OUT = ROOT / "docs" / "LINK_AUDIT.md"
JSON_OUT = ROOT / "registry" / "link-audit.json"

SCAN_ROOTS = ["AGENTS.md", "README.md", "CODEX_BUILD_PROMPT.md", "docs", "wikis", "codex-skills"]
KNOWN_ROOTS = (".github", "wikis", "scripts", "docs", "registry", "codex-skills", "index", "packs")
WIKI_LOCAL_ROOTS = ("concepts", "rules", "workflows", "cases", "tools", "prompts", "evals", "sources")
ROOT_FILES = {"AGENTS.md", "README.md", "CODEX_BUILD_PROMPT.md"}
LOCAL_FILES = {"manifest.yaml", "README.md", "AGENTS.md", "update-log.md", "source-notes.md"}
TEXT_SUFFIXES = {".md"}

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
ROOT_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_~./-])(?:\.github|wikis|scripts|docs|registry|codex-skills|index|packs)/[A-Za-z0-9_./<>{}*~\"'-]+/?"
)
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
CODE_TOKEN_RE = re.compile(
    r"(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.<>{}*~\"'-]+/?|(?:AGENTS|README|CODEX_BUILD_PROMPT)\.md|manifest\.yaml|update-log\.md|source-notes\.md"
)
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "app://", "file://", "data:")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for item in SCAN_ROOTS:
        path = ROOT / item
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES))
    return sorted(p for p in set(files) if p.resolve() != DOCS_OUT.resolve())


def wiki_root_for(path: Path) -> Path | None:
    try:
        parts = path.relative_to(ROOT).parts
    except ValueError:
        return None
    if len(parts) >= 2 and parts[0] == "wikis":
        return ROOT / parts[0] / parts[1]
    return None


def line_number(text: str, start: int) -> int:
    return text.count("\n", 0, start) + 1


def strip_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target and not target.startswith("#"):
        # Markdown link titles are not paths.
        target = target.split()[0]
    target = target.strip().strip("\"'")
    target = target.split("#", 1)[0].split("?", 1)[0]
    target = target.replace("\\", "/")
    while target and target[-1] in ".,;:)]}":
        target = target[:-1]
    return target


def should_skip(target: str) -> bool:
    if not target or target.startswith("#"):
        return True
    lowered = target.casefold()
    if lowered.startswith(EXTERNAL_SCHEMES):
        return True
    if any(ch in target for ch in "<>{}*"):
        return True
    if "~" in target or "$" in target:
        return True
    return False


def resolve_target(target: str, source: Path) -> Path | None:
    if should_skip(target):
        return None
    target_path = Path(target)
    first = target.split("/", 1)[0]

    if target.startswith("./") or target.startswith("../"):
        return (source.parent / target_path).resolve()
    if first in KNOWN_ROOTS:
        return (ROOT / target_path).resolve()

    wiki_root = wiki_root_for(source)
    if wiki_root and (first in WIKI_LOCAL_ROOTS or target in LOCAL_FILES):
        return (wiki_root / target_path).resolve()
    if target in ROOT_FILES:
        if wiki_root and (wiki_root / target).exists():
            return (wiki_root / target).resolve()
        return (ROOT / target).resolve()
    return None


def path_kind(target: str, resolved: Path | None) -> str:
    if target.endswith("/"):
        return "directory"
    if resolved and resolved.exists() and resolved.is_dir():
        return "directory"
    return "file"


def check_reference(source: Path, source_text: str, start: int, raw_target: str, ref_type: str) -> dict | None:
    target = strip_target(raw_target)
    resolved = resolve_target(target, source)
    if resolved is None:
        return None
    kind = path_kind(target, resolved)
    passed = resolved.is_dir() if kind == "directory" else resolved.exists()
    rel_source = source.relative_to(ROOT).as_posix()
    try:
        rel_resolved = resolved.relative_to(ROOT).as_posix()
    except ValueError:
        rel_resolved = str(resolved)
    return {
        "source": rel_source,
        "line": line_number(source_text, start),
        "type": ref_type,
        "target": target,
        "resolved": rel_resolved,
        "kind": kind,
        "passed": passed,
    }


def references_in_file(path: Path) -> list[dict]:
    text = read_text(path)
    records: list[dict] = []
    seen: set[tuple[str, int, str, str]] = set()

    for match in MARKDOWN_LINK_RE.finditer(text):
        record = check_reference(path, text, match.start(1), match.group(1), "markdown_link")
        if record:
            key = (record["source"], record["line"], record["type"], record["target"])
            if key not in seen:
                records.append(record)
                seen.add(key)

    for match in ROOT_PATH_RE.finditer(text):
        record = check_reference(path, text, match.start(0), match.group(0), "path_reference")
        if record:
            key = (record["source"], record["line"], record["type"], record["target"])
            if key not in seen:
                records.append(record)
                seen.add(key)

    for code_match in CODE_SPAN_RE.finditer(text):
        code = code_match.group(1)
        for token_match in CODE_TOKEN_RE.finditer(code):
            raw = token_match.group(0)
            record = check_reference(path, text, code_match.start(1) + token_match.start(0), raw, "code_reference")
            if record:
                key = (record["source"], record["line"], record["type"], record["target"])
                if key not in seen:
                    records.append(record)
                    seen.add(key)
    return records


def audit() -> list[dict]:
    records: list[dict] = []
    for path in markdown_files():
        records.extend(references_in_file(path))
    # Deduplicate references repeated in generated command output on the same line.
    unique: dict[tuple[str, int, str, str], dict] = {}
    for record in records:
        unique[(record["source"], record["line"], record["type"], record["target"])] = record
    return sorted(unique.values(), key=lambda r: (r["source"], r["line"], r["type"], r["target"]))


def markdown_report(records: list[dict]) -> str:
    failed = [record for record in records if not record["passed"]]
    by_type = Counter(record["type"] for record in records)
    by_kind = Counter(record["kind"] for record in records)
    lines = [
        "# Link Audit",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Internal references checked: {len(records)}",
        f"- Passed: {len(records) - len(failed)}",
        f"- Failed: {len(failed)}",
        "",
        "## Counts By Type",
        "",
        "| Type | References |",
        "| --- | ---: |",
    ]
    for ref_type, count in sorted(by_type.items()):
        lines.append(f"| {ref_type} | {count} |")

    lines.extend(["", "## Counts By Target Kind", "", "| Kind | References |", "| --- | ---: |"])
    for kind, count in sorted(by_kind.items()):
        lines.append(f"| {kind} | {count} |")

    lines.extend(["", "## Failed References", ""])
    if failed:
        lines.extend(["| Source | Line | Type | Target | Resolved |", "| --- | ---: | --- | --- | --- |"])
        for record in failed:
            lines.append(
                f"| {record['source']} | {record['line']} | {record['type']} | "
                f"{record['target']} | {record['resolved']} |"
            )
    else:
        lines.append("No broken internal references found.")

    lines.extend(
        [
            "",
            "## Usage Notes",
            "",
            "- This audit checks local Markdown links, root-relative repository paths, and common code-spanned path references.",
            "- External URLs, anchors, placeholders such as `wikis/<domain>-agent-wiki/`, globs, and home-directory examples are intentionally skipped.",
            "- Run this after renaming files, moving wiki pages, or changing generated report locations.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    records = audit()
    failed = [record for record in records if not record["passed"]]
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(records), encoding="utf-8")
    JSON_OUT.write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": not failed, "references": records}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if failed:
        print("LINK AUDIT FAILED")
        for record in failed:
            print(f"- {record['source']}:{record['line']} {record['target']} -> {record['resolved']}")
        return 1
    print(f"LINK AUDIT PASSED ({len(records)} references)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
