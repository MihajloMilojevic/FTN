from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from screens.film_details.UI import setupUi
import screens.film_details.local_state as LocalState

def FilmDetailsScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setFixedWidth(900)
    # frame.setStyleSheet("background: red; border: 1px solid blue;")
    # frame.setStyleSheet("border: 1px solid red")
    components = setupUi(frame)

    id_label: QtWidgets.QLabel = components["id_label"]
    name_label: QtWidgets.QLabel = components["name_label"]
    director_label: QtWidgets.QLabel = components["director_label"]
    country_label: QtWidgets.QLabel = components["country_label"]
    year_label: QtWidgets.QLabel = components["year_label"]
    roles_label: QtWidgets.QLabel = components["roles_label"]
    genres_label: QtWidgets.QLabel = components["genres_label"]
    description_label: QtWidgets.QLabel = components["description_label"]
    reserve_button: QtWidgets.QLabel = components["reserve_button"]
    sell_button: QtWidgets.QLabel = components["sell_button"]
    back_button: QtWidgets.QLabel = components["back_button"]


    def back_button_click():
        parent.back()
    back_button.clicked.connect(back_button_click)
 
    def showEvent(event):
        if LocalState.current_film is not None:
            id_label.setText(LocalState.current_film.id)
            name_label.setText(LocalState.current_film.name)
            director_label.setText(LocalState.current_film.director)
            country_label.setText(LocalState.current_film.country)
            year_label.setText(str(LocalState.current_film.year))
            roles_label.setText(", ".join(LocalState.current_film.main_roles))
            genres_label.setText(", ".join(LocalState.current_film.genres))
            description_label.setText(LocalState.current_film.description)
            if State.user is None:
                reserve_button.hide()
                sell_button.hide()
            elif State.user.role == Models.Roles.kupac:
                reserve_button.show()
                sell_button.hide()
            else:
                reserve_button.show()
                sell_button.show()
        else:
            parent.back()

        return QtWidgets.QFrame.showEvent(frame, event)
    
    frame.showEvent = showEvent
    return frame
