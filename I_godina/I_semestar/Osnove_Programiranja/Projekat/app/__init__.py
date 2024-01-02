import screens as Screens
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.get_path import get_relative_path

class App(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setup()
        self.history = []
        self.add_screens()
        self.show_screen("unregistered")

        self.show()

    def add_screens(self):

        self._screen_login = Screens.LoginScreen(self)
        self._screen_register = Screens.RegisterScreen(self)
        self._screen_unregistered = Screens.UnregisteredScreen(self)
        self._screen_shopper = Screens.ShopperScreen(self)
        self._screen_seller = Screens.SellerScreen(self)
        self._screen_manager = Screens.ManagerScreen(self)
        self._screen_employees = Screens.EmployeesScreen(self)
        self._screen_user_data = Screens.UserDataScreen(self)
        self._screen_data = Screens.DataScreen(self)
        self._screen_films = Screens.FilmsScreen(self)
        self._screen_film_details = Screens.FilmDetailsScreen(self)
        self._repertoire_screen = Screens.RepertoireScreen(self)
        self._shopper_booking_screen = Screens.ShopperBookingScreen(self)
        self._shopper_ticketlist_screen = Screens.ShopperTicketListScreen(self)
        self._seller_booking_screen = Screens.SellerBookingScreen(self)

        self.content_layout.addWidget(self._screen_unregistered)
        self.content_layout.addWidget(self._screen_login)
        self.content_layout.addWidget(self._screen_register)
        self.content_layout.addWidget(self._screen_shopper)
        self.content_layout.addWidget(self._screen_seller)
        self.content_layout.addWidget(self._screen_manager)
        self.content_layout.addWidget(self._screen_employees)
        self.content_layout.addWidget(self._screen_user_data)
        self.content_layout.addWidget(self._screen_data)
        self.content_layout.addWidget(self._screen_films)
        self.content_layout.addWidget(self._screen_film_details)
        self.content_layout.addWidget(self._repertoire_screen)
        self.content_layout.addWidget(self._shopper_booking_screen)
        self.content_layout.addWidget(self._shopper_ticketlist_screen)
        self.content_layout.addWidget(self._seller_booking_screen)
        
        self.screens = {
            "unregistered": self._screen_unregistered,
            "login": self._screen_login,
            "register": self._screen_register,
            
            # ostaje na srpskom jer se koristi role kao key da se predje na ove ekrane
            "kupac": self._screen_shopper,          
            "prodavac": self._screen_seller,
            "menadzer": self._screen_manager,

            "employees": self._screen_employees,
            "user_data": self._screen_user_data,
            "data": self._screen_data,
            "films": self._screen_films,
            "film_details": self._screen_film_details,
            "repertoire": self._repertoire_screen,
            "shopper_booking": self._shopper_booking_screen,
            "shopper_ticketlist": self._shopper_ticketlist_screen,
            "seller_booking": self._seller_booking_screen,
        }
        


        ### TESTING #####
        # self.screen1 = Screen("Screen 1", "red", lambda: self.show_screen("scr2"))
        # self.screen2 = Screen("Screen 2", "blue", lambda: self.show_screen("scr3"))
        # self.screen3 = Screen("Screen 3", "yellow", lambda: self.show_screen("scr1"))

        # self.screens = {
        #     "scr1": self.screen1,
        #     "scr2": self.screen2,
        #     "scr3": self.screen3
        # }

        # self.content_layout.addWidget(self.screen2)
        # self.content_layout.addWidget(self.screen3)
        # self.content_layout.addWidget(self.screen1)

    def show_screen(self, name, add_to_history = True):
        if add_to_history:
            print(f"'{name}' added to history")
            self.history.append(name)
        for screen in self.screens.values():
            screen.hide()
        self.screens[name].show()
    
    def back(self):
        if(len(self.history) == 0):
            print("End of history reached")
            return
        current = self.history.pop()
        print(f"'{current}' removed from history")
        redirect_to = self.history[-1]
        print(f"Redirecting to '{redirect_to}'")
        self.show_screen(redirect_to, add_to_history=False)
    
    def setup(self):
        self.setWindowIcon(QtGui.QIcon(get_relative_path(["assets", "LOGO.ico"])))
        self.setWindowTitle("Bioskop")
        self.setObjectName("Form")
        self.resize(500, 500)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(76, 76, 76);\n"
        "color: white;"
        # "border: 1px solid blue"
        )
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Serbian, QtCore.QLocale.Serbia))

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setLayout(QtWidgets.QVBoxLayout())
        self.scrollArea.layout().setContentsMargins(0, 0, 0, 0)
        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setContentsMargins(0, 0, 0, 0)
        self.content_widget.setObjectName("content")
        # self.scrollArea.setStyleSheet("border: 1px solid red")
        # self.content_widget.setStyleSheet("border: 1px solid green")
        self.scrollArea.setWidget(self.content_widget)

        

        self.content_layout = QtWidgets.QVBoxLayout()
        self.content_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.content_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName("content_layout")
        self.content_widget.setLayout(self.content_layout)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")
        self.main_layout.addWidget(self.scrollArea)
        self.setLayout(self.main_layout)