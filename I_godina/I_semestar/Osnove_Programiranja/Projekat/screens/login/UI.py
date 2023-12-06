from PyQt5 import QtCore, QtGui, QtWidgets

def setupUi(Form):
    
    verticalLayout = QtWidgets.QVBoxLayout()
    # verticalLayout.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter)
    verticalLayout.setContentsMargins(20, 20, 20, 20)
    verticalLayout.setSpacing(30)
    verticalLayout.setObjectName("verticalLayout")
    buttonLayout = QtWidgets.QVBoxLayout()
    buttonLayout.setContentsMargins(0, 0, 0, 0)
    buttonLayout.setSpacing(10)
    buttonLayout.setObjectName("buttonLayout")
    font = QtGui.QFont()
    font.setPointSize(12)
    formLayout = QtWidgets.QFormLayout()
    formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
    formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
    formLayout.setLabelAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
    formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
    formLayout.setHorizontalSpacing(10)
    formLayout.setVerticalSpacing(20)
    formLayout.setObjectName("formLayout")
    label = QtWidgets.QLabel(Form)
    label.setFont(font)
    label.setText("Korisničko name:")
    label.setObjectName("label")
    formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, label)
    username_input = QtWidgets.QLineEdit(Form)
    username_input.setStyleSheet("padding: 5px 10px;")
    username_input.setDragEnabled(False)
    username_input.setObjectName("username_input")
    username_input.setFont(font)
    username_input.setMaximumWidth(300)
    formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, username_input)
    label_2 = QtWidgets.QLabel(Form)
    label_2.setObjectName("label_2")
    label_2.setText("Lozinka: ")
    label_2.setFont(font)
    formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, label_2)
    password_input = QtWidgets.QLineEdit(Form)
    password_input.setStyleSheet("padding: 5px 10px;")
    password_input.setMaximumWidth(300)
    password_input.setInputMask("")
    password_input.setText("")
    password_input.setMaxLength(32767)
    password_input.setFrame(True)
    password_input.setEchoMode(QtWidgets.QLineEdit.Password)
    password_input.setDragEnabled(False)
    password_input.setObjectName("password_input")
    password_input.setFont(font)
    formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, password_input)
    login_button = QtWidgets.QPushButton(Form)
    login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    login_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    login_button.setText("Prijavi se")
    login_button.setFont(font)
    # login_button.setMaximumWidth(300)
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
    buttonLayout.addWidget(login_button)
    cancel_button = QtWidgets.QPushButton(Form)
    cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    cancel_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    cancel_button.setText("Odustani")
    cancel_button.setFont(font)
    # cancel_button.setMaximumWidth(300)
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
    buttonLayout.addWidget(cancel_button)

    verticalLayout.addLayout(formLayout)
    verticalLayout.addLayout(buttonLayout)
    Form.setLayout(verticalLayout)
    return {
        "username_input": username_input,
        "password_input": password_input,
        "login_button": login_button,
        "cancel_button": cancel_button
    }