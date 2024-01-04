from screens.unregistered import UnregisteredScreen
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.shopper import ShopperScreen
from screens.seller import SellerScreen
from screens.manager import ManagerScreen
from screens.manager.employees import EmployeesScreen
from screens.user_data import UserDataScreen
from screens.manager.cinema_data import DataScreen
from screens.films import FilmsScreen
from screens.film_details import FilmDetailsScreen
from screens.showtimes import RepertoireScreen
from screens.booking_shopper import ShopperBookingScreen
from screens.ticketlist_shopper import ShopperTicketListScreen
from screens.booking_seller import SellerBookingScreen
from screens.ticketlist_seller import SellerTicketListScreen
from screens.selling_seller import SellerSellingScreen
from screens.ticket_edit import TicketEditScreen


from PyQt5 import QtCore, QtGui, QtWidgets

def TestScreen(text, color, switch):
    frame = QtWidgets.QFrame()

    layout = QtWidgets.QVBoxLayout()
    layout.setContentsMargins(50, 50, 50, 50)
    layout.setSpacing(10)

    
    button = QtWidgets.QPushButton()
    font = QtGui.QFont()
    font.setPointSize(12)
    button.setFont(font)
    button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    button.setFocusPolicy(QtCore.Qt.ClickFocus)
    button.setStyleSheet(f"background: {color};\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    button.setAutoDefault(False)
    button.setDefault(False)
    button.setFlat(True)
    button.setObjectName("button")
    button.setText(text)
    def click():
        print(text),
        switch()
    button.clicked.connect(click)
    layout.addWidget(button)
    frame.setLayout(layout)
    return frame
