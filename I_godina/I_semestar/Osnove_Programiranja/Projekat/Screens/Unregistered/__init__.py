from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import GetRelativePath
from Screens.Unregistered.UI import setupUi

def UnregisteredScreen(parent):
    frame = QtWidgets.QFrame()
    components = setupUi(frame)
    prijavi_se_button = components["prijavi_se_button"]
    def prijavi_se_button_click():
        parent.show_screen("login")
    prijavi_se_button: QtWidgets.QPushButton = frame.findChild(QtWidgets.QPushButton, "prijavi_se_button")
    prijavi_se_button.clicked.connect(prijavi_se_button_click)
    return frame