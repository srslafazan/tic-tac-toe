import unittest

from flask.testing import FlaskClient

from api.app import app


class TestAPIMoveHuman(unittest.TestCase):
    def setUp(self):
        self.client = FlaskClient(app)

    def test_move_game_over(self):
        response = self.client.put(
            "/games",
            json={
                "gamestate": {"grid": {"cells": "X XOO    "}, "starting_mark": "X"},
                "move": {"move_type": "human", "cell_index": 1},
            },
        )

        expected_response = {
            "after_state": {
                "current_mark": "O",
                "game_not_started": False,
                "game_over": True,
                "grid": {"cells": "XXXOO    "},
                "possible_moves": [],
                "starting_mark": "X",
                "tie": False,
                "winner": "X",
                "winning_cells": [0, 1, 2],
            },
            "before_state": {
                "current_mark": "X",
                "game_not_started": False,
                "game_over": False,
                "grid": {"cells": "X XOO    "},
                "possible_moves": [
                    {
                        "after_state": {
                            "grid": {"cells": "XXXOO    "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X XOO    "},
                            "starting_mark": "X",
                        },
                        "cell_index": 1,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X XOOX   "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X XOO    "},
                            "starting_mark": "X",
                        },
                        "cell_index": 5,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X XOO X  "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X XOO    "},
                            "starting_mark": "X",
                        },
                        "cell_index": 6,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X XOO  X "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X XOO    "},
                            "starting_mark": "X",
                        },
                        "cell_index": 7,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X XOO   X"},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X XOO    "},
                            "starting_mark": "X",
                        },
                        "cell_index": 8,
                        "mark": "X",
                    },
                ],
                "starting_mark": "X",
                "tie": False,
                "winner": None,
                "winning_cells": [],
            },
            "cell_index": 1,
            "mark": "X",
        }
        self.assertEqual(response.get_json(), expected_response)

    def test_move_game_in_progress(self):
        response = self.client.put(
            "/games",
            json={
                "gamestate": {"grid": {"cells": "X    O   "}, "starting_mark": "X"},
                "move": {"move_type": "human", "cell_index": 2},
            },
        )
        expected_response = {
            "after_state": {
                "current_mark": "O",
                "game_not_started": False,
                "game_over": False,
                "grid": {"cells": "X X  O   "},
                "possible_moves": [
                    {
                        "after_state": {
                            "grid": {"cells": "XOX  O   "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X X  O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 1,
                        "mark": "O",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X XO O   "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X X  O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 3,
                        "mark": "O",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X X OO   "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X X  O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 4,
                        "mark": "O",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X X  OO  "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X X  O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 6,
                        "mark": "O",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X X  O O "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X X  O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 7,
                        "mark": "O",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X X  O  O"},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X X  O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 8,
                        "mark": "O",
                    },
                ],
                "starting_mark": "X",
                "tie": False,
                "winner": None,
                "winning_cells": [],
            },
            "before_state": {
                "current_mark": "X",
                "game_not_started": False,
                "game_over": False,
                "grid": {"cells": "X    O   "},
                "possible_moves": [
                    {
                        "after_state": {
                            "grid": {"cells": "XX   O   "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X    O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 1,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X X  O   "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X    O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 2,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X  X O   "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X    O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 3,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X   XO   "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X    O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 4,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X    OX  "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X    O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 6,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X    O X "},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X    O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 7,
                        "mark": "X",
                    },
                    {
                        "after_state": {
                            "grid": {"cells": "X    O  X"},
                            "starting_mark": "X",
                        },
                        "before_state": {
                            "grid": {"cells": "X    O   "},
                            "starting_mark": "X",
                        },
                        "cell_index": 8,
                        "mark": "X",
                    },
                ],
                "starting_mark": "X",
                "tie": False,
                "winner": None,
                "winning_cells": [],
            },
            "cell_index": 2,
            "mark": "X",
        }
        self.assertEqual(response.get_json(), expected_response)


if __name__ == "__main__":
    unittest.main()
