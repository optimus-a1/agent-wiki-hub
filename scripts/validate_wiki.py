#!/usr/bin/env python3
"""Validate Agent Wiki Hub structure without external dependencies."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
REQUIRED_DIRS = ["concepts", "rules", "workflows", "cases", "tools", "prompts", "evals", "sources"]
REQUIRED_FILES = ["manifest.yaml", "README.md", "AGENTS.md", "update-log.md"]


def parse_eval_file(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    wiki = None
    updated = None
    has_tests = False
    tests = []
    current = None

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("wiki:"):
            wiki = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("updated:"):
            updated = stripped.split(":", 1)[1].strip()
        elif stripped == "tests:":
            has_tests = True
        elif re.match(r"^-\s+id:\s*", stripped):
            if current:
                tests.append(current)
            current = {"id": stripped.split(":", 1)[1].strip(), "question": False, "expected_behavior": False}
        elif current and stripped.startswith("question:"):
            current["question"] = True
        elif current and stripped.startswith("expected_behavior:"):
            current["expected_behavior"] = True

    if current:
        tests.append(current)
    return wiki, updated, has_tests, tests


def main() -> int:
    errors = []
    eval_count = 0
    seen_eval_ids = {}
    if not WIKIS.exists():
        errors.append("Missing wikis/ directory")
    else:
        wiki_dirs = sorted([p for p in WIKIS.iterdir() if p.is_dir()])
        if not wiki_dirs:
            errors.append("No wiki directories found under wikis/")
        for wiki in wiki_dirs:
            for name in REQUIRED_FILES:
                if not (wiki / name).exists():
                    errors.append(f"{wiki.relative_to(ROOT)} missing file {name}")
            for name in REQUIRED_DIRS:
                if not (wiki / name).is_dir():
                    errors.append(f"{wiki.relative_to(ROOT)} missing directory {name}/")
            # Require at least one knowledge file per main directory.
            for name in REQUIRED_DIRS:
                d = wiki / name
                if d.is_dir() and not any(x.suffix.lower() in {'.md', '.yaml', '.yml', '.json'} for x in d.rglob('*') if x.is_file()):
                    errors.append(f"{wiki.relative_to(ROOT)}/{name}/ has no knowledge files")
            eval_dir = wiki / "evals"
            if eval_dir.is_dir():
                for path in sorted(eval_dir.glob("*.y*ml")):
                    rel = path.relative_to(ROOT).as_posix()
                    eval_wiki, updated, has_tests, tests = parse_eval_file(path)
                    if eval_wiki != wiki.name:
                        errors.append(f"{rel}: wiki field must be {wiki.name!r}, got {eval_wiki!r}")
                    if not updated:
                        errors.append(f"{rel}: missing updated field")
                    if not has_tests:
                        errors.append(f"{rel}: missing tests section")
                    if not tests:
                        errors.append(f"{rel}: no test ids found")
                    for test in tests:
                        test_id = test["id"].strip('"').strip("'")
                        if not test_id:
                            errors.append(f"{rel}: empty test id")
                            continue
                        key = (wiki.name, test_id)
                        if key in seen_eval_ids:
                            errors.append(f"{rel}: duplicate test id {test_id!r}; first seen in {seen_eval_ids[key]}")
                        else:
                            seen_eval_ids[key] = rel
                            eval_count += 1
                        if not test["question"]:
                            errors.append(f"{rel}: test {test_id!r} missing question")
                        if not test["expected_behavior"]:
                            errors.append(f"{rel}: test {test_id!r} missing expected_behavior")
    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"VALIDATION PASSED ({eval_count} eval tests)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
