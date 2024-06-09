import os.path
from src.get_path import get_relative_path

class Constants:
    CELL_SIZE = 75
    CELL_COUNT = 8
    
    BG_COLOR = (118, 150, 86)
    BOARD_COLOR = (238, 238, 210)

    WHITE_COLOR = (170, 0, 0)
    WHITE_QUEEN_COLOR = (255, 0, 0)
    BLACK_COLOR = (73, 73, 73)
    BLACK_QUEEN_COLOR = (0, 0, 0)
    MOVE_COLOR = (0, 0, 200)
    JUMP_COLOR = (0, 200, 0)

    PIECE_SIZE = CELL_SIZE // 3
    QUEEN_SIZE = CELL_SIZE // 5
    MOVE_JUMP_SIZE = CELL_SIZE // 5

    ICON_PATH = get_relative_path(["assets", "checkers.png"])