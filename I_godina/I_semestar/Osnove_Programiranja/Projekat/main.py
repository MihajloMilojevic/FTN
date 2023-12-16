from app.state import db
from PyQt5.QtWidgets import QApplication
from app import App
from utils.generate_showtimes import generate
import sys


def main():
    db.load()
    generate(14)
    q_app = QApplication(sys.argv)
    app = App()
    code = q_app.exec_()
    db.save()
    sys.exit(code)


if __name__ == '__main__':
    main()
