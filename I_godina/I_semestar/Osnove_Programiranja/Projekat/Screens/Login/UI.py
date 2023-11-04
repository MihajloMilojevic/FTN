from PyQt5 import QtCore, QtGui, QtWidgets

def setupUi(Form):
    
    verticalLayout = QtWidgets.QVBoxLayout()
    verticalLayout
    verticalLayout.setContentsMargins(20, 20, 20, 20)
    verticalLayout.setObjectName("verticalLayout")
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
    formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, username_input)
    label_2 = QtWidgets.QLabel(Form)
    label_2.setObjectName("label_2")
    label_2.setText("Lozinka: ")
    label_2.setFont(font)
    formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, label_2)
    password_input = QtWidgets.QLineEdit(Form)
    password_input.setStyleSheet("padding: 5px 10px;")
    password_input.setInputMask("")
    password_input.setText("")
    password_input.setMaxLength(32767)
    password_input.setFrame(True)
    password_input.setEchoMode(QtWidgets.QLineEdit.Password)
    password_input.setDragEnabled(False)
    password_input.setObjectName("password_input")
    password_input.setFont(font)
    formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, password_input)
    verticalLayout.addLayout(formLayout)
    prijavi_se_button = QtWidgets.QPushButton(Form)
    prijavi_se_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    prijavi_se_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    prijavi_se_button.setText("Prijavi se")
    prijavi_se_button.setFont(font)
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
    verticalLayout.addWidget(prijavi_se_button)
    odustani_button = QtWidgets.QPushButton(Form)
    odustani_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    odustani_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    odustani_button.setText("Odustani")
    odustani_button.setFont(font)
    odustani_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    odustani_button.setAutoDefault(False)
    odustani_button.setDefault(False)
    odustani_button.setFlat(True)
    odustani_button.setObjectName("odustani_button")
    verticalLayout.addWidget(odustani_button)
    Form.setLayout(verticalLayout)
    return {
        "username_input": username_input,
        "password_input": password_input,
        "prijavi_se_button": prijavi_se_button,
        "odustani_button": odustani_button
    }