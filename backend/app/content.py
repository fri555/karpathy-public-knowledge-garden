import json
import re
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MarkdownPage:
    path: Path
    title: str
    kind: str
    tags: list[str]
    links: list[str]
    body: str


@dataclass(frozen=True)
class GeneratedCard:
    id: str
    type: str
    question: str
    answer: str
    explanation: str
    source_page: str
    concepts: list[str]
    difficulty: str
    created: str


@dataclass(frozen=True)
class PublicPage:
    title: str
    kind: str
    path: str
    tags: list[str]
    links: list[str]
    body: str


def parse_markdown_page(path: Path) -> MarkdownPage:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _split_frontmatter(text)
    title = _extract_title(body) or path.stem
    kind = frontmatter.get("type", "page")
    tags = _parse_inline_list(frontmatter.get("tags", "[]"))
    links = _extract_wiki_links(body)

    return MarkdownPage(
        path=path,
        title=title,
        kind=kind,
        tags=tags,
        links=links,
        body=body.strip(),
    )


def generate_cards_for_page(page: MarkdownPage) -> list[GeneratedCard]:
    cards: list[GeneratedCard] = []
    definition = _extract_one_sentence_definition(page.body)

    if definition:
        cards.append(
            GeneratedCard(
                id=_card_id(page, "definition"),
                type="definition",
                question=f"什么是 {page.title}？",
                answer=definition,
                explanation="先用一句话回忆概念，再回到来源页补充上下文。",
                source_page=str(page.path),
                concepts=[page.title],
                difficulty="medium",
                created="2026-06-25",
            )
        )

    if page.links:
        cards.append(
            GeneratedCard(
                id=_card_id(page, "connection"),
                type="connection",
                question=f"{page.title} 和哪些旧概念发生连接？",
                answer="、".join(page.links),
                explanation="连接卡用于保持知识网络活性，避免新知识孤立存在。",
                source_page=str(page.path),
                concepts=page.links,
                difficulty="medium",
                created="2026-06-25",
            )
        )

    return cards


def collect_cards_from_wiki(root: Path) -> list[GeneratedCard]:
    cards: list[GeneratedCard] = []
    public_dirs = [
        root / "wiki" / "concepts",
        root / "wiki" / "entities",
        root / "wiki" / "summaries",
        root / "wiki" / "syntheses",
    ]

    for directory in public_dirs:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            page = parse_markdown_page(path)
            page = MarkdownPage(
                path=path.relative_to(root),
                title=page.title,
                kind=page.kind,
                tags=page.tags,
                links=page.links,
                body=page.body,
            )
            cards.extend(generate_cards_for_page(page))

    return cards


def collect_public_pages(root: Path) -> list[PublicPage]:
    pages: list[PublicPage] = []

    for path in _iter_public_markdown_paths(root):
        page = _page_with_relative_path(parse_markdown_page(path), path, root)
        pages.append(_to_public_page(page))

    return pages


def read_public_page(root: Path, public_path: str) -> PublicPage:
    path = _resolve_public_path(root, public_path)
    page = _page_with_relative_path(parse_markdown_page(path), path, root)
    return _to_public_page(page)


def get_today_cards(root: Path) -> list[GeneratedCard]:
    cards = collect_cards_from_wiki(root)
    if cards:
        return cards
    return [_demo_card()]


def write_cards_json(root: Path, output_path: Path) -> None:
    cards = get_today_cards(root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            {"cards": [_to_frontend_card(card) for card in cards]},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def write_pages_json(root: Path, output_path: Path) -> None:
    pages = collect_public_pages(root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            {
                "pages": [
                    {
                        "title": page.title,
                        "kind": page.kind,
                        "path": page.path,
                        "tags": page.tags,
                        "links": page.links,
                    }
                    for page in pages
                ]
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def _to_frontend_card(card: GeneratedCard) -> dict[str, object]:
    data = asdict(card)
    return {
        "id": data["id"],
        "type": data["type"],
        "question": data["question"],
        "answer": data["answer"],
        "explanation": data["explanation"],
        "sourcePage": data["source_page"],
        "concepts": data["concepts"],
        "difficulty": data["difficulty"],
        "created": data["created"],
    }


def _demo_card() -> GeneratedCard:
    return GeneratedCard(
        id="concept-llm-wiki-definition-001",
        type="definition",
        question="什么是 LLM Wiki？",
        answer="LLM Wiki 是由 Agent 持续维护和编译的知识网络。",
        explanation="重点不是存文档，而是让每份资料和每次提问都沉淀为可链接、可复用、可继续生长的知识。",
        source_page="wiki/concepts/LLM Wiki.md",
        concepts=["LLM Wiki", "知识复利", "Ingest 录入"],
        difficulty="medium",
        created="2026-06-25",
    )


def _iter_public_markdown_paths(root: Path) -> list[Path]:
    public_dirs = [
        root / "wiki" / "concepts",
        root / "wiki" / "entities",
        root / "wiki" / "summaries",
        root / "wiki" / "syntheses",
    ]
    paths: list[Path] = []

    for directory in public_dirs:
        if directory.exists():
            paths.extend(sorted(directory.glob("*.md")))

    return paths


def _page_with_relative_path(page: MarkdownPage, path: Path, root: Path) -> MarkdownPage:
    return MarkdownPage(
        path=path.relative_to(root),
        title=page.title,
        kind=page.kind,
        tags=page.tags,
        links=page.links,
        body=page.body,
    )


def _to_public_page(page: MarkdownPage) -> PublicPage:
    return PublicPage(
        title=page.title,
        kind=page.kind,
        path=str(page.path),
        tags=page.tags,
        links=page.links,
        body=page.body,
    )


def _resolve_public_path(root: Path, public_path: str) -> Path:
    requested = Path(public_path)

    if requested.is_absolute() or ".." in requested.parts:
        raise ValueError("Invalid public page path")

    if len(requested.parts) < 3 or requested.parts[0] != "wiki":
        raise ValueError("Only public wiki paths are allowed")

    if requested.parts[1] not in {"concepts", "entities", "summaries", "syntheses"}:
        raise ValueError("Only public wiki directories are allowed")

    path = root / requested
    if not path.exists() or path.suffix != ".md":
        raise ValueError("Public page does not exist")

    return path


def _split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    raw_frontmatter = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}

    for line in raw_frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()

    return data, body


def _extract_title(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def _parse_inline_list(value: str) -> list[str]:
    cleaned = value.strip()
    if not (cleaned.startswith("[") and cleaned.endswith("]")):
        return []

    inner = cleaned[1:-1].strip()
    if not inner:
        return []

    return [item.strip().strip("\"'") for item in inner.split(",") if item.strip()]


def _extract_wiki_links(body: str) -> list[str]:
    links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", body)
    seen: set[str] = set()
    result: list[str] = []

    for link in links:
        name = link.strip()
        if name and name not in seen:
            seen.add(name)
            result.append(name)

    return result


def _extract_one_sentence_definition(body: str) -> str | None:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("> 一句话定义："):
            return stripped.removeprefix("> 一句话定义：").strip()
    return None


def _card_id(page: MarkdownPage, card_type: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", page.title).strip("-").lower()
    return f"{page.kind}-{slug}-{card_type}-001"
