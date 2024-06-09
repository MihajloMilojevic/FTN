from copy import deepcopy
class History:
    def __init__(self, state) -> None:
        self.state = state
        self.records: list[Record] = []
    def insert(self, records: list['Record']):
        self.records.append(records)
    def undo(self) -> list['Record']:
        if len(self.records) == 0:
            return None
        return self.records.pop()
    
class Record:
    def __init__(self, state, from_cell, to_cell=None, over_cell = None, over_piece=None) -> None:
        self.from_cell = from_cell
        self.to_cell = to_cell
        self.over_cell = over_cell
        self.over_piece = over_piece
        self.piece = state.pieces[from_cell[0]][from_cell[1]]
        self.current_player = state.player.player
        self.number_white_queens = state.number_white_queens
        self.number_black_queens = state.number_black_queens
        self.number_white_pieces = state.number_white_pieces
        self.number_black_pieces = state.number_black_pieces
        self.white_defences = state.white_defences
        self.black_defences = state.black_defences
        self.heuristic = state.heuristic
        self.current_player_moves = state.current_player_moves
        self.white_positions = state.white_positions.copy()
        self.black_positions = state.black_positions.copy()
        # self.current_player_moves = deepcopy(state.current_player_moves)
