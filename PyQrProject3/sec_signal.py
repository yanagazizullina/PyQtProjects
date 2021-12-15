from PyQt5.QtCore import pyqtSignal, QObject

class SecondsSignal(QObject):
    upd_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.value = ''

    def upd_value(self, new_val: int):
        self.value = str(int(new_val) * 60)