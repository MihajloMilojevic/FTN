from PyQt5 import QtCore, QtGui, QtWidgets
from Screens.Menadzer.Data.Sale.UI import setupUi
import App.State as State
import Database.Models as Models


def SaleTab():
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

    show_table()

    # Buttons Frame

    buttons_add: QtWidgets.QPushButton = frames["frame_buttons"]["add_button"]
    buttons_delete: QtWidgets.QPushButton = frames["frame_buttons"]["delete_button"]
    buttons_edit: QtWidgets.QPushButton = frames["frame_buttons"]["edit_button"]

    buttons_add.clicked.connect(show_add)
    buttons_edit.clicked.connect(show_edit)

    # Table

    table = frame_table
    def table_showEvent(event):
        table.setRowCount(0)
        data = State.db.sale.SelectAll()
        table.setRowCount(len(data))
        for index in range(len(data)):
            sala: Models.Sala  = data[index]
            item = QtWidgets.QTableWidgetItem(sala.sifra)
            # item.setBackground(QtGui.QColor)
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(sala.naziv)
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(str(sala.broj_redova))
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(str(sala.broj_kolona))
            table.setItem(index, 3, item)

        return QtWidgets.QTableWidget.showEvent(table, event)
    table.showEvent = table_showEvent


    # Add Form

    add_sifra_input: QtWidgets.QLineEdit = frames["frame_add"]["sifra_input"]
    add_naziv_input: QtWidgets.QLineEdit = frames["frame_add"]["naziv_input"]
    add_redovi_sb: QtWidgets.QSpinBox = frames["frame_add"]["redovi_sb"]
    add_sedista_sb: QtWidgets.QSpinBox = frames["frame_add"]["sedista_sb"]
    add_potvrdi_button: QtWidgets.QPushButton = frames["frame_add"]["potvrdi_button"]
    add_odustani_button: QtWidgets.QPushButton = frames["frame_add"]["odustani_button"]

    def add_potvrdi_button_click():
        sifra = add_sifra_input.text()
        naziv = add_naziv_input.text()
        broj_redova = add_redovi_sb.value()
        broj_sedista = add_sedista_sb.value()

        if sifra == "":
            QtWidgets.QMessageBox.warning(tab, "Greška", f"Morate uneti šifru")
            return
        if naziv == "":
            QtWidgets.QMessageBox.warning(tab, "Greška", f"Morate uneti naziv")
            return
        if broj_redova < 1:
            QtWidgets.QMessageBox.warning(tab, "Greška", f"Sala mora ima prirodan broj redova")
            return
        if broj_sedista < 1:
            QtWidgets.QMessageBox.warning(tab, "Greška", f"Sala mora ima prirodan broj sedišta")
            return

        sala = Models.Sala(sifra, naziv, broj_redova, broj_sedista)
        inserted = State.db.sale.Insert(sala)

        if not inserted:
            QtWidgets.QMessageBox.warning(tab, "Greška", f"Sala sa unetom šifrom već postoji")
            return

        add_sifra_input.setText("")
        add_naziv_input.setText("")
        add_redovi_sb.setValue(1)
        add_sedista_sb.setValue(1)
        show_table()
    add_potvrdi_button.clicked.connect(add_potvrdi_button_click)

    def add_odustani_button_click():
        add_sifra_input.setText("")
        add_naziv_input.setText("")
        add_redovi_sb.setValue(1)
        add_sedista_sb.setValue(1)
        show_table()
    add_odustani_button.clicked.connect(add_odustani_button_click)

    # Edit Form
    edit_sifra_input: QtWidgets.QLineEdit = frames["frame_edit"]["sifra_input"]
    edit_naziv_input: QtWidgets.QLineEdit = frames["frame_edit"]["naziv_input"]
    edit_redovi_sb: QtWidgets.QSpinBox = frames["frame_edit"]["redovi_sb"]
    edit_sedista_sb: QtWidgets.QSpinBox = frames["frame_edit"]["sedista_sb"]
    edit_potvrdi_button: QtWidgets.QPushButton = frames["frame_edit"]["potvrdi_button"]
    edit_odustani_button: QtWidgets.QPushButton = frames["frame_edit"]["odustani_button"]

    def edit_odustani_button_click():
        edit_sifra_input.setText("")
        edit_naziv_input.setText("")
        edit_redovi_sb.setValue(1)
        edit_sedista_sb.setValue(1)
        show_table()
    edit_odustani_button.clicked.connect(edit_odustani_button_click)

    return tab