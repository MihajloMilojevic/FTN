from PyQt5 import QtCore, QtGui, QtWidgets


def setupUi(Form):

    font = QtGui.QFont()
    font.setPointSize(12)
    vbox_layout = QtWidgets.QVBoxLayout(Form)
    vbox_layout.setContentsMargins(50, 50, 50, 50)
    vbox_layout.setSpacing(10)
    vbox_layout.setObjectName("vbox_layout")
    odjavi_se_button = QtWidgets.QPushButton(Form)
    odjavi_se_button.setFont(font)
    odjavi_se_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    odjavi_se_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    odjavi_se_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    odjavi_se_button.setAutoDefault(False)
    odjavi_se_button.setDefault(False)
    odjavi_se_button.setFlat(True)
    odjavi_se_button.setObjectName("odjavi_se_button")
    odjavi_se_button.setText("Odjavi se")

    user_data_button = QtWidgets.QPushButton(Form)
    user_data_button.setFont(font)
    user_data_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    user_data_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    user_data_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    user_data_button.setAutoDefault(False)
    user_data_button.setDefault(False)
    user_data_button.setFlat(True)
    user_data_button.setObjectName("user_data_button")
    user_data_button.setText("Promeni lične podatke")

    name_label = QtWidgets.QLabel(Form)
    name_label.setFont(font)
    name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    uloga_label = QtWidgets.QLabel(Form)
    uloga_label.setFont(font)
    uloga_label.setText("Kupac")
    uloga_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    
    vbox_layout.addWidget(name_label)
    vbox_layout.addWidget(uloga_label)
    vbox_layout.addWidget(odjavi_se_button)
    vbox_layout.addWidget(user_data_button)

    Form.setLayout(vbox_layout)
    QtCore.QMetaObject.connectSlotsByName(Form)
    return {
        "odjavi_se_button": odjavi_se_button,
        "name_label": name_label,
        "user_data_button": user_data_button
    }

