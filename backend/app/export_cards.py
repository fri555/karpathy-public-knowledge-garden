from pathlib import Path

from app.content import write_cards_json, write_pages_json


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    cards_output_path = project_root / "frontend" / "public" / "cards" / "today.json"
    pages_output_path = project_root / "frontend" / "public" / "pages" / "index.json"
    write_cards_json(project_root, cards_output_path)
    write_pages_json(project_root, pages_output_path)
    print(f"Wrote {cards_output_path}")
    print(f"Wrote {pages_output_path}")


if __name__ == "__main__":
    main()
