from PyQt5 import QtCore, QtGui, QtWidgets
from Screens.Manager.Data.Sale.UI import setupUi
import App.State as State
import Screens.Manager.Data.Sale.LocalState as LocalState
import Database.Models as Models
from Utils.MessageBox import MessageBox

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

    def showEvent(event):
        show_table()
        return QtWidgets.QWidget.showEvent(tab, event)
    tab.showEvent = showEvent

    show_table()

    # Table

    table = frame_table
    def refresh_table():
        table.setRowCount(0)
        data = State.db.halls.SelectAll()
        table.setRowCount(len(data))
        for index in range(len(data)):
            sala: Models.Hall  = data[index]
            item = QtWidgets.QTableWidgetItem(sala.id)
            # item.setBackground(QtGui.QColor)
            table.setItem(index, 0, item)
            item = QtWidgets.QTableWidgetItem(sala.name)
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(str(sala.row_count))
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(str(sala.seats_per_row))
            table.setItem(index, 3, item)
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
            MessageBox().warning(tab, "Greška", f"Morate odabrati salu za brisanje")
            return
        id = table.item(row, 0).text()
        name = table.item(row, 1).text()
        res = MessageBox().question(tab, "Brisanje halls", f"Da li ste sigurni da želite da obrišete salu '{name}'?")
        if res != QtWidgets.QMessageBox.StandardButton.Yes:
            return
        State.db.halls.DeleteById(id)
        refresh_table()
    def buttons_edit_click():
        row = table.currentRow()
        if row < 0:
            MessageBox().warning(tab, "Greška", f"Morate odabrati salu za izmenu")
            return
        id = table.item(row, 0).text()
        LocalState.sala_to_edit = State.db.halls.SelectById(id)
        show_edit()
    buttons_add.clicked.connect(show_add)
    buttons_delete.clicked.connect(buttons_delete_click)
    buttons_edit.clicked.connect(buttons_edit_click)

    

    # Add Form

    add_sifra_input: QtWidgets.QLineEdit = frames["frame_add"]["sifra_input"]
    add_naziv_input: QtWidgets.QLineEdit = frames["frame_add"]["naziv_input"]
    add_redovi_sb: QtWidgets.QSpinBox = frames["frame_add"]["redovi_sb"]
    add_sedista_sb: QtWidgets.QSpinBox = frames["frame_add"]["sedista_sb"]
    add_confirm_button: QtWidgets.QPushButton = frames["frame_add"]["confirm_button"]
    add_cancel_button: QtWidgets.QPushButton = frames["frame_add"]["cancel_button"]

    def add_confirm_button_click():
        id = add_sifra_input.text()
        name = add_naziv_input.text()
        row_count = add_redovi_sb.value()
        seats_per_row = add_sedista_sb.value()

        if id == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti šifru")
            return
        if name == "":
            MessageBox().warning(tab, "Greška", f"Morate uneti name")
            return
        if row_count < 1:
            MessageBox().warning(tab, "Greška", f"Hall mora ima prirodan broj redova")
            return
        if seats_per_row < 1:
            MessageBox().warning(tab, "Greška", f"Hall mora ima prirodan broj sedišta")
            return

        sala = Models.Hall(id, name, row_count, seats_per_row)
        inserted = State.db.halls.Insert(sala)

        if not inserted:
            MessageBox().warning(tab, "Greška", f"Hall sa unetom šifrom već postoji")
            return

        add_sifra_input.setText("")
        add_naziv_input.setText("")
        add_redovi_sb.setValue(1)
        add_sedista_sb.setValue(1)
        show_table()
    add_confirm_button.clicked.connect(add_confirm_button_click)

    def add_cancel_button_click():
        add_sifra_input.setText("")
        add_naziv_input.setText("")
        add_redovi_sb.setValue(1)
        add_sedista_sb.setValue(1)
        show_table()
    add_cancel_button.clicked.connect(add_cancel_button_click)

    def add_frame_showEvent(event):
        add_sifra_input.setEnabled(True)
        return QtWidgets.QFrame.showEvent(frame_add, event)
    frame_add.showEvent = add_frame_showEvent

    # Edit Form
    edit_sifra_input: QtWidgets.QLineEdit = frames["frame_edit"]["sifra_input"]
    edit_naziv_input: QtWidgets.QLineEdit = frames["frame_edit"]["naziv_input"]
    edit_redovi_sb: QtWidgets.QSpinBox = frames["frame_edit"]["redovi_sb"]
    edit_sedista_sb: QtWidgets.QSpinBox = frames["frame_edit"]["sedista_sb"]
    edit_confirm_button: QtWidgets.QPushButton = frames["frame_edit"]["confirm_button"]
    edit_cancel_button: QtWidgets.QPushButton = frames["frame_edit"]["cancel_button"]

    def edit_frame_showEvent(event):
        edit_sifra_input.setText(LocalState.sala_to_edit.id)
        edit_sifra_input.setEnabled(False)
        edit_naziv_input.setText(LocalState.sala_to_edit.name)
        edit_redovi_sb.setValue(LocalState.sala_to_edit.row_count)
        edit_sedista_sb.setValue(LocalState.sala_to_edit.seats_per_row)
        return QtWidgets.QFrame.showEvent(frame_edit, event)
    frame_edit.showEvent = edit_frame_showEvent

    def edit_confirm_button_click():
        name = edit_naziv_input.text()
        row_count = edit_redovi_sb.value()
        seats_per_row = edit_sedista_sb.value()
        if row_count < 1:
            MessageBox().warning(tab, "Greška", "Broj redova mora biti prirodan broj")
            show_table()
            return
        if seats_per_row < 1:
            MessageBox().warning(tab, "Greška", "Broj sedišta mora biti prirodan broj")
            show_table()
            return
        LocalState.sala_to_edit.name = name
        LocalState.sala_to_edit.row_count = row_count
        LocalState.sala_to_edit.seats_per_row = seats_per_row
        show_table()
    edit_confirm_button.clicked.connect(edit_confirm_button_click)

    def edit_cancel_button_click():
        edit_sifra_input.setText("")
        edit_naziv_input.setText("")
        edit_redovi_sb.setValue(1)
        edit_sedista_sb.setValue(1)
        show_table()
    edit_cancel_button.clicked.connect(edit_cancel_button_click)

    return tab