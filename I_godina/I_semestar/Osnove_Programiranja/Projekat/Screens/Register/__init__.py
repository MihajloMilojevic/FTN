from PyQt5 import QtWidgets
from utils.message_box import MessageBox
import app.state as State
import database.models as Models
from screens.register.UI import setupUi

def RegisterScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMaximumHeight(900)
    frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    username_input: QtWidgets.QLineEdit  = components["username_input"]
    password_input: QtWidgets.QLineEdit  = components["password_input"]
    name_input: QtWidgets.QLineEdit  = components["name_input"]
    surname_input: QtWidgets.QLineEdit  = components["surname_input"]
    register_button: QtWidgets.QPushButton  = components["register_button"]
    cancel_button: QtWidgets.QPushButton  = components["cancel_button"]
    frame.setMinimumSize(400, 150)
    def register_button_click():
        username = username_input.text().strip()
        password = password_input.text().strip()
        name = name_input.text().strip()
        surname = surname_input.text().strip()
        if username == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti korisničko name")
            return
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
        
        user = Models.User(username, password, name, surname, Models.Roles.kupac)
        inserted = State.db.users.Insert(user)
        if not inserted:
            MessageBox().warning(frame, "Greška", f"Korisničko name je zauzeto")
            return
        State.user = user
        
        username_input.setText("")
        password_input.setText("")
        name_input.setText("")
        surname_input.setText("")
        # MessageBox().information(frame, "Uspeh", f"Uspešno ste se registrovali kao {user.name} {user.surname}")
        parent.show_screen(State.user.role)
    register_button.clicked.connect(register_button_click)
    def cancel_button_click():
        username_input.setText("")
        password_input.setText("")
        name_input.setText("")
        surname_input.setText("")
        parent.show_screen("unregistered")
    cancel_button.clicked.connect(cancel_button_click)
    return frame
