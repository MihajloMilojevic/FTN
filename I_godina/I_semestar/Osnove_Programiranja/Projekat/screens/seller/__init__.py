from PyQt5 import QtWidgets
from screens.seller.UI import setupUi
import app.state as State
from utils.cancel_upcoming import cancel_upcoming_tickets
from utils.message_box import MessageBox

def SellerScreen(parent):
    frame = QtWidgets.QFrame()
    components = setupUi(frame)
    odjavi_se_button: QtWidgets.QPushButton = components["odjavi_se_button"]
    name_label: QtWidgets.QLabel = components["name_label"]
    user_data_button: QtWidgets.QPushButton = components["user_data_button"]
    search_films_button:  QtWidgets.QPushButton = components["search_films_button"]
    booking_button:  QtWidgets.QPushButton = components["booking_button"]
    selling_button:  QtWidgets.QPushButton = components["selling_button"]
    ticketlist_button:  QtWidgets.QPushButton = components["ticketlist_button"]
    cancel_upcoming_button:  QtWidgets.QPushButton = components["cancel_upcoming_button"]
    
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

    def booking_button_click():
        parent.show_screen("seller_booking")
    booking_button.clicked.connect(booking_button_click)

    def selling_button_click():
        parent.show_screen("seller_selling")
    selling_button.clicked.connect(selling_button_click)

    def ticketlist_button_click():
        parent.show_screen("seller_ticketlist")
    ticketlist_button.clicked.connect(ticketlist_button_click)

    def cancel_upcoming_button_click():
        canceled = cancel_upcoming_tickets()
        MessageBox().information(frame, "Poništavanje rezervacija", f"Poništeno {canceled} rezervacija")
    cancel_upcoming_button.clicked.connect(cancel_upcoming_button_click)
    
    def showEvent(event):
        name_label.setText(f"Zdravo, {State.user.name} {State.user.surname}")
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    return frame