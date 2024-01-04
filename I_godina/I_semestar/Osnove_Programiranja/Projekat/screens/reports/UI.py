from PyQt5 import QtCore, QtGui, QtWidgets


def setupUi(Form):

    font = QtGui.QFont()
    font.setPointSize(12)

    vbox_layout = QtWidgets.QVBoxLayout(Form)
    vbox_layout.setContentsMargins(50, 50, 50, 50)
    vbox_layout.setSpacing(10)
    vbox_layout.setObjectName("vbox_layout")
    vbox_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    report_a_button = QtWidgets.QPushButton(Form)
    report_a_button.setFont(font)
    report_a_button.setFixedWidth(300)
    report_a_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    report_a_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    report_a_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    report_a_button.setAutoDefault(False)
    report_a_button.setDefault(False)
    report_a_button.setFlat(True)
    report_a_button.setObjectName("report_a_button")
    report_a_button.setText("Izveštaj A")
    vbox_layout.addWidget(report_a_button)

    report_b_button = QtWidgets.QPushButton(Form)
    report_b_button.setFont(font)
    report_b_button.setFixedWidth(300)
    report_b_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    report_b_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    report_b_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    report_b_button.setAutoDefault(False)
    report_b_button.setDefault(False)
    report_b_button.setFlat(True)
    report_b_button.setObjectName("report_b_button")
    report_b_button.setText("Izveštaj B")
    vbox_layout.addWidget(report_b_button)

    report_c_button = QtWidgets.QPushButton(Form)
    report_c_button.setFont(font)
    report_c_button.setFixedWidth(300)
    report_c_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    report_c_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    report_c_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    report_c_button.setAutoDefault(False)
    report_c_button.setDefault(False)
    report_c_button.setFlat(True)
    report_c_button.setObjectName("report_c_button")
    report_c_button.setText("Izveštaj C")
    vbox_layout.addWidget(report_c_button)

    report_d_button = QtWidgets.QPushButton(Form)
    report_d_button.setFont(font)
    report_d_button.setFixedWidth(300)
    report_d_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    report_d_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    report_d_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    report_d_button.setAutoDefault(False)
    report_d_button.setDefault(False)
    report_d_button.setFlat(True)
    report_d_button.setObjectName("report_d_button")
    report_d_button.setText("Izveštaj D")
    vbox_layout.addWidget(report_d_button)

    report_e_button = QtWidgets.QPushButton(Form)
    report_e_button.setFont(font)
    report_e_button.setFixedWidth(300)
    report_e_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    report_e_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    report_e_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    report_e_button.setAutoDefault(False)
    report_e_button.setDefault(False)
    report_e_button.setFlat(True)
    report_e_button.setObjectName("report_e_button")
    report_e_button.setText("Izveštaj E")
    vbox_layout.addWidget(report_e_button)

    report_f_button = QtWidgets.QPushButton(Form)
    report_f_button.setFont(font)
    report_f_button.setFixedWidth(300)
    report_f_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    report_f_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    report_f_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    report_f_button.setAutoDefault(False)
    report_f_button.setDefault(False)
    report_f_button.setFlat(True)
    report_f_button.setObjectName("report_f_button")
    report_f_button.setText("Izveštaj F")
    vbox_layout.addWidget(report_f_button)

    report_g_button = QtWidgets.QPushButton(Form)
    report_g_button.setFont(font)
    report_g_button.setFixedWidth(300)
    report_g_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    report_g_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    report_g_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    report_g_button.setAutoDefault(False)
    report_g_button.setDefault(False)
    report_g_button.setFlat(True)
    report_g_button.setObjectName("report_g_button")
    report_g_button.setText("Izveštaj G")
    vbox_layout.addWidget(report_g_button)

    report_h_button = QtWidgets.QPushButton(Form)
    report_h_button.setFont(font)
    report_h_button.setFixedWidth(300)
    report_h_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    report_h_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    report_h_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    report_h_button.setAutoDefault(False)
    report_h_button.setDefault(False)
    report_h_button.setFlat(True)
    report_h_button.setObjectName("report_h_button")
    report_h_button.setText("Izveštaj H")
    vbox_layout.addWidget(report_h_button)

    back_button = QtWidgets.QPushButton(Form)
    back_button.setFont(font)
    back_button.setFixedWidth(300)
    back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    back_button.setFocusPolicy(QtCore.Qt.ClickFocus)
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
    back_button.setText("Nazad ")
    vbox_layout.addWidget(back_button)

    Form.setLayout(vbox_layout)
    QtCore.QMetaObject.connectSlotsByName(Form)
    return {
        "report_a_button": report_a_button,
        "report_b_button": report_b_button,
        "report_c_button": report_c_button,
        "report_d_button": report_d_button,
        "report_e_button": report_e_button,
        "report_f_button": report_f_button,
        "report_g_button": report_g_button,
        "report_h_button": report_h_button,
        "back_button": back_button
    }

