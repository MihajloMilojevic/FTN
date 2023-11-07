from PyQt5 import QtWidgets

def MessageBox():
    message_box = QtWidgets.QMessageBox()
    message_box.setStyleSheet("color: white")
    return message_box