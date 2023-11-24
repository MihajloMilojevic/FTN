from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import get_relative_path
from Screens.Unregistered.UI import setupUi

def UnregisteredScreen(parent):
    frame = QtWidgets.QFrame()

    components = setupUi(frame)
    login_button = components["login_button"]
    register_button = components["register_button"]

    def login_button_click():
        parent.show_screen("login")
    def register_button_click():
        parent.show_screen("register")

    login_button.clicked.connect(login_button_click)
    register_button.clicked.connect(register_button_click)

    return frame