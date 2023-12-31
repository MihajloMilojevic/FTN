from PyQt5 import QtWidgets
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from screens.login.UI import setupUi

def LoginScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMaximumHeight(900)
    frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)
    username_input: QtWidgets.QLineEdit  = components["username_input"]
    password_input: QtWidgets.QLineEdit  = components["password_input"]
    login_button: QtWidgets.QPushButton  = components["login_button"]
    cancel_button: QtWidgets.QPushButton  = components["cancel_button"]
    frame.setMinimumSize(400, 150)
    def login_button_click():
        username = username_input.text().strip()
        password = password_input.text().strip()
        username_input.setText("")
        password_input.setText("")
        if username == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti korisničko name")
            return
        if password == "":
            MessageBox().warning(frame, "Greška", f"Morate uneti lozinku")
            return
        user: Models.User = State.db.users.SelectById(username)
        if user is None:
            MessageBox().warning(frame, "Greška", f"User sa korisničkim imenom {username} ne postoji.")
            return
        if user.password != password:
            MessageBox().warning(frame, "Greška", f"Pogrešna lozinka")
            return
        State.user = user
        # MessageBox().information(frame, "Uspeh", f"Uspešno ste se ulogovali kao {user.name} {user.surname}")
        parent.show_screen(user.role)
    login_button.clicked.connect(login_button_click)
    def cancel_button_click():
        username_input.setText("")
        password_input.setText("")
        parent.back()
    cancel_button.clicked.connect(cancel_button_click)
    return frame
