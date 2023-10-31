import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class WindowExample(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Buttons")
        self.setWindowIcon(QIcon("LOGO.ico"))
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        self.setStyleSheet("background-color: #ccc")
        

        self.create_buttons()

        self.show()
    def create_buttons(self):
        btn1 = QPushButton("Button 1", self)
        btn1.setGeometry(150, 100, 200, 100)
        btn1.setIcon(QIcon("LOGO.ico"))
        btn1.setStyleSheet("font-size: 30px; background-color: lime")
        btn1.clicked.connect(self.button_click(1))
        

        btn2 = QPushButton("Button 2", self)
        btn2.setGeometry(150, 300, 200, 100)
        btn2.setIcon(QIcon("LOGO.ico"))
        btn2.setStyleSheet("font-size: 30px; background-color: cyan")
        btn2.clicked.connect(self.button_click(2))
        
    def button_click(self, num):
        def click():
            print(f"Button {num} clicked")
        return click
    

app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())

