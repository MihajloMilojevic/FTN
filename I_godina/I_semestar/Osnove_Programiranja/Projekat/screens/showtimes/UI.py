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

    header_layout = QtWidgets.QHBoxLayout()
    header_layout.setContentsMargins(0, 0, 0, 0)
    header_layout.setObjectName("header_layout")

    datepicker_label = QtWidgets.QLabel(frame)
    datepicker_label.setText("Datum: ")
    datepicker_label.setMaximumWidth(75)
    datepicker_label.setFont(font)
    datepicker_label.setStyleSheet("color: white")
    datepicker_label.setObjectName("datepicker_label")

    header_layout.addWidget(datepicker_label)

    datepicker = QtWidgets.QDateEdit()
    datepicker.setFont(font)
    datepicker.setMinimumWidth(150)
    datepicker.setStyleSheet("padding: 5px 10px; border: 1px solid white; border-radius: 5px")
    # datepicker.setStyleSheet("padding: 10px;")
    datepicker.setObjectName("datepicker")
    datepicker.setDate(datetime.datetime.today().date())
    # datepicker.setMinimumDate(datetime.datetime.today().date())
    header_layout.addWidget(datepicker)

    filters_button = QtWidgets.QPushButton()
    filters_button.setFont(font)
    filters_button.setMaximumWidth(250)
    filters_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    filters_button.setObjectName("filters_button")
    filters_button.setText("Filteri")
    filters_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    header_layout.addWidget(filters_button)

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
    table.setColumnCount(6)
    item = QtWidgets.QTableWidgetItem("Šifra")
    table.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem("Film")
    table.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem("Sala")
    table.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem("Datum")
    table.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem("Vreme početka")
    table.setHorizontalHeaderItem(4, item)
    item = QtWidgets.QTableWidgetItem("Vreme kraja")
    table.setHorizontalHeaderItem(5, item)
    table.setColumnWidth(1, 450)

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

    filters_scroll_area = QtWidgets.QScrollArea()

    filters_scroll_area.setWidgetResizable(True)
    filters_scroll_area.setObjectName("scrollArea")
    filters_scroll_area.setMinimumWidth(350)
    filters_scroll_area_layout = QtWidgets.QVBoxLayout()
    filters_scroll_area.setLayout(filters_scroll_area_layout)

    filters_content_widget = QtWidgets.QWidget()
    filters_content_widget.setObjectName("content")
    # filters_content_widget.setMinimumWidth(300)
    filters_scroll_area.setWidget(filters_content_widget)

    filters_content_layout = QtWidgets.QVBoxLayout()
    filters_content_layout.setObjectName("filters_content_layout")

    filters_content_widget.setLayout(filters_content_layout)

    films_group = QtWidgets.QGroupBox(frame)
    films_group.setTitle("Filmovi")
    films_group.setObjectName("films_group")
    films_group.setFont(font)
    films_group.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum))

    films_layout = QtWidgets.QVBoxLayout(films_group)
    films_layout.setObjectName("films_layout")

    def add_film(text):
        film = QtWidgets.QCheckBox(films_group)
        film.setText(text)
        film.setFont(font)
        film.setStyleSheet("color: white")
        films_layout.addWidget(film)
        return film
    
    def clear_films():
        for i in reversed(range(films_layout.count())): 
            films_layout.itemAt(i).widget().setParent(None)
    
    filters_content_layout.addWidget(films_group)

    halls_group = QtWidgets.QGroupBox(frame)
    halls_group.setTitle("Sale")
    halls_group.setObjectName("halls_group")
    halls_group.setFont(font)
    halls_group.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum))

    halls_layout = QtWidgets.QVBoxLayout(halls_group)
    halls_layout.setObjectName("halls_layout")

    def add_hall(text):
        hall = QtWidgets.QCheckBox(halls_group)
        hall.setText(text)
        hall.setFont(font)
        hall.setStyleSheet("color: white")
        halls_layout.addWidget(hall)
        return hall
    
    def clear_halls():
        for i in reversed(range(halls_layout.count())): 
            halls_layout.itemAt(i).widget().setParent(None)
    
    filters_content_layout.addWidget(halls_group)

    time_group = QtWidgets.QGroupBox(frame)
    time_group.setTitle("Vreme")
    time_group.setObjectName("time_group")
    time_group.setFont(font)
    time_group.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum))

    min_time_label = QtWidgets.QLabel(frame)
    min_time_label.setText("Od:")
    min_time_label.setFont(font)
    min_time_label.setStyleSheet("color: white")
    min_time_label.setObjectName("min_time_label")

    min_time_te = QtWidgets.QTimeEdit(frame)
    min_time_te.setFont(font)
    min_time_te.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")    
    min_time_te.setObjectName("min_time_te")

    max_time_label = QtWidgets.QLabel(frame)
    max_time_label.setText("Do:")
    max_time_label.setFont(font)
    max_time_label.setStyleSheet("color: white")
    max_time_label.setObjectName("max_time_label")

    max_time_te = QtWidgets.QTimeEdit(frame)
    max_time_te.setFont(font)
    max_time_te.setStyleSheet("padding: 5px 10px; color: white; border: 1px solid white;")    
    max_time_te.setObjectName("max_time_te")
    t = QtCore.QTime()
    t.setHMS(23, 59, 59)
    max_time_te.setTime(t)
    
    time_layout = QtWidgets.QVBoxLayout()
    time_layout.addWidget(min_time_label)
    time_layout.addWidget(min_time_te)
    time_layout.addWidget(max_time_label)
    time_layout.addWidget(max_time_te)

    time_group.setLayout(time_layout)
    filters_content_layout.addWidget(time_group)

    
    filters_content_layout.addStretch()
    

    frame_layout.addLayout(center_layout)
    frame_layout.addWidget(filters_scroll_area)
    frame.setLayout(frame_layout)

    return {
        "table": table,
        "datepicker": datepicker,
        "back_button": back_button,
        "filters_button": filters_button,
        "min_time_te": min_time_te,
        "max_time_te": max_time_te,
        "filters_scroll_area": filters_scroll_area
    }, {
        "add_film": add_film,
        "add_hall": add_hall,
        "clear_films": clear_films,
        "clear_halls": clear_halls
    }