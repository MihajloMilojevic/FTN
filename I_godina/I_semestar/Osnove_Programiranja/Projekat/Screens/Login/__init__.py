from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from Utils.GetPath import GetRelativePath


class LoginScreen(QDialog):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(GetRelativePath(["Screens", "Login", "LoginScreenDesign.ui"]), self)
        self.setWindowIcon(QIcon(GetRelativePath(["LOGO.ico"])))
        # self.get_components()
        # self.add_functionality()
    
    def get_components(self):
        pass

    def add_functionality(self):
        pass
