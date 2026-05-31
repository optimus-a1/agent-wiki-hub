#!/usr/bin/env python3
"""Dry-run import every source-review packet without writing evidence logs."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
PACKET_DIR = REGISTRY / "source-review-packets"
DOCS_OUT = ROOT / "docs" / "SOURCE_REVIEW_PACKET_REHEARSAL.md"
JSON_OUT = REGISTRY / "source-review-packet-rehearsal.json"
PACKET_AUDIT_JSON = REGISTRY / "source-review-packet-audit.json"

REPORTS = {
    "source_review_readiness_matrix": "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
    "source_review_packet_audit": "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
    "source_review_packet_bundle": "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
    "source_review_session_plan": "docs/SOURCE_REVIEW_SESSION_PLAN.md",
    "source_evidence_packet_importer": "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "source_refresh_completion": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
}

ADVISORY_PACKET_NAME_PARTS = ("-ai-prefill",)


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


def is_advisory_packet(path: str) -> bool:
    name = Path(path).stem.casefold()
    return any(part in name for part in ADVISORY_PACKET_NAME_PARTS)


def is_planning_only_packet(path: Path) -> bool:
    manifest = path.with_name(f"{path.stem}-manifest.json")
    if manifest.exists():
        try:
            data = read_json(manifest)
            return bool(data.get("planning_only") or data.get("no_current_fact_write"))
        except Exception:
            return False
    if path.suffix.lower() == ".json":
        try:
            data = read_json(path)
            return bool(data.get("planning_only") or data.get("no_current_fact_write"))
        except Exception:
            return False
    return False


def discover_packet_paths(audit: dict) -> list[str]:
    paths = [
        packet.get("path", "")
        for packet in audit.get("packets", [])
        if packet.get("path") and packet.get("blocking", True)
    ]
    if paths:
        return paths
    if not PACKET_DIR.exists():
        return []
    return [
        rel(path)
        for path in sorted(PACKET_DIR.iterdir())
        if path.suffix.lower() in {".json", ".jsonl"}
        and not path.name.endswith("-manifest.json")
        and not is_advisory_packet(path.name)
        and not is_planning_only_packet(path)
    ]


def run_rehearsal(packet_path: str) -> dict:
    args = [
        sys.executable,
        "scripts/import_source_evidence_packet.py",
        "--packet",
        packet_path,
        "--dry-run",
        "--no-post-checks",
        "--allow-duplicate",
    ]
    proc = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "packet": packet_path,
        "command": " ".join([Path(args[0]).name, *args[1:]]),
        "returncode": proc.returncode,
        "output": proc.stdout.strip(),
        "passed": proc.returncode == 0,
    }


def build_rehearsal() -> dict:
    audit = read_json(PACKET_AUDIT_JSON)
    paths = discover_packet_paths(audit)
    audit_packet_status = {
        packet.get("path"): packet.get("passed", False)
        for packet in audit.get("packets", [])
        if packet.get("path") and packet.get("blocking", True)
    }
    results = []
    for path in paths:
        if path in audit_packet_status and not audit_packet_status[path]:
            results.append(
                {
                    "packet": path,
                    "command": "<skipped>",
                    "returncode": 1,
                    "output": "skipped because source review packet audit did not pass for this packet",
                    "passed": False,
                }
            )
            continue
        results.append(run_rehearsal(path))

    checks = [
        {
            "check": "source review packet audit exists",
            "passed": PACKET_AUDIT_JSON.exists() and bool(audit),
            "detail": rel(PACKET_AUDIT_JSON) if PACKET_AUDIT_JSON.exists() else "missing registry/source-review-packet-audit.json",
        },
        {
            "check": "source review packet audit passed",
            "passed": bool(audit.get("passed")),
            "detail": f"{audit.get('packet_count', 0)} packets, {audit.get('issue_count', 0)} issues",
        },
        {
            "check": "packets discovered",
            "passed": bool(paths),
            "detail": f"{len(paths)} packet files",
        },
        {
            "check": "all packet dry-runs passed",
            "passed": all(result["passed"] for result in results) if results else False,
            "detail": f"{sum(1 for result in results if result['passed'])}/{len(results)} dry-runs passed",
        },
    ]
    return {
        "generated": date.today().isoformat(),
        "passed": all(check["passed"] for check in checks),
        "purpose": "Rehearse source-review packet imports with importer dry-run and no post-check writes. Existing imported evidence is acceptable in post-import repositories.",
        "packet_count": len(paths),
        "dry_run_count": len(results),
        "passed_dry_run_count": sum(1 for result in results if result["passed"]),
        "failed_dry_run_count": sum(1 for result in results if not result["passed"]),
        "entry_count_from_audit": int(audit.get("entry_count", 0)),
        "advisory_packet_count_from_audit": int(audit.get("advisory_packet_count", 0)),
        "human_gated_entry_count_from_audit": int(audit.get("human_gated_entry_count", 0)),
        "results": results,
        "checks": checks,
        "reports": REPORTS,
    }


def markdown_report(data: dict) -> str:
    lines = [
        "# Source Review Packet Rehearsal",
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
        f"- Dry runs: {data['dry_run_count']}",
        f"- Passed dry runs: {data['passed_dry_run_count']}",
        f"- Failed dry runs: {data['failed_dry_run_count']}",
        f"- Entries from audit: {data['entry_count_from_audit']}",
        f"- Advisory packets from audit: {data['advisory_packet_count_from_audit']}",
        f"- Human-gated entries from audit: {data['human_gated_entry_count_from_audit']}",
        "",
        "## Results",
        "",
        "| Packet | Result | Command |",
        "| --- | --- | --- |",
    ]
    for result in data["results"]:
        outcome = "PASS" if result["passed"] else "FAIL"
        lines.append(f"| {repo_link(result['packet'])} | {outcome} | `{result['command']}` |")

    lines.extend(["", "## Failed Output", ""])
    failures = [result for result in data["results"] if not result["passed"]]
    if failures:
        for result in failures:
            lines.extend([f"### {result['packet']}", "", "```text", result["output"] or "<no output>", "```", ""])
    else:
        lines.append("No dry-run failures.")

    lines.extend(["", "## Related Reports", ""])
    for name, path in data["reports"].items():
        lines.append(f"- {name}: {repo_link(path)}")

    lines.extend(["", "## Checks", "", "| Check | Result | Detail |", "| --- | --- | --- |"])
    for check in data["checks"]:
        result = "PASS" if check["passed"] else "FAIL"
        lines.append(f"| {check['check']} | {result} | {check['detail']} |")

    lines.extend(
        [
            "",
            "## Safety Boundary",
            "",
            "- This rehearsal uses `--dry-run --no-post-checks` and does not write source evidence logs.",
            "- It also uses `--allow-duplicate` so already-imported packets can be rehearsed again without treating existing evidence as a failure.",
            "- It validates importer compatibility only; it does not verify external facts.",
            "- Passing this rehearsal does not make current-fact topics ready for use.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_rehearsal()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(
        f"SOURCE REVIEW PACKET REHEARSAL {'PASSED' if data['passed'] else 'FAILED'} "
        f"({data['passed_dry_run_count']}/{data['dry_run_count']} dry-runs passed)"
    )
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
