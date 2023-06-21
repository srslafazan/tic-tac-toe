from __future__ import annotations

import enum
import random
import re

from dataclasses import dataclass
from functools import cached_property

from tic_tac_toe.logic.exceptions import InvalidMove, UnknownGameScore
from tic_tac_toe.logic.validators import validate_game_state, validate_grid


WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?..",
)


class Mark(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> Mark:
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT


@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    # TODO - validation
    def __post_init__(self) -> None:
        validate_grid(self)

    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")

    @cached_property
    def o_count(self) -> int:
        return self.cells.count("O")

    @cached_property
    def empty_count(self) -> int:
        return self.cells.count(" ")


class MoveType(str, enum.Enum):
    human = "human"
    minimax = "minimax"
    random = "random"


@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

    def to_dict(self):
        return {
            "mark": self.mark,
            "cell_index": self.cell_index,
            "before_state": self.before_state.to_dict(),
            "after_state": self.after_state.to_dict(),
        }


@dataclass(frozen=True)
class GameState:
    grid: Grid
    starting_mark: Mark = Mark("X")

    def __post_init__(self) -> None:
        validate_game_state(self)

    @cached_property
    def current_mark(self) -> Mark:
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        else:
            return self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.empty_count == 9

    @cached_property
    def tie(self) -> bool:
        return self.winner is None and self.grid.empty_count == 0

    @cached_property
    def game_over(self) -> bool:
        return self.winner is not None or self.tie

    @cached_property
    def winner(self) -> Mark | None:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None

    @cached_property
    def winning_cells(self) -> list[int]:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [match.start() for match in re.finditer(r"\?", pattern)]
        return []

    @cached_property
    def possible_moves(self) -> list[Move]:
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))
        return moves

    def make_move(self, move_type: MoveType, index: int) -> Move:
        match move_type:
            case MoveType.human:
                return self.make_move_to(index)
            case MoveType.minimax:
                return self.make_best_move()
            case MoveType.random:
                return self.make_random_move()
            case _:
                raise ValueError("Invalid move type")

    def make_move_to(self, index: int) -> Move:
        if self.grid.cells[index] != " ":
            raise InvalidMove("Cell is not empty")
        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=GameState(
                Grid(
                    self.grid.cells[:index]
                    + self.current_mark
                    + self.grid.cells[index + 1 :]
                ),
                self.starting_mark,
            ),
        )

    def make_best_move(self) -> Move | None:
        from tic_tac_toe.logic.minimax import find_best_move

        return find_best_move(self)

    def to_dict(self):
        return {
            "grid": self.grid,
            "starting_mark": self.starting_mark,
            "current_mark": self.current_mark,
            "game_not_started": self.game_not_started,
            "tie": self.tie,
            "game_over": self.game_over,
            "winner": self.winner,
            "winning_cells": self.winning_cells,
            "possible_moves": self.possible_moves,
        }

    def make_random_move(self) -> Move | None:
        try:
            return random.choice(self.possible_moves)
        except IndexError:
            return None

    def evaluate_score(self, mark: Mark) -> int:
        if self.game_over:
            if self.tie:
                return 0
            if self.winner is mark:
                return 1
            else:
                return -1
        raise UnknownGameScore("Game is not over yet")
