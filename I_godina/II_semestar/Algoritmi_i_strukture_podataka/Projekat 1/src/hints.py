
from src.constants import Constants
from src.cell_state import CellState


all_moves = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

def clear_hints(state):
    for row in range(Constants.CELL_COUNT):
        for col in range(Constants.CELL_COUNT):
            if state.pieces[row][col] == CellState.MOVE or state.pieces[row][col] == CellState.JUMP:
                state.pieces[row][col] = CellState.EMPTY

def draw_hints(state, moves):
    clear_hints(state)
    if moves is None:
        return
    for move in moves:
        # print(move)
        if move[2] is None:
            state.pieces[move[0]][move[1]] = CellState.MOVE
        else:
            state.pieces[move[0]][move[1]] = CellState.JUMP

def get_moves(piece=None):
    if piece is None:
        return []
    if piece == CellState.WHITE:
        return all_moves[-2:]
    if piece == CellState.BLACK:
        return all_moves[:2]
    return all_moves

def calucate_moves(state, row: int, col: int):
    pieces = state.pieces
    possible_moves = []
    moves = get_moves(pieces[row][col])
    for move in moves:
        #print(f"For: {row}, {col} move: {move}, piece: {pieces[row][col]}")
        new_row = row + move[0]
        new_col = col + move[1]
        if __valid_move(new_row, new_col) and pieces[new_row][new_col] == CellState.EMPTY:
            #print("Valid")
            possible_moves.append((new_row, new_col))
    return possible_moves

def calcuate_jumps(state, row: int, col: int, piece=None, previous_jumps=[], possible_jumps=None, deleted_pieces=[]):
    if piece is None:
        piece = state.pieces[row][col]
    if row == 0 and piece == CellState.WHITE:
        piece = CellState.WHITE_QUEEN
    if row == Constants.CELL_COUNT - 1 and piece == CellState.BLACK:
        piece = CellState.BLACK_QUEEN
    moves = get_moves(piece)
    if possible_jumps is None:
        possible_jumps = {}
    else:
        possible_jumps[(row, col)] = previous_jumps.copy()
    pieces = state.pieces
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if not __valid_move(new_row, new_col):
            continue
        oponent_pieces = [CellState.BLACK, CellState.BLACK_QUEEN] if state.player.is_white() else [CellState.WHITE, CellState.WHITE_QUEEN]
        # if the piece is already jumped over
        if (new_row, new_col) in deleted_pieces:
            continue
        # if the piece is oponent's, and we can jump over it
        if pieces[new_row][new_col] in oponent_pieces:
            test_row = new_row + move[0]
            test_col = new_col + move[1]
            # if the cell is empty, we can jump over it
            if __valid_move(test_row, test_col) and pieces[test_row][test_col] == CellState.EMPTY:
                # remove the oponent's piece (not really removing, just marking it so next jumps can't jump over it again)
                deleted_pieces.append((new_row, new_col))
                previous_jumps.append((test_row, test_col))
                # recursively check for more jumps
                calcuate_jumps(state, test_row, test_col, piece, previous_jumps, possible_jumps, deleted_pieces)
                previous_jumps.pop()
                deleted_pieces.pop()
    return possible_jumps

def __valid_move(row, col):
        return row >= 0 and col >= 0 and row < Constants.CELL_COUNT and col < Constants.CELL_COUNT