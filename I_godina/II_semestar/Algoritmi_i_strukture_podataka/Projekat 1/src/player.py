class Player:
    WHITE = 0
    BLACK = 1
    def __init__(self) -> None:
        self.player = Player.WHITE
    
    def change_player(self):
        self.player = 1 - self.player

    def is_white(self):
        return self.player == Player.WHITE
    def is_black(self):
        return self.player == Player.BLACK