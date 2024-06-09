from src.hints import draw_hints
from src.cell_state import CellState
from src.hints import clear_hints, draw_hints, calcuate_jumps, calucate_moves
from src.constants import Constants


def white_click_handler(game, row: int, col: int):
    # if black piece is clicked no need to do anything
    if game.state.pieces[row][col] in [CellState.BLACK, CellState.BLACK_QUEEN]:
        return
    play(game, row, col)

def black_click_handler(game, row: int, col: int):
    # if black piece is clicked no need to do anything
    if game.state.pieces[row][col] in [CellState.WHITE, CellState.WHITE_QUEEN]:
        return
    play(game, row, col)

def play(game, row, col):
    # print(game.state.current_player_moves)
    # make a move
    if game.state.selected is not None:
        if game.state.pieces[row][col] == CellState.MOVE:
            game.state.make_move(game.state.selected, (row, col))
            clear_hints(game.state)
            return
        if game.state.pieces[row][col] == CellState.JUMP:
            
            for move in game.state.current_player_moves[game.state.selected[0], game.state.selected[1]]:
                if move[0] == row and move[1] == col:
                    game.state.make_move(game.state.selected, None, move[2])
            clear_hints(game.state)
            return
    game.state.selected = (row, col)
    clear_hints(game.state)
    if (row, col) in game.state.current_player_moves:
        draw_hints(game.state, game.state.current_player_moves[row, col])