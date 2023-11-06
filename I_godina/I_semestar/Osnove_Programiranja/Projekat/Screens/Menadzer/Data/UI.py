from PyQt5 import QtCore, QtGui, QtWidgets
from Utils.GetPath import GetRelativePath
from Screens.Menadzer.Data.Sale import SaleTab

def setupUi(Frame: QtWidgets.QFrame):
    frame_layout = QtWidgets.QVBoxLayout()
    frame_layout.setObjectName("frame_layout")

    tab = QtWidgets.QTabWidget(Frame)
    tab.setObjectName("tab")
    tab.setStyleSheet("color: black;")
    font = QtGui.QFont()
    font.setPointSize(12)
    tab.setFont(font)

    sale_tab = SaleTab()
    tab.addTab(sale_tab, "")
    tab.setTabText(tab.indexOf(sale_tab), "Sale")

    frame_layout.addWidget(tab)

    Frame.setLayout(frame_layout)