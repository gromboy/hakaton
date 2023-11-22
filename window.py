import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from UI import Ui_MainWindow
from PyQt5.QtGui import QIcon
from main import *


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.ico'))
        self.status = QLabel(self)
        self.statusbar.addWidget(self.status)
        self.now = self.general
        self.btn.clicked.connect(lambda k: self.now())

        self.action6.triggered.connect(self.general)
        self.action.triggered.connect(self.timeon)
        self.action2.triggered.connect(self.proc)
        self.action3.triggered.connect(self.ram)
        self.action4.triggered.connect(self.disks)

        self.general()

    @staticmethod
    def randperc():
        return randint(10, 40)

    def disks(self):
        self.progress.setValue(self.randperc())
        text = ''''''
        time.sleep(0.02)
        inf = disk()

        for i in inf:
            text += i + '\n'
            for j in inf[i]:
                text += '\t' + j + ' - ' + inf[i][j] + '\n'

        self.progress.setValue(100)
        self.status.setText('Диски')
        self.now = self.disks
        self.place.setText(text)

    def ram(self):
        self.progress.setValue(self.randperc())
        text = ''''''
        time.sleep(0.02)
        inf = op()
        for i in inf:
            text += i + ' - ' + str(inf[i]) + '\n'
        self.progress.setValue(100)
        self.status.setText('Оперативная память')
        self.now = self.ram
        self.place.setText(text)

    def proc(self):
        self.progress.setValue(self.randperc())

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
        self.progress.setValue(self.randperc())
        time.sleep(0.02)
        self.progress.setValue(100)
        self.place.setText(time_on())
        self.now = self.timeon
        self.status.setText('Время включения')

    def general(self):
        self.progress.setValue(self.randperc())
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
