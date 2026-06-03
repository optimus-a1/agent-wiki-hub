#!/usr/bin/env python3
"""Classify source-review packet artifacts by acceptance role."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
PACKET_DIR = REGISTRY / "source-review-packets"
DOCS_OUT = ROOT / "docs" / "SOURCE_REVIEW_PACKET_CLASSIFICATION.md"
JSON_OUT = REGISTRY / "source-review-packet-classification.json"

ADVISORY_NAME_PARTS = ("-ai-prefill",)


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def repo_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def bool_word(value: bool) -> str:
    return "yes" if value else "no"


def packet_paths() -> list[Path]:
    if not PACKET_DIR.exists():
        return []
    return sorted(
        path
        for path in PACKET_DIR.iterdir()
        if path.suffix.lower() in {".json", ".jsonl"} and not path.name.endswith("-manifest.json")
    )


def packet_manifest(path: Path) -> dict:
    return read_json(path.with_name(f"{path.stem}-manifest.json"))


def packet_metadata(path: Path) -> dict:
    if path.suffix.lower() == ".json":
        try:
            data = read_json(path)
            if isinstance(data, dict):
                return data
        except Exception:
            return {}
    return packet_manifest(path)


def entry_count(path: Path, metadata: dict) -> int:
    if path.suffix.lower() == ".jsonl":
        return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    entries = metadata.get("entries", [])
    if isinstance(entries, list):
        return len(entries)
    return 1 if metadata else 0


def classify(path: Path) -> dict:
    metadata = packet_metadata(path)
    name = path.stem.casefold()
    if any(part in name for part in ADVISORY_NAME_PARTS):
        classification = "advisory-prefill-artifact"
        acceptance_role = "non-blocking"
        strict_audit = False
        rationale = "Historical AI-prefill/source-assistance artifact; retained for traceability, not an active import target."
    elif "auto-pending" in name or metadata.get("planning_only") or metadata.get("no_current_fact_write"):
        classification = "planning-only-pending-packet"
        acceptance_role = "non-blocking"
        strict_audit = False
        rationale = "Pending template packet for future source review; it contains placeholders and must not certify current facts."
    elif "backup" in name or "archive" in name or "historical" in name:
        classification = "backup-historical-artifact"
        acceptance_role = "non-blocking"
        strict_audit = False
        rationale = "Backup or historical packet retained for audit trail."
    else:
        classification = "active-import-packet"
        acceptance_role = "blocking"
        strict_audit = True
        rationale = "Current active packet; participates in strict packet audit and rehearsal."
    return {
        "path": rel(path),
        "classification": classification,
        "acceptance_role": acceptance_role,
        "strict_audit": strict_audit,
        "entry_count": entry_count(path, metadata),
        "packet_id": metadata.get("packet_id", ""),
        "planning_only": bool("auto-pending" in name or metadata.get("planning_only") or metadata.get("no_current_fact_write")),
        "rationale": rationale,
    }


def build_report() -> dict:
    records = [classify(path) for path in packet_paths()]
    counts = Counter(record["classification"] for record in records)
    checks = [
        {
            "check": "packet directory exists",
            "passed": PACKET_DIR.exists(),
            "detail": rel(PACKET_DIR) if PACKET_DIR.exists() else "missing registry/source-review-packets",
        },
        {
            "check": "packet files classified",
            "passed": bool(records),
            "detail": f"{len(records)} packet files",
        },
        {
            "check": "active packet exists",
            "passed": any(record["classification"] == "active-import-packet" for record in records),
            "detail": f"{counts.get('active-import-packet', 0)} active packet files",
        },
        {
            "check": "planning packets are non-blocking",
            "passed": all(
                not record["strict_audit"]
                for record in records
                if record["classification"] == "planning-only-pending-packet"
            ),
            "detail": f"{counts.get('planning-only-pending-packet', 0)} planning-only packet files",
        },
    ]
    return {
        "generated": date.today().isoformat(),
        "passed": all(check["passed"] for check in checks),
        "purpose": "Document which source-review packets are active import targets versus advisory, planning-only, or historical artifacts.",
        "packet_dir": rel(PACKET_DIR),
        "packet_count": len(records),
        "classification_counts": dict(sorted(counts.items())),
        "records": records,
        "checks": checks,
    }


def markdown_report(data: dict) -> str:
    lines = [
        "# Source Review Packet Classification",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        data["purpose"],
        "",
        "## Summary",
        "",
        f"- Passed: {bool_word(data['passed'])}",
        f"- Packet files: {data['packet_count']}",
    ]
    for name, count in data["classification_counts"].items():
        lines.append(f"- {name}: {count}")
    lines.extend(
        [
            "",
            "## Classification Table",
            "",
            "| Packet | Classification | Acceptance Role | Strict Audit | Entries | Rationale |",
            "| --- | --- | --- | --- | ---: | --- |",
        ]
    )
    for record in data["records"]:
        lines.append(
            f"| {repo_link(record['path'])} | {record['classification']} | {record['acceptance_role']} | "
            f"{bool_word(record['strict_audit'])} | {record['entry_count']} | {record['rationale']} |"
        )
    lines.extend(["", "## Checks", "", "| Check | Result | Detail |", "| --- | --- | --- |"])
    for check in data["checks"]:
        lines.append(f"| {check['check']} | {'PASS' if check['passed'] else 'FAIL'} | {check['detail']} |")
    lines.extend(
        [
            "",
            "## Safety Boundary",
            "",
            "- Classification does not verify external facts.",
            "- Planning-only and advisory packets are retained for traceability but must not be treated as verified evidence.",
            "- Active import packets still require audit and rehearsal before any real evidence import.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_report()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"SOURCE REVIEW PACKET CLASSIFICATION {'PASSED' if data['passed'] else 'FAILED'} ({data['packet_count']} packets)")
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
