from dataclasses import dataclass
from typing import Callable, TypeAlias

from tic_tac_toe.game.players import Player

# from frontends.console.renderers import Renderer
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Grid, Mark
from tic_tac_toe.logic.validators import validate_players


ErrorHandler: TypeAlias = Callable[[Exception], None]


@dataclass(frozen=True)
class TicTacToe:
    player1: Player
    player2: Player
    renderer: any
    starting_mark: Mark = Mark("X")
    game_state: GameState = GameState(Grid(), Mark("X"))
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        validate_players(self.player1, self.player2)

    @property
    def gamestate(self) -> GameState:
        return GameState(self.game_state.grid, self.starting_mark)

    def play(self, starting_mark: Mark = Mark("X")) -> None:
        game_state = GameState(Grid(), starting_mark)
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)

    def get_current_player(self, game_state: GameState) -> Player:
        if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2
