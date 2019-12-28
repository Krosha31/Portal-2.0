import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.Qt import QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, \
    QErrorMessage, QTableWidgetItem, QHeaderView, QInputDialog, QStyle, QWidget
from PyQt5.QtGui import QColor, QImage, QPalette, QBrush, QIcon, QPixmap


class LevelsWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/LevelsWindow.ui", self)
        self.initUI()

    def initUI(self):
        # Загрузка фона
        self.set_background()

        # Стиль кнопок
        style_buttons = '''
        QPushButton {background-color: rgb(139, 210, 238);
                     border: none;
                     color: rgb(255, 255, 255)}
        QPushButton::hover {background-color: rgb(224, 232, 246)}
        QPushButton::clicked {background-color: rgb(139, 210, 238);
                              border: 1px solid rgb(660, 127, 177)}
        '''

        # Изменение названия главного окна
        self.setWindowTitle("Portal")

    def game_start(self):
        # Запуск игры с самого начала (со сбросом предыдущего прогресса)
        pass

    def game_continue(self):
        # Продолжение игры
        pass

    def levels(self):
        pass

    def set_background(self):
        # Загрузка фона для главного окна
        oImage = QImage("data/MenuWindow_background.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)