#!/usr/bin/env python3
"""Tiny keyword search over index/search_index.json."""
from pathlib import Path
import argparse, json, re, math

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index" / "search_index.json"

def tokenize(text: str):
    return re.findall(r"[A-Za-z0-9_\-\.]+|[\u4e00-\u9fff]", text.lower())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--query', required=True)
    ap.add_argument('--wiki', default=None)
    ap.add_argument('--top-k', type=int, default=8)
    args = ap.parse_args()
    if not INDEX.exists():
        raise SystemExit("Missing index/search_index.json. Run: python3 scripts/update_index.py")
    data = json.loads(INDEX.read_text(encoding='utf-8'))
    q = tokenize(args.query)
    results = []
    for d in data['docs']:
        if args.wiki and d.get('wiki') != args.wiki:
            continue
        toks = d.get('tokens', [])
        score = sum(toks.count(term) for term in q)
        if score:
            results.append((score, d))
    results.sort(key=lambda x: x[0], reverse=True)
    for score, d in results[:args.top_k]:
        print(f"[{score}] {d['path']} :: {d['title']}")
        print(f"    {d['preview'][:220]}...")
    if not results:
        print("No results")

if __name__ == "__main__":
    main()
