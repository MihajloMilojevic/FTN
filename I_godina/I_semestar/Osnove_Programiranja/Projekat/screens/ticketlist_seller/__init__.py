from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from screens.ticketlist_seller.UI import setupUi
import screens.ticketlist_seller.local_state as LocalState

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
        table.resizeRowsToContents()

    def filters_button_click():
        if filters_scroll_area.isVisible():
            filters_scroll_area.hide()
        else:
            filters_scroll_area.show()
    filters_button.clicked.connect(filters_button_click)
    
    def showEvent(event):
        refresh_table()
        filters_scroll_area.hide()
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent

    return frame
