from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from Utils.GetPath import GetRelativePath
from Screens.Login import LoginScreen

class MainScreen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(GetRelativePath(["Screens", "Main", "MainScreenDesign.ui"]), self)
        self.setWindowIcon(QIcon(GetRelativePath(["LOGO.ico"])))
        self.get_components()
        self.add_functionality()
    
    def get_components(self):
        self.prijavi_se_button: QPushButton = self.findChild(QPushButton, "prijavi_se_button")

    def add_functionality(self):
        self.prijavi_se_button.clicked.connect(self.prijavi_se_button_click)

    def prijavi_se_button_click(self):
        self.hide()
        login_screen = LoginScreen()
        login_screen.exec_()
        self.show()