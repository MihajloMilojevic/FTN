import pygame as pg
from src.board import Board
from src.constants import Constants
from src.state import GameState
from src.cell_state import CellState
from src.hints import clear_hints
from src.click_event import white_click_handler, black_click_handler
from src.bot import make_bot_move, randomizer
import time

class Checkers:
    SINGLE_PLAYER = 1
    TWO_PLAYERS = 2
    def __init__(self, mode, force_jump = False) -> None:
        pg.init()
        pg.display.set_caption("Checkers")
        icon = pg.image.load(Constants.ICON_PATH)
        pg.display.set_icon(icon)
        self.screen = pg.display.set_mode((Constants.CELL_COUNT * Constants.CELL_SIZE, Constants.CELL_COUNT * Constants.CELL_SIZE))
        self.board = Board(self.screen)
        self.state = GameState(self.screen, force_jump)
        self.mode = mode
        self.bot_move = False
        # self.force_jump = force_jump
        #print(self.state)

    def run(self, onEnd, onClose):
        while True:
            try:
                if self.state.is_game_over():
                    print("Game Over")
                    self.state.winner = 1 - self.state.player.player
                    pg.quit()
                    onEnd(self)
                    return
                # to learn moves
                # if self.state.player.is_black():
                #     make_bot_move(self)
                # else:
                #     randomizer(self)
                # self.board.draw()
                # self.state.draw()
                # pg.display.update()
                # continue
                if self.bot_move:
                    start_time = time.perf_counter()
                    make_bot_move(self)
                    end_time = time.perf_counter()
                    elapsed_time = end_time - start_time
                    print("Elapsed time: ", elapsed_time)
                    self.bot_move = False
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        onClose()
                        return
                    if event.type == pg.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        row = y // Constants.CELL_SIZE
                        col = x // Constants.CELL_SIZE
                        #print((row, col))
                        self.handle_click(row, col)
                self.board.draw()
                self.state.draw()
                pg.display.update()
            except Exception as e:
                self.bot_move = False
                print(e)
                #raise e
            
    def undo(self):
        self.state.undo_move()
    
    def handle_click(self, row, col):
        #print("Clicked: ", (row, col))
        # if an empty cell is clicked no need to do anything
        if self.state.pieces[row][col] == CellState.EMPTY:
            clear_hints(self.state)
            self.state.selected = None
            return
        if self.state.player.is_white():
            white_click_handler(self, row, col)
            if self.state.player.is_black() and self.mode == Checkers.SINGLE_PLAYER:
                self.bot_move = True
        elif self.state.player.is_black() and self.mode != Checkers.SINGLE_PLAYER:
            black_click_handler(self, row, col)

    def evaluate(self):
        return self.state.calucalte_heuristic()