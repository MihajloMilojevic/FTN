from PyQt5 import QtWidgets
from screens.unregistered.UI import setupUi

def UnregisteredScreen(parent):
    frame = QtWidgets.QFrame()

    components = setupUi(frame)
    login_button = components["login_button"]
    register_button = components["register_button"]
    search_films_button:  QtWidgets.QPushButton = components["search_films_button"]

    def login_button_click():
        parent.show_screen("login")
    def register_button_click():
        parent.show_screen("register")
    def search_films_button_click():
        parent.show_screen("films")
    search_films_button.clicked.connect(search_films_button_click)

    login_button.clicked.connect(login_button_click)
    register_button.clicked.connect(register_button_click)

    return frame