from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from components.select_showtime.UI import setupUi
import components.select_showtime.local_state as LocalState
from datetime import datetime
from utils.generate_showtimes import generate_all

def SelectShowtimeComponent(parent):
    onSelect = None
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    components, functions = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    datepicker: QtWidgets.QDateEdit = components["datepicker"]
    filters_button: QtWidgets.QPushButton = components["filters_button"]
    min_time_te: QtWidgets.QTimeEdit = components["min_time_te"]
    max_time_te: QtWidgets.QTimeEdit = components["max_time_te"]
    filters_scroll_area: QtWidgets.QScrollArea = components["filters_scroll_area"]

    add_film = functions["add_film"]
    add_hall = functions["add_hall"]
    clear_films = functions["clear_films"]
    clear_halls = functions["clear_halls"]

    def get_check_box_change(box: QtWidgets.QCheckBox, criteria_name):
        def ret_func():
            if box.isChecked():
                LocalState.criteria[criteria_name].append(box.text())
            else:
                LocalState.criteria[criteria_name].remove(box.text())
            refresh_table()
        return ret_func
    def populate(data, field, function):
        dataset = set()
        for item in data:
            dataset.add(item[field])
        for item in dataset:
            check_box = function(item)
            check_box.stateChanged.connect(get_check_box_change(check_box, field))
    def refresh_table():
        print("refresh")
        table.setRowCount(0)
        input_date = datepicker.date()
        date = datetime(input_date.year(), input_date.month(), input_date.day())
        data = LocalState.get_data(date)
        table.setRowCount(len(data))
        def get_handle_click(id):
            def handler():
                if LocalState.onSelect is not None:
                    LocalState.onSelect(id)
            return handler
        for index in range(len(data)):
            current = data[index]
            select_button = QtWidgets.QWidget()
            select_button.setLayout(QtWidgets.QVBoxLayout())
            details_button = QtWidgets.QPushButton("Odaberi")
            details_button.setStyleSheet("border: 1px solid black; padding: 5px 10px")
            details_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            details_button.clicked.connect(get_handle_click(current["id"]))
            select_button.layout().addWidget(details_button)
            select_button.layout().setContentsMargins(5, 5, 5, 5)
            table.setCellWidget(index, 0, select_button)
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
    def datepicker_change():
        LocalState.reset()
        input_date = datepicker.date()
        date = datetime(input_date.year(), input_date.month(), input_date.day())
        generate_all(date, 1)
        clear_films()
        clear_halls()
        data = LocalState.get_data(date)
        populate(data, "film", add_film)
        populate(data, "hall", add_hall)
        refresh_table()
    datepicker.dateChanged.connect(datepicker_change)

    def time_min_change():
        LocalState.criteria["time"]["min"] = min_time_te.time().toPyTime()
        refresh_table()
    min_time_te.timeChanged.connect(time_min_change)
    def time_max_change():
        LocalState.criteria["time"]["max"] = max_time_te.time().toPyTime()
        refresh_table()
    max_time_te.timeChanged.connect(time_max_change)

    def filters_button_click():
        if filters_scroll_area.isVisible():
            filters_scroll_area.hide()
        else:
            filters_scroll_area.show()
    filters_button.clicked.connect(filters_button_click)

    def showEvent(event):
        filters_scroll_area.hide()
        datepicker_change()
        return QtWidgets.QFrame.showEvent(frame, event)

    frame.showEvent = showEvent

    def setHandler(handle):
        LocalState.onSelect = handle

    return frame, setHandler
