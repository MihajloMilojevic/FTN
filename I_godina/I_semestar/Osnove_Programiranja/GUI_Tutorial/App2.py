import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt5.QtGui import QIcon

class WindowExample(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Hello world")
        self.setWindowIcon(QIcon("LOGO.ico"))
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        # self.setWindowOpacity(0.75)
        self.setStyleSheet("background-color: #999999")
        self.show()
    

app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())
