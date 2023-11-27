from PyQt5 import QtCore, QtGui, QtWidgets
from Utils.GetPath import get_relative_path

def setupUi(tab: QtWidgets.QWidget):

    # main layout
    layout = QtWidgets.QVBoxLayout()
    layout.setObjectName("layout")
    layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter|QtCore.Qt.AlignmentFlag.AlignHCenter)

    frame_buttons = buttons_frame(layout)
    frame_table = table_frame(layout)
    frame_add = form(layout, "Dodaj salu")
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
    add_button.setText("Dodaj salu")
    icon = QtGui.QIcon(get_relative_path(["Assets", "plus.png"]))
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
    delete_button.setText("Izbriši salu")
    icon = QtGui.QIcon(get_relative_path(["Assets", "trash.png"]))
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
    edit_button.setText("Izmeni salu")
    icon = QtGui.QIcon(get_relative_path(["Assets", "edit.png"]))
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
    table.setColumnCount(4)
    item = QtWidgets.QTableWidgetItem("Šifra")
    table.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem("name")
    table.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem("Broj redova")
    table.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem("Broj sedišta")
    table.setHorizontalHeaderItem(3, item)
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

    main_layout = QtWidgets.QVBoxLayout(frame)
    main_layout.setObjectName("main_layout")
    main_layout.setSpacing(10)

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
    sifra_input.setStyleSheet("padding: 5px 10px; color: white;")
    sifra_input.setDragEnabled(False)
    sifra_input.setObjectName("sifra_input")
    sifra_input.setFont(font)
    sifra_input.setMaximumWidth(300)
    form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, sifra_input)

    naziv_label = QtWidgets.QLabel(frame)
    naziv_label.setText("name:")
    naziv_label.setFont(font)
    naziv_label.setStyleSheet("color: white")
    naziv_label.setObjectName("naziv_label")
    form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, naziv_label)

    naziv_input = QtWidgets.QLineEdit(frame)
    naziv_input.setStyleSheet("padding: 5px 10px; color: white;")
    naziv_input.setDragEnabled(False)
    naziv_input.setObjectName("naziv_input")
    naziv_input.setFont(font)
    naziv_input.setMaximumWidth(300)
    form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, naziv_input)

    redovi_label = QtWidgets.QLabel(frame)
    redovi_label.setText("Broj redova: ")
    redovi_label.setFont(font)
    redovi_label.setStyleSheet("color: white")
    redovi_label.setObjectName("redovi_label")
    form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, redovi_label)

    redovi_sb = QtWidgets.QSpinBox(frame)
    redovi_sb.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    redovi_sb.setMinimum(1)
    redovi_sb.setObjectName("redovi_sb")
    redovi_sb.setFont(font)
    redovi_sb.setMaximumWidth(300)
    form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, redovi_sb)

    sedista_label = QtWidgets.QLabel(frame)
    sedista_label.setToolTip("Broj sedišta u svakom redu")
    sedista_label.setText("Broj sedišta: ")
    sedista_label.setFont(font)
    sedista_label.setStyleSheet("color: white")
    sedista_label.setObjectName("sedista_label")
    form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, sedista_label)

    sedista_sb = QtWidgets.QSpinBox(frame)
    sedista_sb.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")
    sedista_sb.setMinimum(1)
    sedista_sb.setObjectName("sedista_sb")
    sedista_sb.setFont(font)
    sedista_sb.setMaximumWidth(300)
    form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, sedista_sb)

    main_layout.addLayout(form_layout)

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

    main_layout.addWidget(confirm_button)

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
    main_layout.addWidget(cancel_button)
    parent_layout.addWidget(frame)

    return {
        "frame": frame,
        "sifra_input": sifra_input,
        "naziv_input": naziv_input,
        "redovi_sb": redovi_sb,
        "sedista_sb": sedista_sb,
        "confirm_button": confirm_button,
        "cancel_button": cancel_button
    }
