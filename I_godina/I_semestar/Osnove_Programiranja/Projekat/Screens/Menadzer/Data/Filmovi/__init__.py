from PyQt5 import QtCore, QtGui, QtWidgets
from Screens.Menadzer.Data.Filmovi.UI import setupUi
import App.State as State
import Screens.Menadzer.Data.Filmovi.LocalState as LocalState
import Database.Models as Models
from Utils.MessageBox import MessageBox
import Utils.GenerateID 
from datetime import datetime

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
        data = State.db.filmovi.SelectAll()
        table.setRowCount(len(data))
        for index in range(len(data)):
            film: Models.Film  = data[index]
            item = QtWidgets.QTableWidgetItem(film.sifra)
            # item.setBackground(QtGui.QColor)
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(film.naziv)
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(", ".join(film.zanrovi))
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(str(film.trajanje))
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(film.reziser)
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(", ".join(film.glavne_uloge))
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(film.zemlja_porekla)
            table.setItem(index, 6, item)
            item = QtWidgets.QTableWidgetItem(str(film.godina_proizvodnje))
            table.setItem(index, 7, item)
            item = QtWidgets.QTableWidgetItem(film.opis)
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
        State.db.filmovi.DeleteById(id)
        refresh_table()
    def buttons_edit_click():
        row = table.currentRow()
        if row < 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati film za izmenu")
            return
        id = table.item(row, 0).text()
        LocalState.film_to_edit = State.db.filmovi.SelectById(id)
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
    add_potvrdi_button: QtWidgets.QPushButton = frames["frame_add"]["potvrdi_button"]
    add_odustani_button: QtWidgets.QPushButton = frames["frame_add"]["odustani_button"]

    def add_potvrdi_button_click():
        sifra = add_sifra_input.text()
        naziv = add_naziv_input.text()
        reziser = add_reziser_input.text()
        zemlja = add_zemlja_input.text()
        godina = add_godina_sb.value()
        trajanje = add_trajanje_sb.value()
        opis = add_opis_input.toPlainText().replace("\n", " ")
        uloge = [ime.strip() for ime in add_uloge_input.toPlainText().replace("\n", "").split(",") if ime.strip() != ""]
        zanrovi = [checkbox.text() for checkbox in add_checkbox_list if checkbox.isChecked()]

        if sifra == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if naziv == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti naziv filma")
            return
        if reziser == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti ime režisera")
            return
        if zemlja == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti zemlju porekla filma")
            return
        if opis == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti zemlju porekla filma")
            return
        if len(uloge) == 0:
            MessageBox().warning(tab, "Greška", f"Morate uneti bar jednu glavnu ulogu")
            return
        if len(zanrovi) == 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati bar jedan zanr")
            return
        

        film = Models.Film(
            sifra,
            naziv,
            zanrovi,
            trajanje,
            reziser,
            uloge,
            zemlja,
            godina,
            opis   
        )
        inserted = State.db.filmovi.Insert(film)

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
    add_potvrdi_button.clicked.connect(add_potvrdi_button_click)

    def add_odustani_button_click():
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
    add_odustani_button.clicked.connect(add_odustani_button_click)

    def add_frame_showEvent(event):
        id = Utils.GenerateID.generateString(8, lower=False, digits=False)
        while State.db.filmovi.SelectById(id) is not None:
            id = Utils.GenerateID.generateString(8, lower=False, digits=False)
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
    edit_potvrdi_button: QtWidgets.QPushButton = frames["frame_edit"]["potvrdi_button"]
    edit_odustani_button: QtWidgets.QPushButton = frames["frame_edit"]["odustani_button"]

    def edit_frame_showEvent(event):
        if LocalState.film_to_edit is None:
            show_table()
            return
        edit_sifra_input.setText(LocalState.film_to_edit.sifra)
        edit_naziv_input.setText(LocalState.film_to_edit.naziv)
        edit_reziser_input.setText(LocalState.film_to_edit.reziser)
        edit_godina_sb.setValue(LocalState.film_to_edit.godina_proizvodnje)
        edit_trajanje_sb.setValue(LocalState.film_to_edit.trajanje)
        edit_zemlja_input.setText(LocalState.film_to_edit.zemlja_porekla)
        edit_uloge_input.setText(", ".join(LocalState.film_to_edit.glavne_uloge))
        edit_opis_input.setText(LocalState.film_to_edit.opis)
        for checkbox in edit_checkbox_list:
            checkbox.setChecked(checkbox.text() in LocalState.film_to_edit.zanrovi)
        return QtWidgets.QFrame.showEvent(frame_edit, event)
    frame_edit.showEvent = edit_frame_showEvent

    def edit_potvrdi_button_click():
        sifra = edit_sifra_input.text()
        naziv = edit_naziv_input.text()
        reziser = edit_reziser_input.text()
        zemlja = edit_zemlja_input.text()
        godina = edit_godina_sb.value()
        trajanje = edit_trajanje_sb.value()
        opis = edit_opis_input.toPlainText().replace("\n", " ")
        uloge = [ime.strip() for ime in edit_uloge_input.toPlainText().replace("\n", "").split(",") if ime.strip() != ""]
        zanrovi = [checkbox.text() for checkbox in edit_checkbox_list if checkbox.isChecked()]

        if sifra == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if naziv == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti naziv filma")
            return
        if reziser == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti ime režisera")
            return
        if zemlja == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti zemlju porekla filma")
            return
        if opis == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti zemlju porekla filma")
            return
        if len(uloge) == 0:
            MessageBox().warning(tab, "Greška", f"Morate uneti bar jednu glavnu ulogu")
            return
        if len(zanrovi) == 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati bar jedan zanr")
            return
        
        LocalState.film_to_edit.naziv = naziv
        LocalState.film_to_edit.reziser = reziser
        LocalState.film_to_edit.glavne_uloge = uloge
        LocalState.film_to_edit.godina_proizvodnje = godina
        LocalState.film_to_edit.opis = opis
        LocalState.film_to_edit.zanrovi = zanrovi
        LocalState.film_to_edit.trajanje = trajanje
        LocalState.film_to_edit.zemlja_porekla = zemlja

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
    edit_potvrdi_button.clicked.connect(edit_potvrdi_button_click)

    def edit_odustani_button_click():
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
    edit_odustani_button.clicked.connect(edit_odustani_button_click)

    return tab