import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Layout")
        self.setWindowIcon(QIcon("LOGO.ico"))
        self.setStyleSheet("background-color: #ccc")
        
        vbox = QVBoxLayout()

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)
        btn3 = QPushButton("Button 3", self)
        btn4 = QPushButton("Button 4", self)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)

        self.show()
    

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

