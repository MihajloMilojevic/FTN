from Screens.Unregistered import UnregisteredScreen
from Screens.Login import LoginScreen
from Screens.Register import RegisterScreen
from Screens.Kupac import KupacScreen
from Screens.Prodavac import ProdavacScreen
from Screens.Menadzer import MenadzerScreen

from PyQt5 import QtCore, QtGui, QtWidgets

def TestScreen(text, color, switch):
    frame = QtWidgets.QFrame()

    layout = QtWidgets.QVBoxLayout()
    layout.setContentsMargins(50, 50, 50, 50)
    layout.setSpacing(10)

    
    button = QtWidgets.QPushButton()
    font = QtGui.QFont()
    font.setPointSize(12)
    button.setFont(font)
    button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    button.setFocusPolicy(QtCore.Qt.ClickFocus)
    button.setStyleSheet(f"background: {color};\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    button.setAutoDefault(False)
    button.setDefault(False)
    button.setFlat(True)
    button.setObjectName("button")
    button.setText(text)
    def click():
        print(text),
        switch()
    button.clicked.connect(click)
    layout.addWidget(button)
    frame.setLayout(layout)
    return frame
