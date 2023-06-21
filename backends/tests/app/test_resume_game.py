import unittest

from flask.testing import FlaskClient

from api.app import app


class TestAPIResumeGame(unittest.TestCase):
    def setUp(self):
        self.client = FlaskClient(app)

    def test_resume_game(self):
        response = self.client.post(
            "/games",
            json={
                "player1": "human",
                "player2": "minimax",
                "starting_mark": "X",
                "game_state": " X O    X",
            },
        )
        expected_response = {
            "current_mark": "O",
            "game_not_started": False,
            "game_over": False,
            "grid": {"cells": " X O    X"},
            "possible_moves": [
                {
                    "after_state": {
                        "grid": {"cells": "OX O    X"},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": " X O    X"},
                        "starting_mark": "X",
                    },
                    "cell_index": 0,
                    "mark": "O",
                },
                {
                    "after_state": {
                        "grid": {"cells": " XOO    X"},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": " X O    X"},
                        "starting_mark": "X",
                    },
                    "cell_index": 2,
                    "mark": "O",
                },
                {
                    "after_state": {
                        "grid": {"cells": " X OO   X"},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": " X O    X"},
                        "starting_mark": "X",
                    },
                    "cell_index": 4,
                    "mark": "O",
                },
                {
                    "after_state": {
                        "grid": {"cells": " X O O  X"},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": " X O    X"},
                        "starting_mark": "X",
                    },
                    "cell_index": 5,
                    "mark": "O",
                },
                {
                    "after_state": {
                        "grid": {"cells": " X O  O X"},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": " X O    X"},
                        "starting_mark": "X",
                    },
                    "cell_index": 6,
                    "mark": "O",
                },
                {
                    "after_state": {
                        "grid": {"cells": " X O   OX"},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": " X O    X"},
                        "starting_mark": "X",
                    },
                    "cell_index": 7,
                    "mark": "O",
                },
            ],
            "starting_mark": "X",
            "tie": False,
            "winner": None,
            "winning_cells": [],
        }
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
