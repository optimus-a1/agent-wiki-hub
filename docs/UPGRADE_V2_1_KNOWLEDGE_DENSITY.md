# Upgrade V2.1 Knowledge Density

v2.1 expands Agent Wiki Hub with stable, model-synthesized domain knowledge. The expansion does not use network access, does not crawl sources, does not write current facts, and does not change source-review evidence state.

## Added Capabilities

- Per-wiki stable concepts, rules, workflows, cases, prompts, and evals.
- Knowledge density reports and audits.
- Current-fact leakage audit.
- High-risk human/source gate audit.
- Root wiki MOC pages.
- Obsidian backlinks and density dashboards.
- Dashboard JSON snapshots for density and gates.
- RAG fallback metadata for stable knowledge retrieval.

## Boundary

The new pages are reusable stable knowledge. They are not authoritative citations. Finance, legal, health, security, node operations, customs, airdrop/Web3, platform rules, laws, policies, prices, versions, live vulnerability status, and project status still require source review before use.

## Commands

```bash
python scripts/generate_knowledge_density_report.py
python scripts/audit_knowledge_density.py
python scripts/audit_current_fact_leakage.py
python scripts/audit_high_risk_boundaries.py
python scripts/generate_knowledge_expansion_summary.py
python scripts/generate_wiki_moc_pages.py
python scripts/generate_obsidian_backlinks.py
python scripts/run_acceptance.py
```
