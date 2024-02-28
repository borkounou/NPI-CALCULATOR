import unittest
from fastapi.testclient import TestClient 
import os 
import sys

MAIN_PATH = os.getenv("MAIN_PATH")
sys.path.append(MAIN_PATH)

from Backend.app.main import app

client = TestClient(app)


class TestCalculatorAPI(unittest.TestCase):

    def test_compute_data(self):
        payload = {"expression": "23 3 - 3 *"}
        response = client.post("/api/calculator", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("result", response.json())

if __name__ == '__main__':
    unittest.main()
