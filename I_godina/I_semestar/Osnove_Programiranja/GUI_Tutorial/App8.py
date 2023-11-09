import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import uic

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("Design3.ui", self)
        self.show()
    

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

