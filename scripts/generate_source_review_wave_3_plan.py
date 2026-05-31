#!/usr/bin/env python3
"""Generate the planning-only wave-3 source-review plan."""
from __future__ import annotations

import json

from generate_source_review_wave_plan import DOCS, REGISTRY, ROOT, build_plan, markdown_report


def main() -> int:
    data = build_plan("wave-3")
    docs_out = DOCS / "SOURCE_REVIEW_WAVE_3_PLAN.md"
    json_out = REGISTRY / "source-review-wave-3-plan.json"
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    docs_out.write_text(markdown_report(data), encoding="utf-8")
    json_out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {docs_out.relative_to(ROOT)}")
    print(f"Wrote {json_out.relative_to(ROOT)}")
    print(
        "SOURCE REVIEW WAVE-3 PLAN GENERATED "
        f"({data['selected_review_count']} work orders, {data['selected_human_review_gate_count']} human gates)"
    )
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
