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
    uloga_label.setText("Prodavac")
    uloga_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    search_films_button = QtWidgets.QPushButton(Form)
    search_films_button.setFont(font)
    search_films_button.setFixedWidth(300)
    search_films_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    search_films_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    search_films_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    search_films_button.setAutoDefault(False)
    search_films_button.setDefault(False)
    search_films_button.setFlat(True)
    search_films_button.setObjectName("search_films_button")
    search_films_button.setText("Pretraži filmove")

    booking_button = QtWidgets.QPushButton(Form)
    booking_button.setFont(font)
    booking_button.setFixedWidth(300)
    booking_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    booking_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    booking_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    booking_button.setAutoDefault(False)
    booking_button.setDefault(False)
    booking_button.setFlat(True)
    booking_button.setObjectName("booking_button")
    booking_button.setText("Rezerviši kartu")

    ticketlist_button = QtWidgets.QPushButton(Form)
    ticketlist_button.setFont(font)
    ticketlist_button.setFixedWidth(300)
    ticketlist_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    ticketlist_button.setFocusPolicy(QtCore.Qt.ClickFocus)
    ticketlist_button.setStyleSheet("background: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"outline: none;\n"
"padding: 10px 30px;")
    ticketlist_button.setAutoDefault(False)
    ticketlist_button.setDefault(False)
    ticketlist_button.setFlat(True)
    ticketlist_button.setObjectName("ticketlist_button")
    ticketlist_button.setText("Pogledaj karte")
    
    vbox_layout.addWidget(name_label)
    vbox_layout.addWidget(uloga_label)
    vbox_layout.addWidget(odjavi_se_button)
    vbox_layout.addWidget(user_data_button)
    vbox_layout.addWidget(search_films_button)
    vbox_layout.addWidget(booking_button)
    vbox_layout.addWidget(ticketlist_button)

    Form.setLayout(vbox_layout)
    QtCore.QMetaObject.connectSlotsByName(Form)
    return {
        "odjavi_se_button": odjavi_se_button,
        "name_label": name_label,
        "user_data_button": user_data_button,
        "search_films_button": search_films_button,
        "booking_button": booking_button,
        "ticketlist_button": ticketlist_button,
    }

