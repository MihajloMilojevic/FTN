from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from screens.ticketlist_seller.UI import setupUi
import screens.ticketlist_seller.local_state as LocalState
from datetime import datetime, date, time

def SellerTicketListScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components, functions = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    back_button: QtWidgets.QPushButton = components["back_button"]
    filters_button: QtWidgets.QPushButton = components["filters_button"]
    # min_date_de: QtWidgets.QDateEdit = components["min_date_de"]
    # max_date_de: QtWidgets.QDateEdit = components["max_date_de"]
    filters_scroll_area: QtWidgets.QScrollArea = components["filters_scroll_area"]
    name_input: QtWidgets.QLineEdit = components["name_input"]
    min_time_te: QtWidgets.QTimeEdit = components["min_time_te"]
    max_time_te: QtWidgets.QTimeEdit = components["max_time_te"]
    min_date_de: QtWidgets.QDateEdit = components["min_date_de"]
    max_date_de: QtWidgets.QDateEdit = components["max_date_de"]

    add_status = functions["add_status"]
    clear_status = functions["clear_status"]
    add_film = functions["add_film"]
    clear_films = functions["clear_films"]
    add_projection = functions["add_projection"]
    clear_projections = functions["clear_projections"]

    def back_button_click():
        parent.back()
    back_button.clicked.connect(back_button_click)
    def refresh_table():
        print("refresh")
        table.setRowCount(0)
        data = LocalState.get_data()
        table.setRowCount(len(data))
        def get_handle_sell_click(ticket_id):
            def handler():
                # res = MessageBox().question(frame, "Prodaja karte", f"Da li ste sigurni da želite da poništite rezervaciju sa id-jem '{ticket_id}'?")
                # if res != QtWidgets.QMessageBox.StandardButton.Yes:
                #     return
                # State.db.tickets.DeleteById(ticket_id)
                refresh_table()
            return handler
        def get_handle_cancel_click(ticket_id):
            def handler():
                res = MessageBox().question(frame, "Poništavanje rezervacije", f"Da li ste sigurni da želite da poništite rezervaciju sa id-jem '{ticket_id}'?")
                if res != QtWidgets.QMessageBox.StandardButton.Yes:
                    return
                State.db.tickets.DeleteById(ticket_id)
                refresh_table()
            return handler
        def get_handle_edit_click(ticket_id):
            def handler():
                # res = MessageBox().question(frame, "Poništavanje rezervacije", f"Da li ste sigurni da želite da poništite rezervaciju sa id-jem '{ticket_id}'?")
                # if res != QtWidgets.QMessageBox.StandardButton.Yes:
                #     return
                # State.db.tickets.DeleteById(ticket_id)
                refresh_table()
            return handler
        for index in range(len(data)):
            current = data[index]

            if current["status"] == "Rezervisano":
                sell_widget = QtWidgets.QWidget()
                sell_widget.setLayout(QtWidgets.QVBoxLayout())
                sell_button = QtWidgets.QPushButton("Prodaj")
                sell_button.setStyleSheet("border: 1px solid black; padding: 5px 10px")
                sell_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                sell_button.clicked.connect(get_handle_sell_click(current["id"]))
                sell_widget.layout().addWidget(sell_button)
                sell_widget.layout().setContentsMargins(5, 5, 5, 5)
                table.setCellWidget(index, 0, sell_widget)

            cancel_widget = QtWidgets.QWidget()
            cancel_widget.setLayout(QtWidgets.QVBoxLayout())
            cancel_button = QtWidgets.QPushButton("Poništi")
            cancel_button.setStyleSheet("border: 1px solid black; padding: 5px 10px")
            cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            cancel_button.clicked.connect(get_handle_cancel_click(current["id"]))
            cancel_widget.layout().addWidget(cancel_button)
            cancel_widget.layout().setContentsMargins(5, 5, 5, 5)
            table.setCellWidget(index, 1, cancel_widget)

            edit_widget = QtWidgets.QWidget()
            edit_widget.setLayout(QtWidgets.QVBoxLayout())
            edit_button = QtWidgets.QPushButton("Izmeni")
            edit_button.setStyleSheet("border: 1px solid black; padding: 5px 10px")
            edit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            edit_button.clicked.connect(get_handle_edit_click(current["id"]))
            edit_widget.layout().addWidget(edit_button)
            edit_widget.layout().setContentsMargins(5, 5, 5, 5)
            table.setCellWidget(index, 2, edit_widget)

            item = QtWidgets.QTableWidgetItem(current["id"])
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(current["film"])
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(current["hall"])
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(current["status"])
            table.setItem(index, 6, item)
            item = QtWidgets.QTableWidgetItem(current["date"])
            table.setItem(index, 7, item)
            item = QtWidgets.QTableWidgetItem(current["starting_time"])
            table.setItem(index, 8, item)
            item = QtWidgets.QTableWidgetItem(current["ending_time"])
            table.setItem(index, 9, item)
            item = QtWidgets.QTableWidgetItem(current["seat_tag"])
            table.setItem(index, 10, item)
            item = QtWidgets.QTableWidgetItem(current["name"])
            table.setItem(index, 11, item)
        table.resizeRowsToContents()

    def filters_button_click():
        if filters_scroll_area.isVisible():
            filters_scroll_area.hide()
        else:
            filters_scroll_area.show()
    filters_button.clicked.connect(filters_button_click)
    def get_check_box_change(box: QtWidgets.QCheckBox, field: str):
            def ret_func():
                if box.isChecked():
                    LocalState.criteria[field].append(box.text())
                else:
                    LocalState.criteria[field].remove(box.text())
                refresh_table()
            return ret_func
    def populate_projections():
        clear_projections()
        LocalState.criteria["projections"].clear()
        for projection_id in set([ticket.showtime.get(State.db).projection_id for ticket in State.db.tickets.SelectAll()]):
            check_box = add_projection(projection_id)
            check_box.stateChanged.connect(get_check_box_change(check_box, "projections"))   
    def populate_films():
        clear_films()
        LocalState.criteria["films"].clear()
        for film_name in set([
                ticket.showtime.get(State.db).projection.get(State.db).film.get(State.db).name 
                for ticket in State.db.tickets.SelectAll()]):
            check_box = add_film(film_name)
            check_box.stateChanged.connect(get_check_box_change(check_box, "films"))   
    def populate_status():
        clear_status()
        LocalState.criteria["status"].clear()
        for status in ["Rezervisano", "Prodato"]:
            check_box = add_status(status)
            check_box.stateChanged.connect(get_check_box_change(check_box, "status"))

    def populate_datetimes():
        LocalState.criteria["date"] = {"min": None, "max": None}
        LocalState.criteria["time"] = {"min": None, "max": None}

        dates = [ticket.showtime.get(State.db).date.date() for ticket in State.db.tickets.SelectAll()]
        
        max_date: date  = max(dates)
        min_date: date = min(dates)
        
        d = QtCore.QDate()
        d.setDate(max_date.year, max_date.month, max_date.day)
        max_date_de.setDate(d)
        d.setDate(min_date.year, min_date.month, min_date.day)
        min_date_de.setDate(d)

        t = QtCore.QTime()
        t.setHMS(0, 0, 0)
        max_time_te.setTime(t)
        t.setHMS(23, 59, 59)
        min_time_te.setTime(t)

    def name_input_change():
        LocalState.criteria["name"] = name_input.text()
        refresh_table()
    name_input.textChanged.connect(name_input_change)

    def min_date_change():
        LocalState.criteria["date"]["min"] = min_date_de.date().toPyDate()
        refresh_table()
    min_date_de.dateChanged.connect(min_date_change)
    def max_date_change():
        LocalState.criteria["date"]["max"] = max_date_de.date().toPyDate()
        refresh_table()
    max_date_de.dateChanged.connect(max_date_change)
    def min_time_change():
        LocalState.criteria["time"]["min"] = min_time_te.time().toPyTime()
        refresh_table()
    min_time_te.timeChanged.connect(min_time_change)
    def max_time_change():
        LocalState.criteria["time"]["max"] = max_time_te.time().toPyTime()
        refresh_table()
    max_time_te.timeChanged.connect(max_time_change)

    def showEvent(event):
        refresh_table()
        filters_scroll_area.hide()
        populate_projections()
        populate_films()
        populate_status()
        populate_datetimes()
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent

    return frame
