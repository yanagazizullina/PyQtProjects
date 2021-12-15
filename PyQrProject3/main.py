import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QLineEdit, QTextEdit

from ms_sygnal import MssSignal
from sec_signal import SecondsSignal


class App(QWidget):

    def __init__(self):
        super(App, self).__init__()

        self.secSignal = SecondsSignal()
        self.mssSignal = MssSignal()


        self.title = 'PyQtApp3'
        self.left = 300
        self.top = 200
        self.width = 300
        self.height = 230

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.minlabel = QLabel(self)
        self.minlabel.setText('Минуты')
        self.minlabel.move(30, 30)

        self.minqtext = QLineEdit(self)
        self.minqtext.setGeometry(140, 30, 140, 30)


        self.seclabl = QLabel(self)
        self.seclabl.setText('Секунды')
        self.seclabl.move(30, 80)

        self.secqtext = QLineEdit(self)
        self.secqtext.setGeometry(140, 80, 140, 30)

        self.msslabl = QLabel(self)
        self.msslabl.setText('Миллисекунды')
        self.msslabl.move(30, 130)

        self.mssqtext = QLineEdit(self)
        self.mssqtext.setGeometry(140, 130, 140, 30)

        self.button = QPushButton(self)
        self.button.move(110, 180)
        self.button.setText("Перевести")

        self.secSignal.upd_signal.connect(self.secSignal.upd_value)
        self.mssSignal.upd_signal.connect(self.mssSignal.upd_value)

        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        text_val = int(self.minqtext.text())
        self.secSignal.upd_signal.emit(text_val)
        self.mssSignal.upd_signal.emit(text_val)
        self.secqtext.setText(self.secSignal.value)
        self.mssqtext.setText(self.mssSignal.value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())