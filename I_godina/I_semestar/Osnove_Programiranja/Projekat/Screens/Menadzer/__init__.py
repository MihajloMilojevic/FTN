from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import GetRelativePath
from Screens.Menadzer.UI import setupUi
import App.State as State

def MenadzerScreen(parent):
    frame = QtWidgets.QFrame()
    components = setupUi(frame)
    odjavi_se_button: QtWidgets.QPushButton = components["odjavi_se_button"]
    zaposleni_button: QtWidgets.QPushButton = components["zaposleni_button"]
    name_label: QtWidgets.QLabel = components["name_label"]
    
    def odjavi_se_button_click():
        State.user = None
        parent.show_screen("unregistered")
    odjavi_se_button.clicked.connect(odjavi_se_button_click)

    def zaposleni_button_click():
        parent.show_screen("employees")
    zaposleni_button.clicked.connect(zaposleni_button_click)

    
    def showEvent(event):
        name_label.setText(f"Zdravo, {State.user.ime} {State.user.prezime}")
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    return frame