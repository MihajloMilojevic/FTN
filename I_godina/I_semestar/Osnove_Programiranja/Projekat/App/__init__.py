import Screens
from PyQt5 import QtCore, QtGui, QtWidgets
from Utils.GetPath import get_relative_path

class App(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setup()
        self.add_screens()
        self.show_screen("unregistered")

        self.show()

    def add_screens(self):

        self._screen_login = Screens.LoginScreen(self)
        self._screen_register = Screens.RegisterScreen(self)
        self._screen_unregistered = Screens.UnregisteredScreen(self)
        self._screen_kupac = Screens.KupacScreen(self)
        self._screen_prodavac = Screens.ProdavacScreen(self)
        self._screen_menadzer = Screens.MenadzerScreen(self)
        self._screen_employees = Screens.EmployeesScreen(self)
        self._screen_user_data = Screens.UserDataScreen(self)
        self._screen_data = Screens.DataScreen(self)

        self.content_layout.addWidget(self._screen_unregistered)
        self.content_layout.addWidget(self._screen_login)
        self.content_layout.addWidget(self._screen_register)
        self.content_layout.addWidget(self._screen_kupac)
        self.content_layout.addWidget(self._screen_prodavac)
        self.content_layout.addWidget(self._screen_menadzer)
        self.content_layout.addWidget(self._screen_employees)
        self.content_layout.addWidget(self._screen_user_data)
        self.content_layout.addWidget(self._screen_data)
        
        self.screens = {
            "unregistered": self._screen_unregistered,
            "login": self._screen_login,
            "register": self._screen_register,
            "kupac": self._screen_kupac,
            "prodavac": self._screen_prodavac,
            "menadzer": self._screen_menadzer,
            "employees": self._screen_employees,
            "user_data": self._screen_user_data,
            "data": self._screen_data,
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

    def show_screen(self, name):
        for screen in self.screens.values():
            screen.hide()
        self.screens[name].show()

    def setup(self):
        self.setWindowIcon(QtGui.QIcon(get_relative_path(["Assets", "LOGO.ico"])))
        self.setWindowTitle("Bioskop")
        self.setObjectName("Form")
        self.resize(500, 500)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(76, 76, 76);\n"
        "color: white;"
        # "border: 1px solid red"
        )
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Serbian, QtCore.QLocale.Serbia))

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setLayout(QtWidgets.QVBoxLayout())
        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setGeometry(QtCore.QRect(0, 0, 837, 1450))
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