from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import get_relative_path
from Screens.Unregistered.UI import setupUi

def UnregisteredScreen(parent):
    frame = QtWidgets.QFrame()

    components = setupUi(frame)
    prijavi_se_button = components["prijavi_se_button"]
    registruj_se_button = components["registruj_se_button"]

    def prijavi_se_button_click():
        parent.show_screen("login")
    def registruj_se_button_click():
        parent.show_screen("register")

    prijavi_se_button.clicked.connect(prijavi_se_button_click)
    registruj_se_button.clicked.connect(registruj_se_button_click)

    return frame