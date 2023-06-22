import argparse
from typing import NamedTuple

from tic_tac_toe.logic.models import Mark

from tic_tac_toe.game.players import (
    Player,
    PLAYER_CLASSES,
)

from .players import ConsolePlayer

PLAYER_CLASSES_CONSOLE = {
    **PLAYER_CLASSES,
    "human": ConsolePlayer,
}


class Args(NamedTuple):
    player1: Player
    player2: Player
    starting_mark: Mark


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-X",
        dest="player_x",
        choices=PLAYER_CLASSES_CONSOLE.keys(),
        default="human",
    )
    parser.add_argument(
        "-O",
        dest="player_o",
        choices=PLAYER_CLASSES_CONSOLE.keys(),
        default="minimax",
    )
    parser.add_argument(
        "--starting",
        dest="starting_mark",
        choices=Mark,
        type=Mark,
        default="X",
    )
    args = parser.parse_args()

    player1 = PLAYER_CLASSES_CONSOLE[args.player_x](Mark("X"))
    player2 = PLAYER_CLASSES_CONSOLE[args.player_o](Mark("O"))

    if args.starting_mark == "O":
        player1, player2 = player2, player1

    return Args(player1, player2, args.starting_mark)
