import unittest

from flask.testing import FlaskClient

from api.app import app

class TestAPICreateGame(unittest.TestCase):
    def setUp(self):
        self.client = FlaskClient(app)

    def test_create_game_empty(self):
        response = self.client.post(
            "/games",
            json={"player1": "human", "player2": "human", "starting_mark": "X"},
        )
        expected_response = expected_response = {
            "current_mark": "X",
            "game_not_started": True,
            "game_over": False,
            "grid": {"cells": "         "},
            "possible_moves": [
                {
                    "after_state": {
                        "grid": {"cells": "X        "},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
                        "starting_mark": "X",
                    },
                    "cell_index": 0,
                    "mark": "X",
                },
                {
                    "after_state": {
                        "grid": {"cells": " X       "},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
                        "starting_mark": "X",
                    },
                    "cell_index": 1,
                    "mark": "X",
                },
                {
                    "after_state": {
                        "grid": {"cells": "  X      "},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
                        "starting_mark": "X",
                    },
                    "cell_index": 2,
                    "mark": "X",
                },
                {
                    "after_state": {
                        "grid": {"cells": "   X     "},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
                        "starting_mark": "X",
                    },
                    "cell_index": 3,
                    "mark": "X",
                },
                {
                    "after_state": {
                        "grid": {"cells": "    X    "},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
                        "starting_mark": "X",
                    },
                    "cell_index": 4,
                    "mark": "X",
                },
                {
                    "after_state": {
                        "grid": {"cells": "     X   "},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
                        "starting_mark": "X",
                    },
                    "cell_index": 5,
                    "mark": "X",
                },
                {
                    "after_state": {
                        "grid": {"cells": "      X  "},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
                        "starting_mark": "X",
                    },
                    "cell_index": 6,
                    "mark": "X",
                },
                {
                    "after_state": {
                        "grid": {"cells": "       X "},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
                        "starting_mark": "X",
                    },
                    "cell_index": 7,
                    "mark": "X",
                },
                {
                    "after_state": {
                        "grid": {"cells": "        X"},
                        "starting_mark": "X",
                    },
                    "before_state": {
                        "grid": {"cells": "         "},
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
        }
        self.assertEqual(response.get_json(), expected_response)
