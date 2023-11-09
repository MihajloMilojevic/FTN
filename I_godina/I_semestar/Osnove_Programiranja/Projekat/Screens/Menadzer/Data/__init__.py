from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import GetRelativePath
import App.State as State
import Database.Models as Models
from Screens.Menadzer.Data.UI import setupUi

def DataScreen(parent):
    frame = QtWidgets.QFrame()
    # frame.setMaximumHeight(1000)
    # frame.setMaximumWidth(1000)
    components = setupUi(frame)
    tab: QtWidgets.QTabWidget = components["tab"]
    back_button: QtWidgets.QPushButton = components["back_button"]
    def showEvent(event):
        tab.setCurrentIndex(0)
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    def back_button_click():
        parent.show_screen(State.user.uloga)
    back_button.clicked.connect(back_button_click)

    return frame