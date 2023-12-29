from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from screens.repertoire.UI import setupUi
import screens.repertoire.local_state as LocalState
# import screens.film_details.local_state as FilmDetailsState
from datetime import datetime
from utils.generate_showtimes import generate_all

def RepertoireScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    datepicker: QtWidgets.QDateEdit = components["datepicker"]
    # search_button: QtWidgets.QPushButton = components["search_button"]
    back_button: QtWidgets.QPushButton = components["back_button"]

    def back_button_click():
        datepicker.setDate(datetime.today().date())
        parent.back()
    back_button.clicked.connect(back_button_click)
    def refresh_table():
        print("refresh")
        table.setRowCount(0)
        input_date = datepicker.date()
        date = datetime(input_date.year(), input_date.month(), input_date.day())
        generate_all(date, 1)
        data = LocalState.get_data(date)
        table.setRowCount(len(data))
        # def get_handle_click(film_id):
        #     def handler():
        #         FilmDetailsState.current_film = State.db.films.SelectById(film_id)
        #         parent.show_screen("film_details")
        #     return handler
        for index in range(len(data)):
            current = data[index]
            item = QtWidgets.QTableWidgetItem(current["id"])
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(current["film"])
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(current["hall"])
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(current["date"])
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(current["starting_time"])
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(current["ending_time"])
            table.setItem(index, 6, item)
        table.resizeRowsToContents()
   
    datepicker.dateChanged.connect(refresh_table)

    def showEvent(event):
        refresh_table()
        return QtWidgets.QFrame.showEvent(frame, event)

    frame.showEvent = showEvent
    return frame
