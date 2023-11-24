from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import get_relative_path
from Screens.Manager.UI import setupUi
import App.State as State

def ManagerScreen(parent):
    frame = QtWidgets.QFrame()
    components = setupUi(frame)
    odjavi_se_button: QtWidgets.QPushButton = components["odjavi_se_button"]
    zaposleni_button: QtWidgets.QPushButton = components["zaposleni_button"]
    name_label: QtWidgets.QLabel = components["name_label"]
    user_data_button: QtWidgets.QPushButton = components["user_data_button"]
    data_button: QtWidgets.QPushButton = components["data_button"]
    
    def odjavi_se_button_click():
        State.user = None
        parent.show_screen("unregistered")
    odjavi_se_button.clicked.connect(odjavi_se_button_click)

    def zaposleni_button_click():
        parent.show_screen("employees")
    zaposleni_button.clicked.connect(zaposleni_button_click)

    def user_data_button_click():
        parent.show_screen("user_data")
    user_data_button.clicked.connect(user_data_button_click)

    def data_button_click():
        parent.show_screen("data")
    data_button.clicked.connect(data_button_click)

    
    
    def showEvent(event):
        name_label.setText(f"Zdravo, {State.user.ime} {State.user.prezime}")
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    return frame