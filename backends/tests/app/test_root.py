from importlib.metadata import distribution
import unittest
import json

from flask.testing import FlaskClient

from api.app import app


class TestAPIRoot(unittest.TestCase):
    def setUp(self):
        self.client = FlaskClient(app)
        self.version = distribution("api").version

    def get_version_string(self):
        data = {
            "application": "tic_tac_toe.api",
            "version": self.version,
        }
        string = json.dumps(data, separators=(",", ":")) + "\n"
        return bytes(string, "utf-8")

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            self.get_version_string(),
        )

    def test_version(self):
        response = self.client.get("/version")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            self.get_version_string(),
        )
