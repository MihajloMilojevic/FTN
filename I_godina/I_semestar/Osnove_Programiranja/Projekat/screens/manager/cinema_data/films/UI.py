from PyQt5 import QtCore, QtGui, QtWidgets
from utils.get_path import get_relative_path
from database.models.enums import Genres
from datetime import datetime


def setupUi(tab: QtWidgets.QWidget):

    # main layout
    layout = QtWidgets.QVBoxLayout()
    layout.setObjectName("layout")
    layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter|QtCore.Qt.AlignmentFlag.AlignHCenter)

    frame_buttons = buttons_frame(layout)
    frame_table = table_frame(layout)
    frame_add = form(layout, "Dodaj film")
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
    add_button.setText("Dodaj film")
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
    delete_button.setText("Izbriši film")
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
    edit_button.setText("Izmeni film")
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
    table.setColumnCount(9)
    item = QtWidgets.QTableWidgetItem("Šifra")
    table.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem("Ime")
    table.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem("Žanrovi")
    table.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem("Trajanje(min)")
    table.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem("Režiser")
    table.setHorizontalHeaderItem(4, item)
    item = QtWidgets.QTableWidgetItem("Glavne uloge")
    table.setHorizontalHeaderItem(5, item)
    item = QtWidgets.QTableWidgetItem("Zemlja porekla")
    table.setHorizontalHeaderItem(6, item)
    item = QtWidgets.QTableWidgetItem("Godina proizvodnje")
    table.setHorizontalHeaderItem(7, item)
    item = QtWidgets.QTableWidgetItem("Opis")
    table.setHorizontalHeaderItem(8, item)
    parent_layout.addWidget(table)
    return {
        "table": table
    }

def form(parent_layout: QtWidgets.QVBoxLayout, button_text):

    frame = QtWidgets.QFrame()
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    frame.setObjectName("frame")
    # frame.setMaximumHeight(900)
    frame.setMaximumWidth(800)

    frame_layout = QtWidgets.QVBoxLayout(frame)
    frame_layout.setObjectName("frame_layout")

    form_layout = QtWidgets.QFormLayout()
    form_layout.setVerticalSpacing(15)
    form_layout.setObjectName("form_layout")

    font = QtGui.QFont()
    font.setPointSize(12)

    sifra_label = QtWidgets.QLabel(frame)
    sifra_label.setText("Šifra:")
    sifra_label.setFont(font)
    sifra_label.setStyleSheet("color: white")
    sifra_label.setObjectName("sifra_label")
    form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, sifra_label)

    sifra_input = QtWidgets.QLineEdit(frame)
    sifra_input.setEnabled(False)
    sifra_input.setFont(font)
    sifra_input.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    sifra_input.setObjectName("sifra_input")
    form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, sifra_input)

    naziv_label = QtWidgets.QLabel(frame)
    naziv_label.setText("Ime:")
    naziv_label.setFont(font)
    naziv_label.setStyleSheet("color: white")
    naziv_label.setObjectName("naziv_label")
    form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, naziv_label)

    naziv_input = QtWidgets.QLineEdit(frame)
    naziv_input.setFont(font)
    naziv_input.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    naziv_input.setObjectName("naziv_input")
    form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, naziv_input)

    reziser_label = QtWidgets.QLabel(frame)
    reziser_label.setText("Režiser: ")
    reziser_label.setFont(font)
    reziser_label.setStyleSheet("color: white")
    reziser_label.setObjectName("reziser_label")
    form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, reziser_label)

    reziser_input = QtWidgets.QLineEdit(frame)
    reziser_input.setFont(font)
    reziser_input.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    reziser_input.setObjectName("reziser_input")
    form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, reziser_input)
    
    zemlja_label = QtWidgets.QLabel(frame)
    zemlja_label.setText("Zemlja porekla:")
    zemlja_label.setFont(font)
    zemlja_label.setStyleSheet("color: white")
    zemlja_label.setObjectName("zemlja_label")
    form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, zemlja_label)

    zemlja_input = QtWidgets.QLineEdit(frame)
    zemlja_input.setFont(font)
    zemlja_input.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    zemlja_input.setObjectName("zemlja_input")
    form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, zemlja_input)
    
    godina_label = QtWidgets.QLabel(frame)
    godina_label.setText("Godina:")
    godina_label.setFont(font)
    godina_label.setStyleSheet("color: white")
    godina_label.setObjectName("godina_label")
    form_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, godina_label)

    godina_sb = QtWidgets.QSpinBox(frame)
    godina_sb.setFont(font)
    godina_sb.setMinimum(1800)
    godina_sb.setMaximum(datetime.now().year)
    godina_sb.setValue(datetime.now().year)
    godina_sb.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")    
    godina_sb.setObjectName("godina_sb")
    form_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, godina_sb)
    
    trajanje_label = QtWidgets.QLabel(frame)
    trajanje_label.setText("Trajanje (min):")
    trajanje_label.setFont(font)
    trajanje_label.setStyleSheet("color: white")
    trajanje_label.setObjectName("trajanje_label")
    form_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, trajanje_label)

    trajanje_sb = QtWidgets.QSpinBox(frame)
    trajanje_sb.setFont(font)
    trajanje_sb.setMinimum(1)
    trajanje_sb.setMaximum(999999990)
    trajanje_sb.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")    
    trajanje_sb.setObjectName("trajanje_sb")
    form_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, trajanje_sb)

    uloge_label = QtWidgets.QLabel(frame)
    uloge_label.setText("Glavne uloge:")
    uloge_label.setToolTip("Glavne uloge razdvojene razmakom")
    uloge_label.setFont(font)
    uloge_label.setStyleSheet("color: white")
    uloge_label.setObjectName("uloge_label")
    form_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, uloge_label)
    
    uloge_input = QtWidgets.QTextEdit(frame)
    uloge_input.setFont(font)
    uloge_input.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    uloge_input.setObjectName("uloge_input")
    form_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, uloge_input)
    
    zanrovi_label = QtWidgets.QLabel(frame)
    zanrovi_label.setText("Žanrovi: ")
    zanrovi_label.setFont(font)
    zanrovi_label.setStyleSheet("color: white")
    zanrovi_label.setObjectName("zanrovi_label")
    form_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, zanrovi_label)

    zanrovi_group = QtWidgets.QGroupBox(frame)
    zanrovi_group.setTitle("")
    zanrovi_group.setObjectName("zanrovi_group")

    zanrovi_layout = QtWidgets.QGridLayout(zanrovi_group)
    zanrovi_layout.setObjectName("zanrovi_layout")

    checkBox_12 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_12.setText(Genres.akcija)
    checkBox_12.setFont(font)
    checkBox_12.setStyleSheet("color: white")
    checkBox_12.setObjectName("checkBox_12")
    zanrovi_layout.addWidget(checkBox_12, 9, 3, 1, 1)

    checkBox_17 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_17.setText(Genres.animacija)
    checkBox_17.setFont(font)
    checkBox_17.setStyleSheet("color: white")
    checkBox_17.setObjectName("checkBox_17")
    zanrovi_layout.addWidget(checkBox_17, 9, 0, 1, 1)

    checkBox_19 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_19.setText(Genres.avantura)
    checkBox_19.setFont(font)
    checkBox_19.setStyleSheet("color: white")
    checkBox_19.setObjectName("checkBox_19")
    zanrovi_layout.addWidget(checkBox_19, 9, 2, 1, 1)

    checkBox_18 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_18.setText(Genres.biografski)
    checkBox_18.setFont(font)
    checkBox_18.setStyleSheet("color: white")
    checkBox_18.setObjectName("checkBox_18")
    zanrovi_layout.addWidget(checkBox_18, 5, 3, 1, 1)

    checkBox_5 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_5.setText(Genres.decji)
    checkBox_5.setFont(font)
    checkBox_5.setStyleSheet("color: white")
    checkBox_5.setObjectName("checkBox_5")
    zanrovi_layout.addWidget(checkBox_5, 4, 0, 1, 1)

    checkBox_15 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_15.setText(Genres.dokumentarni)
    checkBox_15.setFont(font)
    checkBox_15.setStyleSheet("color: white")
    checkBox_15.setObjectName("checkBox_15")
    zanrovi_layout.addWidget(checkBox_15, 4, 4, 1, 1)

    checkBox_3 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_3.setText(Genres.drama)
    checkBox_3.setFont(font)
    checkBox_3.setStyleSheet("color: white")
    checkBox_3.setObjectName("checkBox_3")
    zanrovi_layout.addWidget(checkBox_3, 5, 4, 1, 1)

    checkBox_9 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_9.setText(Genres.fantastika)
    checkBox_9.setFont(font)
    checkBox_9.setStyleSheet("color: white")
    checkBox_9.setObjectName("checkBox_9")
    zanrovi_layout.addWidget(checkBox_9, 5, 0, 1, 1)

    checkBox_7 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_7.setText(Genres.horor)
    checkBox_7.setFont(font)
    checkBox_7.setStyleSheet("color: white")
    checkBox_7.setObjectName("checkBox_7")
    zanrovi_layout.addWidget(checkBox_7, 5, 2, 1, 1)

    checkBox_14 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_14.setText(Genres.istorijski)
    checkBox_14.setFont(font)
    checkBox_14.setStyleSheet("color: white")
    checkBox_14.setObjectName("checkBox_14")
    zanrovi_layout.addWidget(checkBox_14, 4, 3, 1, 1)

    checkBox_6 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_6.setText(Genres.komedija)
    checkBox_6.setFont(font)
    checkBox_6.setStyleSheet("color: white")
    checkBox_6.setObjectName("checkBox_6")
    zanrovi_layout.addWidget(checkBox_6, 4, 2, 1, 1)

    checkBox_16 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_16.setText(Genres.kriminalisticki)
    checkBox_16.setFont(font)
    checkBox_16.setStyleSheet("color: white")
    checkBox_16.setObjectName("checkBox_16")
    zanrovi_layout.addWidget(checkBox_16, 7, 3, 1, 1)

    checkBox_13 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_13.setText(Genres.misterija)
    checkBox_13.setFont(font)
    checkBox_13.setStyleSheet("color: white")
    checkBox_13.setObjectName("checkBox_13")
    zanrovi_layout.addWidget(checkBox_13, 7, 0, 1, 1)

    checkBox_11 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_11.setText(Genres.mjuzikl)
    checkBox_11.setFont(font)
    checkBox_11.setStyleSheet("color: white")
    checkBox_11.setObjectName("checkBox_11")
    zanrovi_layout.addWidget(checkBox_11, 7, 2, 1, 1)

    checkBox_20 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_20.setText(Genres.naucnofantasticni)
    checkBox_20.setFont(font)
    checkBox_20.setStyleSheet("color: white")
    checkBox_20.setObjectName("checkBox_20")
    zanrovi_layout.addWidget(checkBox_20, 7, 4, 1, 1)

    checkBox_4 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_4.setText(Genres.porodicni)
    checkBox_4.setFont(font)
    checkBox_4.setStyleSheet("color: white")
    checkBox_4.setObjectName("checkBox_4")
    zanrovi_layout.addWidget(checkBox_4, 9, 4, 1, 1)

    checkBox_10 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_10.setText(Genres.triler)
    checkBox_10.setFont(font)
    checkBox_10.setStyleSheet("color: white")
    checkBox_10.setObjectName("checkBox_10")
    zanrovi_layout.addWidget(checkBox_10, 1, 3, 1, 1)

    checkBox_2 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_2.setText(Genres.ratni)
    checkBox_2.setFont(font)
    checkBox_2.setStyleSheet("color: white")
    checkBox_2.setObjectName("checkBox_2")
    zanrovi_layout.addWidget(checkBox_2, 1, 2, 1, 1)

    checkBox_1 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_1.setText(Genres.vestern)
    checkBox_1.setFont(font)
    checkBox_1.setStyleSheet("color: white")
    checkBox_1.setObjectName("checkBox_1")
    zanrovi_layout.addWidget(checkBox_1, 1, 0, 1, 1)

    checkBox_8 = QtWidgets.QCheckBox(zanrovi_group)
    checkBox_8.setText(Genres.ljubavni)
    checkBox_8.setFont(font)
    checkBox_8.setStyleSheet("color: white")
    checkBox_8.setObjectName("checkBox_8")
    zanrovi_layout.addWidget(checkBox_8, 1, 4, 1, 1)

    form_layout.setWidget(7, QtWidgets.QFormLayout.FieldRole, zanrovi_group)

    opis_label = QtWidgets.QLabel(frame)
    opis_label.setText("Opis:")
    opis_label.setFont(font)
    opis_label.setStyleSheet("color: white")
    opis_label.setObjectName("opis_label")
    form_layout.setWidget(8, QtWidgets.QFormLayout.LabelRole, opis_label)

    opis_input = QtWidgets.QTextEdit(frame)
    opis_input.setFont(font)
    opis_input.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    opis_input.setObjectName("opis_input")
    form_layout.setWidget(8, QtWidgets.QFormLayout.FieldRole, opis_input)

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

    checkbox_list = [
        checkBox_1,
        checkBox_2,
        checkBox_3,
        checkBox_4,
        checkBox_5,
        checkBox_6,
        checkBox_7,
        checkBox_8,
        checkBox_9,
        checkBox_10,
        checkBox_11,
        checkBox_12,
        checkBox_13,
        checkBox_14,
        checkBox_15,
        checkBox_16,
        checkBox_17,
        checkBox_18,
        checkBox_19,
        checkBox_20
    ]

    return {
        "frame": frame,
        "checkbox_list": checkbox_list,
        "sifra_input": sifra_input,
        "naziv_input": naziv_input,
        "reziser_input": reziser_input,
        "zemlja_input": zemlja_input,
        "godina_sb": godina_sb,
        "trajanje_sb": trajanje_sb,
        "uloge_input": uloge_input,
        "opis_input": opis_input,
        "confirm_button": confirm_button,
        "cancel_button": cancel_button
    }
