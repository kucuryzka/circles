import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.paint)

        self.qp = QPainter()
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.flag = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor("yellow"))
        coords = [random.randint(50, 550), random.randint(50, 450)]
        size = random.randint(5, 50)
        qp.drawEllipse(*coords, size, size)


if __name__ == '__main__':
    ex = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(ex.exec())