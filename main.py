import sys
import pygame
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, \
    QErrorMessage, QTableWidgetItem, QHeaderView, QInputDialog, QStyle, QWidget, QTableWidget, QAbstractItemView, \
    QHBoxLayout
from PyQt5.QtGui import QColor, QImage, QPalette, QBrush, QIcon, QPixmap, QPainter
from PyQt5.QtCore import Qt
from game import load_image, load_level, reinit_groups
import time


class ImageWidget(QWidget):
    def __init__(self, imagePath, parent):
        super(ImageWidget, self).__init__(parent)
        self.picture = QPixmap(imagePath)
        width, height = self.picture.size().width(), self.picture.size().height()
        self.picture = self.picture.scaled(500, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.picture)


class LevelsWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/LevelsWindow.ui", self)
        self.click_sound = pygame.mixer.Sound('data/click_sound.wav')
        self.window = None
        self.error_message = None
        self.hack = False
        self.initUI()

    def initUI(self):
        # Загрузка иконки
        self.setWindowIcon(QIcon('data/icon.gif'))

        self.reinit_pygame()

        # Загрузка фона
        self.set_background()

        # Загрузка кнопок
        self.setting_buttons()

        # Загрузка таблицы уровней
        self.load_table()

        # Изменение названия главного окна
        self.setWindowTitle("Portal")

        # Настройка надписи
        self.label.setStyleSheet("color: rgb(255, 255, 255)")

        file_level = open('data/save.txt', encoding='utf8')
        data = file_level.read().split()
        self.num_level, self.max_level = int(data[0]), int(data[1])

    def reinit_pygame(self):
        pygame.init()

        # включение фоновой музыки
        pygame.mixer.music.load('data/background_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.AltModifier + Qt.ShiftModifier):
            if event.key() == Qt.Key_P:
                self.hack = True

    def load_table(self):
        # Настройка стиля таблицы
        style = "background-color: rgb(18,115,166);" \
                "color: rgb(255,255,255);"
        self.tableWidget.setStyleSheet(style)

        # Настройка вида таблицы
        fnt = self.tableWidget.font()
        fnt.setPointSize(25)
        self.tableWidget.setFont(fnt)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setRowCount(4)

        for i in range(4):
            self.tableWidget.setItem(i, 1, QTableWidgetItem("Уровень " + str(i + 1)))
            try:
                image = ImageWidget("data/level_" + str(i + 1) + "_image.png", self.tableWidget)
                layout = QHBoxLayout()
                layout.addWidget(image, 0, Qt.AlignCenter)
                self.tableWidget.setCellWidget(i, 0, image)
                self.tableWidget.setRowHeight(i, 300)
            except Exception as error:
                print(error)
            self.tableWidget.cellClicked.connect(self.load_level)

        header = self.tableWidget.horizontalHeader()
        self.tableWidget.resizeColumnsToContents()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

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

    def load_level(self, row, col):
        if row + 1 > self.max_level and not self.hack:
            return
        # Запуск выбранного уровня
        if self.window is None:
            self.close()
            self.window = MainWindow()
            self.window.show()
            self.window.load_lev(row + 1)


class SavesWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/SavesWindow.ui", self)
        self.click_sound = pygame.mixer.Sound('data/click_sound.wav')
        self.saves = []
        self.window = None
        self.initUI()

    def initUI(self):
        # Загрузка иконки
        self.setWindowIcon(QIcon('data/icon.gif'))

        self.reinit_pygame()

        # Загрузка фона
        self.set_background()

        # Загрузка кнопок
        self.setting_buttons()

        # Загрузка таблицы
        self.load_table()

        # Изменение названия главного окна
        self.setWindowTitle("Portal")

        # Настройка надписи
        self.label.setStyleSheet("color: rgb(255, 255, 255)")

    def reinit_pygame(self):
        pygame.init()

        # включение фоновой музыки
        pygame.mixer.music.load('data/background_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def load_table(self):
        # Настройка стиля таблицы
        style = "background-color: rgb(18,115,166);" \
                "color: rgb(255,255,255);"
        self.tableWidget.setStyleSheet(style)

        # Настройка вида таблицы
        fnt = self.tableWidget.font()
        fnt.setPointSize(25)
        self.tableWidget.setFont(fnt)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()

        self.saves = os.listdir("data/saves")
        self.saves = [elem for elem in self.saves if 'txt' in elem and elem != "last_save.txt"]
        self.tableWidget.setRowCount(len(self.saves))

        for i in range(len(self.saves)):
            name = self.saves[i].split('.')[0]
            self.tableWidget.setItem(i, 1, QTableWidgetItem(name.replace('_', ':')))
            try:
                image = ImageWidget("data/saves/images/" + name + ".png", self.tableWidget)
                layout = QHBoxLayout()
                layout.addWidget(image, 0, Qt.AlignCenter)
                self.tableWidget.setCellWidget(i, 0, image)
                self.tableWidget.setRowHeight(i, 300)
            except Exception as error:
                print(error)
            self.tableWidget.cellClicked.connect(self.load_save)

        header = self.tableWidget.horizontalHeader()
        self.tableWidget.resizeColumnsToContents()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

    def load_save(self, row, col):
        savename = "data/saves/" + self.saves[row]
        if self.window is None:
            self.close()
            self.window = MainWindow()
            self.window.show()
            self.window.load_save(savename)

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
        self.pushButton.clicked.connect(self.return_in_menu)

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


class FinishWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1200, 680)
        self.setWindowTitle('Congratulations')
        # Загрузка иконки
        self.setWindowIcon(QIcon('data/icon.gif'))

        # Загрузка фона
        self.set_background()

        pygame.init()
        # включение фоновой музыки
        pygame.mixer.music.load('data/finish_music.mp3')
        pygame.mixer.music.play(-1)

    def set_background(self):
        # Загрузка фона для главного окна
        oImage = QImage("data/finish_image.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)


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

        self.pushButton_5.setStyleSheet(style_buttons)
        self.pushButton_5.clicked.connect(self.saves)

        self.pushButton_6.setStyleSheet(style_buttons)
        self.pushButton_6.clicked.connect(self.game_last_save)

    def reinit_pygame(self):
        pygame.init()

        # включение фоновой музыки
        pygame.mixer.music.load('data/background_music.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def game_start(self):
        self.reinit_pygame()
        pygame.mixer.Sound.play(self.click_sound)
        # Запуск игры с самого начала (со сбросом предыдущего прогресса)
        num_level, max_level = 1, 1
        file_level = open('data/save.txt', 'w')
        file_level.write(str(num_level) + ' ' + str(max_level))
        file_level.close()

        self.reinit_pygame()
        self.hide()
        reinit_groups()
        try:
            win_flag = load_level()
        except Exception as error:
            print(error)
        reinit_groups()

        while num_level < 4 and win_flag == 1:
            max_level = max(num_level, max_level)
            num_level += 1
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level))
            file_level.close()
            self.reinit_pygame()
            reinit_groups()
            win_flag = load_level()
        if num_level == 4 and win_flag == 1:
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level + 1))
            file_level.close()
            reinit_groups()
            self.win = FinishWindow()
            self.win.show()
        elif win_flag == 2:
            reinit_groups()
            self.reinit_pygame()
            self.game_last_save()
        elif win_flag == 3:
            reinit_groups()
            self.reinit_pygame()
            self.game_continue()
        else:
            reinit_groups()
            self.reinit_pygame()
            self.show()

    def game_continue(self):
        self.reinit_pygame()
        pygame.mixer.Sound.play(self.click_sound)
        # Продолжение игры
        file_level = open('data/save.txt', encoding='utf8')
        data = file_level.read().split()
        num_level, max_level = int(data[0]), int(data[1])

        self.reinit_pygame()
        self.hide()
        reinit_groups()
        win_flag = load_level()
        reinit_groups()

        while num_level < 4 and win_flag == 1:
            max_level = max(num_level, max_level)
            num_level += 1
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level))
            file_level.close()
            self.reinit_pygame()
            reinit_groups()
            win_flag = load_level()
        if num_level == 4 and win_flag == 1:
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level + 1))
            file_level.close()
            reinit_groups()
            self.win = FinishWindow()
            self.win.show()
        elif win_flag == 2:
            reinit_groups()
            self.reinit_pygame()
            self.game_last_save()
        elif win_flag == 3:
            reinit_groups()
            self.reinit_pygame()
            self.game_continue()
        else:
            reinit_groups()
            self.reinit_pygame()
            self.show()

    def game_last_save(self):
        self.reinit_pygame()
        pygame.mixer.Sound.play(self.click_sound)
        # Продолжение игры c последнего сохранения
        file_level = open('data/save.txt', encoding='utf8')
        data = file_level.read().split()
        num_level, max_level = int(data[0]), int(data[1])
        try:
            name_last_save = open('data/saves/last_save.txt').readlines()[0]
        except Exception:
            return
        num_level = int(open(name_last_save).readlines()[0])
        file_level = open('data/save.txt', "w")
        file_level.write(str(num_level) + " " + str(max_level))
        file_level.close()

        self.reinit_pygame()
        self.hide()
        reinit_groups()
        win_flag = load_level(name_last_save)
        reinit_groups()

        while num_level < 4 and win_flag == 1:
            max_level = max(num_level, max_level)
            num_level += 1
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level))
            file_level.close()
            self.reinit_pygame()
            reinit_groups()
            win_flag = load_level()
        if num_level == 4 and win_flag == 1:
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level + 1))
            file_level.close()
            reinit_groups()
            self.win = FinishWindow()
            self.win.show()
        elif win_flag == 2:
            reinit_groups()
            self.reinit_pygame()
            self.game_last_save()
        elif win_flag == 3:
            reinit_groups()
            self.reinit_pygame()
            self.game_continue()
        else:
            reinit_groups()
            self.reinit_pygame()
            self.show()

    def load_save(self, savename):
        self.reinit_pygame()
        pygame.mixer.Sound.play(self.click_sound)
        # Загрузка сохранения
        file_level = open('data/save.txt', encoding='utf8')
        data = file_level.read().split()
        num_level, max_level = int(data[0]), int(data[1])
        num_level = int(open(savename).readlines()[0])
        file_level = open('data/save.txt', "w")
        file_level.write(str(num_level) + " " + str(max_level))
        file_level.close()

        self.reinit_pygame()
        self.hide()
        reinit_groups()
        win_flag = load_level(filename=savename)
        reinit_groups()

        while num_level < 4 and win_flag == 1:
            max_level = max(num_level, max_level)
            num_level += 1
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level))
            file_level.close()
            self.reinit_pygame()
            reinit_groups()
            win_flag = load_level()
        if num_level == 4 and win_flag == 1:
            file_level = open('data/save.txt', 'w')
            file_level.write(str(num_level) + ' ' + str(max_level + 1))
            file_level.close()
            reinit_groups()
            self.win = FinishWindow()
            self.win.show()
        elif win_flag == 2:
            reinit_groups()
            self.reinit_pygame()
            self.game_last_save()
        elif win_flag == 3:
            reinit_groups()
            self.reinit_pygame()
            self.game_continue()
        else:
            reinit_groups()
            self.reinit_pygame()
            self.show()

    def load_lev(self, num_level):
        self.reinit_pygame()
        pygame.mixer.Sound.play(self.click_sound)
        # Продолжение игры
        self.reinit_pygame()
        self.hide()
        reinit_groups()
        win_flag = load_level(val=num_level)
        reinit_groups()

        if win_flag == 2:
            reinit_groups()
            self.reinit_pygame()
            self.game_last_save()
        elif win_flag == 3:
            reinit_groups()
            self.reinit_pygame()
            self.load_lev(num_level)
        else:
            reinit_groups()
            self.reinit_pygame()
            self.show()

    def levels(self):
        pygame.mixer.Sound.play(self.click_sound)
        # Запуск окна загрузки уровней
        self.window = LevelsWindow()
        self.window.show()
        self.close()

    def saves(self):
        pygame.mixer.Sound.play(self.click_sound)
        # Запуск окна загрузки сохранений
        self.window = SavesWindow()
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