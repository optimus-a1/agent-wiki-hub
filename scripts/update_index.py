#!/usr/bin/env python3
"""Build a simple JSON search index for all Markdown/YAML files."""
from pathlib import Path
import json, re, hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "index" / "search_index.json"
INCLUDE_SUFFIXES = {".md", ".yaml", ".yml", ".json"}
STOP = set("的 了 和 是 在 与 或 对 为 及 一个 一种 this that with from into your you are the and or for to of in on".split())

def tokenize(text: str):
    words = re.findall(r"[A-Za-z0-9_\-\.]+|[\u4e00-\u9fff]", text.lower())
    return [w for w in words if w not in STOP and len(w.strip()) > 0]

def main():
    docs = []
    for path in sorted((ROOT / "wikis").rglob("*")):
        if not path.is_file() or path.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="ignore")
        tokens = tokenize(text)
        docs.append({
            "id": hashlib.sha1(rel.encode()).hexdigest()[:12],
            "path": rel,
            "wiki": rel.split('/')[1] if rel.startswith('wikis/') else None,
            "title": next((line.lstrip('# ').strip() for line in text.splitlines() if line.strip().startswith('#')), path.stem),
            "tokens": tokens[:2000],
            "preview": re.sub(r"\s+", " ", text)[:500]
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"doc_count": len(docs), "docs": docs}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Indexed {len(docs)} docs -> {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
