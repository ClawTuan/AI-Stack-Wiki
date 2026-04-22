import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class Page:
    rel_path: str
    abs_path: Path
    title: str
    category: str
    node_id: str


def _safe_node_id(s: str) -> str:
    s = s.replace(os.sep, "/")
    s = re.sub(r"[^A-Za-z0-9_]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return f"n_{s}" if s else "n"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _extract_title(md: str, fallback: str) -> str:
    m = FRONT_MATTER_RE.match(md)
    if not m:
        return fallback
    fm = m.group(1)
    for line in fm.splitlines():
        if line.strip().startswith("title:"):
            value = line.split(":", 1)[1].strip()
            if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            return value or fallback
    return fallback


def _category_for(rel_path: str) -> str:
    rel_path = rel_path.replace(os.sep, "/")
    if rel_path.startswith("wiki/concepts/"):
        return "Concepts"
    if rel_path.startswith("wiki/models/"):
        return "Models"
    if rel_path.startswith("wiki/papers/"):
        return "Papers"
    return "Other"


def _normalize_md_link(link: str) -> Optional[str]:
    link = link.strip()
    if not link or link.startswith("#"):
        return None
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", link):
        return None
    link = link.split("#", 1)[0].split("?", 1)[0].strip()
    if not link.endswith(".md"):
        return None
    return link


def load_pages(repo_root: Path) -> dict[str, Page]:
    pages: dict[str, Page] = {}
    wiki_dir = repo_root / "wiki"
    for path in sorted(wiki_dir.rglob("*.md")):
        if path.name == "index.md":
            continue
        if path.stem.startswith("test"):
            continue
        rel = str(path.relative_to(repo_root)).replace(os.sep, "/")
        md = _read_text(path)
        fallback = path.stem
        title = _extract_title(md, fallback)
        category = _category_for(rel)
        node_id = _safe_node_id(rel)
        pages[rel] = Page(rel_path=rel, abs_path=path, title=title, category=category, node_id=node_id)
    return pages


def extract_edges(repo_root: Path, pages: dict[str, Page]) -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()
    for rel, page in pages.items():
        md = _read_text(page.abs_path)
        for raw_link in MD_LINK_RE.findall(md):
            link = _normalize_md_link(raw_link)
            if not link:
                continue
            base_dir = page.abs_path.parent
            target_abs = (base_dir / link).resolve()
            try:
                target_rel = str(target_abs.relative_to(repo_root)).replace(os.sep, "/")
            except ValueError:
                continue
            if target_rel in pages:
                edges.add((rel, target_rel))
    return edges


def render_mermaid(pages: dict[str, Page], edges: set[tuple[str, str]]) -> str:
    lines: list[str] = []
    lines.append("graph TD")
    category_nodes = {
        "Concepts": "cat_concepts",
        "Models": "cat_models",
        "Papers": "cat_papers",
        "Other": "cat_other",
    }
    for cat, nid in category_nodes.items():
        lines.append(f'  {nid}["{cat}"]')

    for rel, page in sorted(pages.items(), key=lambda x: (x[1].category, x[1].title.lower())):
        label = page.title.replace('"', '\\"')
        lines.append(f'  {page.node_id}["{label}"]')
        lines.append(f"  {category_nodes.get(page.category, 'cat_other')} --> {page.node_id}")

    for src_rel, dst_rel in sorted(edges):
        src = pages[src_rel].node_id
        dst = pages[dst_rel].node_id
        lines.append(f"  {src} --> {dst}")
    return "\n".join(lines) + "\n"


def update_index_md(repo_root: Path, mermaid: str) -> None:
    index_path = repo_root / "wiki" / "index.md"
    text = _read_text(index_path)
    start = "<!-- GRAPH:START -->"
    end = "<!-- GRAPH:END -->"
    if start not in text or end not in text:
        raise SystemExit("wiki/index.md missing GRAPH markers")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    new_block = f"{start}\n\n```mermaid\n{mermaid}```\n\n{end}"
    index_path.write_text(before + new_block + after, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".", help="repo root")
    parser.add_argument("--write-index", action="store_true", help="update wiki/index.md between GRAPH markers")
    args = parser.parse_args()

    repo_root = Path(args.repo).resolve()
    pages = load_pages(repo_root)
    edges = extract_edges(repo_root, pages)
    mermaid = render_mermaid(pages, edges)

    if args.write_index:
        update_index_md(repo_root, mermaid)
    else:
        print(mermaid, end="")


if __name__ == "__main__":
    main()
