# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FilmsScreenDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database.models.enums import Genres
import datetime


def setupUi( frame):
    
    font = QtGui.QFont()
    font.setPointSize(12)

    frame_layout = QtWidgets.QHBoxLayout()
    frame_layout.setObjectName("frame_layout")
    frame_layout.setContentsMargins(0, 0, 0, 0)


    center_layout = QtWidgets.QVBoxLayout()
    center_layout.setContentsMargins(10, 10, 10, 10)
    center_layout.setObjectName("center_layout")

    header_layout = QtWidgets.QVBoxLayout()
    header_layout.setContentsMargins(0, 0, 0, 0)
    header_layout.setObjectName("header_layout")

    description_label = QtWidgets.QLabel(frame)
    description_label.setText("Lista prodatih karata za odabran datum prodaje i odabranog prodavca")
    description_label.setFont(font)
    description_label.setStyleSheet("color: white")
    description_label.setObjectName("description_label")

    header_layout.addWidget(description_label)

    date_layout = QtWidgets.QHBoxLayout()
    date_layout.setContentsMargins(0, 0, 0, 0)
    date_layout.setObjectName("date_layout")

    datepicker_label = QtWidgets.QLabel(frame)
    datepicker_label.setText("Datum: ")
    datepicker_label.setMaximumWidth(100)
    datepicker_label.setFont(font)
    datepicker_label.setStyleSheet("color: white")
    datepicker_label.setObjectName("datepicker_label")

    date_layout.addWidget(datepicker_label)

    datepicker = QtWidgets.QDateEdit()
    datepicker.setFont(font)
    datepicker.setMinimumWidth(150)
    datepicker.setStyleSheet("padding: 5px 10px; border: 1px solid white; border-radius: 5px")
    # datepicker.setStyleSheet("padding: 10px;")
    datepicker.setObjectName("datepicker")
    datepicker.setDate(datetime.datetime.today().date())
    # datepicker.setMinimumDate(datetime.datetime.today().date())
    date_layout.addWidget(datepicker)
    
    header_layout.addLayout(date_layout)

    seller_layout = QtWidgets.QHBoxLayout()
    seller_layout.setContentsMargins(0, 0, 0, 0)
    seller_layout.setObjectName("seller_layout")

    seller_label = QtWidgets.QLabel(frame)
    seller_label.setText("Prodavac: ")
    seller_label.setMaximumWidth(100)
    seller_label.setFont(font)
    seller_label.setStyleSheet("color: white")
    seller_label.setObjectName("seller_label")

    seller_layout.addWidget(seller_label)

    seller_select = QtWidgets.QComboBox()
    seller_select.setFont(font)
    seller_select.setMinimumWidth(150)
    seller_select.setStyleSheet("padding: 5px 10px; border: 1px solid white; border-radius: 5px")
    seller_select.setObjectName("seller_select")
    seller_layout.addWidget(seller_select)
    
    header_layout.addLayout(seller_layout)

    center_layout.addLayout(header_layout)

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
    table.setColumnCount(10)
    item = QtWidgets.QTableWidgetItem("Šifra")
    table.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem("Film")
    table.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem("Sala")
    table.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem("Status")
    table.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem("Datum")
    table.setHorizontalHeaderItem(4, item)
    item = QtWidgets.QTableWidgetItem("Vreme početka")
    table.setHorizontalHeaderItem(5, item)
    item = QtWidgets.QTableWidgetItem("Vreme kraja")
    table.setHorizontalHeaderItem(6, item)
    item = QtWidgets.QTableWidgetItem("Sedište")
    table.setHorizontalHeaderItem(7, item)
    item = QtWidgets.QTableWidgetItem("Ime i prezime")
    table.setHorizontalHeaderItem(8, item)
    item = QtWidgets.QTableWidgetItem("Prodavac")
    table.setHorizontalHeaderItem(9, item)
    table.setColumnWidth(1, 450)

    center_layout.addWidget(table)

    bottom_layout = QtWidgets.QHBoxLayout()
    bottom_layout.setContentsMargins(0, 0, 0, 0)
    bottom_layout.setObjectName("bottom_layout")

    back_button = QtWidgets.QPushButton()
    back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    back_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    back_button.setText("Nazad")
    back_button.setFont(font)
    back_button.setMaximumWidth(300)
    back_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    back_button.setAutoDefault(False)
    back_button.setDefault(False)
    back_button.setFlat(True)
    back_button.setObjectName("back_button")

    bottom_layout.addWidget(back_button)
    bottom_layout.addStretch()

    
    save_button = QtWidgets.QPushButton()
    save_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    save_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    save_button.setText("Sačuvaj")
    save_button.setFont(font)
    save_button.setMaximumWidth(300)
    save_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    save_button.setAutoDefault(False)
    save_button.setDefault(False)
    save_button.setFlat(True)
    save_button.setObjectName("save_button")

    bottom_layout.addWidget(save_button)
    
    center_layout.addLayout(bottom_layout)

    frame_layout.addLayout(center_layout)
    frame.setLayout(frame_layout)

    return {
        "table": table,
        "datepicker": datepicker,
        "seller_select": seller_select,
        "back_button": back_button,
        "save_button": save_button
    }