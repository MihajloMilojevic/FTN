from PyQt5 import QtWidgets, QtGui, QtCore
from screens.reports.report_h.UI import setupUi
from datetime import datetime
import database.models as Models
import app.state as State
from utils.reports import report_h

def ReportHScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    back_button: QtWidgets.QPushButton = components["back_button"]

    def back_button_click():
        parent.back()
    back_button.clicked.connect(back_button_click)


    def refresh_table():
        print("refresh")
        table.setRowCount(0)
        
        data = report_h()
        table.setRowCount(len(data))
    
        for index in range(len(data)):
            current = data[index]

            item = QtWidgets.QTableWidgetItem(current["seller"])
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(current["number"])
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(current["total"])
            table.setItem(index, 2, item)

        table.resizeRowsToContents()


    def showEvent(event):
        refresh_table()
        return QtWidgets.QFrame.showEvent(frame, event)

    frame.showEvent = showEvent
    return frame
