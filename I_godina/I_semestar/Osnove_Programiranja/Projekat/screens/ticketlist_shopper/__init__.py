from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from screens.ticketlist_shopper.UI import setupUi
import screens.ticketlist_shopper.local_state as LocalState

def ShopperTicketListScreen(parent):
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
        data = LocalState.get_data()
        table.setRowCount(len(data))
        def get_handle_click(ticket_id):
            def handler():
                res = MessageBox().question(frame, "Poništavanje rezervacije", f"Da li ste sigurni da želite da poništite rezervaciju sa id-jem '{ticket_id}'?")
                if res != QtWidgets.QMessageBox.StandardButton.Yes:
                    return
                State.db.tickets.DeleteById(ticket_id)
                refresh_table()
            return handler
        for index in range(len(data)):
            current = data[index]
            button = QtWidgets.QWidget()
            button.setLayout(QtWidgets.QVBoxLayout())
            details_button = QtWidgets.QPushButton("Poništi")
            details_button.setStyleSheet("border: 1px solid black; padding: 5px 10px")
            details_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            details_button.clicked.connect(get_handle_click(current["id"]))
            button.layout().addWidget(details_button)
            button.layout().setContentsMargins(5, 5, 5, 5)
            table.setCellWidget(index, 0, button)
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
            item = QtWidgets.QTableWidgetItem(current["seat_tag"])
            table.setItem(index, 7, item)
        table.resizeRowsToContents()
    
    def showEvent(event):
        refresh_table()
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent

    return frame
