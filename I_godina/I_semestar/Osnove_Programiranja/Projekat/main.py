from App.State import db
from Database.initialDB import populateDatabase
from PyQt5.QtWidgets import QApplication
from App import App
import sys

def main():
    db.load()
    q_app = QApplication(sys.argv)
    app = App()
    code = q_app.exec_()
    db.save()
    sys.exit(code)

if __name__ == '__main__':
    # populateDatabase()
    main()
