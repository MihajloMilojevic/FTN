from App.State import db
from PyQt5.QtWidgets import QApplication
from App import App
import sys

if __name__ == '__main__':
    db.load()
    # print("Učitano: \n", db.toJsonString(2))
    q_app = QApplication(sys.argv)
    app = App()
    code = q_app.exec_()
    # print("Upisano: \n", db.toJsonString(2))
    db.save()
    sys.exit(code)
