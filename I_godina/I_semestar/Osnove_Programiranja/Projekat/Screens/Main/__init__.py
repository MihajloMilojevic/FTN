from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from Utils.GetPath import GetRelativePath

class MainScreen(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(GetRelativePath(["Screens", "Main", "MainScreenDesign.ui"]), self)