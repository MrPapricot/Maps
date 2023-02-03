import qtfunc
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self, size=10, x=60, y=60, delta=0.821, mod='map'):
        super().__init__()
        uic.loadUi('qtinterface.ui', self)  # Загружаем дизайн
        self.map.toggled.connect(self.setMode)
        self.skl.toggled.connect(self.setMode)
        self.sat.toggled.connect(self.setMode)
        self.size = size
        self.x, self.y = x, y
        self.delta = delta
        self.mod = mod
        self._get()

    def _get(self):
        self.label.setPixmap(QPixmap(qtfunc.createMap(self.x, self.y, self.size, self.mod)))

    def setMode(self):
        send = self.sender().text()
        self.mod = send
        self._get()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
