import sys
import pygame
import os
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.Qt import QSize, QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, \
    QErrorMessage, QTableWidgetItem, QHeaderView, QInputDialog, QStyle, QWidget
from PyQt5.QtGui import QColor, QImage, QPalette, QBrush, QIcon, QPixmap
from game import load_image, load_level, reinit_groups


class LevelsWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/LevelsWindow.ui", self)
        self.click_sound = pygame.mixer.Sound('data/click_sound.wav')
        self.initUI()

    def initUI(self):
        # Загрузка иконки
        self.setWindowIcon(QIcon('data/icon.gif'))

        self.reinit_pygame()

        # Загрузка фона
        self.set_background()

        # Загрузка кнопок
        self.setting_buttons()

        # Загрузка изображений
        self.load_maps()

        # Изменение названия главного окна
        self.setWindowTitle("Portal")

        file_level = open('data/save.txt', encoding='utf8')
        data = file_level.read().split()
        self.num_level, self.max_level = int(data[0]), int(data[1])

    def reinit_pygame(self):
        pygame.init()

        # включение фоновой музыки
        pygame.mixer.music.load('data/background_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def load_maps(self):
        # Загрузка картинок карт
        self.pixmap = QPixmap("data/level_1_image.png")
        self.label_2.setPixmap(self.pixmap)
        self.pixmap = QPixmap("data/level_2_image.png")
        self.label_4.setPixmap(self.pixmap)
        self.pixmap = QPixmap("data/level_3_image.png")
        self.label_6.setPixmap(self.pixmap)
        self.pixmap = QPixmap("data/level_4_image.png")
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
        # Возвращение в главное меню
        self.window = MainWindow()
        self.window.show()
        self.close()

    def load_level(self):
        # Запуск выбранного уровня
        pygame.mixer.Sound.play(self.click_sound)
        name = int(self.sender().text()[-1])
        if name > self.max_level:
            # Проверка на пройденность
            error_message = QErrorMessage(self)
            error_message.showMessage("Вы еще не прошли этот уровень")
            return
        # Запуск уровня name
        file_level = open('data/save.txt', 'w')
        file_level.write(str(name) + ' ' + str(self.max_level))
        file_level.close()
        self.reinit_pygame()
        self.hide()
        reinit_groups()
        load_level()
        file_level = open('data/save.txt', 'w')
        file_level.write(str(self.num_level) + ' ' + str(self.max_level))
        file_level.close()
        self.reinit_pygame()
        self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/MenuWindow.ui", self)
        self.click_sound = pygame.mixer.Sound('data/click_sound.wav')
        self.initUI()

    def initUI(self):
        # Загрузка иконки
        self.setWindowIcon(QIcon('data/icon.gif'))

        self.reinit_pygame()

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
        self.pushButton.clicked.connect(self.game_continue)

        self.pushButton_2.setStyleSheet(style_buttons)
        self.pushButton_2.clicked.connect(self.game_start)

        self.pushButton_3.setStyleSheet(style_buttons)
        self.pushButton_3.clicked.connect(self.levels)

        self.pushButton_4.setStyleSheet(style_buttons)
        self.pushButton_4.clicked.connect(self.quit)

    def reinit_pygame(self):
        pygame.init()

        # включение фоновой музыки
        pygame.mixer.music.load('data/background_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def game_start(self):
        pygame.mixer.Sound.play(self.click_sound)
        # Запуск игры с самого начала (со сбросом предыдущего прогресса)
        num_level, max_level = 1, 1
        file_level = open('data/save.txt', 'w')
        file_level.write(str(num_level) + ' ' + str(max_level))
        file_level.close()
        self.reinit_pygame()
        self.hide()
        reinit_groups()
        win_flag = load_level()
        while num_level < 4 and win_flag:
            max_level = max(num_level, max_level)
            num_level += 1
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level))
            file_level.close()
            self.reinit_pygame()
            reinit_groups()
            win_flag = load_level()
        if num_level == 4:
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level + 1))
            file_level.close()
        self.reinit_pygame()
        self.show()

    def game_continue(self):
        pygame.mixer.Sound.play(self.click_sound)
        # Продолжение игры
        file_level = open('data/save.txt', encoding='utf8')
        data = file_level.read().split()
        num_level, max_level = int(data[0]), int(data[1])
        self.reinit_pygame()
        self.hide()
        reinit_groups()
        win_flag = load_level()
        while num_level < 4 and win_flag:
            max_level = max(num_level, max_level)
            num_level += 1
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level))
            file_level.close()
            self.reinit_pygame()
            reinit_groups()
            win_flag = load_level()
        if num_level == 4:
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level + 1))
            file_level.close()
        self.reinit_pygame()
        self.show()

    def levels(self):
        pygame.mixer.Sound.play(self.click_sound)
        # Запуск окна загрузки уровней
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