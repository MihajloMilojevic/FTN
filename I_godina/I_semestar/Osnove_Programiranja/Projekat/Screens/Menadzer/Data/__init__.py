from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import GetRelativePath
import App.State as State
import Database.Models as Models
from Screens.Menadzer.Data.UI import setupUi

def DataScreen(parent):
    frame = QtWidgets.QFrame()
    # frame.setMaximumHeight(1000)
    # frame.setMaximumWidth(1000)
    setupUi(frame)

    return frame
