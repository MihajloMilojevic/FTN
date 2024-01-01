from PyQt5 import QtCore, QtGui, QtWidgets, uic
from screens.shopper.UI import setupUi
import app.state as State


def ShopperScreen(parent):
    frame = QtWidgets.QFrame()
    components = setupUi(frame)
    odjavi_se_button: QtWidgets.QPushButton = components["odjavi_se_button"]
    name_label: QtWidgets.QLabel = components["name_label"]
    user_data_button: QtWidgets.QPushButton = components["user_data_button"]
    search_films_button:  QtWidgets.QPushButton = components["search_films_button"]
    book_ticket_button:  QtWidgets.QPushButton = components["book_ticket_button"]
    ticketlist_button:  QtWidgets.QPushButton = components["ticketlist_button"]
    
    def odjavi_se_button_click():
        State.user = None
        parent.show_screen("unregistered")
    odjavi_se_button.clicked.connect(odjavi_se_button_click)

    def user_data_button_click():
        parent.show_screen("user_data")
    user_data_button.clicked.connect(user_data_button_click)

    def search_films_button_click():
        parent.show_screen("films")
    search_films_button.clicked.connect(search_films_button_click)

    def book_ticket_button_click():
        parent.show_screen("shopper_booking")
    book_ticket_button.clicked.connect(book_ticket_button_click)

    def ticketlist_button_click():
        parent.show_screen("shopper_ticketlist")
    ticketlist_button.clicked.connect(ticketlist_button_click)

    def showEvent(event):
        name_label.setText(f"Zdravo, {State.user.name} {State.user.surname}")
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    return frame
