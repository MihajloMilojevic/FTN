# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from components import SelectShowtimeComponent


def setupUi(Frame):
    font = QtGui.QFont()
    font.setPointSize(12)
    frame_layout = QtWidgets.QVBoxLayout(Frame)
    frame_layout.setObjectName("frame_layout")

    select_widget, setSelectHandler = SelectShowtimeComponent(Frame)
    frame_layout.addWidget(select_widget)

    label = QtWidgets.QLabel(Frame)
    label.setText("Odaberite sedišta:")
    label.setFont(font)
    label.setStyleSheet("color: white")
    label.setObjectName("label")
    frame_layout.addWidget(label)

    table = QtWidgets.QTableWidget(Frame)
    table.setFont(font)
    table.setLayoutDirection(QtCore.Qt.LeftToRight)
    table.setAutoFillBackground(False)
    table.setStyleSheet("background: rgba(0, 0, 0, 0)")
    table.setShowGrid(True)
    table.setGridStyle(QtCore.Qt.SolidLine)
    table.setWordWrap(True)
    table.setCornerButtonEnabled(False)
    table.setObjectName("table")
    table.setColumnCount(0)
    table.setRowCount(0)
    table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
    table.horizontalHeader().setVisible(False)
    table.horizontalHeader().setDefaultSectionSize(55)
    table.horizontalHeader().setMinimumSectionSize(55)
    table.verticalHeader().setVisible(False)
    table.verticalHeader().setDefaultSectionSize(35)
    frame_layout.addWidget(table)

    confirm_button = QtWidgets.QPushButton()
    confirm_button.setFont(font)
    confirm_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    confirm_button.setObjectName("confirm_button")
    confirm_button.setText("Potvrdi rezervaciju")
    confirm_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    confirm_button.setFixedWidth(300)
    frame_layout.addWidget(confirm_button, 0, QtCore.Qt.AlignHCenter)
    
    change_showtime_button = QtWidgets.QPushButton()
    change_showtime_button.setFont(font)
    change_showtime_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    change_showtime_button.setObjectName("change_showtime_button")
    change_showtime_button.setText("Odaberi drugi termin")
    change_showtime_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    change_showtime_button.setFixedWidth(300)
    frame_layout.addWidget(change_showtime_button, 0, QtCore.Qt.AlignHCenter)

    back_button = QtWidgets.QPushButton()
    back_button.setFont(font)
    back_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    back_button.setObjectName("back_button")
    back_button.setText("Nazad")
    back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    back_button.setFixedWidth(300)
    frame_layout.addWidget(back_button, 0, QtCore.Qt.AlignHCenter)

    return {
        "label": label,
        "table": table,
        "select_widget": select_widget,
        "back_button": back_button,
        "confirm_button": confirm_button,
        "change_showtime_button": change_showtime_button
    }, {
        "setSelectHandler": setSelectHandler
    }