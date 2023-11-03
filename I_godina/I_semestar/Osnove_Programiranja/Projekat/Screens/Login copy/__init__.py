from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic

from Utils.GetPath import GetRelativePath
import App.State as State
import Database.Models as Models



class LoginScreen(QDialog):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(GetRelativePath(["Screens", "Login", "LoginScreenDesign.ui"]), self)
        self.setWindowIcon(QIcon(GetRelativePath(["LOGO.ico"])))
        self.get_components()
        self.add_functionality()
    
    def get_components(self):
        self.prijavi_se_button: QPushButton = self.findChild(QPushButton, "prijavi_se_button")
        self.username_input: QLineEdit = self.findChild(QLineEdit, "username_input")
        self.password_input: QLineEdit = self.findChild(QLineEdit, "password_input")

    def add_functionality(self):
        self.prijavi_se_button.clicked.connect(self.prijavi_se_button_click)

    def prijavi_se_button_click(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "":
            QMessageBox.warning(self, "Greška", f"Morate uneti korisničko ime")
            return
        if password == "":
            QMessageBox.warning(self, "Greška", f"Morate uneti lozinku")
            return
        user: Models.Korisnik = State.db.korisnici.SelectById(username)
        if user is None:
            QMessageBox.warning(self, "Greška", f"Korisnik sa korisničkim imenom {username} ne postoji.")
            return
        if user.lozinka != password:
            QMessageBox.warning(self, "Greška", f"Pogrešna lozinka")
            return
        State.user = user
        QMessageBox.information(self, "Uspeh", f"Uspešno ste se ulogovali kao {user.ime} {user.prezime}")
        self.close() 
