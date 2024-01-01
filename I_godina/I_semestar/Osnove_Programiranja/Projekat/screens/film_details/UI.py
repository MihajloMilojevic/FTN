from PyQt5 import QtCore, QtGui, QtWidgets

def setupUi(frame):
    frame_layout = QtWidgets.QVBoxLayout()
    frame.setLayout(frame_layout)
    frame_layout.setObjectName("frame_layout")
    formLayout = QtWidgets.QFormLayout()
    formLayout.setVerticalSpacing(15)
    formLayout.setObjectName("formLayout")
    font = QtGui.QFont()
    font.setPointSize(12)
    label = QtWidgets.QLabel(frame)

    label.setFont(font)
    label.setText("Šifra:")
    label.setStyleSheet("color: white")
    label.setObjectName("label")
    formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, label)
    label_2 = QtWidgets.QLabel(frame)

    label_2.setFont(font)
    label_2.setText("Ime: ")
    label_2.setStyleSheet("color: white")
    label_2.setObjectName("label_2")
    formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, label_2)
    label_6 = QtWidgets.QLabel(frame)

    label_6.setFont(font)
    label_6.setText("Režiser: ")
    label_6.setStyleSheet("color: white")
    label_6.setObjectName("label_6")
    formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, label_6)
    label_7 = QtWidgets.QLabel(frame)

    label_7.setFont(font)
    label_7.setText("Zemlja porekla:")
    label_7.setStyleSheet("color: white")
    label_7.setObjectName("label_7")
    formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, label_7)
    label_8 = QtWidgets.QLabel(frame)

    label_8.setFont(font)
    label_8.setText("Godina:")
    label_8.setStyleSheet("color: white")
    label_8.setObjectName("label_8")
    formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, label_8)
    label_10 = QtWidgets.QLabel(frame)

    label_10.setFont(font)
    label_10.setText("Glavne uloge:")
    label_10.setStyleSheet("color: white")
    label_10.setObjectName("label_10")
    formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, label_10)
    label_5 = QtWidgets.QLabel(frame)

    label_5.setFont(font)
    label_5.setText("Žanrovi: ")
    label_5.setStyleSheet("color: white")
    label_5.setObjectName("label_5")
    formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, label_5)
    label_9 = QtWidgets.QLabel(frame)

    label_9.setFont(font)
    label_9.setText("Opis:")
    label_9.setStyleSheet("color: white")
    label_9.setObjectName("label_9")
    formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, label_9)
    id_label = QtWidgets.QLabel(frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(id_label.sizePolicy().hasHeightForWidth())
    id_label.setSizePolicy(sizePolicy)
    id_label.setMinimumSize(QtCore.QSize(0, 0))

    id_label.setFont(font)
    id_label.setText("Šifra")
    id_label.setStyleSheet("color: white; border: 1px solid white; padding: 10px;")
    id_label.setObjectName("id_label")
    formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, id_label)
    name_label = QtWidgets.QLabel(frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(name_label.sizePolicy().hasHeightForWidth())
    name_label.setSizePolicy(sizePolicy)
    name_label.setMinimumSize(QtCore.QSize(0, 0))

    name_label.setFont(font)
    name_label.setText("Ime")
    name_label.setStyleSheet("color: white; border: 1px solid white; padding: 10px;")
    name_label.setObjectName("name_label")
    formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, name_label)
    director_label = QtWidgets.QLabel(frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(director_label.sizePolicy().hasHeightForWidth())
    director_label.setSizePolicy(sizePolicy)
    director_label.setMinimumSize(QtCore.QSize(0, 0))

    director_label.setFont(font)
    director_label.setText("Režiser")
    director_label.setStyleSheet("color: white; border: 1px solid white; padding: 10px;")
    director_label.setObjectName("director_label")
    formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, director_label)
    country_label = QtWidgets.QLabel(frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(country_label.sizePolicy().hasHeightForWidth())
    country_label.setSizePolicy(sizePolicy)
    country_label.setMinimumSize(QtCore.QSize(0, 0))

    country_label.setFont(font)
    country_label.setText("Zemlja")
    country_label.setStyleSheet("color: white; border: 1px solid white; padding: 10px;")
    country_label.setObjectName("country_label")
    formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, country_label)
    year_label = QtWidgets.QLabel(frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(year_label.sizePolicy().hasHeightForWidth())
    year_label.setSizePolicy(sizePolicy)
    year_label.setMinimumSize(QtCore.QSize(0, 0))

    year_label.setFont(font)
    year_label.setText("Godina:")
    year_label.setStyleSheet("color: white; border: 1px solid white; padding: 10px;")
    year_label.setObjectName("year_label")
    formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, year_label)
    roles_label = QtWidgets.QLabel(frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(roles_label.sizePolicy().hasHeightForWidth())
    roles_label.setSizePolicy(sizePolicy)
    roles_label.setMinimumSize(QtCore.QSize(0, 0))

    roles_label.setFont(font)
    roles_label.setText("Glavne uloge")
    roles_label.setStyleSheet("color: white; border: 1px solid white; padding: 10px;")
    roles_label.setObjectName("roles_label")
    formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, roles_label)
    genres_label = QtWidgets.QLabel(frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(genres_label.sizePolicy().hasHeightForWidth())
    genres_label.setSizePolicy(sizePolicy)
    genres_label.setMinimumSize(QtCore.QSize(0, 0))

    genres_label.setFont(font)
    genres_label.setText("Žanrovi")
    genres_label.setStyleSheet("color: white; border: 1px solid white; padding: 10px;")
    genres_label.setObjectName("genres_label")
    formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, genres_label)

    description_label = QtWidgets.QLabel(frame)
    description_label.setFont(font)
    description_label.setText("Opis")
    description_label.setStyleSheet("color: white; border: 1px solid white; padding: 10px;")
    description_label.setObjectName("description_label")
    formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, description_label)

    id_label.setWordWrap(True)
    name_label.setWordWrap(True)
    director_label.setWordWrap(True)
    country_label.setWordWrap(True)
    year_label.setWordWrap(True)
    roles_label.setWordWrap(True)
    genres_label.setWordWrap(True)
    description_label.setWordWrap(True)

    frame_layout.addLayout(formLayout)
    
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
    frame_layout.addWidget(back_button)
    

    return {
        "id_label": id_label,
        "name_label": name_label,
        "director_label": director_label,
        "country_label": country_label,
        "year_label": year_label,
        "roles_label": roles_label,
        "genres_label": genres_label,
        "description_label": description_label,
        "back_button": back_button,
    }
