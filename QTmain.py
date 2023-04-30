import qtfunc
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self, size=10, x=60, y=60, delta=0.821, mod='map'):
        super().__init__()
        uic.loadUi('qtinterface.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.find_toponim)
        self.pushButton_2.clicked.connect(self.type_map)
        self.pushButton_3.clicked.connect(self.type_map)
        self.pushButton_4.clicked.connect(self.type_map)
        self.pushButton_5.clicked.connect(self.reset)
        self.pushButton_6.clicked.connect(self.switch)
        print(1)
        self.size = size
        self.x, self.y = x, y
        self.delta = delta
        self.mod = mod
        self.get_zapros()

    def reset(self):
        self.textBrowser.setText('')
        qtfunc.pt = ''
        self.get_zapros()

    def switch(self):
        qtfunc.flag = not qtfunc.flag
        self.find_toponim()


    def find_toponim(self):
        text = self.lineEdit.text()
        a = qtfunc.find_toponim(text)
        self.textBrowser.setText(a[1])
        a = a[0].split()
        self.x = float(a[0])
        self.y = float(a[1])
        self.get_zapros()

    def get_zapros(self):
        print((self.x, self.y, self.size, self.mod))
        self.label.setPixmap(QPixmap(qtfunc.createMap(self.x, self.y, self.size, self.mod)))

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == Qt.Key_PageUp:
            self.size += 1
            self.size %= 18
            self.delta /= 2
        elif event.key() == Qt.Key_PageDown:
            self.size -= 1
            self.size %= 18
            self.delta *= 2
        elif event.key() == Qt.Key_Up or event.key() == Qt.Key_W:
            if -90 < self.y + self.delta < 90:
                self.y += self.delta
        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_S:
            if -90 < self.y - self.delta < 90:
                print(123)
                self.y -= self.delta
        elif event.key() == Qt.Key_Right or event.key() == Qt.Key_D:
            if -180 < self.x + self.delta < 180:
                self.x += self.delta
        elif event.key() == Qt.Key_Left or event.key() == Qt.Key_A:
            if -180 < self.x - self.delta < 180:
                self.x -= self.delta
        self.get_zapros()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x, y = (event.x(), event.y())
            mx, my = self.label.width(), self.label.height()
            print(((y - my // 2) / my) * self.delta)
            if y <= my:
                x = self.x + (((x - mx // 2) / mx) * self.delta)
                y = self.y - (((y - my // 2) / my) * self.delta / 3)
                a = qtfunc.click_map(x, y, str(self.delta / 2))
                if a:
                    self.textBrowser.setText(a)
                else:
                    self.textBrowser.setText('не удалось ничего найти')
        elif event.button() == Qt.RightButton:
            print(event)
        self.get_zapros()


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