from PyQt5 import QtCore, QtGui, QtWidgets


def setupUi(Form):

    font = QtGui.QFont()
    font.setPointSize(12)

    vbox_layout = QtWidgets.QVBoxLayout(Form)
    vbox_layout.setContentsMargins(50, 50, 50, 50)
    vbox_layout.setSpacing(10)
    vbox_layout.setObjectName("vbox_layout")
    vbox_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    prijavi_se_button = QtWidgets.QPushButton(Form)
    prijavi_se_button.setFont(font)
    prijavi_se_button.setMaximumWidth(300)
    prijavi_se_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    prijavi_se_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    prijavi_se_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    prijavi_se_button.setAutoDefault(False)
    prijavi_se_button.setDefault(False)
    prijavi_se_button.setFlat(True)
    prijavi_se_button.setObjectName("prijavi_se_button")
    prijavi_se_button.setText("Prijavi se")
    vbox_layout.addWidget(prijavi_se_button)

    registruj_se_button = QtWidgets.QPushButton(Form)
    registruj_se_button.setFont(font)
    registruj_se_button.setMaximumWidth(300)
    registruj_se_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    registruj_se_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    registruj_se_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    registruj_se_button.setAutoDefault(False)
    registruj_se_button.setDefault(False)
    registruj_se_button.setFlat(True)
    registruj_se_button.setObjectName("registruj_se_button")
    registruj_se_button.setText("Registuj se")
    vbox_layout.addWidget(registruj_se_button)
    Form.setLayout(vbox_layout)
    QtCore.QMetaObject.connectSlotsByName(Form)
    return {
        "prijavi_se_button": prijavi_se_button,
        "registruj_se_button": registruj_se_button
    }

