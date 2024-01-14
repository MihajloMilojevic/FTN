from PyQt5 import QtWidgets, QtGui, QtCore
from screens.reports.report_b.UI import setupUi
from datetime import datetime
from utils.reports import report_b, save_report_b
from utils.save_file_dialog import get_save_file_name

def ReportBScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    datepicker: QtWidgets.QDateEdit = components["datepicker"]
    back_button: QtWidgets.QPushButton = components["back_button"]
    save_button: QtWidgets.QPushButton = components["save_button"]

    def back_button_click():
        datepicker.setDate(datetime.today().date())
        parent.back()
    back_button.clicked.connect(back_button_click)
    
    def save_button_click():
        file_name = get_save_file_name(frame)
        if file_name:
            input_data = datepicker.date().toPyDate()
            date = datetime(input_data.year, input_data.month, input_data.day)
            save_report_b(file_name, date)
    save_button.clicked.connect(save_button_click)

    def refresh_table():
        print("refresh")
        table.setRowCount(0)
        input_data = datepicker.date().toPyDate()
        date = datetime(input_data.year, input_data.month, input_data.day)
        data = report_b(date)
        table.setRowCount(len(data))
    
        for index in range(len(data)):
            current = data[index]

            item = QtWidgets.QTableWidgetItem(current["id"])
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(current["film"])
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(current["hall"])
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(current["status"])
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(current["date"])
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(current["starting_time"])
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(current["ending_time"])
            table.setItem(index, 6, item)
            item = QtWidgets.QTableWidgetItem(current["seat_tag"])
            table.setItem(index, 7, item)
            item = QtWidgets.QTableWidgetItem(current["name"])
            table.setItem(index, 8, item)
            item = QtWidgets.QTableWidgetItem(current["seller"])
            table.setItem(index, 9, item)

        table.resizeRowsToContents()

    datepicker.dateChanged.connect(refresh_table)

    def showEvent(event):
        refresh_table()
        return QtWidgets.QFrame.showEvent(frame, event)

    frame.showEvent = showEvent
    return frame
