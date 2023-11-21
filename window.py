import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from UI import Ui_MainWindow
from PyQt5.QtGui import QIcon
from main import *


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.ico'))
        self.status = QLabel(self)
        self.statusbar.addWidget(self.status)
        self.now = self.general
        self.btn.clicked.connect(lambda k: self.now())
        self.general()

        self.action6.triggered.connect(self.general)
        self.action.triggered.connect(self.timeon)
        self.action2.triggered.connect(self.proc)

    def proc(self):
        self.progress.setValue(20)

        def correct_cores(arr):
            for i, j in enumerate(arr):
                yield f'Ядро {i + 1} - {j}%'

        text = ''''''
        inf = process_inf()
        for i in inf:
            if i == 'Ядра':
                text += i + ':\n' + '\n'.join(correct_cores(inf[i])) + '\n'
            else:
                text += i + ' - ' + str(inf[i]) + '\n'
        self.progress.setValue(100)
        self.status.setText('Процессор')
        self.now = self.proc
        self.place.setText(text)

    def timeon(self):
        self.progress.setValue(20)
        time.sleep(0.02)
        self.progress.setValue(100)
        self.place.setText(time_on())
        self.now = self.timeon
        self.status.setText('Время включения')

    def general(self):
        self.progress.setValue(20)
        text = ''''''
        inf = general_info()
        for i in inf:
            text += i + ' - ' + str(inf[i]) + '\n'
        self.progress.setValue(100)
        self.status.setText('Общая информация')
        self.now = self.general
        self.place.setText(text)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_app = Main()
    admin_app.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
