import unittest

from flask.testing import FlaskClient

from api.app import app


class TestAPISanity(unittest.TestCase):
    def setUp(self):
        self.client = FlaskClient(app)

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, world!")
