from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Utils.GetPath import get_relative_path
import App.State as State
import Database.Models as Models
from Utils.MessageBox import MessageBox
from Screens.Login.UI import setupUi

def LoginScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMaximumHeight(900)
    frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    username_input: QtWidgets.QLineEdit  = components["username_input"]
    password_input: QtWidgets.QLineEdit  = components["password_input"]
    prijavi_se_button: QtWidgets.QPushButton  = components["prijavi_se_button"]
    odustani_button: QtWidgets.QPushButton  = components["odustani_button"]
    frame.setMinimumSize(400, 150)
    def prijavi_se_button_click():
        username = username_input.text()
        password = password_input.text()
        username_input.setText("")
        password_input.setText("")
        if username == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti korisničko ime")
            return
        if password == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti lozinku")
            return
        user: Models.Korisnik = State.db.korisnici.SelectById(username)
        if user is None:
            MessageBox().warning(frame, "Greška", f"Korisnik sa korisničkim imenom {username} ne postoji.")
            return
        if user.lozinka != password:
            MessageBox().warning(frame, "Greška", f"Pogrešna lozinka")
            return
        State.user = user
        # MessageBox().information(frame, "Uspeh", f"Uspešno ste se ulogovali kao {user.ime} {user.prezime}")
        parent.show_screen(user.uloga)
    prijavi_se_button.clicked.connect(prijavi_se_button_click)
    def odustani_button_click():
        username_input.setText("")
        password_input.setText("")
        parent.show_screen("unregistered")
    odustani_button.clicked.connect(odustani_button_click)
    return frame
