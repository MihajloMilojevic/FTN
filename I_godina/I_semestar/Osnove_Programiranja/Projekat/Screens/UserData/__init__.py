from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import GetRelativePath
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
    potvrdi_button: QtWidgets.QPushButton  = components["potvrdi_button"]
    odustani_button: QtWidgets.QPushButton  = components["odustani_button"]
    frame.setMinimumSize(400, 150)
    def potvrdi_button_click():
        password = password_input.text()
        name = name_input.text()
        surname = surname_input.text()
        if password == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti lozinku")
            return
        if name == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti ime")
            return
        if surname == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti prezime")
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
        State.user.ime = name
        State.user.prezime = surname
        State.user.lozinka = password
        # MessageBox().information(frame, "Uspeh", f"Uspešno ste se registrovali kao {user.ime} {user.prezime}")
        parent.show_screen(State.user.uloga)
    potvrdi_button.clicked.connect(potvrdi_button_click)
    def odustani_button_click():
        username_input.setText("")
        password_input.setText("")
        name_input.setText("")
        surname_input.setText("")
        parent.show_screen("menadzer")
    odustani_button.clicked.connect(odustani_button_click)

    def showEvent(event):
        username_input.setText(State.user.korisnicko_ime)
        password_input.setText(State.user.lozinka)
        name_input.setText(State.user.ime)
        surname_input.setText(State.user.prezime)
        role_input.setText(State.user.uloga)
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    return frame
