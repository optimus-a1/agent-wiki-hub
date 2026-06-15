# Local Usage Guide

This guide describes local-only operation for Agent Wiki Hub v2.1. It does not require network access and does not promote current facts without a review gate.

## Prerequisites

- Run commands from the repository root.
- Keep secrets in `.env` only. Do not commit API keys, tokens, cookies, or private keys.
- Treat `pending` source evidence as review material, not as verified knowledge.

## Obsidian Mode

Open `obsidian-vault/` as an Obsidian vault.

Regenerate the vault mirror and dashboards:

```bash
python scripts/generate_obsidian_vault.py
python scripts/generate_obsidian_canvas.py
python scripts/audit_obsidian_vault.py
```

Use `obsidian-vault/02_Knowledge/MOCs/` for wiki maps and `obsidian-vault/05_Dashboard/` for review, source, and knowledge dashboards. v2.1 adds `Knowledge Density.md`, `Current Fact Gates.md`, `Human Review Gates.md`, `High Risk Boundaries.md`, and `Knowledge Density Map.canvas`.

## Dashboard Mode

Refresh dashboard data:

```bash
python dashboard/scripts/collect_dashboard_data.py
python scripts/audit_dashboard.py
```

Open `dashboard/index.html` locally. The dashboard reads JSON snapshots from `dashboard/data/` and does not call external services. v2.1 adds knowledge density, boundary status, current-fact gate status, Obsidian vault status, wiki MOC status, and automation-generated page counts.

## RAG Mode

Inspect and search local wiki content:

```bash
python rag/index_wikis.py
python rag/index_obsidian.py
python rag/search_knowledge.py --query "risk control" --top-k 5
```

Optional vector indexing uses local dependencies listed in `rag/requirements-rag.txt`. Runtime vector stores belong under `rag/chroma/` and are ignored by git. Keyword fallback indexes v2.1 pages and includes metadata for `current_fact`, `source_status`, `generated_by`, `risk_level`, and `human_gate_required`.

## Knowledge Density Mode

Generate and audit stable knowledge density:

```bash
python scripts/generate_knowledge_density_report.py
python scripts/audit_knowledge_density.py
python scripts/audit_current_fact_leakage.py
python scripts/audit_high_risk_boundaries.py
python scripts/generate_knowledge_expansion_summary.py
python scripts/generate_wiki_moc_pages.py
python scripts/generate_obsidian_backlinks.py
```

The added knowledge is model-synthesized stable knowledge. It is not an authoritative source, contains no current facts, and does not mark evidence as verified.

## Crawler And Ingestion Mode

The crawler is controlled by `crawler/sources.yaml`. Use dry-run output first, then review candidates before promotion:

```bash
python crawler/generate_crawl_report.py
python scripts/classify_candidate_knowledge.py --dry-run
python scripts/promote_stable_knowledge.py --dry-run
python scripts/generate_source_review_from_candidates.py --dry-run
```

Raw material belongs in `obsidian-vault/01_Raw/`. Stable, timeless knowledge may be promoted only through the review flow. Changing facts must remain in source review and must not be written into current wiki facts.

## Source Review Gates

Use source review packets for facts that may change over time:

```bash
python scripts/generate_source_review_packet_classification.py
python scripts/audit_source_review_packets.py
python scripts/rehearse_source_review_packet_imports.py
```

Planning-only pending packets are allowed to exist without blocking acceptance. Verified evidence packets remain the only path for importing source-backed current facts.

## Acceptance

Run the full local suite before handoff:

```bash
python scripts/validate_wiki.py
python scripts/update_index.py
python scripts/audit_links.py
python scripts/run_acceptance.py
```

Acceptance reports are written to `docs/ACCEPTANCE_REPORT.md` and `registry/acceptance-report.json`.
