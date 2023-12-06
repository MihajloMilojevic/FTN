from PyQt5 import QtWidgets
from screens.manager.cinema_data.films.UI import setupUi
import app.state as State
import screens.manager.cinema_data.films.local_state as LocalState
import database.models as Models
from utils.message_box import MessageBox
from datetime import datetime
from utils.generate_id import generate_number, generate_string

def FilmoviTab():
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
        data = State.db.films.SelectAll()
        table.setRowCount(len(data))
        for index in range(len(data)):
            film: Models.Film  = data[index]
            item = QtWidgets.QTableWidgetItem(film.id)
            # item.setBackground(QtGui.QColor)
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(film.name)
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(", ".join(film.genres))
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(str(film.duration))
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(film.director)
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(", ".join(film.main_roles))
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(film.country)
            table.setItem(index, 6, item)
            item = QtWidgets.QTableWidgetItem(str(film.year))
            table.setItem(index, 7, item)
            item = QtWidgets.QTableWidgetItem(film.description)
            table.setItem(index, 8, item)
        # table.resizeRowsToContents()
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
            MessageBox().warning(tab, "Greška", f"Morate odabrati film za brisanje")
            return
        id = table.item(row, 0).text()
        name = table.item(row, 1).text()
        res = MessageBox().question(tab, "Brisanje filma", f"Da li ste sigurni da želite da obrišete film '{name}'?")
        if res != QtWidgets.QMessageBox.StandardButton.Yes:
            return
        State.db.films.DeleteById(id)
        refresh_table()
    def buttons_edit_click():
        row = table.currentRow()
        if row < 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati film za izmenu")
            return
        id = table.item(row, 0).text()
        LocalState.film_to_edit = State.db.films.SelectById(id)
        show_edit()
    buttons_add.clicked.connect(show_add)
    buttons_delete.clicked.connect(buttons_delete_click)
    buttons_edit.clicked.connect(buttons_edit_click)

    

    # Add Form

    add_checkbox_list: list[QtWidgets.QCheckBox] = frames["frame_add"]["checkbox_list"]
    add_sifra_input: QtWidgets.QLineEdit = frames["frame_add"]["sifra_input"]
    add_naziv_input: QtWidgets.QLineEdit = frames["frame_add"]["naziv_input"]
    add_reziser_input: QtWidgets.QLineEdit = frames["frame_add"]["reziser_input"]
    add_zemlja_input: QtWidgets.QLineEdit = frames["frame_add"]["zemlja_input"]
    add_godina_sb: QtWidgets.QSpinBox = frames["frame_add"]["godina_sb"]
    add_trajanje_sb: QtWidgets.QSpinBox = frames["frame_add"]["trajanje_sb"]
    add_uloge_input: QtWidgets.QTextEdit = frames["frame_add"]["uloge_input"]
    add_opis_input: QtWidgets.QTextEdit = frames["frame_add"]["opis_input"]
    add_confirm_button: QtWidgets.QPushButton = frames["frame_add"]["confirm_button"]
    add_cancel_button: QtWidgets.QPushButton = frames["frame_add"]["cancel_button"]

    def add_confirm_button_click():
        id = add_sifra_input.text().strip()
        name = add_naziv_input.text().strip()
        director = add_reziser_input.text().strip()
        zemlja = add_zemlja_input.text().strip()
        godina = add_godina_sb.value()
        duration = add_trajanje_sb.value()
        description = add_opis_input.toPlainText().replace("\n", " ").strip()
        uloge = [name.strip() for name in add_uloge_input.toPlainText().replace("\n", "").split(",") if name.strip() != ""]
        genres = [checkbox.text() for checkbox in add_checkbox_list if checkbox.isChecked()]

        if id == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if name == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti name filma")
            return
        if director == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti name režisera")
            return
        if zemlja == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti zemlju porekla filma")
            return
        if description == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti zemlju porekla filma")
            return
        if len(uloge) == 0:
            MessageBox().warning(tab, "Greška", f"Morate uneti bar jednu glavnu ulogu")
            return
        if len(genres) == 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati bar jedan zanr")
            return
        

        film = Models.Film(
            id,
            name,
            genres,
            duration,
            director,
            uloge,
            zemlja,
            godina,
            description   
        )
        inserted = State.db.films.Insert(film)

        if not inserted:
            MessageBox().warning(tab, "Greška", f"Film sa ovom šifrom već postoji")
            return

        add_sifra_input.setText("")
        add_naziv_input.setText("")
        add_reziser_input.setText("")
        add_godina_sb.setValue(datetime.now().year)
        add_trajanje_sb.setValue(1)
        add_zemlja_input.setText("")
        add_uloge_input.setText("")
        add_opis_input.setText("")
        for checkbox in add_checkbox_list:
            checkbox.setChecked(False)
        show_table()
    add_confirm_button.clicked.connect(add_confirm_button_click)

    def add_cancel_button_click():
        add_sifra_input.setText("")
        add_naziv_input.setText("")
        add_reziser_input.setText("")
        add_godina_sb.setValue(datetime.now().year)
        add_trajanje_sb.setValue(1)
        add_zemlja_input.setText("")
        add_uloge_input.setText("")
        add_opis_input.setText("")
        for checkbox in add_checkbox_list:
            checkbox.setChecked(False)

        show_table()
    add_cancel_button.clicked.connect(add_cancel_button_click)

    def add_frame_showEvent(event):
        id = generate_string(8, lower=False, digits=False)
        while State.db.films.SelectById(id) is not None:
            id = generate_string(8, lower=False, digits=False)
        add_sifra_input.setText(id)
        return QtWidgets.QFrame.showEvent(frame_add, event)
    frame_add.showEvent = add_frame_showEvent

    # # Edit Form
    edit_checkbox_list: list[QtWidgets.QCheckBox] = frames["frame_edit"]["checkbox_list"]
    edit_sifra_input: QtWidgets.QLineEdit = frames["frame_edit"]["sifra_input"]
    edit_naziv_input: QtWidgets.QLineEdit = frames["frame_edit"]["naziv_input"]
    edit_reziser_input: QtWidgets.QLineEdit = frames["frame_edit"]["reziser_input"]
    edit_zemlja_input: QtWidgets.QLineEdit = frames["frame_edit"]["zemlja_input"]
    edit_godina_sb: QtWidgets.QSpinBox = frames["frame_edit"]["godina_sb"]
    edit_trajanje_sb: QtWidgets.QSpinBox = frames["frame_edit"]["trajanje_sb"]
    edit_uloge_input: QtWidgets.QTextEdit = frames["frame_edit"]["uloge_input"]
    edit_opis_input: QtWidgets.QTextEdit = frames["frame_edit"]["opis_input"]
    edit_confirm_button: QtWidgets.QPushButton = frames["frame_edit"]["confirm_button"]
    edit_cancel_button: QtWidgets.QPushButton = frames["frame_edit"]["cancel_button"]

    def edit_frame_showEvent(event):
        if LocalState.film_to_edit is None:
            show_table()
            return
        edit_sifra_input.setText(LocalState.film_to_edit.id)
        edit_naziv_input.setText(LocalState.film_to_edit.name)
        edit_reziser_input.setText(LocalState.film_to_edit.director)
        edit_godina_sb.setValue(LocalState.film_to_edit.year)
        edit_trajanje_sb.setValue(LocalState.film_to_edit.duration)
        edit_zemlja_input.setText(LocalState.film_to_edit.country)
        edit_uloge_input.setText(", ".join(LocalState.film_to_edit.main_roles))
        edit_opis_input.setText(LocalState.film_to_edit.description)
        for checkbox in edit_checkbox_list:
            checkbox.setChecked(checkbox.text() in LocalState.film_to_edit.genres)
        return QtWidgets.QFrame.showEvent(frame_edit, event)
    frame_edit.showEvent = edit_frame_showEvent

    def edit_confirm_button_click():
        id = edit_sifra_input.text().strip()
        name = edit_naziv_input.text().strip()
        director = edit_reziser_input.text().strip()
        zemlja = edit_zemlja_input.text().strip()
        godina = edit_godina_sb.value()
        duration = edit_trajanje_sb.value()
        description = edit_opis_input.toPlainText().replace("\n", " ")
        uloge = [name.strip() for name in edit_uloge_input.toPlainText().replace("\n", "").split(",") if name.strip() != ""]
        genres = [checkbox.text() for checkbox in edit_checkbox_list if checkbox.isChecked()]

        if id == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if name == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti name filma")
            return
        if director == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti name režisera")
            return
        if zemlja == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti zemlju porekla filma")
            return
        if description == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti zemlju porekla filma")
            return
        if len(uloge) == 0:
            MessageBox().warning(tab, "Greška", f"Morate uneti bar jednu glavnu ulogu")
            return
        if len(genres) == 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati bar jedan zanr")
            return
        
        LocalState.film_to_edit.name = name
        LocalState.film_to_edit.director = director
        LocalState.film_to_edit.main_roles = uloge
        LocalState.film_to_edit.year = godina
        LocalState.film_to_edit.description = description
        LocalState.film_to_edit.genres = genres
        LocalState.film_to_edit.duration = duration
        LocalState.film_to_edit.country = zemlja

        edit_sifra_input.setText("")
        edit_naziv_input.setText("")
        edit_reziser_input.setText("")
        edit_godina_sb.setValue(datetime.now().year)
        edit_trajanje_sb.setValue(1)
        edit_zemlja_input.setText("")
        edit_uloge_input.setText("")
        edit_opis_input.setText("")
        for checkbox in edit_checkbox_list:
            checkbox.setChecked(False)
        show_table()
    edit_confirm_button.clicked.connect(edit_confirm_button_click)

    def edit_cancel_button_click():
        edit_sifra_input.setText("")
        edit_naziv_input.setText("")
        edit_reziser_input.setText("")
        edit_godina_sb.setValue(datetime.now().year)
        edit_trajanje_sb.setValue(1)
        edit_zemlja_input.setText("")
        edit_uloge_input.setText("")
        edit_opis_input.setText("")
        for checkbox in edit_checkbox_list:
            checkbox.setChecked(False)
        show_table()
    edit_cancel_button.clicked.connect(edit_cancel_button_click)

    return tab