import unittest
from pathlib import Path


FRONTEND_APP = Path(__file__).resolve().parents[2] / "frontend" / "src" / "App.vue"


class FrontendContractTests(unittest.TestCase):
    def test_next_card_uses_random_selection(self) -> None:
        source = FRONTEND_APP.read_text(encoding="utf-8")

        self.assertIn("function goToRandomCard(", source)
        self.assertIn("function nextCard() {\n  goToRandomCard();\n}", source)


if __name__ == "__main__":
    unittest.main()
