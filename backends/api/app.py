import re
from flask import Flask, request, jsonify
from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import MinimaxComputerPlayer, Player
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Grid, Mark, Move, MoveType


class DataRenderer:
    def render(self, game_state: GameState) -> GameState:
        return game_state


def grid_to_index(grid: str) -> int:
    if re.match(r"[abcABC][123]", grid):
        col, row = grid
    elif re.match(r"[123][abcABC]", grid):
        row, col = grid
    else:
        raise ValueError("Invalid grid coordinates")
    return 3 * (int(row) - 1) + (ord(col.upper()) - ord("A"))


class ClientPlayer(Player):
    def get_move(self, game_state: GameState) -> Move | None:
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"{self.mark}'s move: ").strip())
            except ValueError:
                print("Please provide coordinates in the form of A1 or 1A")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("That cell is already occupied.")
        return None


PLAYER_CLASSES = {
    "human": ClientPlayer,
    "minimax": MinimaxComputerPlayer,
}

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


"""
Creates a new game object.

Parameters:
    player1 (str): The name of the first player.
    player2 (str): The name of the second player.
    startingMark (str): The mark that the first player will use.

Returns:
    A JSON object with the following keys:
        player1: The name of the first player.
        player2: The name of the second player.
        startingMark: The mark that the first player will use.
"""


@app.route("/games", methods=["POST"])
def create_game():
    player1 = PLAYER_CLASSES[request.json["player1"]](Mark("X"))
    player2 = PLAYER_CLASSES[request.json["player2"]](Mark("O"))
    starting_mark = request.json["starting_mark"]
    game = TicTacToe(player1, player2, DataRenderer(), starting_mark)
    return jsonify(game.gamestate)


@app.route("/games", methods=["PUT"])
def move():
    # Options:
    # - Move Given and Player
    # - Move Given and Computer
    # - Move Not Given and Player -> Error
    # - Move Not Given and Computer -> Computer Move
    current_gamestate = GameState(
        Grid(request.json["gamestate"]["grid"]["cells"]),
        starting_mark=Mark(request.json["gamestate"]["starting_mark"]),
    )
    move_type = MoveType(request.json["move"]["move_type"])
    # print(current_gamestate)
    new_gamestate = current_gamestate.make_move(
        move_type, request.json["move"]["cell_index"]
    )
    return jsonify(new_gamestate)


if __name__ == "__main__":
    app.run(use_reloader=True)
