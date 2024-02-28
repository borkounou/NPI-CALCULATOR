import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestCalculatorAPI(unittest.TestCase):
    def test_get_data(self):
        response = client.get("/api/calculator")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.headers["Content-Type"] == "text/csv")

    def test_compute_data(self):
        payload = {"expression": "2 3 +"}
        response = client.post("/api/calculator", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("result", response.json())

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
