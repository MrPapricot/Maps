import qtfunc
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self, size=10, x=60, y=60, delta=0.821, mod='map'):
        super().__init__()
        uic.loadUi('qtinterface.ui', self)  # Загружаем дизайн
        self.pushButton_2.clicked.connect(self.type_map)
        self.pushButton_3.clicked.connect(self.type_map)
        self.pushButton_4.clicked.connect(self.type_map)


        self.size = size
        self.x, self.y = x, y
        self.delta = delta
        self.mod = mod
        self.get_zapros()

    def get_zapros(self):
        self.label.setPixmap(QPixmap(qtfunc.createMap(self.x, self.y, self.size, self.mod)))

    def type_map(self):
        bt = self.sender()
        dict = {
            'Карта': 'map',
            'Спутник': 'sat',
            'Гибрид': 'sat,skl'
        }
        n = bt.text()
        self.mod = dict[n]
        self.get_zapros()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())