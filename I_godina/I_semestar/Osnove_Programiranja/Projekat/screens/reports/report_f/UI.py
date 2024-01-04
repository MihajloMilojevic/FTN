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
import database.models as Models


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
    description_label.setText("Ukupna cena prodatih karata za zadati film")
    description_label.setFont(font)
    description_label.setStyleSheet("color: white")
    description_label.setObjectName("description_label")

    header_layout.addWidget(description_label)

    film_layout = QtWidgets.QHBoxLayout()
    film_layout.setContentsMargins(0, 0, 0, 0)
    film_layout.setObjectName("film_layout")

    film_label = QtWidgets.QLabel(frame)
    film_label.setText("Film: ")
    film_label.setMaximumWidth(100)
    film_label.setFont(font)
    film_label.setStyleSheet("color: white")
    film_label.setObjectName("film_label")

    film_layout.addWidget(film_label)

    film_select = QtWidgets.QComboBox()
    film_select.setFont(font)
    film_select.setMinimumWidth(150)
    film_select.setStyleSheet("padding: 5px 10px; border: 1px solid white; border-radius: 5px")
    film_select.setObjectName("film_select")
    film_layout.addWidget(film_select)
    
    header_layout.addLayout(film_layout)

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
    table.setColumnCount(2)
    item = QtWidgets.QTableWidgetItem("Broj karata")
    table.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem("Ukupna cena")
    table.setHorizontalHeaderItem(1, item)
    table.setColumnWidth(0, 100)
    table.setColumnWidth(1, 100)

    center_layout.addWidget(table)

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
    
    center_layout.addWidget(back_button)

    frame_layout.addLayout(center_layout)
    frame.setLayout(frame_layout)

    return {
        "table": table,
        "film_select": film_select,
        "back_button": back_button,
    }