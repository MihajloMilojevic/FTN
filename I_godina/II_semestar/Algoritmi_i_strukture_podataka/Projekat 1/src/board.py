import pygame as pg
from src.constants import Constants

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = pg.Surface((Constants.CELL_COUNT * Constants.CELL_SIZE, Constants.CELL_COUNT * Constants.CELL_SIZE))
        self.board.fill(Constants.BOARD_COLOR)
        for row in range(Constants.CELL_COUNT):
            for col in range(Constants.CELL_COUNT):
                if (row + col) % 2 == 0:
                    pg.draw.rect(
                        self.board, 
                        Constants.BG_COLOR, 
                        (
                            col * Constants.CELL_SIZE, 
                            row * Constants.CELL_SIZE, 
                            Constants.CELL_SIZE, 
                            Constants.CELL_SIZE)
                    )

    def draw(self):
        self.screen.blit(self.board, self.board.get_rect())