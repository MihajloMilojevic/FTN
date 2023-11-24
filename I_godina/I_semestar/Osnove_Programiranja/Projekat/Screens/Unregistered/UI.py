from PyQt5 import QtCore, QtGui, QtWidgets


def setupUi(Form):

    font = QtGui.QFont()
    font.setPointSize(12)

    vbox_layout = QtWidgets.QVBoxLayout(Form)
    vbox_layout.setContentsMargins(50, 50, 50, 50)
    vbox_layout.setSpacing(10)
    vbox_layout.setObjectName("vbox_layout")
    vbox_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    login_button = QtWidgets.QPushButton(Form)
    login_button.setFont(font)
    login_button.setFixedWidth(300)
    login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    login_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    login_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    login_button.setAutoDefault(False)
    login_button.setDefault(False)
    login_button.setFlat(True)
    login_button.setObjectName("login_button")
    login_button.setText("Prijavi se")
    vbox_layout.addWidget(login_button)

    register_button = QtWidgets.QPushButton(Form)
    register_button.setFont(font)
    register_button.setFixedWidth(300)
    register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    register_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    register_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    register_button.setAutoDefault(False)
    register_button.setDefault(False)
    register_button.setFlat(True)
    register_button.setObjectName("register_button")
    register_button.setText("Registuj se")
    vbox_layout.addWidget(register_button)
    Form.setLayout(vbox_layout)
    QtCore.QMetaObject.connectSlotsByName(Form)
    return {
        "login_button": login_button,
        "register_button": register_button
    }

