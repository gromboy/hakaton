from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from main import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_app = Main()
    admin_app.show()
    sys.exit(app.exec())
