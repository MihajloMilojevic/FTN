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
    label.setText("Korisničko ime:")
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

    label_3 = QtWidgets.QLabel(Form)
    label_3.setFont(font)
    label_3.setText("Ime:")
    label_3.setObjectName("label_3")
    formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, label_3)
    name_input = QtWidgets.QLineEdit(Form)
    name_input.setStyleSheet("padding: 5px 10px;")
    name_input.setDragEnabled(False)
    name_input.setObjectName("name_input")
    name_input.setFont(font)
    name_input.setMaximumWidth(300)
    formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, name_input)

    label_4 = QtWidgets.QLabel(Form)
    label_4.setFont(font)
    label_4.setText("Prezime:")
    label_4.setObjectName("label_4")
    formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, label_4)
    surname_input = QtWidgets.QLineEdit(Form)
    surname_input.setStyleSheet("padding: 5px 10px;")
    surname_input.setDragEnabled(False)
    surname_input.setObjectName("surname_input")
    surname_input.setFont(font)
    surname_input.setMaximumWidth(300)
    formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, surname_input)

    register_button = QtWidgets.QPushButton(Form)
    register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    register_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    register_button.setText("Registruj se")
    register_button.setFont(font)
    # register_button.setMaximumWidth(300)
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
    buttonLayout.addWidget(register_button)

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
        "name_input": name_input,
        "surname_input": surname_input,
        "register_button": register_button,
        "cancel_button": cancel_button
    }