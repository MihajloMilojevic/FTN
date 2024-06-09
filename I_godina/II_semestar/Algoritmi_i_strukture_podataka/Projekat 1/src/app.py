from typing import Any
from src.game import Checkers
from PyQt5 import QtCore, QtGui, QtWidgets
from src.constants import Constants 

# so that we can access the game instance from anywhere
class State:
    game = None

class App(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi()
        self.play_btn.clicked.connect(self.play)
        self.setVisible(True)

    def play(self):
        force = self.force_jump_cb.isChecked()
        if self.one_player_rb.isChecked():
            State.game = Checkers(Checkers.SINGLE_PLAYER, force)
        else:
            State.game = Checkers(Checkers.TWO_PLAYERS, force)
        self.setVisible(False)
        State.game.run(self.onEnd, self.onClose)

    def onEnd(self, game: Any):
        print("onEnd called")
        self.setVisible(True)
        if game.state.player.is_black():
            self.winner_label.setText("White Wins")
        else:
            self.winner_label.setText("Black Wins")
        State.game = None

    def onClose(self):
        print("onClose called")
        self.setVisible(True)
        self.winner_label.setText("Game Closed")
        State.game = None

    def setupUi(self):
        self.setWindowIcon(QtGui.QIcon(Constants.ICON_PATH))
        self.resize(500, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(500, 450)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setFont(font)
        self.setStyleSheet("background: rgb(73,73,73); color: white")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 511, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.one_player_rb = QtWidgets.QRadioButton(self)
        self.one_player_rb.setGeometry(QtCore.QRect(50, 220, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.one_player_rb.setFont(font)
        self.one_player_rb.setObjectName("one_player_rb")
        self.two_players_rb = QtWidgets.QRadioButton(self)
        self.two_players_rb.setGeometry(QtCore.QRect(280, 220, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.two_players_rb.setFont(font)
        self.two_players_rb.setChecked(True)
        self.two_players_rb.setObjectName("two_players_rb")
        self.play_btn = QtWidgets.QPushButton(self)
        self.play_btn.setGeometry(QtCore.QRect(160, 350, 171, 61))
        self.force_jump_cb = QtWidgets.QCheckBox(self)
        self.force_jump_cb.setGeometry(QtCore.QRect(50, 280, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.force_jump_cb.setFont(font)
        self.force_jump_cb.setObjectName("force_jump_cb")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.play_btn.setFont(font)
        self.play_btn.setStyleSheet("background: white; color: black; border: 1px solid rgb(200, 200, 200);")
        self.play_btn.setFlat(False)
        self.play_btn.setObjectName("play_btn")
        self.winner_label = QtWidgets.QLabel(self)
        self.winner_label.setGeometry(QtCore.QRect(0, 110, 511, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.winner_label.setFont(font)
        self.winner_label.setAlignment(QtCore.Qt.AlignCenter)
        self.winner_label.setObjectName("winner_label")

        self.setWindowTitle("Checkers")
        self.label.setText("CHECKERSSSSS")
        self.winner_label.setText("Select Mode")
        self.one_player_rb.setText("One Player")
        self.two_players_rb.setText("Two Players")
        self.force_jump_cb.setText("Force Jump?")
        self.play_btn.setText("PLAY")

