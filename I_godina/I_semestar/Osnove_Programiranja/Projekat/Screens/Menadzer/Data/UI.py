from PyQt5 import QtCore, QtGui, QtWidgets
from Utils.GetPath import GetRelativePath
from Screens.Menadzer.Data.Sale import SaleTab
from Screens.Menadzer.Data.Filmovi import FilmoviTab
from Screens.Menadzer.Data.Projekcije import ProjekcijeTab

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

    filmovi_tab = FilmoviTab()
    tab.addTab(filmovi_tab, "")
    tab.setTabText(tab.indexOf(filmovi_tab), "Filmovi")

    projekcije_tab = ProjekcijeTab()
    tab.addTab(projekcije_tab, "")
    tab.setTabText(tab.indexOf(projekcije_tab), "Projekcije")

    frame_layout.addWidget(tab)

    back_button = QtWidgets.QPushButton()
    back_button.setMaximumWidth(150)
    back_button.setFont(font)
    back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    back_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    back_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    back_button.setAutoDefault(False)
    back_button.setDefault(False)
    back_button.setFlat(True)
    back_button.setObjectName("back_button")
    back_button.setText("Nazad")

    frame_layout.addWidget(back_button)

    Frame.setLayout(frame_layout)

    return {
        "tab": tab,
        "back_button": back_button
    }