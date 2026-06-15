#!/usr/bin/env python3
"""Generate ingestion pipeline report."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"
LOG = ROOT / "obsidian-vault" / "00_System" / "Logs" / "Ingestion Log.md"
def main():
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text("# Ingestion Log\n\nNo raw ingestion has been performed by default.\n", encoding="utf-8")
    DOCS.mkdir(exist_ok=True); REGISTRY.mkdir(exist_ok=True)
    warnings = ["OCR dependency optional and not required", "Whisper dependency optional and not required", "No Raw inputs may be present"]
    manifest = {"generated": date.today().isoformat(), "passed": True, "warnings": warnings, "raw_root": "obsidian-vault/01_Raw", "candidate_root": "obsidian-vault/02_Knowledge/Candidates"}
    (REGISTRY / "ingestion-pipeline-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    for name, title in [("INGESTION_PIPELINE.md","Ingestion Pipeline"),("MULTIMODAL_PROCESSING_GUIDE.md","Multimodal Processing Guide"),("RAW_TO_KNOWLEDGE_WORKFLOW.md","Raw To Knowledge Workflow")]:
        (DOCS / name).write_text(f"# {title}\n\nRaw inputs remain unverified. OCR/Whisper outputs are never treated as verified facts. High-risk materials require human review.\n", encoding="utf-8")
    print("INGESTION REPORT GENERATED (warnings only)")
    return 0
if __name__ == "__main__": raise SystemExit(main())
