#!/usr/bin/env python3
"""Check Agent Wiki eval YAML files with no third-party dependencies."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"


def parse_eval_file(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    wiki = None
    updated = None
    has_tests = False
    tests = []
    current = None

    for line in lines:
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
    seen_ids = {}

    for wiki_dir in sorted(p for p in WIKIS.iterdir() if p.is_dir()):
        eval_dir = wiki_dir / "evals"
        for path in sorted(eval_dir.glob("*.y*ml")):
            wiki, updated, has_tests, tests = parse_eval_file(path)
            rel = path.relative_to(ROOT).as_posix()
            if wiki != wiki_dir.name:
                errors.append(f"{rel}: wiki field must be {wiki_dir.name!r}, got {wiki!r}")
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
                key = (wiki_dir.name, test_id)
                if key in seen_ids:
                    errors.append(f"{rel}: duplicate test id {test_id!r}; first seen in {seen_ids[key]}")
                else:
                    seen_ids[key] = rel
                if not test["question"]:
                    errors.append(f"{rel}: test {test_id!r} missing question")
                if not test["expected_behavior"]:
                    errors.append(f"{rel}: test {test_id!r} missing expected_behavior")

    if errors:
        print("EVAL CHECK FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"EVAL CHECK PASSED ({len(seen_ids)} tests)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
