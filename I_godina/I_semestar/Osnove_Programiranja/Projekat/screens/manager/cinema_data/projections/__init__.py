from PyQt5 import QtCore, QtWidgets
from screens.manager.cinema_data.projections.UI import setupUi
import app.state as State
import screens.manager.cinema_data.projections.local_state as LocalState
import database.models as Models
from utils.message_box import MessageBox
from utils.generate_id import generate_number
from utils.validate_projection import validate_projection
from utils.serialize import serialize_time
from datetime import datetime

def ProjekcijeTab():
    tab = QtWidgets.QWidget()
    tab.setObjectName("tab")

    frames = setupUi(tab)
    
    frame_buttons: QtWidgets.QFrame = frames["frame_buttons"]["frame"]
    frame_table: QtWidgets.QTableWidget = frames["frame_table"]["table"]
    frame_add: QtWidgets.QFrame = frames["frame_add"]["frame"]
    frame_edit: QtWidgets.QFrame = frames["frame_edit"]["frame"]

    def show_table():
        frame_buttons.show()
        frame_table.show()
        frame_add.hide()
        frame_edit.hide()
    def show_add():
        frame_buttons.hide()
        frame_table.hide()
        frame_add.show()
        frame_edit.hide()
    def show_edit():
        frame_buttons.hide()
        frame_table.hide()
        frame_add.hide()
        frame_edit.show()

    def showEvent(event):
        show_table()
        return QtWidgets.QWidget.showEvent(tab, event)
    tab.showEvent = showEvent

    show_table()

    # Table

    table = frame_table
    def refresh_table():
        table.setRowCount(0)
        data = State.db.projections.SelectAll()
        table.setRowCount(len(data))
        for index in range(len(data)):
            projection: Models.Projection  = data[index]
            sala: Models.Hall = projection.hall.get(State.db)
            film: Models.Film = projection.film.get(State.db)
            item = QtWidgets.QTableWidgetItem(projection.id)
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(sala.name)
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(film.name)
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(datetime.strftime(projection.starting_time, "%H:%M"))
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(datetime.strftime(projection.ending_time, "%H:%M"))
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(str(projection.price))
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(", ".join(projection.days))
            table.setItem(index, 6, item)
        table.resizeColumnsToContents()
    def table_showEvent(event):
        refresh_table()
        return QtWidgets.QTableWidget.showEvent(table, event)
    table.showEvent = table_showEvent


    # Buttons Frame

    buttons_add: QtWidgets.QPushButton = frames["frame_buttons"]["add_button"]
    buttons_delete: QtWidgets.QPushButton = frames["frame_buttons"]["delete_button"]
    buttons_edit: QtWidgets.QPushButton = frames["frame_buttons"]["edit_button"]
    def buttons_delete_click():
        row = table.currentRow()
        if row < 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati projekciju za brisanje")
            return
        id = table.item(row, 0).text()
        film = table.item(row, 2).text()
        res = MessageBox().question(tab, "Brisanje projections", f"Da li ste sigurni da želite da obrišete projekciju za film '{film}'?")
        if res != QtWidgets.QMessageBox.StandardButton.Yes:
            return
        State.db.projections.DeleteById(id)
        refresh_table()
    def buttons_edit_click():
        row = table.currentRow()
        if row < 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati projekciju za izmenu")
            return
        id = table.item(row, 0).text()
        LocalState.projection_to_edit = State.db.projections.SelectById(id)
        show_edit()
    buttons_add.clicked.connect(show_add)
    buttons_delete.clicked.connect(buttons_delete_click)
    buttons_edit.clicked.connect(buttons_edit_click)

    

    # Add Form

    add_sifra_input: QtWidgets.QLineEdit = frames["frame_add"]["sifra_input"]
    add_sala_cb: QtWidgets.QComboBox = frames["frame_add"]["sala_cb"]
    add_film_cb: QtWidgets.QComboBox = frames["frame_add"]["film_cb"]
    add_vreme_pocetka_time: QtWidgets.QTimeEdit = frames["frame_add"]["vreme_pocetka_time"]
    add_vreme_kraja_time: QtWidgets.QTimeEdit = frames["frame_add"]["vreme_kraja_time"]
    add_cena_sb: QtWidgets.QDoubleSpinBox = frames["frame_add"]["cena_sb"]
    add_dani_checkboxes: list[QtWidgets.QCheckBox] = frames["frame_add"]["dani_checkboxes"]
    add_confirm_button: QtWidgets.QPushButton = frames["frame_add"]["confirm_button"]
    add_cancel_button: QtWidgets.QPushButton = frames["frame_add"]["cancel_button"]

    def add_calculate_end_time():
        name = add_film_cb.currentText()
        if name == "" or name not in [f.name for f in State.db.films.SelectAll()]:   
            add_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
            return
        film: Models.Film = State.db.films.Select(lambda film: film.name == name)[0]
        time: QtCore.QTime = QtCore.QTime(add_vreme_pocetka_time.time().hour(), add_vreme_pocetka_time.time().minute())
        time = time.addSecs(film.duration * 60)
        add_vreme_kraja_time.setTime(time)
    add_film_cb.currentTextChanged.connect(add_calculate_end_time)
    add_vreme_pocetka_time.timeChanged.connect(add_calculate_end_time)

    def add_confirm_button_click():
        id = add_sifra_input.text().strip()
        ime_filma = add_film_cb.currentText().strip()
        ime_sale = add_sala_cb.currentText().strip()
        price = add_cena_sb.value()
        starting_time = add_vreme_pocetka_time.dateTime().toPyDateTime()
        ending_time = add_vreme_kraja_time.dateTime().toPyDateTime()
        days = [checkbox.text() for checkbox in add_dani_checkboxes if checkbox.isChecked()]

        if id == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if ime_filma == "" or ime_filma not in [film.name for film in State.db.films.SelectAll()]:
            MessageBox().warning(tab, "Greška", f"Morate odabrati neki film")
            return
        if ime_sale == "" or ime_sale not in [sala.name for sala in State.db.halls.SelectAll()]:
            MessageBox().warning(tab, "Greška", f"Morate odabrati neku salu")
            return
        if price == 0.00:
            MessageBox().warning(tab, "Greška", f"Morate uneti cenu tickets")
            return
        if len(days) == 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati bar jedan dan projections")
            return
        
        film = State.db.films.Select(lambda film: film.name == ime_filma)[0]
        sala = State.db.halls.Select(lambda sala: sala.name == ime_sale)[0]

        projection = Models.Projection(id, sala.id, film.id, starting_time, ending_time, days, price)
        validated = validate_projection(projection, State.db.projections.SelectAll())
        if validated is not None:   
            error_projection: Models.Projection = State.db.projections.SelectById(validated[1])
            error_film = error_projection.film.get(State.db).name or "?"
            MessageBox().warning(tab, 
                "Greška", 
                f"Preklapanje sa projekcijom filma '{error_film}' ({validated[0]})")
            return
        inserted = State.db.projections.Insert(projection)

        if not inserted:
            MessageBox().warning(tab, "Greška", f"Projekcija sa unetom šifrom već postoji")
            return

        add_sifra_input.setText("")
        add_film_cb.setCurrentIndex(0)
        add_sala_cb.setCurrentIndex(0)
        add_cena_sb.setValue(0)
        add_vreme_pocetka_time.setTime(QtCore.QTime(0, 0, 0))
        add_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
        for checkbox in add_dani_checkboxes:
            checkbox.setChecked(False)
        show_table()
    add_confirm_button.clicked.connect(add_confirm_button_click)

    def add_cancel_button_click():
        add_sifra_input.setText("")
        add_film_cb.setCurrentIndex(0)
        add_sala_cb.setCurrentIndex(0)
        add_cena_sb.setValue(0)
        add_vreme_pocetka_time.setTime(QtCore.QTime(0, 0, 0))
        add_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
        for checkbox in add_dani_checkboxes:
            checkbox.setChecked(False)
        show_table()
    add_cancel_button.clicked.connect(add_cancel_button_click)

    def add_frame_showEvent(event):
        add_sala_cb.clear()
        add_sala_cb.addItem("")
        for sala in State.db.halls.SelectAll():
            add_sala_cb.addItem(sala.name)
        add_film_cb.clear()
        add_film_cb.addItem("")
        for film in State.db.films.SelectAll():
            add_film_cb.addItem(film.name)
        id = generate_number(1000, 9999)
        while id in [pr.id for pr in State.db.projections.SelectAll()]:
            id = generate_number(1000, 9999)
        add_sifra_input.setText(str(id))
        return QtWidgets.QFrame.showEvent(frame_add, event)
    frame_add.showEvent = add_frame_showEvent

    # # Edit Form
    edit_sifra_input: QtWidgets.QLineEdit = frames["frame_edit"]["sifra_input"]
    edit_sala_cb: QtWidgets.QComboBox = frames["frame_edit"]["sala_cb"]
    edit_film_cb: QtWidgets.QComboBox = frames["frame_edit"]["film_cb"]
    edit_vreme_pocetka_time: QtWidgets.QTimeEdit = frames["frame_edit"]["vreme_pocetka_time"]
    edit_vreme_kraja_time: QtWidgets.QTimeEdit = frames["frame_edit"]["vreme_kraja_time"]
    edit_cena_sb: QtWidgets.QDoubleSpinBox = frames["frame_edit"]["cena_sb"]
    edit_dani_checkboxes: list[QtWidgets.QCheckBox] = frames["frame_edit"]["dani_checkboxes"]
    edit_confirm_button: QtWidgets.QPushButton = frames["frame_edit"]["confirm_button"]
    edit_cancel_button: QtWidgets.QPushButton = frames["frame_edit"]["cancel_button"]

    def edit_calculate_end_time():
        name = edit_film_cb.currentText()
        if name == "" or name not in [f.name for f in State.db.films.SelectAll()]:   
            edit_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
            return
        film: Models.Film = State.db.films.Select(lambda film: film.name == name)[0]
        time: QtCore.QTime = QtCore.QTime(edit_vreme_pocetka_time.time().hour(), edit_vreme_pocetka_time.time().minute())
        time = time.addSecs(film.duration * 60)
        edit_vreme_kraja_time.setTime(time)
    edit_film_cb.currentTextChanged.connect(edit_calculate_end_time)
    edit_vreme_pocetka_time.timeChanged.connect(edit_calculate_end_time)

    def edit_confirm_button_click():
        id = edit_sifra_input.text().strip()
        ime_filma = edit_film_cb.currentText().strip()
        ime_sale = edit_sala_cb.currentText().strip()
        price = edit_cena_sb.value()
        starting_time = edit_vreme_pocetka_time.dateTime().toPyDateTime()
        ending_time = edit_vreme_kraja_time.dateTime().toPyDateTime()
        days = [checkbox.text() for checkbox in edit_dani_checkboxes if checkbox.isChecked()]

        if id == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if ime_filma == "" or ime_filma not in [film.name for film in State.db.films.SelectAll()]:
            MessageBox().warning(tab, "Greška", f"Morate odabrati neki film")
            return
        if ime_sale == "" or ime_sale not in [sala.name for sala in State.db.halls.SelectAll()]:
            MessageBox().warning(tab, "Greška", f"Morate odabrati neku salu")
            return
        if price == 0.00:
            MessageBox().warning(tab, "Greška", f"Morate uneti cenu tickets")
            return
        if len(days) == 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati bar jedan dan projections")
            return
        
        film = State.db.films.Select(lambda film: film.name == ime_filma)[0]
        sala = State.db.halls.Select(lambda sala: sala.name == ime_sale)[0]
        projection = Models.Projection(id, sala.id, film.id, starting_time, ending_time, days, price)
        validated = validate_projection(projection, State.db.projections.SelectAll())
        if validated is not None:   
            error_projection: Models.Projection = State.db.projections.SelectById(validated[1])
            error_film = error_projection.film.get(State.db).name or "?"
            MessageBox().warning(tab, 
                "Greška", 
                f"Preklapanje sa projekcijom filma '{error_film}' ({validated[0]})")
            return

        LocalState.projection_to_edit.film_id = film.id
        LocalState.projection_to_edit.hall_id = sala.id
        LocalState.projection_to_edit.price = price
        LocalState.projection_to_edit.days = days
        LocalState.projection_to_edit.starting_time = starting_time
        LocalState.projection_to_edit.ending_time = ending_time

        edit_sifra_input.setText("")
        edit_film_cb.setCurrentIndex(0)
        edit_sala_cb.setCurrentIndex(0)
        edit_cena_sb.setValue(0)
        edit_vreme_pocetka_time.setTime(QtCore.QTime(0, 0, 0))
        edit_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
        for checkbox in edit_dani_checkboxes:
            checkbox.setChecked(False)
        show_table()
    edit_confirm_button.clicked.connect(edit_confirm_button_click)

    def edit_cancel_button_click():
        edit_sifra_input.setText("")
        edit_film_cb.setCurrentIndex(0)
        edit_sala_cb.setCurrentIndex(0)
        edit_cena_sb.setValue(0)
        edit_vreme_pocetka_time.setTime(QtCore.QTime(0, 0, 0))
        edit_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
        for checkbox in edit_dani_checkboxes:
            checkbox.setChecked(False)
        show_table()
    edit_cancel_button.clicked.connect(edit_cancel_button_click)

    def edit_frame_showEvent(event):
        edit_sala_cb.clear()
        edit_sala_cb.addItem("")
        for sala in State.db.halls.SelectAll():
            edit_sala_cb.addItem(sala.name)
        edit_film_cb.clear()
        edit_film_cb.addItem("")
        for film in State.db.films.SelectAll():
            edit_film_cb.addItem(film.name)
        edit_sifra_input.setText(LocalState.projection_to_edit.id)
        edit_film_cb.setCurrentText(LocalState.projection_to_edit.film.get(State.db).name)
        edit_sala_cb.setCurrentText(LocalState.projection_to_edit.hall.get(State.db).name)
        edit_cena_sb.setValue(LocalState.projection_to_edit.price)
        edit_vreme_pocetka_time.setTime(QtCore.QTime(LocalState.projection_to_edit.starting_time.hour, LocalState.projection_to_edit.starting_time.minute))
        edit_vreme_kraja_time.setTime(QtCore.QTime(LocalState.projection_to_edit.ending_time.hour, LocalState.projection_to_edit.ending_time.minute))
        for checkbox in edit_dani_checkboxes:
            checkbox.setChecked(checkbox.text() in LocalState.projection_to_edit.days)
        return QtWidgets.QFrame.showEvent(frame_add, event)
    frame_edit.showEvent = edit_frame_showEvent

    return tab