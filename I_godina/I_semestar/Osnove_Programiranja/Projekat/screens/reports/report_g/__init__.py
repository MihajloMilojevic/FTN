from PyQt5 import QtWidgets, QtGui, QtCore
from screens.reports.report_g.UI import setupUi
from datetime import datetime
import database.models as Models
import app.state as State
from utils.reports import report_g

def ReportGScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    day_select: QtWidgets.QComboBox = components["day_select"]
    seller_select: QtWidgets.QComboBox = components["seller_select"]
    back_button: QtWidgets.QPushButton = components["back_button"]

    def back_button_click():
        parent.back()
    back_button.clicked.connect(back_button_click)

    def populate_sellers():
        def isSeller(user: Models.User):
            return user.role == Models.Roles.prodavac
        sellers = State.db.users.Select(isSeller)
        seller_select.clear()
        seller_select.addItems([f"{seller.name} {seller.surname}" for seller in sellers])

    def refresh_table():
        print("refresh")
        table.setRowCount(0)
        data = report_g(day_select.currentText(), seller_select.currentText())
        table.setRowCount(1)
    
        item = QtWidgets.QTableWidgetItem(str(data[0]))
        table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem(str(data[1]))
        table.setItem(0, 1, item)

        table.resizeRowsToContents()

    day_select.currentTextChanged.connect(refresh_table)
    seller_select.currentTextChanged.connect(refresh_table)

    def showEvent(event):
        refresh_table()
        populate_sellers()
        return QtWidgets.QFrame.showEvent(frame, event)

    frame.showEvent = showEvent
    return frame