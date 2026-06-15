#!/usr/bin/env python3
"""Generate Obsidian JSON Canvas maps."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DASH = ROOT / "obsidian-vault" / "05_Dashboard"
REGISTRY = ROOT / "registry"
DOCS = ROOT / "docs"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def text_node(node_id: str, text: str, x: int, y: int) -> dict:
    return {"id": node_id, "type": "text", "text": text, "x": x, "y": y, "width": 260, "height": 110}


def file_node(node_id: str, path: str, x: int, y: int) -> dict:
    return {"id": node_id, "type": "file", "file": path, "x": x, "y": y, "width": 280, "height": 120}


def edge(edge_id: str, from_id: str, to_id: str) -> dict:
    return {"id": edge_id, "fromNode": from_id, "toNode": to_id}


def write_canvas(path: Path, nodes: list[dict], edges: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"nodes": nodes, "edges": edges}, indent=2), encoding="utf-8")


def main() -> int:
    DASH.mkdir(parents=True, exist_ok=True)
    wiki_ids = sorted(p.name for p in WIKIS.iterdir() if p.is_dir())
    hub_nodes = [file_node("wiki-status", "05_Dashboard/Wiki Status.md", 0, 0)]
    hub_edges = []
    x, y = -720, 180
    for idx, wiki in enumerate(wiki_ids):
        node_id = f"wiki-{idx}"
        hub_nodes.append(text_node(node_id, wiki, x + (idx % 4) * 360, y + (idx // 4) * 180))
        hub_edges.append(edge(f"edge-{idx}", "wiki-status", node_id))
    for idx, label in enumerate(["Source Review", "Acceptance", "RAG", "Obsidian Vault", "Dashboard", "Ingestion", "Crawler", "Knowledge Density", "Current Fact Gates"]):
        node_id = f"system-{idx}"
        hub_nodes.append(text_node(node_id, label, 820, idx * 150))
        hub_edges.append(edge(f"system-edge-{idx}", "wiki-status", node_id))
    write_canvas(DASH / "Agent Wiki Hub.canvas", hub_nodes, hub_edges)

    wave_nodes = [
        file_node("source-review", "05_Dashboard/Source Review Status.md", 0, 0),
        text_node("wave-1", "Wave-1 active packet", -420, 190),
        text_node("wave-2", "Wave-2 planning-only", 0, 190),
        text_node("wave-3", "Wave-3 planning-only", 420, 190),
        file_node("human-gates", "05_Dashboard/Human Gates.md", 0, 390),
    ]
    wave_edges = [edge("e1", "source-review", "wave-1"), edge("e2", "source-review", "wave-2"), edge("e3", "source-review", "wave-3"), edge("e4", "source-review", "human-gates")]
    write_canvas(DASH / "Source Review Waves.canvas", wave_nodes, wave_edges)

    map_nodes = [file_node("graph", "05_Dashboard/Knowledge Graph Status.md", 0, 0)]
    map_edges = []
    for idx, wiki in enumerate(wiki_ids):
        node_id = f"moc-{idx}"
        map_nodes.append(text_node(node_id, f"{wiki} MOC", -700 + (idx % 3) * 420, 170 + (idx // 3) * 170))
        map_edges.append(edge(f"moc-edge-{idx}", "graph", node_id))
    write_canvas(DASH / "Wiki Knowledge Map.canvas", map_nodes, map_edges)

    density_nodes = [
        file_node("density", "05_Dashboard/Knowledge Density.md", 0, 0),
        file_node("current-facts", "05_Dashboard/Current Fact Gates.md", -420, 190),
        file_node("human-review", "05_Dashboard/Human Review Gates.md", 0, 190),
        file_node("high-risk", "05_Dashboard/High Risk Boundaries.md", 420, 190),
    ]
    density_edges = [
        edge("density-current", "density", "current-facts"),
        edge("density-human", "density", "human-review"),
        edge("density-risk", "density", "high-risk"),
    ]
    for idx, wiki in enumerate(wiki_ids):
        node_id = f"density-wiki-{idx}"
        density_nodes.append(text_node(node_id, wiki, -700 + (idx % 4) * 360, 390 + (idx // 4) * 160))
        density_edges.append(edge(f"density-edge-{idx}", "density", node_id))
    write_canvas(DASH / "Knowledge Density Map.canvas", density_nodes, density_edges)

    manifest = {
        "generated": date.today().isoformat(),
        "passed": True,
        "canvas_files": [rel(DASH / name) for name in ["Agent Wiki Hub.canvas", "Source Review Waves.canvas", "Wiki Knowledge Map.canvas", "Knowledge Density Map.canvas"]],
        "wiki_count": len(wiki_ids),
    }
    REGISTRY.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "obsidian-canvas-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (DOCS / "OBSIDIAN_CANVAS_GUIDE.md").write_text(
        "# Obsidian Canvas Guide\n\nGenerated JSON Canvas maps live in `obsidian-vault/05_Dashboard/` and require no external services.\n",
        encoding="utf-8",
    )
    print(f"OBSIDIAN CANVAS GENERATED ({len(manifest['canvas_files'])} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
