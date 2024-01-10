from PyQt5 import QtCore, QtGui, QtWidgets
from utils.get_path import get_relative_path
from database.models.enums import Days

def setupUi(tab: QtWidgets.QWidget):

    # main layout
    layout = QtWidgets.QVBoxLayout()
    layout.setObjectName("layout")
    layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter|QtCore.Qt.AlignmentFlag.AlignHCenter)

    frame_buttons = buttons_frame(layout)
    frame_table = table_frame(layout)
    frame_add = form(layout, "Dodaj projekciju")
    frame_edit = form(layout, "Sačuvaj izemene")

    tab.setLayout(layout)

    return {
        "frame_buttons": frame_buttons,
        "frame_table": frame_table,
        "frame_add": frame_add,
        "frame_edit": frame_edit
    }

def buttons_frame(parent_layout: QtWidgets.QVBoxLayout):
    frame = QtWidgets.QFrame()
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    frame.setObjectName("frame")

    font = QtGui.QFont()
    font.setPointSize(12)

    layout = QtWidgets.QHBoxLayout(frame)
    layout.setObjectName("layout")

    font = QtGui.QFont()
    font.setPointSize(12)
    add_button = QtWidgets.QPushButton(frame)
    add_button.setMaximumWidth(300)
    add_button.setFont(font)
    add_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    add_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    add_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    add_button.setAutoDefault(False)
    add_button.setDefault(False)
    add_button.setFlat(True)
    add_button.setObjectName("add_button")
    add_button.setText("Dodaj projekciju")
    icon = QtGui.QIcon(get_relative_path(["assets", "plus.png"]))
    add_button.setIcon(icon)
    layout.addWidget(add_button)

    delete_button = QtWidgets.QPushButton(frame)
    delete_button.setMaximumWidth(300)
    delete_button.setFont(font)
    delete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    delete_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    delete_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    delete_button.setAutoDefault(False)
    delete_button.setDefault(False)
    delete_button.setFlat(True)
    delete_button.setObjectName("delete_button")
    delete_button.setText("Izbriši projekciju")
    icon = QtGui.QIcon(get_relative_path(["assets", "trash.png"]))
    delete_button.setIcon(icon)
    delete_button.setIconSize(QtCore.QSize(15, 15))
    layout.addWidget(delete_button)
    
    edit_button = QtWidgets.QPushButton(frame)
    edit_button.setMaximumWidth(300)
    edit_button.setFont(font)
    edit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    edit_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    edit_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    edit_button.setAutoDefault(False)
    edit_button.setDefault(False)
    edit_button.setFlat(True)
    edit_button.setObjectName("edit_button")
    edit_button.setText("Izmeni projekciju")
    icon = QtGui.QIcon(get_relative_path(["assets", "edit.png"]))
    edit_button.setIcon(icon)
    layout.addWidget(edit_button)

    frame.setLayout(layout)
    parent_layout.addWidget(frame)

    return {
        "frame": frame,
        "add_button": add_button,
        "delete_button": delete_button,
        "edit_button": edit_button
    }

def table_frame(parent_layout: QtWidgets.QVBoxLayout):
    table = QtWidgets.QTableWidget()
    table.setEnabled(True)
    table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
    table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
    table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    table.setCornerButtonEnabled(True)
    table.setAlternatingRowColors(True)
    table.setStyleSheet("background-color: white; color: black")
    table.setObjectName("table")
    table.horizontalHeader().setVisible(True)
    table.horizontalHeader().setCascadingSectionResizes(True)
    table.horizontalHeader().setSortIndicatorShown(False)
    table.horizontalHeader().setStretchLastSection(True)
    table.verticalHeader().setVisible(False)
    table.setColumnCount(7)
    item = QtWidgets.QTableWidgetItem("Šifra")
    table.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem("Sala")
    table.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem("Film")
    table.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem("Vreme početka")
    table.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem("Vreme kraja")
    table.setHorizontalHeaderItem(4, item)
    item = QtWidgets.QTableWidgetItem("Cena")
    table.setHorizontalHeaderItem(5, item)
    item = QtWidgets.QTableWidgetItem("Dani")
    table.setHorizontalHeaderItem(6, item)
    parent_layout.addWidget(table)
    return {
        "table": table
    }

def form(parent_layout: QtWidgets.QVBoxLayout, button_text):

    frame = QtWidgets.QFrame()
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    frame.setObjectName("frame")
    frame.setMaximumHeight(900)
    frame.setMaximumWidth(500)

    frame_layout = QtWidgets.QVBoxLayout(frame)
    frame_layout.setSpacing(15)
    frame_layout.setObjectName("frame_layout")
    
    font = QtGui.QFont()
    font.setPointSize(12)

    form_layout = QtWidgets.QFormLayout()
    form_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
    form_layout.setObjectName("form_layout")

    sifra_label = QtWidgets.QLabel(frame)
    sifra_label.setText("Šifra: ")
    sifra_label.setFont(font)
    sifra_label.setStyleSheet("color: white")
    sifra_label.setObjectName("sifra_label")
    form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, sifra_label)

    sifra_input = QtWidgets.QLineEdit(frame)
    sifra_input.setEnabled(False)
    sifra_input.setFont(font)
    sifra_input.setStyleSheet("padding: 5px 10px; color: white;")
    sifra_input.setObjectName("sifra_input")
    form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, sifra_input)

    sala_label = QtWidgets.QLabel(frame)
    sala_label.setText("Sala:")
    sala_label.setFont(font)
    sala_label.setStyleSheet("color: white")
    sala_label.setObjectName("sala_label")
    form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, sala_label)

    sala_cb = QtWidgets.QComboBox(frame)
    sala_cb.setFont(font)
    sala_cb.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    sala_cb.setObjectName("sala_cb")
    form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, sala_cb)

    film_label = QtWidgets.QLabel(frame)
    film_label.setText("Film:")
    film_label.setFont(font)
    film_label.setStyleSheet("color: white")
    film_label.setObjectName("film_label")
    form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, film_label)

    film_cb = QtWidgets.QComboBox(frame)
    film_cb.setFont(font)
    film_cb.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    film_cb.setObjectName("film_cb")
    form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, film_cb)

    vreme_pocetka_label = QtWidgets.QLabel(frame)
    vreme_pocetka_label.setText("Vreme početka: ")
    vreme_pocetka_label.setFont(font)
    vreme_pocetka_label.setStyleSheet("color: white")
    vreme_pocetka_label.setObjectName("vreme_pocetka_label")
    form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, vreme_pocetka_label)

    vreme_pocetka_time = QtWidgets.QTimeEdit(frame)
    vreme_pocetka_time.setFont(font)
    vreme_pocetka_time.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    vreme_pocetka_time.setObjectName("vreme_pocetka_time")
    form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, vreme_pocetka_time)

    vreme_kraja_label = QtWidgets.QLabel(frame)
    vreme_kraja_label.setText("Vreme kraja:  ")
    vreme_kraja_label.setFont(font)
    vreme_kraja_label.setStyleSheet("color: white")
    vreme_kraja_label.setObjectName("vreme_kraja_label")
    form_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, vreme_kraja_label)

    vreme_kraja_time = QtWidgets.QTimeEdit(frame)
    vreme_kraja_time.setEnabled(False)
    vreme_kraja_time.setFont(font)
    vreme_kraja_time.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    vreme_kraja_time.setObjectName("vreme_kraja_time")
    form_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, vreme_kraja_time)

    cena_label = QtWidgets.QLabel(frame)
    cena_label.setText("Cena: ")
    cena_label.setFont(font)
    cena_label.setStyleSheet("color: white")
    cena_label.setObjectName("cena_label")
    form_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, cena_label)

    cena_sb = QtWidgets.QDoubleSpinBox(frame)
    cena_sb.setFont(font)
    cena_sb.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    cena_sb.setMaximum(9999999)
    cena_sb.setObjectName("cena_sb")
    form_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, cena_sb)

    dani_label = QtWidgets.QLabel(frame)
    dani_label.setText("Dani: ")
    dani_label.setFont(font)
    dani_label.setStyleSheet("color: white")
    dani_label.setObjectName("dani_label")
    form_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, dani_label)

    dani_group = QtWidgets.QGroupBox(frame)
    dani_group.setTitle("")
    dani_group.setObjectName("dani_group")

    dani_layout = QtWidgets.QGridLayout(dani_group)
    dani_layout.setObjectName("dani_layout")

    checkbox_pondeljak = QtWidgets.QCheckBox(dani_group)
    checkbox_pondeljak.setText(Days.ponedeljak)
    checkbox_pondeljak.setFont(font)
    checkbox_pondeljak.setStyleSheet("color: white")
    checkbox_pondeljak.setObjectName("checkbox_pondeljak")
    dani_layout.addWidget(checkbox_pondeljak, 0, 0, 1, 1)

    checkbox_utorak = QtWidgets.QCheckBox(dani_group)
    checkbox_utorak.setText(Days.utorak)
    checkbox_utorak.setFont(font)
    checkbox_utorak.setStyleSheet("color: white")
    checkbox_utorak.setObjectName("checkbox_utorak")
    dani_layout.addWidget(checkbox_utorak, 0, 1, 1, 1)

    checkbox_sreda = QtWidgets.QCheckBox(dani_group)
    checkbox_sreda.setText(Days.sreda)
    checkbox_sreda.setFont(font)
    checkbox_sreda.setStyleSheet("color: white")
    checkbox_sreda.setObjectName("checkbox_sreda")
    dani_layout.addWidget(checkbox_sreda, 1, 0, 1, 1)

    checkbox_cetvrtak = QtWidgets.QCheckBox(dani_group)
    checkbox_cetvrtak.setText(Days.cetvrtak)
    checkbox_cetvrtak.setFont(font)
    checkbox_cetvrtak.setStyleSheet("color: white")
    checkbox_cetvrtak.setObjectName("checkbox_cetvrtak")
    dani_layout.addWidget(checkbox_cetvrtak, 1, 1, 1, 1)

    checkbox_petak = QtWidgets.QCheckBox(dani_group)
    checkbox_petak.setText(Days.petak)
    checkbox_petak.setFont(font)
    checkbox_petak.setStyleSheet("color: white")
    checkbox_petak.setObjectName("checkbox_petak")
    dani_layout.addWidget(checkbox_petak, 2, 0, 1, 1)

    checkbox_subota = QtWidgets.QCheckBox(dani_group)
    checkbox_subota.setText(Days.subota)
    checkbox_subota.setFont(font)
    checkbox_subota.setStyleSheet("color: white")
    checkbox_subota.setObjectName("checkbox_subota")
    dani_layout.addWidget(checkbox_subota, 2, 1, 1, 1)

    checkbox_nedelja = QtWidgets.QCheckBox(dani_group)
    checkbox_nedelja.setText(Days.nedelja)
    checkbox_nedelja.setFont(font)
    checkbox_nedelja.setStyleSheet("color: white")
    checkbox_nedelja.setObjectName("checkbox_nedelja")
    dani_layout.addWidget(checkbox_nedelja, 3, 0, 1, 1)

    form_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, dani_group)

    frame_layout.addLayout(form_layout)

    confirm_button = QtWidgets.QPushButton(frame)
    confirm_button.setFont(font)
    confirm_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    confirm_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    confirm_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    confirm_button.setAutoDefault(False)
    confirm_button.setDefault(False)
    confirm_button.setFlat(True)
    confirm_button.setObjectName("confirm_button")
    confirm_button.setText(button_text)

    frame_layout.addWidget(confirm_button)

    cancel_button = QtWidgets.QPushButton(frame)
    cancel_button.setFont(font)
    cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    cancel_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    cancel_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    cancel_button.setAutoDefault(False)
    cancel_button.setDefault(False)
    cancel_button.setFlat(True)
    cancel_button.setObjectName("cancel_button")
    cancel_button.setText("Odustani")
    frame_layout.addWidget(cancel_button)
    
    parent_layout.addWidget(frame)

    dani_checkboxes = [
        checkbox_pondeljak,
        checkbox_utorak,
        checkbox_sreda,
        checkbox_cetvrtak,
        checkbox_petak,
        checkbox_subota,
        checkbox_nedelja
    ]

    return {
        "frame": frame,
        "sifra_input": sifra_input,
        "sala_cb": sala_cb,
        "film_cb": film_cb,
        "vreme_pocetka_time": vreme_pocetka_time,
        "vreme_kraja_time": vreme_kraja_time,
        "cena_sb": cena_sb,
        "dani_checkboxes": dani_checkboxes,
        "confirm_button": confirm_button,
        "cancel_button": cancel_button
    }
