from PyQt5 import QtWidgets, QtGui, QtCore
from screens.reports.report_f.UI import setupUi
from datetime import datetime
import database.models as Models
import app.state as State
from utils.reports import report_f, save_report_f
from utils.save_file_dialog import get_save_file_name

def ReportFScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    film_select: QtWidgets.QComboBox = components["film_select"]
    back_button: QtWidgets.QPushButton = components["back_button"]
    save_button: QtWidgets.QPushButton = components["save_button"]

    def back_button_click():
        parent.back()
    back_button.clicked.connect(back_button_click)
    def save_button_click():
        file_name = get_save_file_name(frame)
        if file_name:
            save_report_f(file_name, film_select.currentText())
    save_button.clicked.connect(save_button_click)

    def populate_films():
        filmnames = set([film.name for film in State.db.films.SelectAll()])
        film_select.clear()
        film_select.addItems(list(filmnames))

    def refresh_table():
        print("refresh")
        table.setRowCount(0)
        data = report_f(film_select.currentText())
        table.setRowCount(1)
    
        item = QtWidgets.QTableWidgetItem(str(data[0]))
        table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem(str(data[1]))
        table.setItem(0, 1, item)

        table.resizeRowsToContents()

    film_select.currentTextChanged.connect(refresh_table)

    def showEvent(event):
        refresh_table()
        populate_films()
        return QtWidgets.QFrame.showEvent(frame, event)

    frame.showEvent = showEvent
    return frame
