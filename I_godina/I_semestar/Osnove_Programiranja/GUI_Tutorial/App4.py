# Loading .ui file from designer

import typing
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore, uic
import sys

class UI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("Design1.ui", self)
        self.show()

        button = self.findChild(QPushButton, "pushButton")
        button.clicked.connect(self.click)
    def click(self):
        print("Button click")

app = QApplication(sys.argv)
window = UI()
sys.exit(app.exec_())