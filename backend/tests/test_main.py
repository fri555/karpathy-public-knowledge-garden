import unittest

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


class ApiEndpointTests(unittest.TestCase):
    def test_health_endpoint(self) -> None:
        response = client.get("/api/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "status": "ok",
                "service": "public-review-cards",
            },
        )

    def test_today_cards_endpoint(self) -> None:
        response = client.get("/api/cards/today")

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertGreaterEqual(len(body["cards"]), 1)
        self.assertIn("question", body["cards"][0])

    def test_pages_endpoint_lists_public_wiki_pages(self) -> None:
        response = client.get("/api/pages")

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertGreaterEqual(len(body["pages"]), 1)
        self.assertIn("path", body["pages"][0])

    def test_page_content_endpoint_returns_public_page(self) -> None:
        pages = client.get("/api/pages").json()["pages"]
        first_path = pages[0]["path"]

        response = client.get("/api/pages/content", params={"path": first_path})

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["path"], first_path)
        self.assertIn("body", body)


if __name__ == "__main__":
    unittest.main()
