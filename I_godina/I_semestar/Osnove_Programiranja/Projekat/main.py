from App.State import db
from PyQt5.QtWidgets import QApplication
from App import App
import sys

if __name__ == '__main__':
    db.load()
    q_app = QApplication(sys.argv)
    app = App()
    code = q_app.exec_()
    db.save()
    sys.exit(code)
