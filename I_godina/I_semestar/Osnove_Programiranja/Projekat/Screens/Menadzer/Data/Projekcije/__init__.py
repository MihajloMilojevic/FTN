from PyQt5 import QtCore, QtGui, QtWidgets
from Screens.Menadzer.Data.Projekcije.UI import setupUi
import App.State as State
import Screens.Menadzer.Data.Projekcije.LocalState as LocalState
import Database.Models as Models
from Utils.MessageBox import MessageBox
from Utils.GenerateID import generateNumber
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
        data = State.db.projekcije.SelectAll()
        table.setRowCount(len(data))
        for index in range(len(data)):
            projekcija: Models.Projekcija  = data[index]
            sala: Models.Sala = projekcija.sala.get(State.db)
            film: Models.Film = projekcija.film.get(State.db)
            item = QtWidgets.QTableWidgetItem(projekcija.sifra)
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(sala.naziv)
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(film.naziv)
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(datetime.strftime(projekcija.vreme_pocetka, "%H:%M"))
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(datetime.strftime(projekcija.vreme_kraja, "%H:%M"))
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(str(projekcija.cena))
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(", ".join(projekcija.dani))
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
        res = MessageBox().question(tab, "Brisanje projekcije", f"Da li ste sigurni da želite da obrišete projekciju za film '{film}'?")
        if res != QtWidgets.QMessageBox.StandardButton.Yes:
            return
        State.db.projekcije.DeleteById(id)
        refresh_table()
    def buttons_edit_click():
        row = table.currentRow()
        if row < 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati projekciju za izmenu")
            return
        id = table.item(row, 0).text()
        LocalState.projekcija_to_edit = State.db.projekcije.SelectById(id)
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
    add_potvrdi_button: QtWidgets.QPushButton = frames["frame_add"]["potvrdi_button"]
    add_odustani_button: QtWidgets.QPushButton = frames["frame_add"]["odustani_button"]

    def add_calculate_end_time():
        naziv = add_film_cb.currentText()
        if naziv == "" or naziv not in [f.naziv for f in State.db.filmovi.SelectAll()]:   
            add_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
            return
        film: Models.Film = State.db.filmovi.Select(lambda film: film.naziv == naziv)[0]
        time: QtCore.QTime = QtCore.QTime(add_vreme_pocetka_time.time().hour(), add_vreme_pocetka_time.time().minute())
        time = time.addSecs(film.trajanje * 60)
        add_vreme_kraja_time.setTime(time)
    add_film_cb.currentTextChanged.connect(add_calculate_end_time)
    add_vreme_pocetka_time.timeChanged.connect(add_calculate_end_time)

    def add_potvrdi_button_click():
        sifra = add_sifra_input.text()
        ime_filma = add_film_cb.currentText()
        ime_sale = add_sala_cb.currentText()
        cena = add_cena_sb.value()
        vreme_pocetka = add_vreme_pocetka_time.dateTime().toPyDateTime()
        vreme_kraja = add_vreme_kraja_time.dateTime().toPyDateTime()
        dani = [checkbox.text() for checkbox in add_dani_checkboxes if checkbox.isChecked()]

        if sifra == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if ime_filma == "" or ime_filma not in [film.naziv for film in State.db.filmovi.SelectAll()]:
            MessageBox().warning(tab, "Greška", f"Morate odabrati neki film")
            return
        if ime_sale == "" or ime_sale not in [sala.naziv for sala in State.db.sale.SelectAll()]:
            MessageBox().warning(tab, "Greška", f"Morate odabrati neku salu")
            return
        if cena == 0.00:
            MessageBox().warning(tab, "Greška", f"Morate uneti cenu karte")
            return
        if len(dani) == 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati bar jedan dan projekcije")
            return
        
        film = State.db.filmovi.Select(lambda film: film.naziv == ime_filma)[0]
        sala = State.db.sale.Select(lambda sala: sala.naziv == ime_sale)[0]

        projekcija = Models.Projekcija(sifra, sala.sifra, film.sifra, vreme_pocetka, vreme_kraja, dani, cena)
        inserted = State.db.projekcije.Insert(projekcija)

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
    add_potvrdi_button.clicked.connect(add_potvrdi_button_click)

    def add_odustani_button_click():
        add_sifra_input.setText("")
        add_film_cb.setCurrentIndex(0)
        add_sala_cb.setCurrentIndex(0)
        add_cena_sb.setValue(0)
        add_vreme_pocetka_time.setTime(QtCore.QTime(0, 0, 0))
        add_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
        for checkbox in add_dani_checkboxes:
            checkbox.setChecked(False)
        show_table()
    add_odustani_button.clicked.connect(add_odustani_button_click)

    def add_frame_showEvent(event):
        add_sala_cb.clear()
        add_sala_cb.addItem("")
        for sala in State.db.sale.SelectAll():
            add_sala_cb.addItem(sala.naziv)
        add_film_cb.clear()
        add_film_cb.addItem("")
        for film in State.db.filmovi.SelectAll():
            add_film_cb.addItem(film.naziv)
        sifra = generateNumber(1000, 9999)
        while sifra in [pr.sifra for pr in State.db.projekcije.SelectAll()]:
            sifra = generateNumber(1000, 9999)
        add_sifra_input.setText(str(sifra))
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
    edit_potvrdi_button: QtWidgets.QPushButton = frames["frame_edit"]["potvrdi_button"]
    edit_odustani_button: QtWidgets.QPushButton = frames["frame_edit"]["odustani_button"]

    def edit_calculate_end_time():
        naziv = edit_film_cb.currentText()
        if naziv == "" or naziv not in [f.naziv for f in State.db.filmovi.SelectAll()]:   
            edit_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
            return
        film: Models.Film = State.db.filmovi.Select(lambda film: film.naziv == naziv)[0]
        time: QtCore.QTime = QtCore.QTime(edit_vreme_pocetka_time.time().hour(), edit_vreme_pocetka_time.time().minute())
        time = time.addSecs(film.trajanje * 60)
        edit_vreme_kraja_time.setTime(time)
    edit_film_cb.currentTextChanged.connect(edit_calculate_end_time)
    edit_vreme_pocetka_time.timeChanged.connect(edit_calculate_end_time)

    def edit_potvrdi_button_click():
        sifra = edit_sifra_input.text()
        ime_filma = edit_film_cb.currentText()
        ime_sale = edit_sala_cb.currentText()
        cena = edit_cena_sb.value()
        vreme_pocetka = edit_vreme_pocetka_time.dateTime().toPyDateTime()
        vreme_kraja = edit_vreme_kraja_time.dateTime().toPyDateTime()
        dani = [checkbox.text() for checkbox in edit_dani_checkboxes if checkbox.isChecked()]

        if sifra == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if ime_filma == "" or ime_filma not in [film.naziv for film in State.db.filmovi.SelectAll()]:
            MessageBox().warning(tab, "Greška", f"Morate odabrati neki film")
            return
        if ime_sale == "" or ime_sale not in [sala.naziv for sala in State.db.sale.SelectAll()]:
            MessageBox().warning(tab, "Greška", f"Morate odabrati neku salu")
            return
        if cena == 0.00:
            MessageBox().warning(tab, "Greška", f"Morate uneti cenu karte")
            return
        if len(dani) == 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati bar jedan dan projekcije")
            return
        
        film = State.db.filmovi.Select(lambda film: film.naziv == ime_filma)[0]
        sala = State.db.sale.Select(lambda sala: sala.naziv == ime_sale)[0]

        LocalState.projekcija_to_edit.sifra_filma = film.sifra
        LocalState.projekcija_to_edit.sifra_sale = sala.sifra
        LocalState.projekcija_to_edit.cena = cena
        LocalState.projekcija_to_edit.dani = dani
        LocalState.projekcija_to_edit.vreme_pocetka = vreme_pocetka
        LocalState.projekcija_to_edit.vreme_kraja = vreme_kraja

        edit_sifra_input.setText("")
        edit_film_cb.setCurrentIndex(0)
        edit_sala_cb.setCurrentIndex(0)
        edit_cena_sb.setValue(0)
        edit_vreme_pocetka_time.setTime(QtCore.QTime(0, 0, 0))
        edit_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
        for checkbox in edit_dani_checkboxes:
            checkbox.setChecked(False)
        show_table()
    edit_potvrdi_button.clicked.connect(edit_potvrdi_button_click)

    def edit_odustani_button_click():
        edit_sifra_input.setText("")
        edit_film_cb.setCurrentIndex(0)
        edit_sala_cb.setCurrentIndex(0)
        edit_cena_sb.setValue(0)
        edit_vreme_pocetka_time.setTime(QtCore.QTime(0, 0, 0))
        edit_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
        for checkbox in edit_dani_checkboxes:
            checkbox.setChecked(False)
        show_table()
    edit_odustani_button.clicked.connect(edit_odustani_button_click)

    def edit_frame_showEvent(event):
        edit_sala_cb.clear()
        edit_sala_cb.addItem("")
        for sala in State.db.sale.SelectAll():
            edit_sala_cb.addItem(sala.naziv)
        edit_film_cb.clear()
        edit_film_cb.addItem("")
        for film in State.db.filmovi.SelectAll():
            edit_film_cb.addItem(film.naziv)
        edit_sifra_input.setText(LocalState.projekcija_to_edit.sifra)
        edit_film_cb.setCurrentText(LocalState.projekcija_to_edit.film.get(State.db).naziv)
        edit_sala_cb.setCurrentText(LocalState.projekcija_to_edit.sala.get(State.db).naziv)
        edit_cena_sb.setValue(LocalState.projekcija_to_edit.cena)
        edit_vreme_pocetka_time.setTime(QtCore.QTime(LocalState.projekcija_to_edit.vreme_pocetka.hour, LocalState.projekcija_to_edit.vreme_pocetka.minute))
        edit_vreme_kraja_time.setTime(QtCore.QTime(LocalState.projekcija_to_edit.vreme_kraja.hour, LocalState.projekcija_to_edit.vreme_kraja.minute))
        for checkbox in edit_dani_checkboxes:
            checkbox.setChecked(checkbox.text() in LocalState.projekcija_to_edit.dani)
        return QtWidgets.QFrame.showEvent(frame_add, event)
    frame_edit.showEvent = edit_frame_showEvent

    return tab