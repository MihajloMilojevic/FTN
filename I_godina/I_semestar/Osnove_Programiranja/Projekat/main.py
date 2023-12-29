from app.state import db
from PyQt5.QtWidgets import QApplication
from app import App
import sys
from utils.generate_showtimes import generate_all
from datetime import datetime

def main():
    db.load()
    # generate_all(datetime.today(), 14)
    q_app = QApplication(sys.argv)
    app = App()
    code = q_app.exec_()
    db.save()
    sys.exit(code)


if __name__ == '__main__':
    main()
