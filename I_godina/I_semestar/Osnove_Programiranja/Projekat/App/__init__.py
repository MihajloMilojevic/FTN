from App.State import db
from PyQt5.QtWidgets import QApplication
from Screens.Main import MainScreen
import sys

class App:
    def __init__(self) -> None:
        db.load()
    def run(self):
        app = QApplication(sys.argv)
        main_screen = MainScreen()
        main_screen.show()
        code = app.exec_()
        db.save()
        sys.exit(code)
