# RAG Usage

Local-first RAG scaffold. Chroma is optional; scripts fall back to keyword search when optional dependencies are unavailable.

Run `python rag/search_knowledge.py --query "source review human gate" --top-k 5`.

v2.1 fallback indexing includes stable knowledge pages and these metadata fields:

- `knowledge_density_group`
- `current_fact`
- `source_status`
- `generated_by`
- `risk_level`
- `human_gate_required`

No Chroma runtime store is required for acceptance, and `rag/chroma/` is ignored by git.
