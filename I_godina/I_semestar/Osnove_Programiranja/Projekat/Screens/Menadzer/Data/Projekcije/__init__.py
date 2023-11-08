from PyQt5 import QtCore, QtGui, QtWidgets
from Screens.Menadzer.Data.Projekcije.UI import setupUi
import App.State as State
import Screens.Menadzer.Data.Projekcije.LocalState as LocalState
import Database.Models as Models
from Utils.MessageBox import MessageBox
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
            item = QtWidgets.QTableWidgetItem(datetime.strftime(projekcija.vreme_pocetka, "%d.%m.%Y"))
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(datetime.strftime(projekcija.vreme_kraja, "%d.%m.%Y"))
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(str(projekcija.cena))
            table.setItem(index, 5, item)
        table.resizeColumnsToContents()
    def table_showEvent(event):
        refresh_table()
        return QtWidgets.QTableWidget.showEvent(table, event)
    table.showEvent = table_showEvent


    # Buttons Frame

    buttons_add: QtWidgets.QPushButton = frames["frame_buttons"]["add_button"]
    buttons_delete: QtWidgets.QPushButton = frames["frame_buttons"]["delete_button"]
    buttons_edit: QtWidgets.QPushButton = frames["frame_buttons"]["edit_button"]
    # def buttons_delete_click():
    #     row = table.currentRow()
    #     if row < 0:
    #         MessageBox().warning(tab, "Greška", f"Morate odabrati salu za brisanje")
    #         return
    #     id = table.item(row, 0).text()
    #     name = table.item(row, 1).text()
    #     res = MessageBox().question(tab, "Brisanje sale", f"Da li ste sigurni da želite da obrišete salu '{name}'?")
    #     if res != QtWidgets.QMessageBox.StandardButton.Yes:
    #         return
    #     State.db.sale.DeleteById(id)
    #     refresh_table()
    # def buttons_edit_click():
    #     row = table.currentRow()
    #     if row < 0:
    #         MessageBox().warning(tab, "Greška", f"Morate odabrati salu za izmenu")
    #         return
    #     id = table.item(row, 0).text()
    #     LocalState.sala_to_edit = State.db.sale.SelectById(id)
    #     show_edit()
    buttons_add.clicked.connect(show_add)
    # buttons_delete.clicked.connect(buttons_delete_click)
    # buttons_edit.clicked.connect(buttons_edit_click)

    

    # Add Form

    add_sifra_input: QtWidgets.QLineEdit = frames["frame_add"]["sifra_input"]
    add_sala_cb: QtWidgets.QComboBox = frames["frame_add"]["sala_cb"]
    add_film_cb: QtWidgets.QComboBox = frames["frame_add"]["film_cb"]
    add_vreme_pocetka_time: QtWidgets.QTimeEdit = frames["frame_add"]["vreme_pocetka_time"]
    add_vreme_kraja_time: QtWidgets.QTimeEdit = frames["frame_add"]["vreme_kraja_time"]
    add_cena_sb: QtWidgets.QSpinBox = frames["frame_add"]["cena_sb"]
    add_potvrdi_button: QtWidgets.QPushButton = frames["frame_add"]["potvrdi_button"]
    add_odustani_button: QtWidgets.QPushButton = frames["frame_add"]["odustani_button"]

    def calculate_end_time():
        naziv = add_film_cb.currentText()
        if naziv == "" or naziv not in [f.naziv for f in State.db.filmovi.SelectAll()]:   
            add_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
            return
        film: Models.Film = State.db.filmovi.Select(lambda film: film.naziv == naziv)[0]
        time: QtCore.QTime = QtCore.QTime(add_vreme_pocetka_time.time().hour(), add_vreme_pocetka_time.time().minute())
        time = time.addSecs(film.trajanje * 60)
        add_vreme_kraja_time.setTime(time)
    add_film_cb.currentTextChanged.connect(calculate_end_time)
    add_vreme_pocetka_time.timeChanged.connect(calculate_end_time)

    # def add_potvrdi_button_click():
    #     sifra = add_sifra_input.text()
    #     naziv = add_naziv_input.text()
    #     broj_redova = add_redovi_sb.value()
    #     broj_sedista = add_sedista_sb.value()

    #     if sifra == "":
    #         MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
    #         return
    #     if naziv == "":
    #         MessageBox().warning(tab, "Greška", f"Morate uneti naziv")
    #         return
    #     if broj_redova < 1:
    #         MessageBox().warning(tab, "Greška", f"Sala mora ima prirodan broj redova")
    #         return
    #     if broj_sedista < 1:
    #         MessageBox().warning(tab, "Greška", f"Sala mora ima prirodan broj sedišta")
    #         return

    #     sala = Models.Sala(sifra, naziv, broj_redova, broj_sedista)
    #     inserted = State.db.sale.Insert(sala)

    #     if not inserted:
    #         MessageBox().warning(tab, "Greška", f"Sala sa unetom šifrom već postoji")
    #         return

    #     add_sifra_input.setText("")
    #     add_naziv_input.setText("")
    #     add_redovi_sb.setValue(1)
    #     add_sedista_sb.setValue(1)
    #     show_table()
    # add_potvrdi_button.clicked.connect(add_potvrdi_button_click)

    def add_odustani_button_click():
        add_sifra_input.setText("")
        add_film_cb.setCurrentIndex(0)
        add_sala_cb.setCurrentIndex(0)
        add_cena_sb.setValue(0)
        add_vreme_pocetka_time.setTime(QtCore.QTime(0, 0, 0))
        add_vreme_kraja_time.setTime(QtCore.QTime(0, 0, 0))
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
        return QtWidgets.QFrame.showEvent(frame_add, event)
    frame_add.showEvent = add_frame_showEvent

    # # Edit Form
    # edit_sifra_input: QtWidgets.QLineEdit = frames["frame_edit"]["sifra_input"]
    # edit_naziv_input: QtWidgets.QLineEdit = frames["frame_edit"]["naziv_input"]
    # edit_redovi_sb: QtWidgets.QSpinBox = frames["frame_edit"]["redovi_sb"]
    # edit_sedista_sb: QtWidgets.QSpinBox = frames["frame_edit"]["sedista_sb"]
    # edit_potvrdi_button: QtWidgets.QPushButton = frames["frame_edit"]["potvrdi_button"]
    # edit_odustani_button: QtWidgets.QPushButton = frames["frame_edit"]["odustani_button"]

    # def edit_frame_showEvent(event):
    #     edit_sifra_input.setText(LocalState.sala_to_edit.sifra)
    #     edit_sifra_input.setEnabled(False)
    #     edit_naziv_input.setText(LocalState.sala_to_edit.naziv)
    #     edit_redovi_sb.setValue(LocalState.sala_to_edit.broj_redova)
    #     edit_sedista_sb.setValue(LocalState.sala_to_edit.broj_sedista)
    #     return QtWidgets.QFrame.showEvent(frame_edit, event)
    # frame_edit.showEvent = edit_frame_showEvent

    # def edit_potvrdi_button_click():
    #     naziv = edit_naziv_input.text()
    #     broj_redova = edit_redovi_sb.value()
    #     broj_sedista = edit_sedista_sb.value()
    #     if broj_redova < 1:
    #         MessageBox().warning(tab, "Greška", "Broj redova mora biti prirodan broj")
    #         show_table()
    #         return
    #     if broj_sedista < 1:
    #         MessageBox().warning(tab, "Greška", "Broj sedišta mora biti prirodan broj")
    #         show_table()
    #         return
    #     LocalState.sala_to_edit.naziv = naziv
    #     LocalState.sala_to_edit.broj_redova = broj_redova
    #     LocalState.sala_to_edit.broj_sedista = broj_sedista
    #     show_table()
    # edit_potvrdi_button.clicked.connect(edit_potvrdi_button_click)

    # def edit_odustani_button_click():
    #     edit_sifra_input.setText("")
    #     edit_naziv_input.setText("")
    #     edit_redovi_sb.setValue(1)
    #     edit_sedista_sb.setValue(1)
    #     show_table()
    # edit_odustani_button.clicked.connect(edit_odustani_button_click)

    return tab