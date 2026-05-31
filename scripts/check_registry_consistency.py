#!/usr/bin/env python3
"""Check consistency between the wiki registry, manifests, and directories."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
REGISTRY = ROOT / "registry" / "wiki-registry.yaml"
DOCS_OUT = ROOT / "docs" / "REGISTRY_CONSISTENCY.md"
JSON_OUT = ROOT / "registry" / "registry-consistency.json"

REQUIRED_ENTRYPOINTS = ["README.md", "AGENTS.md", "rules/core-rules.md"]
REQUIRED_DIRECTORIES = ["concepts", "rules", "workflows", "cases", "tools", "prompts", "evals", "sources"]
REQUIRED_SAFETY_FLAGS = [
    "require_human_confirmation_for_high_risk: true",
    "no_secret_storage: true",
    "no_autonomous_high_risk_execution: true",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def parse_manifest(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for raw in read_text(path).splitlines():
        if ":" not in raw or raw.startswith(" ") or raw.lstrip().startswith("-"):
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def parse_registry(path: Path) -> tuple[dict[str, str], list[dict[str, str]]]:
    meta: dict[str, str] = {}
    records: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    if not path.exists():
        return meta, records

    for raw in read_text(path).splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if raw.startswith("  - id:"):
            if current:
                records.append(current)
            current = {"id": stripped.split(":", 1)[1].strip().strip('"')}
        elif current is not None and raw.startswith("    ") and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip().strip('"')
        elif current is None and ":" in stripped:
            key, value = stripped.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    if current:
        records.append(current)
    return meta, records


def check(condition: bool, check_id: str, description: str, evidence: str) -> dict:
    return {
        "check_id": check_id,
        "description": description,
        "passed": condition,
        "evidence": evidence,
    }


def registry_checks() -> list[dict]:
    checks: list[dict] = []
    meta, records = parse_registry(REGISTRY)
    record_by_id = {record.get("id", ""): record for record in records}
    wiki_dirs = sorted(path.name for path in WIKIS.iterdir() if path.is_dir()) if WIKIS.exists() else []

    checks.append(check(REGISTRY.exists(), "registry_exists", "Registry file exists.", str(REGISTRY.relative_to(ROOT))))
    checks.append(check(bool(meta.get("version")), "registry_version", "Registry has a version.", meta.get("version", "")))
    checks.append(check(bool(meta.get("updated")), "registry_updated", "Registry has an updated date.", meta.get("updated", "")))
    checks.append(check(bool(records), "registry_records", "Registry contains wiki records.", f"{len(records)} records"))
    checks.append(
        check(
            len(record_by_id) == len(records),
            "registry_unique_ids",
            "Registry wiki ids are unique.",
            f"{len(record_by_id)} unique ids / {len(records)} records",
        )
    )
    checks.append(
        check(
            set(record_by_id) == set(wiki_dirs),
            "registry_matches_wiki_dirs",
            "Registry ids match directories under wikis/.",
            f"registry={len(record_by_id)}, directories={len(wiki_dirs)}",
        )
    )

    for record in records:
        wiki_id = record.get("id", "")
        rel_path = record.get("path", "")
        wiki_path = ROOT / rel_path
        manifest_path = wiki_path / "manifest.yaml"
        manifest = parse_manifest(manifest_path)
        manifest_text = read_text(manifest_path).casefold() if manifest_path.exists() else ""

        checks.append(
            check(
                wiki_path.is_dir(),
                f"{wiki_id}:path_exists",
                "Registry path points to a wiki directory.",
                rel_path,
            )
        )
        checks.append(
            check(
                wiki_path.name == wiki_id,
                f"{wiki_id}:path_basename_matches_id",
                "Registry path basename matches wiki id.",
                f"{wiki_path.name} vs {wiki_id}",
            )
        )
        checks.append(
            check(
                manifest.get("id") == wiki_id,
                f"{wiki_id}:manifest_id",
                "Manifest id matches registry id.",
                f"{manifest.get('id')} vs {wiki_id}",
            )
        )
        checks.append(
            check(
                manifest.get("domain") == record.get("domain"),
                f"{wiki_id}:domain",
                "Manifest domain matches registry domain.",
                f"{manifest.get('domain')} vs {record.get('domain')}",
            )
        )
        checks.append(
            check(
                manifest.get("risk_level") == record.get("risk_level"),
                f"{wiki_id}:risk_level",
                "Manifest risk_level matches registry risk_level.",
                f"{manifest.get('risk_level')} vs {record.get('risk_level')}",
            )
        )
        checks.append(
            check(
                manifest.get("freshness_requirement") == record.get("freshness"),
                f"{wiki_id}:freshness",
                "Manifest freshness_requirement matches registry freshness.",
                f"{manifest.get('freshness_requirement')} vs {record.get('freshness')}",
            )
        )

        for entrypoint in REQUIRED_ENTRYPOINTS:
            checks.append(
                check(
                    f"- {entrypoint}".casefold() in manifest_text and (wiki_path / entrypoint).exists(),
                    f"{wiki_id}:entrypoint:{entrypoint}",
                    "Manifest declares a required entrypoint and the file exists.",
                    entrypoint,
                )
            )
        for dirname in REQUIRED_DIRECTORIES:
            checks.append(
                check(
                    f"- {dirname}".casefold() in manifest_text and (wiki_path / dirname).is_dir(),
                    f"{wiki_id}:required_directory:{dirname}",
                    "Manifest declares a required directory and the directory exists.",
                    dirname,
                )
            )
        checks.append(
            check(
                "trigger_keywords:" in manifest_text,
                f"{wiki_id}:trigger_keywords",
                "Manifest declares trigger keywords.",
                "trigger_keywords",
            )
        )
        checks.append(
            check(
                all(flag in manifest_text for flag in REQUIRED_SAFETY_FLAGS),
                f"{wiki_id}:safety_flags",
                "Manifest declares all required safety flags.",
                f"{sum(1 for flag in REQUIRED_SAFETY_FLAGS if flag in manifest_text)}/{len(REQUIRED_SAFETY_FLAGS)} flags",
            )
        )
    return checks


def markdown_report(checks: list[dict]) -> str:
    failed = [item for item in checks if not item["passed"]]
    lines = [
        "# Registry Consistency Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Checks: {len(checks)}",
        f"- Passed: {len(checks) - len(failed)}",
        f"- Failed: {len(failed)}",
        "",
        "## Checks",
        "",
        "| Check | Result | Evidence |",
        "| --- | --- | --- |",
    ]
    for item in checks:
        result = "PASS" if item["passed"] else "FAIL"
        lines.append(f"| {item['check_id']} | {result} | {item['evidence']} |")
    lines.extend(
        [
            "",
            "## Usage Notes",
            "",
            "- Run this after adding, renaming, or changing a wiki manifest.",
            "- Failed checks usually mean registry, manifest, or directory metadata drifted apart.",
            "- This report does not verify source freshness or safety behavior; use the source queue and safety audit reports for those gates.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    checks = registry_checks()
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
        print("REGISTRY CONSISTENCY FAILED")
        for item in failed:
            print(f"- {item['check_id']}: {item['evidence']}")
        return 1
    print(f"REGISTRY CONSISTENCY PASSED ({len(checks)} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
