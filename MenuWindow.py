import sys
import pygame
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.Qt import QSize, QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, \
    QErrorMessage, QTableWidgetItem, QHeaderView, QInputDialog, QStyle, QWidget
from PyQt5.QtGui import QColor, QImage, QPalette, QBrush, QIcon, QPixmap


pygame.init()
pygame.mixer.music.load('data/background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


class LevelsWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/LevelsWindow.ui", self)
        self.click_sound = pygame.mixer.Sound('data/click_sound.wav')
        self.initUI()

    def initUI(self):
        # Загрузка фона
        self.set_background()

        # Загрузка кнопок
        self.setting_buttons()

        # Загрузка изображений
        self.load_maps()

        # Изменение названия главного окна
        self.setWindowTitle("Portal")

    def load_maps(self):
        # Загрузка картинок карт
        self.pixmap = QPixmap("data/ExampleMapImage.jpg")

        self.label_2.setPixmap(self.pixmap)
        self.label_4.setPixmap(self.pixmap)
        self.label_6.setPixmap(self.pixmap)
        self.label_8.setPixmap(self.pixmap)

    def setting_buttons(self):
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
        self.pushButton.clicked.connect(self.load_level)

        self.pushButton_2.setStyleSheet(style_buttons)
        self.pushButton_2.clicked.connect(self.load_level)

        self.pushButton_3.setStyleSheet(style_buttons)
        self.pushButton_3.clicked.connect(self.load_level)

        self.pushButton_4.setStyleSheet(style_buttons)
        self.pushButton_4.clicked.connect(self.load_level)

        self.pushButton_5.setStyleSheet(style_buttons)
        self.pushButton_5.clicked.connect(self.return_in_menu)

    def set_background(self):
        # Загрузка фона для главного окна
        oImage = QImage("data/MenuWindow_background.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)

    def return_in_menu(self):
        pygame.mixer.Sound.play(self.click_sound)
        self.window = MainWindow()
        self.window.show()
        self.close()

    def load_level(self):
        pygame.mixer.Sound.play(self.click_sound)
        name = self.sender().text()[-1]
        # Запуск уровня name
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/MenuWindow.ui", self)
        self.click_sound = pygame.mixer.Sound('data/click_sound.wav')
        self.initUI()

    def initUI(self):
        # Загрузка фона
        self.set_background()

        # Загрузка кнопок
        self.setting_buttons()

        # Настройка надписи
        self.label.setStyleSheet("color: rgb(255, 255, 255)")

        # Изменение названия главного окна
        self.setWindowTitle("Portal")

    def setting_buttons(self):
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

    def game_start(self):
        pygame.mixer.Sound.play(self.click_sound)
        # Запуск игры с самого начала (со сбросом предыдущего прогресса)
        pass

    def game_continue(self):
        pygame.mixer.Sound.play(self.click_sound)
        # Продолжение игры
        pass

    def levels(self):
        pygame.mixer.Sound.play(self.click_sound)
        self.window = LevelsWindow()
        self.window.show()
        self.close()

    def quit(self):
        pygame.mixer.Sound.play(self.click_sound)
        self.close()

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