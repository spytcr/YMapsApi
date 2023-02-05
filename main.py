import math
import sys
import api
from ui.main_window import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.btn_find.clicked.connect(self.find)
        self.chb_index.setVisible(False)
        self.chb_index.stateChanged.connect(self.change_index)
        self.cb_mode.currentTextChanged.connect(self.change_mode)

        self.label.mousePressEvent = self.mouse_press
        self.label.setFocusPolicy(Qt.StrongFocus)

        self.mode = 'map'
        self.coord = (0, 0)
        self.zoom = 2
        self.point = None
        self.address = None

        self.draw_map()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.zoom_map(1)
        elif event.key() == Qt.Key_PageDown:
            self.zoom_map(-1)
        elif event.key() == Qt.Key_Up:
            self.move_map(650 / 2, 0)
        elif event.key() == Qt.Key_Down:
            self.move_map(650 / 2, 450)
        elif event.key() == Qt.Key_Left:
            self.move_map(0, 450 / 2)
        elif event.key() == Qt.Key_Right:
            self.move_map(650, 450 / 2)

    def mouse_press(self, event):
        point = self.px_to_coord(event.pos().x(), event.pos().y())
        if event.button() == Qt.LeftButton:
            self.mark(point, api.get_address(point))
        elif event.button() == Qt.RightButton:
            organization = api.get_organization(point)
            if organization is not None:
                self.mark(*organization)
                if self.point is not None:
                    self.coord = self.point
        self.draw_map()

    def mark(self, point, address):
        self.point = point
        self.address = address

        if self.address is None:
            self.le_find.setText('Адрес не найден')
        else:
            self.chb_index.setVisible(True)
            self.change_index(self.chb_index.isChecked())

        self.le_find.setReadOnly(True)

        self.btn_find.setText('Сбросить')
        self.btn_find.clicked.disconnect()
        self.btn_find.clicked.connect(self.reset)

    def find(self):
        point = api.get_point(self.le_find.text())
        self.mark(point, api.get_address(point))
        if self.point is not None:
            self.coord = self.point
        self.draw_map()

    def reset(self):
        self.chb_index.setVisible(False)

        self.le_find.clear()
        self.le_find.setReadOnly(False)

        self.btn_find.setText('Найти')
        self.btn_find.clicked.disconnect()
        self.btn_find.clicked.connect(self.find)

        self.point = None
        self.draw_map()

    def draw_map(self):
        image = api.get_map(self.mode, self.coord, self.zoom, self.point)
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        self.label.setPixmap(pixmap)

    def zoom_map(self, i):
        if 0 <= self.zoom + i <= 17:
            self.zoom += i
        self.draw_map()

    def px_to_coord(self, x, y):
        dpx = 360 / (1 << (self.zoom + 8))
        dpy = 360 / (1 << (self.zoom + 8)) * math.cos(self.coord[1] * math.pi / 180)
        return self.coord[0] - dpx * (650 / 2 - x), self.coord[1] + dpy * (450 / 2 - y)

    def move_map(self, x, y):
        self.coord = self.px_to_coord(x, y)
        self.draw_map()

    def change_mode(self, text):
        self.mode = {
            'Схема': 'map',
            'Спутник': 'sat',
            'Гибрид': 'sat,skl'
        }[text]
        self.draw_map()

    def change_index(self, checked):
        address = self.address[0]
        if checked and self.address[1]:
            address += ', ' + self.address[1]
        self.le_find.setText(address)


def exception_hook(*args, **kwargs):
    sys.__excepthook__(*args, **kwargs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.excepthook = exception_hook
    sys.exit(app.exec())
