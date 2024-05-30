import unittest

from fastapi.testclient import TestClient

from app import app


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_invalid_api_key(self):
        response = self.client.get(
            "/api/v1/flights/FL123", headers={"X-API-KEY": "invalid_key"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {"detail": "Forbidden"})


if __name__ == "__main__":
    unittest.main()
