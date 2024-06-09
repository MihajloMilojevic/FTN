
from PyQt5.QtWidgets import QApplication
from src.app import App
import sys
from src.cache import scores

def main():
    scores.load()
    q_app = QApplication(sys.argv)
    app = App()
    code = q_app.exec_()
    scores.save()
    sys.exit(code)


if __name__ == '__main__':
    main()
