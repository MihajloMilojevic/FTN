from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import get_relative_path
from Utils.MessageBox import MessageBox
import App.State as State
import Database.Models as Models
from Screens.UserData.UI import setupUi

def UserDataScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMaximumHeight(900)
    frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    username_input: QtWidgets.QLineEdit  = components["username_input"]
    password_input: QtWidgets.QLineEdit  = components["password_input"]
    name_input: QtWidgets.QLineEdit  = components["name_input"]
    surname_input: QtWidgets.QLineEdit  = components["surname_input"]
    role_input: QtWidgets.QLineEdit  = components["role_input"]
    confirm_button: QtWidgets.QPushButton  = components["confirm_button"]
    cancel_button: QtWidgets.QPushButton  = components["cancel_button"]
    frame.setMinimumSize(400, 150)
    def confirm_button_click():
        password = password_input.text().strip()
        name = name_input.text().strip()
        surname = surname_input.text().strip()
        if password == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti lozinku")
            return
        if name == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti name")
            return
        if surname == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti surname")
            return
        if len(password) <= 6:
            MessageBox().warning(frame, "Greška", f"Lozinka je prekratka")
            return
        if len([c for c in password if c.isdigit()]) == 0:
            MessageBox().warning(frame, "Greška", f"Lozinka mora sadržati bar jednu cifru")
            return
        
        username_input.setText("")
        password_input.setText("")
        name_input.setText("")
        surname_input.setText("")
        State.user.name = name
        State.user.surname = surname
        State.user.password = password
        # MessageBox().information(frame, "Uspeh", f"Uspešno ste se registrovali kao {user.name} {user.surname}")
        parent.show_screen(State.user.role)
    confirm_button.clicked.connect(confirm_button_click)
    def cancel_button_click():
        username_input.setText("")
        password_input.setText("")
        name_input.setText("")
        surname_input.setText("")
        parent.show_screen("menadzer")
    cancel_button.clicked.connect(cancel_button_click)

    def showEvent(event):
        username_input.setText(State.user.username)
        password_input.setText(State.user.password)
        name_input.setText(State.user.name)
        surname_input.setText(State.user.surname)
        role_input.setText(State.user.role)
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    return frame
