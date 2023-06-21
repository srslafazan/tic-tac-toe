import unittest

from flask.testing import FlaskClient

from src.app import app


class TestAPISanity(unittest.TestCase):
    def setUp(self):
        self.client = FlaskClient(app)

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, world!")


class TestAPIGames(unittest.TestCase):
    def setUp(self):
        self.client = FlaskClient(app)

    def test_create_game(self):
        response = self.client.post(
            "/games",
            json={"player1": "human", "player2": "human", "starting_mark": "X"},
        )
        expected_response = {"grid": {"cells": "         "}, "starting_mark": "X"}
        self.assertEqual(response.get_json(), expected_response)

    def test_move(self):
        response = self.client.put(
            "/games",
            json={
                "gamestate": {"grid": {"cells": "X    O   "}, "starting_mark": "X"},
                "move": {"move_type": "human", "cell_index": 2},
            },
        )
        expected_response = {
            "after_state": {"grid": {"cells": "X X  O   "}, "starting_mark": "X"},
            "before_state": {"grid": {"cells": "X    O   "}, "starting_mark": "X"},
            "cell_index": 2,
            "mark": "X",
        }
        self.assertEqual(response.get_json(), expected_response)


if __name__ == "__main__":
    unittest.main()
