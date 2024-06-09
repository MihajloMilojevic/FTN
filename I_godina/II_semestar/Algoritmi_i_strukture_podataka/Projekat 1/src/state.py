import pygame as pg
from src.hints import calucate_moves, calcuate_jumps, clear_hints
from src.cell_state import CellState
from src.constants import Constants
from src.player import Player
from src.history import History, Record
from src.cache import moves

class GameState:
    def __init__(self, screen, force_jump = False):
        self.screen = screen
        self.winner = None
        self.player = Player()
        self.selected = None
        self.pieces = [
            [CellState.EMPTY, CellState.BLACK, CellState.EMPTY, CellState.BLACK, CellState.EMPTY, CellState.BLACK, CellState.EMPTY, CellState.BLACK],
            [CellState.BLACK, CellState.EMPTY, CellState.BLACK, CellState.EMPTY, CellState.BLACK, CellState.EMPTY, CellState.BLACK, CellState.EMPTY],
            [CellState.EMPTY, CellState.BLACK, CellState.EMPTY, CellState.BLACK, CellState.EMPTY, CellState.BLACK, CellState.EMPTY, CellState.BLACK],
            [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
            [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
            [CellState.WHITE, CellState.EMPTY, CellState.WHITE, CellState.EMPTY, CellState.WHITE, CellState.EMPTY, CellState.WHITE, CellState.EMPTY],
            [CellState.EMPTY, CellState.WHITE, CellState.EMPTY, CellState.WHITE, CellState.EMPTY, CellState.WHITE, CellState.EMPTY, CellState.WHITE],
            [CellState.WHITE, CellState.EMPTY, CellState.WHITE, CellState.EMPTY, CellState.WHITE, CellState.EMPTY, CellState.WHITE, CellState.EMPTY]
        ]
        self.number_white_queens = 0
        self.number_black_queens = 0
        self.number_white_pieces = 12
        self.number_black_pieces = 12
        self.white_defences = 9
        self.black_defences = 9
        self.white_positions: set[tuple] = {(5, 0), (5, 2), (5, 4), (5, 6), (6, 1), (6, 3), (6, 5), (6, 7), (7, 0), (7, 2), (7, 4), (7, 6)}
        self.black_positions: set[tuple] = {(0, 1), (0, 3), (0, 5), (0, 7), (1, 0), (1, 2), (1, 4), (1, 6), (2, 1), (2, 3), (2, 5), (2, 7)}
        self.current_player_moves = {(5, 0): {(4, 1, None)}, (5, 2): {(4, 1, None), (4, 3, None)}, (5, 4): {(4, 3, None), (4, 5, None)}, (5, 6): {(4, 5, None), (4, 7, None)}}
        self.history = History(self)
        self.heuristic = self.calucalte_heuristic()
        self.force_jump = force_jump




    def draw(self):
        for row_index in range(Constants.CELL_COUNT):
            for cell_index in range(Constants.CELL_COUNT):
                if self.pieces[row_index][cell_index] == CellState.EMPTY:
                    continue
                radius = Constants.PIECE_SIZE
                center_x = cell_index * Constants.CELL_SIZE + Constants.CELL_SIZE // 2
                center_y = row_index * Constants.CELL_SIZE + Constants.CELL_SIZE // 2
                isCurrentPlayer = False
                isQueen = self.pieces[row_index][cell_index] in [CellState.WHITE_QUEEN, CellState.BLACK_QUEEN]
                if self.pieces[row_index][cell_index] in [CellState.WHITE, CellState.WHITE_QUEEN]:
                    color = Constants.WHITE_COLOR
                    queen_color = Constants.WHITE_QUEEN_COLOR
                    if self.player.is_white():
                        isCurrentPlayer = True
                elif self.pieces[row_index][cell_index] in [CellState.BLACK, CellState.BLACK_QUEEN]:
                    color = Constants.BLACK_COLOR
                    queen_color = Constants.BLACK_QUEEN_COLOR
                    if self.player.is_black():
                        isCurrentPlayer = True
                elif self.pieces[row_index][cell_index] == CellState.MOVE:
                    color = (0, 0, 200)
                    radius = Constants.MOVE_JUMP_SIZE
                elif self.pieces[row_index][cell_index] == CellState.JUMP:
                    color = (0, 200, 0)
                    radius = Constants.MOVE_JUMP_SIZE
                pg.draw.circle(
                    self.screen, 
                    color, 
                    (center_x, center_y),   
                    radius
                )
                if isQueen:
                    pg.draw.circle(
                        self.screen, 
                        queen_color, 
                        (center_x, center_y),   
                        Constants.QUEEN_SIZE
                    )
                if isCurrentPlayer:
                    pg.draw.circle(
                        self.screen, 
                        (0, 255, 255), 
                        (center_x, center_y),   
                        radius,
                        2
                    )
    def __str__(self) -> str:
        return "".join(map(lambda r: "".join(map(lambda x: str(x), r)), self.pieces)) + str(self.player.player)

    def calucalte_heuristic(self):
        whites = [0, 0, 0, 0, 0, 0, 0]
        blackes = [0, 0, 0, 0, 0, 0, 0]

        for r in range(8):
            for c in range(8):
                checker = self.pieces[r][c]
                if checker == CellState.EMPTY:
                    continue
                if checker in [CellState.WHITE, CellState.WHITE_QUEEN]:
                    if checker == CellState.WHITE:
                        whites[0] += 1
                    else:
                        whites[1] += 1
                    if r == 7:
                        whites[2] += 1
                        whites[6] += 1
                        continue
                    if r == 3 or r == 4:
                        if 2 <= c <= 5:
                            whites[3] += 1
                        else:
                            whites[4] += 1
                    if r > 0 and 0 < c < 7:
                        if self.pieces[r - 1][c - 1] in [CellState.BLACK, CellState.BLACK_QUEEN] and self.pieces[r + 1][c + 1] == CellState.EMPTY:
                            whites[5] += 1
                        if self.pieces[r - 1][c + 1] in [CellState.BLACK, CellState.BLACK_QUEEN] and self.pieces[r + 1][c - 1] == CellState.EMPTY:
                            whites[5] += 1
                    if r < 7:
                        if c == 0 or c == 7:
                            whites[6] += 1
                        elif (self.pieces[r + 1][c - 1] in [CellState.WHITE, CellState.WHITE_QUEEN] or self.pieces[r + 1][c - 1] not in [CellState.BLACK_QUEEN, CellState.WHITE_QUEEN]) and \
                        (self.pieces[r + 1][c + 1] in [CellState.WHITE, CellState.WHITE_QUEEN] or self.pieces[r + 1][c + 1] not in [CellState.BLACK_QUEEN, CellState.WHITE_QUEEN]):
                            whites[6] += 1
                else:
                    if checker == CellState.BLACK:
                        blackes[0] += 1
                    else:
                        blackes[1] += 1
                    if r == 0:
                        blackes[2] += 1
                        blackes[6] += 1
                        continue
                    if r == 3 or r == 4:
                        if 2 <= c <= 5:
                            blackes[3] += 1
                        else:
                            blackes[4] += 1
                    if r < 7 and 0 < c < 7:
                        if self.pieces[r + 1][c - 1] in [CellState.WHITE, CellState.WHITE_QUEEN] and self.pieces[r - 1][c + 1] == CellState.EMPTY:
                            blackes[5] += 1
                        if self.pieces[r + 1][c + 1] in [CellState.WHITE, CellState.WHITE_QUEEN] and self.pieces[r - 1][c - 1] == CellState.EMPTY:
                            blackes[5] += 1
                    if r > 0:
                        if c == 0 or c == 7:
                            blackes[6] += 1
                        elif (self.pieces[r - 1][c - 1] in [CellState.BLACK, CellState.BLACK_QUEEN] or self.pieces[r - 1][c - 1] not in [CellState.BLACK_QUEEN, CellState.WHITE_QUEEN]) and \
                        (self.pieces[r - 1][c + 1] in [CellState.BLACK, CellState.BLACK_QUEEN] or self.pieces[r - 1][c + 1] not in [CellState.BLACK_QUEEN, CellState.WHITE_QUEEN]):
                            blackes[6] += 1
        weights = [5, 7.5, 4, 2.5, 0.5, -3, 3]
        score = 0
        for i in range(7):
            score += weights[i] * (blackes[i] - whites[i])
        return score
                        
                        
    def make_move(self, from_cell, to_cell=None, path=None):
        if path is None:
            records = [Record(self, from_cell, to_cell)]
            self.__move_piece(from_cell, to_cell)
        else:
            records = self.__jump_path(from_cell, path)
        self.history.insert(records)
        self.player.change_player()
        clear_hints(self)
        from_cache = moves.get(str(self))
        self.calculacte_moves()
        self.heuristic = self.calucalte_heuristic()
        moves.put(str(self), str((self.current_player_moves, self.heuristic)))
        # if from_cache is None:
        #     self.calculacte_moves()
        #     self.heuristic = self.calucalte_heuristic()
        #     moves.put(str(self), str((self.current_player_moves, self.heuristic)))
        # else:
        #     current_moves, heuristic = eval(from_cache)
        #     self.current_player_moves = current_moves
        #     self.heuristic = heuristic

    def undo_move(self):
        moves: list['Record'] = self.history.undo()
        if moves is None:
            return
        i = len(moves) - 1
        while i >= 0:
            record = moves[i]
            self.number_white_queens = record.number_white_queens
            self.number_black_queens = record.number_black_queens
            self.number_white_pieces = record.number_white_pieces
            self.number_black_pieces = record.number_black_pieces
            self.white_defences = record.white_defences
            self.black_defences = record.black_defences
            self.white_positions = record.white_positions
            self.black_positions = record.black_positions
            self.current_player_moves = record.current_player_moves
            self.player.player = record.current_player
            self.heuristic = record.heuristic
            from_row, from_col = record.from_cell
            to_row, to_col = record.to_cell
            # if record.piece in [CellState.WHITE, CellState.WHITE_QUEEN]:
            #     try:
            #         self.white_positions.remove((to_row, to_col))
            #     except KeyError:
            #         pass
            #     self.white_positions.add((from_row, from_col))
            # elif record.piece in [CellState.BLACK, CellState.BLACK_QUEEN]:
            #     try:
            #         self.black_positions.remove((to_row, to_col))
            #     except KeyError:
            #         pass
            #     self.black_positions.add((from_row, from_col))
            self.pieces[to_row][to_col] = CellState.EMPTY
            self.pieces[from_row][from_col] = record.piece
            #print(record.piece)
            if(record.over_cell is not None and record.over_piece is not None):
                self.pieces[record.over_cell[0]][record.over_cell[1]] = record.over_piece
            i -= 1
        # print(self.current_player_moves)
        self.selected = None
        clear_hints(self)
    # all of the unnecessary calculations are for quicker calucation of the heuristic

    def __delete_piece(self, row, col):
        if self.pieces[row][col] == CellState.WHITE:
            self.number_white_pieces -= 1
            self.white_positions.remove((row, col))
            self.white_defences = self.__calculate_defence(7)
        elif self.pieces[row][col] == CellState.BLACK:
            self.number_black_pieces -= 1
            self.black_positions.remove((row, col))
            self.white_defences = self.__calculate_defence(0)
        elif self.pieces[row][col] == CellState.WHITE_QUEEN:
            self.number_white_queens -= 1
            self.white_positions.remove((row, col))
            self.white_defences = self.__calculate_defence(7)
        elif self.pieces[row][col] == CellState.BLACK_QUEEN:
            self.number_black_queens -= 1
            self.black_positions.remove((row, col))
            self.white_defences = self.__calculate_defence(0)
        self.pieces[row][col] = CellState.EMPTY

    def __promote_piece(self, row, col):

        if self.pieces[row][col] == CellState.WHITE:
            self.pieces[row][col] = CellState.WHITE_QUEEN
            self.number_white_queens += 1
            self.number_white_pieces -= 1
        elif self.pieces[row][col] == CellState.BLACK:
            self.pieces[row][col] = CellState.BLACK_QUEEN
            self.number_black_queens += 1
            self.number_black_pieces -= 1
        
    def __move_piece(self, from_cell, to_cell):
        from_row, from_col = from_cell
        to_row, to_col = to_cell
        if self.pieces[from_row][from_col] in [CellState.WHITE, CellState.WHITE_QUEEN]:
            if to_row == 0:
                self.__promote_piece(from_row, from_col)
            self.white_positions.remove((from_row, from_col))
            self.white_positions.add((to_row, to_col))
            self.white_defences = self.__calculate_defence(7)
        elif self.pieces[from_row][from_col] in [CellState.BLACK, CellState.BLACK_QUEEN]:
            if to_row == 7:
                self.__promote_piece(from_row, from_col)
            self.black_positions.remove((from_row, from_col))
            self.black_positions.add((to_row, to_col))
            self.white_defences = self.__calculate_defence(0)
        self.pieces[to_row][to_col] = self.pieces[from_row][from_col]
        self.pieces[from_row][from_col] = CellState.EMPTY

    def __jump_path(self, from_cell, path):
        update = []
        for jump in path:
            new_record = self.__jump_piece(from_cell, jump)
            update.append(new_record)
            from_cell = jump
        return update

    def __jump_piece(self, from_cell, to_cell) -> Record:
        from_row, from_col = from_cell
        to_row, to_col = to_cell
        del_row = (from_row + to_row) // 2
        del_col = (from_col + to_col) // 2
        
        if from_col == 1 and to_col == 1:
            del_col = 0
        elif from_col == Constants.CELL_COUNT - 2 and to_col == Constants.CELL_COUNT - 2:
            del_col = Constants.CELL_COUNT - 1
        record = Record(self, from_cell, to_cell, (del_row, del_col), self.pieces[del_row][del_col])
        self.__delete_piece(del_row, del_col)
        self.__move_piece(from_cell, to_cell)
        return record

    def __calculate_defence(self, row):
        if row == 7:
            map(lambda x: x[1] == 0, self.white_positions)
            arr = list(filter(lambda x: x in [CellState.BLACK, CellState.BLACK_QUEEN], [
                    self.pieces[0][0], 
                    self.pieces[0][2],
                    self.pieces[0][4], 
                    self.pieces[0][6], 
                ]))
        else:
            arr = list(filter(lambda x: x in [CellState.WHITE, CellState.WHITE_QUEEN], [
                    self.pieces[7][1], 
                    self.pieces[7][3],
                    self.pieces[7][5], 
                    self.pieces[7][7],
                ]))
        return len(arr)
    def is_game_over(self):
        if (self.number_black_pieces + self.number_black_queens) == 0:
            return True
        if (self.number_white_pieces + self.number_white_queens) == 0:
            return True
        if len(self.current_player_moves) == 0:
            return True
        return False
        
    def calculacte_moves(self):
        if self.player.is_white():
            positions = self.white_positions
        else:
            positions = self.black_positions
        self.current_player_moves = {}
        all_moves = {}
        only_jumps = {}
        for position in positions:
            row, col = position 
            if not self.force_jump or len(only_jumps) == 0:
                moves = calucate_moves(self, row, col)
            else:
                moves = []
            jumps = calcuate_jumps(self, row, col)
            #print(f"Moves: {moves}, jumps: {jumps} for {position}")
            
            all_moves_for_position = set()
            only_jumps_for_position = set()
            for jump_cell, path in jumps.items():
                all_moves_for_position.add((jump_cell[0], jump_cell[1], tuple(path)))
                only_jumps_for_position.add((jump_cell[0], jump_cell[1], tuple(path)))
            if len(only_jumps_for_position) > 0:
                only_jumps[position] = only_jumps_for_position
            for move in moves:
                all_moves_for_position.add((move[0], move[1], None))
            if len(all_moves_for_position) > 0:
                #print(f"Calulated moves: {moves_for_position} for position: {position}")
                all_moves[position] = all_moves_for_position
        if len(only_jumps) > 0 and self.force_jump:
            self.current_player_moves = only_jumps
        else:
            self.current_player_moves = all_moves