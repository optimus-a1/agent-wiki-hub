#!/usr/bin/env python3
"""Audit ingestion pipeline scaffold."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["ingestion/README.md","ingestion/intake_config.yaml","ingestion/import_markdown.py","ingestion/import_webclip.py","ingestion/import_pdf_placeholder.py","ingestion/import_image_ocr_placeholder.py","ingestion/import_audio_whisper_placeholder.py","ingestion/import_video_placeholder.py","ingestion/process_raw_to_knowledge.py","ingestion/generate_ingestion_report.py","obsidian-vault/00_System/Logs/Ingestion Log.md","registry/ingestion-pipeline-manifest.json"]
def main():
    checks = [{"path": p, "passed": (ROOT / p).exists()} for p in REQUIRED]
    failed = [c for c in checks if not c["passed"]]
    lines = ["# Ingestion Pipeline Audit", "", f"Generated: {date.today().isoformat()}", "", f"- Passed: {not failed}", "", "| Path | Result |", "| --- | --- |"]
    lines.extend(f"| {c['path']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in checks)
    (ROOT / "docs" / "INGESTION_PIPELINE_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "registry" / "ingestion-pipeline-audit.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": not failed, "checks": checks, "warnings": ["OCR optional", "Whisper optional"]}, indent=2), encoding="utf-8")
    print(f"INGESTION PIPELINE AUDIT {'PASSED' if not failed else 'FAILED'}")
    return 0 if not failed else 1
if __name__ == "__main__": raise SystemExit(main())
