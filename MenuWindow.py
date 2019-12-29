import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.Qt import QSize
from LevelsWindow import LevelsWindow
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, \
    QErrorMessage, QTableWidgetItem, QHeaderView, QInputDialog, QStyle
from PyQt5.QtGui import QColor, QImage, QPalette, QBrush, QIcon, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/MenuWindow.ui", self)
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

        # Настройка кнопок
        self.pushButton.setStyleSheet(style_buttons)
        self.pushButton.clicked.connect(self.game_start)
        self.pushButton_2.setStyleSheet(style_buttons)
        self.pushButton_2.clicked.connect(self.game_continue)
        self.pushButton_3.setStyleSheet(style_buttons)
        self.pushButton_3.clicked.connect(self.levels)
        self.pushButton_4.setStyleSheet(style_buttons)
        self.pushButton_4.clicked.connect(self.quit)

        # Настройка надписи
        self.label.setStyleSheet("color: rgb(255, 255, 255)")

        # Изменение названия главного окна
        self.setWindowTitle("Portal")

    def game_start(self):
        # Запуск игры с самого начала (со сбросом предыдущего прогресса)
        pass

    def game_continue(self):
        # Продолжение игры
        pass

    def levels(self):
        self.window = LevelsWindow()
        self.window.show()

    def quit(self):
        sys.exit(app.exec_())

    def set_background(self):
        # Загрузка фона для главного окна
        oImage = QImage("data/MenuWindow_background.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())