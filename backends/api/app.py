import os
from importlib.metadata import distribution
from flask import Flask, request, jsonify
from flask_cors import CORS
from tic_tac_toe.game.renderers import DataRenderer
from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import PLAYER_CLASSES
from tic_tac_toe.logic.models import (
    GameState,
    Grid,
    Mark,
    Move,
    MoveType,
)

app = Flask(__name__)

CORS(app)


@app.route("/")
def index():
    return jsonify(
        {
            "application": "tic_tac_toe.api",
            "version": distribution("api").version,
        }
    )


app.add_url_rule("/version", view_func=index)

"""
Creates a new game with initial state.

Parameters:
    player1 (str): The name of the first player.
    player2 (str): The name of the second player.
    starting_mark (str): The mark that the first player will use.
    game_state (str): The starting game state.

Returns:
    JSON serialized GameState.
"""


@app.route("/games", methods=["POST"])
def create_game():
    body = request.get_json()
    player1 = PLAYER_CLASSES[body.get("player1")](Mark("X"))
    player2 = PLAYER_CLASSES[body.get("player2")](Mark("O"))
    starting_mark = Mark(body.get("starting_mark"))
    game_state = GameState(Grid(body.get("game_state") or " " * 9), starting_mark)
    game = TicTacToe(player1, player2, DataRenderer(), starting_mark, game_state)
    return jsonify(game.gamestate.to_dict())


"""
Creates the next game state from the previous game state.

Parameters:
    gamestate (object): The current game state.
        grid (Grid)
        cells (str)
    move (object): The move to make.
        move_type (MoveType)
        cell_index (int)

Returns:
    JSON serialized Move.
"""


@app.route("/games", methods=["PUT"])
def move():
    # Options:
    # - Move Given for Player -> Player Move
    # - Move Given for Computer -> Player Move for Computer
    # - Move Not Given, Player Turn -> Error
    # - Move Not Given, Computer Turn -> Computer Move
    current_gamestate = GameState(
        Grid(request.json["gamestate"]["grid"]["cells"]),
        starting_mark=Mark(request.json["gamestate"]["starting_mark"]),
    )
    move_type = MoveType(request.json["move"]["move_type"])
    move: Move = current_gamestate.make_move(
        move_type, request.json["move"]["cell_index"]
    )
    return jsonify(move.to_dict())


if __name__ == "__main__":
    app.run(use_reloader=os.getenv("FLASK_USE_RELOADER") != "False")
