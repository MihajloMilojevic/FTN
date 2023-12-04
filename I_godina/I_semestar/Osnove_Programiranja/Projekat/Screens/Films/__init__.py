from PyQt5 import QtWidgets
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from screens.films.UI import setupUi

def FilmsScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    name_input: QtWidgets.QLineEdit = components["name_input"]
    search_button: QtWidgets.QPushButton = components["search_button"]
    filters_button: QtWidgets.QPushButton = components["filters_button"]
    back_button: QtWidgets.QPushButton = components["back_button"]
    def back_button_click():
        name_input.setText("")
        parent.back()
    back_button.clicked.connect(back_button_click)
    def refresh_table():
        table.setRowCount(0)
        data = State.db.films.SelectAll()
        table.setRowCount(len(data))
        for index in range(len(data)):
            film: Models.Film  = data[index]
            item = QtWidgets.QTableWidgetItem(film.id)
            # item.setBackground(QtGui.QColor)
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(film.name)
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(", ".join(film.genres))
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(str(film.duration))
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(film.director)
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(", ".join(film.main_roles))
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(film.country)
            table.setItem(index, 6, item)
            item = QtWidgets.QTableWidgetItem(str(film.year))
            table.setItem(index, 7, item)
        table.resizeRowsToContents()
    def showEvent(event):
        refresh_table()
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    return frame
