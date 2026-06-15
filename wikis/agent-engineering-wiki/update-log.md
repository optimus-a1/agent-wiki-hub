# Update Log — Agent Engineering Wiki

## 2026-06-01

- Added stable high-density knowledge pages for agent memory and context, tool grounding, eval loops, and tool-overreach cases.
- Updated README and manifest to register the stable-only expansion boundary.
- Added Agent Wiki Hub v2 local-first architecture scaffolding for Obsidian, RAG, dashboard, ingestion, crawler, candidate classification, promotion audits, source-review queueing, and secret-safe acceptance checks.

## 2026-05-31

- Added source-review packet classification reporting so active import, planning-only, advisory, and historical packet artifacts have explicit acceptance roles.
- Added wave-2 pending packet and independent work-order bundle generation without source verification or current-fact writes.
- Added planning-only source review wave plan generation for wave-level work-order sequencing without writing current facts.

## 2026-05-28

- Added post-import source evidence compatibility for acceptance, packet rehearsal, readiness, work orders, completion audit, and release notes.
- Split source-review packet audit into active import packets and advisory AI-prefill artifacts so historical prefill packets stay visible without blocking post-import acceptance.
- Made dashboard current-fact and acceptance gates visible but non-blocking to avoid self-locking acceptance and release-note generation.
- Added source review work order generation through `scripts/generate_source_review_work_orders.py`.
- Added source review readiness matrix generation through `scripts/generate_source_review_readiness_matrix.py`.
- Added source review packet import rehearsal through `scripts/rehearse_source_review_packet_imports.py`.
- Added source review packet auditing through `scripts/audit_source_review_packets.py`.
- Added source review packet bundle generation through `scripts/generate_source_review_packet_bundle.py`.
- Added source review session planning through `scripts/generate_source_review_session_plan.py`.
- Added source reviewer queue generation through `scripts/generate_source_reviewer_queue.py`.
- Added source evidence packet fixture generation through `scripts/generate_source_evidence_packet_fixtures.py`.
- Added source evidence packet import generation through `scripts/import_source_evidence_packet.py`.
- Added source refresh wave runner generation through `scripts/generate_source_refresh_wave_runner.py`.
- Added Agent handoff generation through `scripts/generate_agent_handoff.py`.
- Added source refresh dashboard generation through `scripts/generate_source_refresh_dashboard.py`.
- Added source evidence quality auditing through `scripts/audit_source_evidence_quality.py`.
- Added source evidence recording through `scripts/record_source_evidence.py`.
- Added source refresh completion auditing through `scripts/audit_source_refresh_completion.py`.
- Added source review packet classification and wave-2 batch planning artifacts for post-import/pending source review handoff.
- Added wave-3 source-review planning, pending packet, and independent work-order generation without current-fact writes.
- Added final source-review status generation for wave handoff, packet classification, human gates, and acceptance state.

## 2026-05-27

- Added source refresh ticket generation through `scripts/generate_source_refresh_tickets.py`.
- Added query-to-wiki routing CLI through `scripts/route_wiki.py`.
- Added Agent routing card generation through `scripts/generate_agent_routing_cards.py`.
- Added hub navigation generation through `scripts/generate_hub_navigation.py`.
- Added change impact summary generation through `scripts/generate_change_summary.py`.
- Made wiki package file ordering deterministic for release manifests.
- Added source refresh log template for authoritative source verification.
- Added source refresh playbook generation through `scripts/generate_source_refresh_playbook.py`.
- Added release notes and release manifest generation through `scripts/generate_release_notes.py`.
- Added CI workflow auditing through `scripts/audit_ci_workflow.py`.
- Added GitHub Actions acceptance workflow and CI usage notes.
- Excluded generated Python cache artifacts from wiki packages.
- Added package integrity auditing through `scripts/audit_pack_integrity.py`.
- Added link integrity auditing through `scripts/audit_links.py`.
- Added content coverage auditing through `scripts/audit_content_coverage.py`.
- Added page metadata auditing through `scripts/audit_page_metadata.py`.
- Added registry, manifest, and directory consistency reporting through `scripts/check_registry_consistency.py`.
- Normalized acceptance subprocess output to UTF-8 for readable generated reports.
- Added machine-readable safety boundary auditing through `scripts/audit_safety_boundaries.py`.
- Added source update queue reporting through `scripts/list_source_updates.py`.
- Added full local acceptance reporting workflow through `scripts/run_acceptance.py`.
- Added sample RAG source-grounding case and eval coverage for latest-model-price refusal.
- Added RAG and Knowledge Pack foundations covering chunking, indexing, recall, reranking, citations, evals, and source updates.
- Added Codex Skills foundations covering SKILL.md, scripts, references, assets, triggers, and safety boundaries.
- Added Knowledge Pack quality rules for structure, metadata, routing, evals, and update logs.
- Added eval design workflow covering golden questions, behavior tests, source-grounding tests, refusal tests, and regressions.
- Updated evals and source notes for Codex Skills, RAG frameworks, model APIs, MCP/tool schemas, and eval harness freshness topics.

## 2026-05-26

- Initialized standard Agent Wiki structure.
- Added base rules, workflow, cases, tools, prompts, evals, and source notes.

## 2026-06-15 - v2.1 knowledge density expansion

- Added model-synthesized stable knowledge pages for concepts, rules, workflows, cases, and prompts.
- Added `evals/stable-knowledge-evals.yaml` with 10 stable eval tests.
- No current facts, live prices, live policies, current laws, current vulnerabilities, or evidence verification were added.
- High-risk outputs remain gated by human review and source review.
