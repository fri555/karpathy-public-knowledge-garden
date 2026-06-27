import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from app.content import (
    collect_cards_from_wiki,
    collect_public_pages,
    generate_cards_for_page,
    get_today_cards,
    parse_markdown_page,
    read_public_page,
    write_cards_json,
    write_pages_json,
)


FIXTURE = Path(__file__).parent / "fixtures" / "sample_concept.md"


class MarkdownContentTests(unittest.TestCase):
    def test_parse_markdown_page_extracts_metadata_title_and_links(self) -> None:
        page = parse_markdown_page(FIXTURE)

        self.assertEqual(page.title, "LLM Wiki")
        self.assertEqual(page.kind, "concept")
        self.assertEqual(page.tags, ["知识管理", "agent"])
        self.assertEqual(page.links, ["知识复利", "Ingest 录入"])

    def test_generate_cards_for_page_creates_definition_and_connection_cards(self) -> None:
        page = parse_markdown_page(FIXTURE)
        cards = generate_cards_for_page(page)

        self.assertEqual([card.type for card in cards], ["definition", "connection"])
        self.assertEqual(cards[0].question, "什么是 LLM Wiki？")
        self.assertIn("由 Agent 持续维护和编译的知识网络", cards[0].answer)
        self.assertEqual(cards[1].concepts, ["知识复利", "Ingest 录入"])

    def test_generate_cards_for_page_strips_inline_markdown_syntax(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "Markdown Concept.md"
            path.write_text(
                "---\ntype: concept\n---\n\n# Markdown Concept\n\n> 一句话定义：**重要概念** 是 [[LLM Wiki]] 的 `核心`。",
                encoding="utf-8",
            )

            cards = generate_cards_for_page(parse_markdown_page(path))

        self.assertEqual(cards[0].answer, "重要概念 是 LLM Wiki 的 核心。")

    def test_collect_cards_from_wiki_scans_supported_public_directories(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            concept_dir = root / "wiki" / "concepts"
            concept_dir.mkdir(parents=True)
            target = concept_dir / "LLM Wiki.md"
            target.write_text(FIXTURE.read_text(encoding="utf-8"), encoding="utf-8")

            cards = collect_cards_from_wiki(root)

        self.assertEqual(len(cards), 2)
        self.assertEqual(cards[0].source_page, "wiki/concepts/LLM Wiki.md")

    def test_get_today_cards_returns_generated_cards_when_wiki_has_content(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            concept_dir = root / "wiki" / "concepts"
            concept_dir.mkdir(parents=True)
            target = concept_dir / "LLM Wiki.md"
            target.write_text(FIXTURE.read_text(encoding="utf-8"), encoding="utf-8")

            cards = get_today_cards(root)

        self.assertEqual(cards[0].question, "什么是 LLM Wiki？")
        self.assertEqual(cards[0].source_page, "wiki/concepts/LLM Wiki.md")

    def test_get_today_cards_falls_back_to_demo_card_when_no_wiki_cards_exist(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            cards = get_today_cards(Path(tmp_dir))

        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0].id, "concept-llm-wiki-definition-001")

    def test_write_cards_json_exports_frontend_friendly_card_payload(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            concept_dir = root / "wiki" / "concepts"
            concept_dir.mkdir(parents=True)
            target = concept_dir / "LLM Wiki.md"
            target.write_text(FIXTURE.read_text(encoding="utf-8"), encoding="utf-8")
            output = root / "public" / "cards" / "today.json"

            write_cards_json(root, output)

            exported = output.read_text(encoding="utf-8")

        self.assertIn('"question": "什么是 LLM Wiki？"', exported)
        self.assertIn('"sourcePage":', exported)

    def test_write_pages_json_exports_public_page_index(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            concept_dir = root / "wiki" / "concepts"
            concept_dir.mkdir(parents=True)
            target = concept_dir / "LLM Wiki.md"
            target.write_text(FIXTURE.read_text(encoding="utf-8"), encoding="utf-8")
            output = root / "public" / "pages" / "index.json"

            write_pages_json(root, output)

            exported = output.read_text(encoding="utf-8")

        self.assertIn('"title": "LLM Wiki"', exported)
        self.assertIn('"path": "wiki/concepts/LLM Wiki.md"', exported)

    def test_collect_public_pages_lists_supported_wiki_pages(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            concept_dir = root / "wiki" / "concepts"
            concept_dir.mkdir(parents=True)
            target = concept_dir / "LLM Wiki.md"
            target.write_text(FIXTURE.read_text(encoding="utf-8"), encoding="utf-8")

            pages = collect_public_pages(root)

        self.assertEqual(len(pages), 1)
        self.assertEqual(pages[0].title, "LLM Wiki")
        self.assertEqual(pages[0].path, "wiki/concepts/LLM Wiki.md")

    def test_read_public_page_returns_body_for_safe_public_path(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            concept_dir = root / "wiki" / "concepts"
            concept_dir.mkdir(parents=True)
            target = concept_dir / "LLM Wiki.md"
            target.write_text(FIXTURE.read_text(encoding="utf-8"), encoding="utf-8")

            page = read_public_page(root, "wiki/concepts/LLM Wiki.md")

        self.assertEqual(page.title, "LLM Wiki")
        self.assertIn("核心要义", page.body)

    def test_read_public_page_rejects_raw_and_path_traversal(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)

            with self.assertRaises(ValueError):
                read_public_page(root, "raw/secret.md")

            with self.assertRaises(ValueError):
                read_public_page(root, "../wiki/concepts/LLM Wiki.md")


if __name__ == "__main__":
    unittest.main()
