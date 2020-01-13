import pygame
import os

pygame.init()
# Объявление констант и некоторых переменных
HEIGHT_CHELL = WIDTH_CHELL = 100
HEIGHT_CUBE = WIDTH_CUBE = 70
HEIGHT_PORTAL = 100
WIDTH_PORTAL = 20
WIDTH_WIRE = HEIGHT_WIRE = 100
HEIGHT_SPHERE = WIDTH_SPHERE = 16
STEP = 20
ZERO_SPEED = 5
walking_event = 25
pygame.time.set_timer(walking_event, 100)
svobod_pad_event = 24
pygame.time.set_timer(svobod_pad_event, 25)
pfly_event = 26
pygame.time.set_timer(pfly_event, 1)
door_event = 23
cube_in_level = True
pygame.time.set_timer(door_event, 1)
player_group = pygame.sprite.Group()
blue_portal_group = pygame.sprite.Group()
yellow_portal_group = pygame.sprite.Group()
cursor_group = pygame.sprite.Group()
cube_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()
player_left_cube = player_right_cube = 0


def load_image(name, colorkey=None):  # Загрузка изображения
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def chell_pass_to_portal(self, color):
    # функция конечной проверки прохождения персонажа через портал
    global speed_horizontal
    if color == 'blue':
        if blue_portal.position == 1 or blue_portal.position == 3:
            if blue_portal.rect.y <= self.rect.y + 15 <= blue_portal.rect.y + HEIGHT_PORTAL and \
                    blue_portal.rect.y <= self.rect.y + HEIGHT_CHELL - 15 <= \
                    blue_portal.rect.y + HEIGHT_PORTAL:
                if (blue_portal.position == 1 and self.rect.x + WIDTH_CHELL >
                    blue_portal.rect.x + 19
                    and (pygame.key.get_pressed()[100] or speed_horizontal > 0)) or \
                        (blue_portal.position == 3 and self.rect.x < blue_portal.rect.x and
                         (pygame.key.get_pressed()[97] or speed_horizontal < 0)):
                    return True
        elif blue_portal.position == 2 or blue_portal.position == 4:
            if blue_portal.rect.x <= self.rect.x + 25 <= blue_portal.rect.x + HEIGHT_PORTAL and \
                    blue_portal.rect.x <= self.rect.x + WIDTH_CHELL - 25 <= \
                    blue_portal.rect.x + HEIGHT_PORTAL:
                if (blue_portal.position == 2 and self.rect.y + HEIGHT_CHELL > blue_portal.rect.y) \
                        or (blue_portal.position == 4 and self.rect.y <
                            blue_portal.rect.y + WIDTH_PORTAL):
                    return True
    elif color == 'yellow':
        if yellow_portal.position == 1 or yellow_portal.position == 3:
            if yellow_portal.rect.y <= self.rect.y + 15 <= yellow_portal.rect.y + HEIGHT_PORTAL and \
                    yellow_portal.rect.y <= self.rect.y + HEIGHT_CHELL - 15 <= \
                    yellow_portal.rect.y + HEIGHT_PORTAL:
                if (yellow_portal.position == 1 and self.rect.x + WIDTH_CHELL >
                    yellow_portal.rect.x + 19
                    and (pygame.key.get_pressed()[100] or speed_horizontal > 0)) or \
                        (yellow_portal.position == 3 and self.rect.x < yellow_portal.rect.x and
                         (pygame.key.get_pressed()[97] or speed_horizontal < 0)):
                    return True
        elif yellow_portal.position == 2 or yellow_portal.position == 4:
            if yellow_portal.rect.x <= self.rect.x + 25 <= yellow_portal.rect.x + HEIGHT_PORTAL and \
                    yellow_portal.rect.x <= self.rect.x + WIDTH_CHELL - 25 <= \
                    yellow_portal.rect.x + HEIGHT_PORTAL:
                if (yellow_portal.position == 2 and self.rect.y + HEIGHT_CHELL >
                    yellow_portal.rect.y) or (yellow_portal.position == 4 and self.rect.y
                                              < yellow_portal.rect.y + WIDTH_PORTAL):
                    return True
    return False


def cube_pass_to_portal(self, color):
    # функция конечной проверки прохождения куба через портал
    global speed_horizontal_cube
    if color == 'blue':
        if blue_portal.position == 1 or blue_portal.position == 3:
            if blue_portal.rect.y <= self.rect.y <= blue_portal.rect.y + HEIGHT_PORTAL and \
                    blue_portal.rect.y <= self.rect.y + HEIGHT_CUBE <= blue_portal.rect.y \
                    + HEIGHT_PORTAL:
                if (blue_portal.position == 1 and self.rect.x + WIDTH_CUBE >= blue_portal.rect.x
                    and (speed_horizontal_cube > 0 or not cube.position)) or \
                        (blue_portal.position == 3 and
                         self.rect.x <= blue_portal.rect.x + WIDTH_PORTAL and
                         (speed_horizontal_cube < 0 or not cube.position)):
                    return True
        elif blue_portal.position == 2 or blue_portal.position == 4:
            if blue_portal.rect.x <= self.rect.x <= blue_portal.rect.x + HEIGHT_PORTAL and \
                    blue_portal.rect.x <= self.rect.x + WIDTH_CUBE <= \
                    blue_portal.rect.x + HEIGHT_PORTAL:
                if (blue_portal.position == 2 and self.rect.y + HEIGHT_CUBE >= blue_portal.rect.y) \
                        or (blue_portal.position == 4 and
                            self.rect.y <= blue_portal.rect.y + WIDTH_PORTAL):
                    return True
    elif color == 'yellow':
        if yellow_portal.position == 1 or yellow_portal.position == 3:
            if yellow_portal.rect.y <= self.rect.y <= yellow_portal.rect.y + HEIGHT_PORTAL and \
                    yellow_portal.rect.y <= self.rect.y + HEIGHT_CUBE <= \
                    yellow_portal.rect.y + HEIGHT_PORTAL:
                if (yellow_portal.position == 1 and
                    self.rect.x + WIDTH_CUBE >= yellow_portal.rect.x
                    and (speed_horizontal_cube > 0 or not cube.position)) or \
                        (yellow_portal.position == 3 and self.rect.x <=
                         yellow_portal.rect.x + WIDTH_PORTAL and
                         (speed_horizontal_cube < 0 or not cube.position)):
                    return True
        elif yellow_portal.position == 2 or yellow_portal.position == 4:
            if yellow_portal.rect.x <= self.rect.x <= yellow_portal.rect.x + HEIGHT_PORTAL and \
                    yellow_portal.rect.x <= self.rect.x + WIDTH_CUBE <= \
                    yellow_portal.rect.x + HEIGHT_PORTAL:
                if (yellow_portal.position == 2 and self.rect.y + HEIGHT_CUBE >=
                    yellow_portal.rect.y) or (yellow_portal.position == 4 and
                                              self.rect.y <= yellow_portal.rect.y + WIDTH_PORTAL):
                    return True
    return False


class Player(pygame.sprite.Sprite):  # класс персонажа
    def __init__(self, x=0, y=0):  # создание спрайта персонажа
        super().__init__(player_group)
        self.left_frames = []
        self.right_frames = []
        self.add_frames()
        self.cur_frame = 3
        self.curse = True
        self.image = self.right_frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def add_frames(self):  # добавление изображений спрайта
        for i in range(6):
            image = load_image("{}_l.gif".format(i))
            image = pygame.transform.scale(image, (HEIGHT_CHELL, WIDTH_CHELL))
            self.left_frames.append(image)
        for i in range(6):
            image = load_image("{}_r.gif".format(i))
            image = pygame.transform.scale(image, (HEIGHT_CHELL, WIDTH_CHELL))
            self.right_frames.append(image)

    def update(self, curse, look):  # функция обновления изображений
        if curse and look:
            self.cur_frame = (self.cur_frame + 1) % len(self.right_frames)
            self.image = self.right_frames[self.cur_frame]
        elif curse and not look:
            self.cur_frame = (self.cur_frame - 1) % len(self.left_frames)
            self.image = self.left_frames[self.cur_frame]
        elif not curse and look:
            self.cur_frame = (self.cur_frame - 1) % len(self.left_frames)
            self.image = self.right_frames[self.cur_frame]
        elif not curse and not look:
            self.cur_frame = (self.cur_frame + 1) % len(self.left_frames)
            self.image = self.left_frames[self.cur_frame]

    def normal(self, look):
        # постановка картинки статичного положения персонажа
        self.cur_frame = 3
        if look:
            self.image = self.right_frames[self.cur_frame]
        else:
            self.image = self.left_frames[self.cur_frame]

    def passing_through_portal(self, color, who='Chell'):
        # запуск проверки прохождения персонажа или персонажа с кубом при телепортации, запуск телепортации
        if color == 'blue':
            if who == 'Chell':
                if chell_pass_to_portal(self, color):
                    self.teleport('yellow', blue_portal.position)
            elif who == 'cube':
                if cube_pass_to_portal(cube, color):
                    self.teleport('yellow', blue_portal.position)
        elif color == 'yellow':
            if who == 'Chell':
                if chell_pass_to_portal(self, color):
                    self.teleport('blue', yellow_portal.position)
            elif who == 'cube':
                if cube_pass_to_portal(cube, color):
                    self.teleport('blue', yellow_portal.position)

    def teleport(self, color, position):
        # телепортация персонажа (с кубом, если он его держит), сохранение скоростей,
        # двигание куба персонажем при телепортации при необхадимости
        global speed_vertical, speed_horizontal, speed_ver_rez, speed_hor_rez, speed_vertical_cube, \
            speed_horizontal_cube
        teleport_sound = pygame.mixer.Sound('data/teleport_sound.wav')
        pygame.mixer.Sound.play(teleport_sound)
        if speed_vertical == 1:
            speed_vertical = 0
        if speed_ver_rez != 0 and speed_vertical == 0:
            speed_vertical = speed_ver_rez
        speed_ver_rez = 0
        if speed_hor_rez != 0 and speed_horizontal == 0:
            speed_horizontal = speed_hor_rez
        speed_hor_rez = 0
        flag_side = ''
        flag_right = False
        flag_left = False
        if not cube.position:
            if player.rect.left < cube.rect.left:
                flag_side = True
            else:
                flag_side = False
        if color == 'blue':
            if blue_portal.position == 1:
                flag_right = True
                self.rect.x = blue_portal.rect.x - WIDTH_CHELL + 19
                self.rect.y = blue_portal.rect.y
                if self.rect.y - 61 < cube.rect.y < self.rect.y + 91 and \
                        self.rect.x - 47 < cube.rect.x < self.rect.x + 82:
                    cube.rect.x = self.rect.x - 47
                if position == 1:
                    if speed_horizontal != 0:
                        speed_horizontal = -speed_horizontal
                    else:
                        speed_horizontal = -ZERO_SPEED
                elif position == 2:
                    speed_horizontal = -speed_vertical + 1
                elif position == 3 and speed_horizontal == 0:
                    speed_horizontal = -ZERO_SPEED
                elif position == 4:
                    speed_horizontal = speed_vertical
                if speed_horizontal > 0:
                    speed_horizontal = 0
                speed_vertical = 0
            elif blue_portal.position == 3:
                flag_left = True
                self.rect.x = blue_portal.rect.x + 1
                self.rect.y = blue_portal.rect.y
                if self.rect.y - 61 < cube.rect.y < self.rect.y + 91 and \
                        self.rect.x - 47 < cube.rect.x < self.rect.x + 82:
                    cube.rect.x = self.rect.x + 82
                if position == 1 and speed_horizontal == 0:
                    speed_horizontal = ZERO_SPEED
                elif position == 3:
                    if speed_horizontal != 0:
                        speed_horizontal = -speed_horizontal
                    else:
                        speed_horizontal = ZERO_SPEED
                elif position == 2:
                    speed_horizontal = speed_vertical - 1
                elif position == 4:
                    speed_horizontal = -speed_vertical
                if speed_horizontal < 0:
                    speed_horizontal = 0
                speed_vertical = 0
            elif blue_portal.position == 2:
                self.rect.y = blue_portal.rect.y - HEIGHT_CHELL
                if position == 1:
                    if speed_horizontal != 0:
                        speed_vertical = -speed_horizontal
                    else:
                        speed_vertical = -ZERO_SPEED
                    self.rect.x = blue_portal.rect.x
                elif position == 2:
                    speed_vertical = -speed_vertical + 1
                    self.rect.x = self.rect.x - yellow_portal.rect.x + blue_portal.rect.x
                elif position == 3:
                    if speed_horizontal != 0:
                        speed_vertical = speed_horizontal
                    else:
                        speed_vertical = -ZERO_SPEED
                    self.rect.x = blue_portal.rect.x
                elif position == 4:
                    self.rect.x = self.rect.x - yellow_portal.rect.x + blue_portal.rect.x
                if self.rect.x - 45 < cube.rect.x < self.rect.x + 80 and \
                        self.rect.y - 63 < cube.rect.y < self.rect.y + 93:
                    cube.rect.y = self.rect.y - 63
                speed_horizontal = 0
            elif blue_portal.position == 4:
                self.rect.y = blue_portal.rect.y + WIDTH_PORTAL
                if position == 1:
                    if speed_horizontal != 0:
                        speed_vertical = speed_horizontal
                    else:
                        speed_vertical = ZERO_SPEED
                    self.rect.x = blue_portal.rect.x
                elif position == 2:
                    self.rect.x = self.rect.x - yellow_portal.rect.x + blue_portal.rect.x
                elif position == 3:
                    if speed_horizontal != 0:
                        speed_vertical = -speed_horizontal
                    else:
                        speed_vertical = ZERO_SPEED
                    self.rect.x = blue_portal.rect.x
                elif position == 4:
                    speed_vertical = -speed_vertical
                    self.rect.x = self.rect.x - yellow_portal.rect.x + blue_portal.rect.x
                if self.rect.x - 45 < cube.rect.x < self.rect.x + 80 and \
                        self.rect.y - 63 < cube.rect.y < self.rect.y + 93:
                    cube.rect.y = self.rect.y + 93
                speed_horizontal = 0
        elif color == 'yellow':
            if yellow_portal.position == 1:
                flag_right = True
                self.rect.x = yellow_portal.rect.x - WIDTH_CHELL + 19
                self.rect.y = yellow_portal.rect.y
                if self.rect.y - 61 < cube.rect.y < self.rect.y + 91 and \
                        self.rect.x - 47 < cube.rect.x < self.rect.x + 82:
                    cube.rect.x = self.rect.x - 47
                if position == 1:
                    if speed_horizontal != 0:
                        speed_horizontal = -speed_horizontal
                    else:
                        speed_horizontal = -ZERO_SPEED
                elif position == 2:
                    speed_horizontal = -speed_vertical + 1
                elif position == 3 and speed_horizontal == 0:
                    speed_horizontal = -ZERO_SPEED
                elif position == 4:
                    speed_horizontal = speed_vertical
                if speed_horizontal > 0:
                    speed_horizontal = 0
                speed_vertical = 0
            elif yellow_portal.position == 3:
                flag_left = True
                self.rect.x = yellow_portal.rect.x + 1
                self.rect.y = yellow_portal.rect.y
                if self.rect.y - 61 < cube.rect.y < self.rect.y + 91 and \
                        self.rect.x - 47 < cube.rect.x < self.rect.x + 82:
                    cube.rect.x = self.rect.x + 82
                if position == 1 and speed_horizontal == 0:
                    speed_horizontal = ZERO_SPEED
                elif position == 3:
                    if speed_horizontal != 0:
                        speed_horizontal = -speed_horizontal
                    else:
                        speed_horizontal = ZERO_SPEED
                elif position == 2:
                    speed_horizontal = speed_vertical - 1
                elif position == 4:
                    speed_horizontal = -speed_vertical
                if speed_horizontal < 0:
                    speed_horizontal = 0
                speed_vertical = 0
            elif yellow_portal.position == 2:
                self.rect.y = yellow_portal.rect.y - HEIGHT_CHELL
                if position == 1:
                    if speed_horizontal != 0:
                        speed_vertical = -speed_horizontal
                    else:
                        speed_vertical = -ZERO_SPEED
                    self.rect.x = yellow_portal.rect.x
                elif position == 2:
                    speed_vertical = -speed_vertical + 1
                    self.rect.x = self.rect.x - blue_portal.rect.x + yellow_portal.rect.x
                elif position == 3:
                    if speed_horizontal != 0:
                        speed_vertical = speed_horizontal
                    else:
                        speed_vertical = -ZERO_SPEED
                    self.rect.x = yellow_portal.rect.x
                elif position == 4:
                    self.rect.x = self.rect.x - blue_portal.rect.x + yellow_portal.rect.x
                if self.rect.x - 45 < cube.rect.x < self.rect.x + 80 and \
                        self.rect.y - 63 < cube.rect.y < self.rect.y + 93:
                    cube.rect.y = self.rect.y - 63
                speed_horizontal = 0
            elif yellow_portal.position == 4:
                self.rect.y = yellow_portal.rect.y + WIDTH_PORTAL
                if position == 1:
                    if speed_horizontal != 0:
                        speed_vertical = speed_horizontal
                    else:
                        speed_vertical = ZERO_SPEED
                    self.rect.x = yellow_portal.rect.x
                elif position == 2:
                    self.rect.x = self.rect.x - blue_portal.rect.x + yellow_portal.rect.x
                elif position == 3:
                    if speed_horizontal != 0:
                        speed_vertical = -speed_horizontal
                    else:
                        speed_vertical = ZERO_SPEED
                    self.rect.x = yellow_portal.rect.x
                elif position == 4:
                    speed_vertical = -speed_vertical
                    self.rect.x = self.rect.x - blue_portal.rect.x + yellow_portal.rect.x
                if self.rect.x - 45 < cube.rect.x < self.rect.x + 80 and \
                        self.rect.y - 63 < cube.rect.y < self.rect.y + 93:
                    cube.rect.y = self.rect.y + 93
                speed_horizontal = 0
        if flag_side != '':
            speed_vertical_cube = speed_vertical
            speed_horizontal_cube = speed_horizontal
            cube.rect.y = self.rect.y + 6
            if flag_side:
                cube.rect.x = self.rect.x + WIDTH_CHELL - 25
                while len(pygame.sprite.spritecollide(cube, all_sprites, False)) > 0:
                    self.rect.x -= 1
                    cube.rect.x -= 1
                if flag_right:
                    self.rect.x -= 1
                    cube.rect.x -= 1
            else:
                cube.rect.x = self.rect.x - WIDTH_CUBE + 25
                while len(pygame.sprite.spritecollide(cube, all_sprites, False)) > 0:
                    self.rect.x += 1
                    cube.rect.x += 1
                if flag_left:
                    self.rect.x += 1
                    cube.rect.x += 1

    def interaction_cube(self, side_of_movement, step=STEP):
        # функция определябщая взаимодействие куба с персонажем со всех четырех сторон
        global speed_vertical_cube, flag_stand, speed_horizontal_cube, speed_ver_rez_cube, \
            speed_hor_rez_cube
        if cube.position:
            if side_of_movement == 'l':
                if self.rect.x + self.rect.w - 25 < cube.rect.left + WIDTH_CUBE:
                    if cube.rect.top + HEIGHT_CUBE < self.rect.y or \
                            cube.rect.y > self.rect.y + self.rect.h:
                        return None
                    else:
                        if cube.rect.left - (self.rect.x + self.rect.w - 25) >= step or \
                                cube.rect.top + HEIGHT_CUBE - HEIGHT_CUBE // 4 < self.rect.y:
                            return None
                        speed_hor_rez_cube = speed_horizontal_cube
                        speed_horizontal_cube = 0
                        return cube.rect.left - (self.rect.x + self.rect.w - 25)
                return None
            elif side_of_movement == 'r':
                if self.rect.x + 25 > cube.rect.left:
                    if cube.rect.top + HEIGHT_CUBE < self.rect.y or \
                            cube.rect.y > self.rect.y + self.rect.h:
                        return None
                    else:
                        if self.rect.x + 25 - cube.rect.left - WIDTH_CHELL >= step or \
                                cube.rect.top + HEIGHT_CUBE - HEIGHT_CUBE // 4 < self.rect.y:
                            return None
                        speed_hor_rez_cube = speed_horizontal_cube
                        speed_horizontal_cube = 0
                        return self.rect.x + 25 - cube.rect.left - WIDTH_CUBE
                return None
            elif side_of_movement == 'v':
                if cube.rect.top > self.rect.y + self.rect.h:
                    if cube.rect.left + WIDTH_CUBE < self.rect.x + 25 or \
                            cube.rect.left > self.rect.x + self.rect.w - 25:
                        return None
                    if cube.rect.top - self.rect.y - self.rect.h > abs(speed_vertical_cube):
                        return None
                    else:
                        speed_ver_rez_cube = speed_vertical_cube
                        speed_vertical_cube = 0
                        return cube.rect.top - self.rect.y - self.rect.h
                return None
            elif side_of_movement == 'n':
                if cube.rect.top + HEIGHT_CUBE < self.rect.y:
                    if cube.rect.left + WIDTH_CUBE < self.rect.x + 25 or \
                            cube.rect.left > self.rect.x + self.rect.w - 25:
                        return None
                    elif self.rect.y - cube.rect.top - HEIGHT_CUBE > speed_vertical_cube:
                        return None
                    else:
                        speed_vertical_cube = 0
                        speed_horizontal_cube = 0
                        return self.rect.y - cube.rect.top - HEIGHT_CUBE
                return None

    def stand_or_not_stand_cube(self):
        # функция, определяющая стоит ли куб на персонаже или не стоит
        if cube.rect.left + WIDTH_CUBE < self.rect.x + 25 or \
                cube.rect.left > self.rect.x + self.rect.w - 25 or \
                self.rect.y - cube.rect.top - HEIGHT_CUBE:
            return True
        else:
            return False


class Wire(pygame.sprite.Sprite):  # класс проводов
    def __init__(self, x, y, pos):  # загрузка изображений проводов
        super().__init__(wire_group)
        self.image_list = []
        if pos == 'ver':
            image1 = load_image('wire_ver_off.png', -1)
            image1 = pygame.transform.scale(image1, (WIDTH_WIRE, HEIGHT_WIRE))
            self.image_list.append(image1)
            image2 = load_image('wire_ver_on.png', -1)
            image2 = pygame.transform.scale(image2, (WIDTH_WIRE, HEIGHT_WIRE))
            self.image_list.append(image2)
        elif pos == 'hor':
            image1 = load_image('wire_hor_off.png', -1)
            image1 = pygame.transform.scale(image1, (WIDTH_WIRE, HEIGHT_WIRE))
            self.image_list.append(image1)
            image2 = load_image('wire_hor_on.png', -1)
            image2 = pygame.transform.scale(image2, (WIDTH_WIRE, HEIGHT_WIRE))
            self.image_list.append(image2)
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def wire_on(self):  # функция включения проводов
        self.image = self.image_list[1]

    def wire_off(self):  # функция отключения проводов
        self.image = self.image_list[0]


class WallFloorCelling(pygame.sprite.Sprite):  # класс стен, потолка и пола
    def __init__(self, x, y, w, h, color, group, interval_list):
        # загрузка изображений в зависимости от цвета
        super().__init__(all_sprites, construction_group)
        if color == 'grey':
            self.image = load_image('grey.png')
        elif color == 'black':
            self.image = load_image('black.png')
        self.image = pygame.transform.scale(self.image, (w, h))
        self.mask = pygame.mask.from_surface(self.image)
        self.group = group
        self.color = color
        self.interval_list = interval_list
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)


class Platform(pygame.sprite.Sprite):
    # класс платформ, который включает в себя еще и двери
    # загрузка изображений платформ или двери
    def __init__(self, x, y, w, h, color, int_sp_1, int_sp_2, int_sp_3,
                 int_sp_4, p_type='n', act_list_l=0, speed_k=1):
        if p_type == 'n':
            super().__init__(all_sprites, construction_group, platform_group)
            if color == 'grey':
                self.image = load_image('grey.png')
            elif color == 'black':
                self.image = load_image('black.png')
        elif p_type == 'door':
            super().__init__(construction_group, platform_group, door_group)
            color = 'black'
            w = 19
            h = 100
            self.image = load_image('door.gif')
            self.y = y
            self.speed = 1
        elif p_type == 'hameleon':
            super().__init__(all_sprites, construction_group, platform_group)
            color = 'black'
            self.image = load_image('black.png')
            self.w = w
            self.h = h
        self.activated_list = [False] * act_list_l
        self.activated_list_len = act_list_l
        self.p_type = p_type
        self.speed_k = speed_k
        self.image = pygame.transform.scale(self.image, (w, h))
        self.mask = pygame.mask.from_surface(self.image)
        self.color = color
        self.group = 'p'
        self.interval_list_1 = int_sp_1
        self.interval_list_2 = int_sp_2
        self.interval_list_3 = int_sp_3
        self.interval_list_4 = int_sp_4
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def interaction(self, side_of_movement, step=STEP):
        # функция взаимодействия персонажа с платформой со всех четырех сторон
        global speed_vertical, flag_stand, speed_horizontal, speed_ver_rez, speed_hor_rez, \
            HEIGHT_CHELL
        if side_of_movement == 'l':
            if self.rect.x + self.rect.w < player.rect.left - player_left_cube + \
                    WIDTH_CHELL + player_right_cube - 25:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if player.rect.left - player_left_cube - self.rect.x - \
                            self.rect.w + 25 >= step or \
                            player.rect.top + HEIGHT_CHELL - HEIGHT_CHELL // 4 < self.rect.y:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return player.rect.left - player_left_cube - self.rect.x - self.rect.w + 25
            return None
        elif side_of_movement == 'r':
            if self.rect.x > player.rect.left - player_left_cube + 25:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if self.rect.x - player.rect.left + player_left_cube - WIDTH_CHELL \
                            - player_right_cube + 25 >= step or player.rect.top + HEIGHT_CHELL \
                            - HEIGHT_CHELL // 4 < self.rect.y:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return self.rect.x - player.rect.left + player_left_cube - WIDTH_CHELL - \
                           player_right_cube + 25
            return None
        elif side_of_movement == 'v':
            if player.rect.top > self.rect.y + self.rect.h:
                if player.rect.left - player_left_cube + WIDTH_CHELL + player_right_cube - 25 < \
                        self.rect.x or player.rect.left - player_left_cube + 25 > \
                        self.rect.x + self.rect.w:
                    return None
                if player.rect.top - self.rect.y - self.rect.h > abs(speed_vertical):
                    return None
                else:
                    speed_ver_rez = speed_vertical
                    speed_vertical = 0
                    return player.rect.top - self.rect.y - self.rect.h + 9
            return None
        elif side_of_movement == 'n':
            if player.rect.top + HEIGHT_CHELL - 30 < self.rect.y:
                if player.rect.left - player_left_cube + WIDTH_CHELL + player_right_cube - 25 < \
                        self.rect.x or player.rect.left - player_left_cube + 30 > \
                        self.rect.x + self.rect.w:
                    return None
                if (player.rect.left + WIDTH_CHELL - 25 < self.rect.x or
                    player.rect.left + 30 > self.rect.x + self.rect.w) and not cube.position:
                    HEIGHT_CHELL -= 14
                if self.rect.y - player.rect.top - HEIGHT_CHELL + 9 > speed_vertical:
                    HEIGHT_CHELL = 100
                    return None
                else:
                    speed_ver_rez = speed_vertical
                    speed_hor_rez = speed_horizontal
                    speed_vertical = 0
                    speed_horizontal = 0
                    dop = HEIGHT_CHELL
                    HEIGHT_CHELL = 100
                    return self.rect.y - player.rect.top - dop + 9
            return None

    def interaction_cube(self, side_of_movement, step=STEP):
        # функция взаимодействия куба с платформой со всех четырех сторон
        global speed_vertical_cube, flag_stand, speed_horizontal_cube, speed_ver_rez_cube, \
            speed_hor_rez_cube
        if cube.position:
            if side_of_movement == 'l':
                if self.rect.x + self.rect.w < cube.rect.left + WIDTH_CUBE:
                    if cube.rect.top + HEIGHT_CUBE < self.rect.y or \
                            cube.rect.y > self.rect.y + self.rect.h:
                        return None
                    else:
                        if cube.rect.left - self.rect.x - self.rect.w >= step or \
                                cube.rect.top + HEIGHT_CUBE - HEIGHT_CUBE // 4 < self.rect.y:
                            return None
                        speed_hor_rez_cube = speed_horizontal_cube
                        speed_horizontal_cube = 0
                        return cube.rect.left - self.rect.x - self.rect.w
                return None
            elif side_of_movement == 'r':
                if self.rect.x > cube.rect.left:
                    if cube.rect.top + HEIGHT_CUBE < self.rect.y or \
                            cube.rect.y > self.rect.y + self.rect.h:
                        return None
                    else:
                        if self.rect.x - cube.rect.left - WIDTH_CHELL >= step or \
                                cube.rect.top + HEIGHT_CUBE - HEIGHT_CUBE // 4 < self.rect.y:
                            return None
                        speed_hor_rez_cube = speed_horizontal_cube
                        speed_horizontal_cube = 0
                        return self.rect.x - cube.rect.left - WIDTH_CUBE
                return None
            elif side_of_movement == 'v':
                if cube.rect.top > self.rect.y + self.rect.h:
                    if cube.rect.left + WIDTH_CUBE < self.rect.x or \
                            cube.rect.left > self.rect.x + self.rect.w:
                        return None
                    if cube.rect.top - self.rect.y - self.rect.h > abs(speed_vertical_cube):
                        return None
                    else:
                        speed_ver_rez_cube = speed_vertical_cube
                        speed_vertical_cube = 0
                        return cube.rect.top - self.rect.y - self.rect.h
                return None
            elif side_of_movement == 'n':
                if cube.rect.top + HEIGHT_CUBE < self.rect.y:
                    if cube.rect.left + WIDTH_CUBE < self.rect.x or \
                            cube.rect.left > self.rect.x + self.rect.w:
                        return None
                    elif self.rect.y - cube.rect.top - HEIGHT_CUBE > speed_vertical_cube:
                        return None
                    else:
                        speed_ver_rez_cube = speed_vertical_cube
                        speed_hor_rez_cube = speed_horizontal_cube
                        speed_vertical_cube = 0
                        speed_horizontal_cube = 0
                        return self.rect.y - cube.rect.top - HEIGHT_CUBE
                return None
        else:
            return 0

    def stand_or_not_stand(self):
        # функция, определяющая стоит ли персонаж на платформе
        if player.rect.left + WIDTH_CHELL - 25 < self.rect.x or \
                player.rect.left + 25 > self.rect.x + self.rect.w or self.rect.y - \
                player.rect.top - HEIGHT_CHELL + 9:
            return True
        else:
            return False

    def stand_or_not_stand_cube(self):
        # функция, определяющая стоит ли персонаж на платформе
        if cube.rect.left + WIDTH_CUBE < self.rect.x or \
                cube.rect.left > self.rect.x + self.rect.w or self.rect.y - \
                cube.rect.top - HEIGHT_CUBE:
            return True
        else:
            return False

    def thing_on(self):
        # Делает платформу серой, если это хамелеон, открывает дверь, если это дверь
        if self.p_type == 'door':
            if self.speed_k:
                self.rect.y -= self.speed
                if self.y - self.rect.y >= self.rect.h:
                    self.rect.y = self.y - self.rect.h
            else:
                self.rect.y += self.speed
                if self.rect.y - self.y >= self.rect.h:
                    self.rect.y = self.y + self.rect.h
        elif self.p_type == 'hameleon':
            self.color = 'grey'
            self.image = load_image('grey.png')
            self.image = pygame.transform.scale(self.image, (self.w, self.h))

    def thing_off(self):
        # Делает платформу чёрной, если это хамелеон, закрывает дверь, если это дверь
        if self.p_type == 'door':
            if self.speed_k:
                self.rect.y += self.speed
                if self.y - self.rect.y <= 0:
                    self.rect.y = self.y
            else:
                self.rect.y -= self.speed
                if self.y - self.rect.y >= 0:
                    self.rect.y = self.y
        elif self.p_type == 'hameleon':
            self.color = 'black'
            self.image = load_image('black.png')
            self.image = pygame.transform.scale(self.image, (self.w, self.h))
            if pygame.sprite.spritecollideany(self, blue_portal_group):
                blue_portal.active = False
                blue_portal.opened = False
            if pygame.sprite.spritecollideany(self, yellow_portal_group):
                yellow_portal.active = False
                yellow_portal.opened = False


class Cube(pygame.sprite.Sprite):
    # класс куба, загрузка ищображения куба
    def __init__(self, x=0, y=0):
        super().__init__(cube_group, construction_group)
        self.image = load_image('cube.gif')
        if cube_in_level:
            self.image = pygame.transform.scale(self.image, (HEIGHT_CUBE, WIDTH_CUBE))
        else:
            self.image = pygame.transform.scale(self.image, (1, 1))
        self.x = x
        self.y = y
        self.color = 'black'
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if cube_in_level:
            self.rect = self.rect.move(x, y)
        else:
            self.rect = self.rect.move(1, 1)
        self.position = True

    def interaction(self, side_of_movement, step=STEP):
        # функция взаимодействия персонажа и куба со всех четырех сторон
        global speed_vertical, flag_stand, speed_horizontal, speed_ver_rez, speed_hor_rez
        if not self.position:
            return None
        if side_of_movement == 'l':
            player_left = player.rect.left - step
            if self.rect.x + self.rect.w < player_left + WIDTH_CHELL:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if player.rect.left - self.rect.x - self.rect.w + 25 >= step or \
                            player.rect.top + HEIGHT_CHELL - HEIGHT_CHELL // 4 < self.rect.y:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return player.rect.left - self.rect.x - self.rect.w + 25
            return None
        elif side_of_movement == 'r':
            if self.rect.x > player.rect.left - player_left_cube + 25:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if self.rect.x - player.rect.left + player_left_cube - WIDTH_CHELL - \
                            player_right_cube + 25 >= step or \
                            player.rect.top + HEIGHT_CHELL - HEIGHT_CHELL // 4 < self.rect.y:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return self.rect.x - player.rect.left + player_left_cube - WIDTH_CHELL - \
                           player_right_cube + 25
            return None
        elif side_of_movement == 'v':
            if player.rect.top > self.rect.y + self.rect.h:
                if player.rect.left + WIDTH_CHELL - 25 < self.rect.x or \
                        player.rect.left + 25 > self.rect.x + self.rect.w:
                    return None
                if player.rect.top - self.rect.y - self.rect.h > abs(speed_vertical):
                    return None
                else:
                    speed_ver_rez = speed_vertical
                    speed_vertical = 0
                    return player.rect.top - self.rect.y - self.rect.h + 9
            return None
        elif side_of_movement == 'n':
            if player.rect.top + HEIGHT_CHELL - 20 < self.rect.y:
                if player.rect.left + WIDTH_CHELL - 25 < self.rect.x or \
                        player.rect.left + 30 > self.rect.x + self.rect.w:
                    return None
                elif self.rect.y - player.rect.top - HEIGHT_CHELL + 9 > speed_vertical:
                    return None
                else:
                    speed_ver_rez = speed_vertical
                    speed_hor_rez = speed_horizontal
                    speed_vertical = 0
                    speed_horizontal = 0
                    return self.rect.y - player.rect.top - HEIGHT_CHELL + 9
            return None

    def stand_or_not_stand(self):
        # функция, определяющая стоит ли персонаж на кубе
        if player.rect.left + WIDTH_CHELL - 25 < self.rect.x or \
                player.rect.left + 25 > self.rect.x + self.rect.w or self.rect.y - \
                player.rect.top - HEIGHT_CHELL + 9:
            return True
        else:
            return False

    def passing_through_portal(self, color):
        # запуск проверки прохождения куба через портал и запуск телепортации
        if color == 'blue':
            if cube_pass_to_portal(self, color):
                self.teleport('yellow', blue_portal.position)
        elif color == 'yellow':
            if cube_pass_to_portal(self, color):
                self.teleport('blue', yellow_portal.position)

    def teleport(self, color, position):
        # телепортирование куба, сохранение скоростей, двигание персонажа кубом при телепортации при необходимости
        global speed_vertical_cube, speed_horizontal_cube, speed_ver_rez_cube, speed_hor_rez_cube
        teleport_sound = pygame.mixer.Sound('data/teleport_sound.wav')
        pygame.mixer.Sound.play(teleport_sound)
        if speed_vertical_cube == 1:
            speed_vertical_cube = 0
        if speed_ver_rez_cube != 0 and speed_vertical_cube == 0:
            speed_vertical_cube = speed_ver_rez_cube
        speed_ver_rez_cube = 0
        if speed_hor_rez_cube != 0 and speed_horizontal_cube == 0:
            speed_horizontal_cube = speed_hor_rez_cube
        speed_hor_rez_cube = 0
        if color == 'blue':
            if blue_portal.position == 1:
                self.rect.x = blue_portal.rect.x - WIDTH_CUBE - 1
                self.rect.y = blue_portal.rect.y + HEIGHT_PORTAL // 2 - HEIGHT_CUBE // 2
                if player.rect.y - 61 < self.rect.y < player.rect.y + 91 and \
                        player.rect.x - 47 < self.rect.x < player.rect.x + 82:
                    player.rect.x = self.rect.x - 82
                if position == 1:
                    speed_horizontal_cube = -speed_horizontal_cube
                elif position == 2:
                    speed_horizontal_cube = -speed_vertical_cube + 1
                elif position == 4:
                    speed_horizontal_cube = speed_vertical_cube
                if speed_horizontal_cube > 0:
                    speed_horizontal_cube = 0
                speed_vertical_cube = 1
            elif blue_portal.position == 3:
                self.rect.x = blue_portal.rect.x + WIDTH_PORTAL + 1
                self.rect.y = blue_portal.rect.y + HEIGHT_PORTAL // 2 - HEIGHT_CUBE // 2
                if player.rect.y - 61 < self.rect.y < player.rect.y + 91 and \
                        player.rect.x - 47 < self.rect.x < player.rect.x + 82:
                    player.rect.x = self.rect.x + 47
                if position == 3:
                    speed_horizontal_cube = -speed_horizontal_cube
                elif position == 2:
                    speed_horizontal_cube = speed_vertical_cube - 1
                elif position == 4:
                    speed_horizontal_cube = -speed_vertical_cube
                if speed_horizontal_cube < 0:
                    speed_horizontal_cube = 0
                speed_vertical_cube = 1
            elif blue_portal.position == 2:
                self.rect.y = blue_portal.rect.y - HEIGHT_CUBE - 1
                self.rect.x = blue_portal.rect.x + HEIGHT_PORTAL // 2 - WIDTH_CUBE // 2
                if player.rect.x - 45 < self.rect.x < player.rect.x + 80 and \
                        player.rect.y - 63 < self.rect.y < player.rect.y + 93:
                    player.rect.y = self.rect.y - 93
                if position == 1:
                    speed_vertical_cube = -speed_horizontal_cube
                elif position == 2:
                    speed_vertical_cube = -speed_vertical_cube + 1
                elif position == 3:
                    speed_vertical_cube = speed_horizontal_cube
                speed_horizontal_cube = 0
            elif blue_portal.position == 4:
                self.rect.y = blue_portal.rect.y + WIDTH_PORTAL + 1
                self.rect.x = blue_portal.rect.x + HEIGHT_PORTAL // 2 - WIDTH_CUBE // 2
                if player.rect.x - 45 < self.rect.x < player.rect.x + 80 and \
                        player.rect.y - 63 < self.rect.y < player.rect.y + 93:
                    player.rect.y = self.rect.y + 63
                if position == 1:
                    speed_vertical_cube = speed_horizontal_cube
                elif position == 3:
                    speed_vertical_cube = -speed_horizontal_cube
                elif position == 4:
                    speed_vertical_cube = -speed_vertical_cube
                speed_horizontal_cube = 0
        elif color == 'yellow':
            if yellow_portal.position == 1:
                self.rect.x = yellow_portal.rect.x - WIDTH_CUBE - 1
                self.rect.y = yellow_portal.rect.y + HEIGHT_PORTAL // 2 - HEIGHT_CUBE // 2
                if player.rect.y - 61 < self.rect.y < player.rect.y + 91 and \
                        player.rect.x - 47 < self.rect.x < player.rect.x + 82:
                    player.rect.x = self.rect.x - 82
                if position == 1:
                    speed_horizontal_cube = -speed_horizontal_cube
                elif position == 2:
                    speed_horizontal_cube = -speed_vertical_cube + 1
                elif position == 4:
                    speed_horizontal_cube = speed_vertical_cube
                if speed_horizontal_cube > 0:
                    speed_horizontal_cube = 0
                speed_vertical_cube = 1
            elif yellow_portal.position == 3:
                self.rect.x = yellow_portal.rect.x + WIDTH_PORTAL + 1
                self.rect.y = yellow_portal.rect.y + HEIGHT_PORTAL // 2 - HEIGHT_CUBE // 2
                if player.rect.y - 61 < self.rect.y < player.rect.y + 91 and \
                        player.rect.x - 47 < self.rect.x < player.rect.x + 82:
                    player.rect.x = self.rect.x + 47
                if position == 3:
                    speed_horizontal_cube = -speed_horizontal_cube
                elif position == 2:
                    speed_horizontal_cube = speed_vertical_cube - 1
                elif position == 4:
                    speed_horizontal_cube = -speed_vertical_cube
                if speed_horizontal_cube < 0:
                    speed_horizontal_cube = 0
                speed_vertical_cube = 1
            elif yellow_portal.position == 2:
                if player.rect.x - 45 < self.rect.x < player.rect.x + 80 and \
                        player.rect.y - 63 < self.rect.y < player.rect.y + 93:
                    player.rect.y = self.rect.y - 93
                self.rect.y = yellow_portal.rect.y - HEIGHT_CUBE - 1
                self.rect.x = yellow_portal.rect.x + HEIGHT_PORTAL // 2 - WIDTH_CUBE // 2
                if position == 1:
                    speed_vertical_cube = -speed_horizontal_cube
                elif position == 2:
                    speed_vertical_cube = -speed_vertical_cube + 1
                elif position == 3:
                    speed_vertical_cube = speed_horizontal_cube
                speed_horizontal_cube = 0
            elif yellow_portal.position == 4:
                self.rect.y = yellow_portal.rect.y + WIDTH_PORTAL + 1
                self.rect.x = yellow_portal.rect.x + HEIGHT_PORTAL // 2 - WIDTH_CUBE // 2
                if player.rect.x - 45 < self.rect.x < player.rect.x + 80 and \
                        player.rect.y - 63 < self.rect.y < player.rect.y + 93:
                    player.rect.y = self.rect.y + 63
                if position == 1:
                    speed_vertical_cube = speed_horizontal_cube
                elif position == 3:
                    speed_vertical_cube = -speed_horizontal_cube
                elif position == 4:
                    speed_vertical_cube = -speed_vertical_cube
                speed_horizontal_cube = 0

    def touch_check(self, portal):
        # проверка касания кубом порталов
        if portal.position == 1 and portal.rect.x == self.rect.x + WIDTH_CUBE:
            return True
        elif portal.position == 3 and portal.rect.x + WIDTH_PORTAL == self.rect.x:
            return True
        elif portal.position == 2 and portal.rect.y == self.rect.y + HEIGHT_CUBE:
            return True
        elif portal.position == 4 and portal.rect.y + WIDTH_PORTAL == self.rect.y:
            return True
        return False


class Button(pygame.sprite.Sprite):
    # класс кнопки, загрузка изображения и звуков
    def __init__(self, x, y, control_thing, wire_list, thing_arg, main_button=False):
        super().__init__(all_sprites, button_group, construction_group)
        self.image = load_image('button.gif')
        self.x = x
        self.y = y
        self.control_thing = control_thing
        self.wire_list = wire_list
        self.thing_arg = thing_arg
        self.main_button = main_button
        self.door_sound = pygame.mixer.Sound('data/open_door_sound.wav')
        self.door_sound.set_volume(0.4)
        self.button_sound = pygame.mixer.Sound('data/click_sound.wav')
        self.button_sound.set_volume(0.4)
        self.color = 'black'
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.activated = False
        self.player_at_the_top = False
        self.cube_at_the_top = False

    def interaction(self, side_of_movement, step=STEP):
        # функция взаимодействия персонажа и кнопки со всех четырех сторон,
        # также в ней определяется стоит ли персонаж на кнопке или нет и
        # выключается кнопка
        global speed_vertical, flag_stand, speed_horizontal, speed_ver_rez, \
            speed_hor_rez, HEIGHT_CHELL
        if (not self.player_at_the_top and not self.cube_at_the_top) or (
                not self.player_at_the_top and not cube.position):
            self.disable_button()
        if side_of_movement == 'l':
            if self.rect.x + self.rect.w < player.rect.left - player_left_cube \
                    + WIDTH_CHELL + player_right_cube:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if player.rect.left - player_left_cube - self.rect.x - self.rect.w + 25 >= \
                            step or player.rect.top + HEIGHT_CHELL - HEIGHT_CHELL // 4 \
                            < self.rect.y:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return player.rect.left - player_left_cube - self.rect.x - self.rect.w + 25
            return None
        elif side_of_movement == 'r':
            if self.rect.x > player.rect.left:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if self.rect.x - (
                            player.rect.left - player_left_cube + WIDTH_CHELL + player_right_cube) \
                            + 40 >= STEP or player.rect.top + HEIGHT_CHELL - HEIGHT_CHELL // 4 \
                            < self.rect.y:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return self.rect.x - (player.rect.left - player_left_cube +
                                          WIDTH_CHELL + player_right_cube) + 40
            return None
        elif side_of_movement == 'v':
            if player.rect.top > self.rect.y + self.rect.h:
                if player.rect.left + WIDTH_CHELL - 25 < self.rect.x or \
                        player.rect.left + 25 > self.rect.x + self.rect.w:
                    return None
                if player.rect.top - self.rect.y - self.rect.h > abs(speed_vertical):
                    return None
                else:
                    speed_ver_rez = speed_vertical
                    speed_vertical = 0
                    return player.rect.top - self.rect.y - self.rect.h + 9
            return None
        elif side_of_movement == 'n':
            if player.rect.top + HEIGHT_CHELL - 30 < self.rect.y:
                if player.rect.left - player_left_cube + WIDTH_CHELL + player_right_cube - 25 < \
                        self.rect.x or player.rect.left - player_left_cube + 25 > \
                        self.rect.x + self.rect.w:
                    self.player_at_the_top = False
                    return None
                if (player.rect.left + WIDTH_CHELL - 25 < self.rect.x or
                    player.rect.left + 30 > self.rect.x + self.rect.w) and not cube.position:
                    HEIGHT_CHELL -= 14
                if self.rect.y - player.rect.top - HEIGHT_CHELL + 9 > speed_vertical:
                    self.player_at_the_top = False
                    HEIGHT_CHELL = 100
                    return None
                else:
                    speed_ver_rez = speed_vertical
                    speed_hor_rez = speed_horizontal
                    speed_vertical = 0
                    speed_horizontal = 0
                    self.player_at_the_top = True
                    self.activate_button()
                    dop = HEIGHT_CHELL
                    HEIGHT_CHELL = 100
                    return self.rect.y - player.rect.top - dop + 9
            return None

    def interaction_cube(self, side_of_movement, step=STEP):
        # функция взаимодействия куба и кнопки со всех четырех сторон,
        # акже в ней определяется стоит ли персонаж на кнопке или нет и
        # выключается кнопка
        global speed_vertical_cube, flag_stand, speed_horizontal_cube, \
            speed_ver_rez_cube, speed_hor_rez_cube
        if cube.position:
            if not self.player_at_the_top and not self.cube_at_the_top:
                self.disable_button()
            if side_of_movement == 'l':
                if self.rect.x + self.rect.w < cube.rect.left + WIDTH_CUBE:
                    if cube.rect.top + HEIGHT_CUBE < self.rect.y or \
                            cube.rect.y > self.rect.y + self.rect.h:
                        return None
                    else:
                        if cube.rect.left - self.rect.x - self.rect.w >= step or \
                                cube.rect.top + HEIGHT_CUBE - HEIGHT_CUBE // 4 < self.rect.y:
                            return None
                        speed_hor_rez_cube = speed_horizontal_cube
                        speed_horizontal_cube = 0
                        return cube.rect.left - self.rect.x - self.rect.w
                return None
            elif side_of_movement == 'r':
                if self.rect.x > cube.rect.left:
                    if cube.rect.top + HEIGHT_CUBE < self.rect.y or \
                            cube.rect.y > self.rect.y + self.rect.h:
                        return None
                    else:
                        if self.rect.x - cube.rect.left - WIDTH_CHELL >= step or \
                                cube.rect.top + HEIGHT_CUBE - HEIGHT_CUBE // 4 < self.rect.y:
                            return None
                        speed_hor_rez_cube = speed_horizontal_cube
                        speed_horizontal_cube = 0
                        return self.rect.x - cube.rect.left - WIDTH_CUBE
                return None
            elif side_of_movement == 'v':
                if cube.rect.top > self.rect.y + self.rect.h:
                    if cube.rect.left + WIDTH_CUBE < self.rect.x or \
                            cube.rect.left > self.rect.x + self.rect.w:
                        return None
                    if cube.rect.top - self.rect.y - self.rect.h > abs(speed_vertical_cube):
                        return None
                    else:
                        speed_ver_rez_cube = speed_vertical_cube
                        speed_vertical_cube = 0
                        return cube.rect.top - self.rect.y - self.rect.h
                return None
            elif side_of_movement == 'n':
                if cube.rect.top + HEIGHT_CUBE - 20 < self.rect.y:
                    if cube.rect.left + WIDTH_CUBE < self.rect.x or \
                            cube.rect.left > self.rect.x + self.rect.w:
                        self.cube_at_the_top = False
                        return None
                    elif self.rect.y - cube.rect.top - HEIGHT_CUBE > speed_vertical_cube:
                        self.cube_at_the_top = False
                        return None
                    else:
                        speed_vertical_cube = 0
                        speed_horizontal_cube = 0
                        self.cube_at_the_top = True
                        self.activate_button()
                        return self.rect.y - cube.rect.top - HEIGHT_CUBE
                return None

    def activate_button(self):
        # функция активации кнопки(со звуком)
        self.image = load_image('button_is_pressed.gif')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y + 5)
        if not self.activated:
            if self.main_button:
                pygame.mixer.Sound.play(self.door_sound)
            pygame.mixer.Sound.play(self.button_sound)
        self.activated = True
        self.control_thing.activated_list[self.thing_arg] = True

    def disable_button(self):
        # функция деактивации кнопки(со звуком)
        self.image = load_image('button.gif')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        if self.activated:
            if self.main_button:
                pygame.mixer.Sound.play(self.door_sound)
            pygame.mixer.Sound.play(self.button_sound)
        self.activated = False
        self.control_thing.activated_list[self.thing_arg] = False

    def stand_or_not_stand(self):
        # функция, определяющая стоит ли персонаж на кнопке
        if player.rect.left + WIDTH_CHELL - 25 < self.rect.x or \
                player.rect.left + 25 > self.rect.x + self.rect.w or self.rect.y - \
                player.rect.top - HEIGHT_CHELL + 9:
            return True
        else:
            return False

    def stand_or_not_stand_cube(self):
        # функция, определяющая стоит ли куб на кнопке
        if cube.rect.left + WIDTH_CUBE < self.rect.x or \
                cube.rect.left > self.rect.x + self.rect.w or self.rect.y - \
                cube.rect.top - HEIGHT_CUBE:
            return True
        else:
            return False


class Portal(pygame.sprite.Sprite):
    def __init__(self, color):
        # инициализация портала
        if color == 'blue':
            super().__init__(blue_portal_group)
            self.sound_shot = pygame.mixer.Sound('data/blue_shot.wav')
            self.sound_portal_open = pygame.mixer.Sound('data/blue_open.wav')
        elif color == 'yellow':
            super().__init__(yellow_portal_group)
            self.sound_shot = pygame.mixer.Sound('data/yellow_shot.wav')
            self.sound_portal_open = pygame.mixer.Sound('data/yellow_open.wav')
        self.speed = 20
        self.image_list = []
        self.color = color
        self.add_frames()
        self.rect = self.image.get_rect()
        self.position = 0
        self.active = False
        self.opened = False

    def add_frames(self):
        # добавление изображений порталов в атрибут класса
        if self.color == 'blue':
            self.image0 = load_image("Шарик 1.gif")
            self.image0 = pygame.transform.scale(self.image0, (WIDTH_SPHERE, HEIGHT_SPHERE))
            self.image = self.image0
            image1 = load_image("Портал 1 вправо.gif")
            image1 = pygame.transform.scale(image1, (WIDTH_PORTAL, HEIGHT_PORTAL))
            self.image_list.append(image1)
            image2 = load_image("Портал 1 вниз.gif")
            image2 = pygame.transform.scale(image2, (HEIGHT_PORTAL, WIDTH_PORTAL))
            self.image_list.append(image2)
            image3 = load_image("Портал 1 влево.gif")
            image3 = pygame.transform.scale(image3, (WIDTH_PORTAL, HEIGHT_PORTAL))
            self.image_list.append(image3)
            image4 = load_image("Портал 1 вверх.gif")
            image4 = pygame.transform.scale(image4, (HEIGHT_PORTAL, WIDTH_PORTAL))
            self.image_list.append(image4)
        elif self.color == 'yellow':
            self.image0 = load_image("Шарик 2.gif")
            self.image0 = pygame.transform.scale(self.image0, (WIDTH_SPHERE, HEIGHT_SPHERE))
            self.image = self.image0
            image1 = load_image("Портал 2 вправо.gif")
            image1 = pygame.transform.scale(image1, (WIDTH_PORTAL, HEIGHT_PORTAL))
            self.image_list.append(image1)
            image2 = load_image("Портал 2 вниз.gif")
            image2 = pygame.transform.scale(image2, (HEIGHT_PORTAL, WIDTH_PORTAL))
            self.image_list.append(image2)
            image3 = load_image("Портал 2 влево.gif")
            image3 = pygame.transform.scale(image3, (WIDTH_PORTAL, HEIGHT_PORTAL))
            self.image_list.append(image3)
            image4 = load_image("Портал 2 вверх.gif")
            image4 = pygame.transform.scale(image4, (HEIGHT_PORTAL, WIDTH_PORTAL))
            self.image_list.append(image4)

    def click_mouse(self, x_curs, y_curs, x_player, y_player):
        # инициализация полёта портала
        pygame.mixer.Sound.play(self.sound_shot)
        self.image = self.image0
        self.rect.w = WIDTH_SPHERE
        self.rect.h = HEIGHT_SPHERE
        self.active = True
        self.opened = False
        if player.rect.left + WIDTH_CHELL // 2 - pygame.mouse.get_pos()[0] > 0:
            self.x = x_player + 29
        else:
            self.x = x_player + 71
        self.y = y_player + 39
        self.rect.x = self.x
        self.rect.y = self.y
        self.xx = abs(x_curs + 18 - self.x)
        self.yy = abs(y_curs + 18 - self.y)
        self.ss = (self.xx ** 2 + self.yy ** 2) ** 0.5
        if self.ss == 0:
            return
        if x_curs + 18 < self.x:
            self.x_nap = -1
        else:
            self.x_nap = 1
        if y_curs + 18 < self.y:
            self.y_nap = -1
        else:
            self.y_nap = 1

    def portal_fly(self):
        # полёт портала
        self.x += self.speed * self.x_nap * self.xx / self.ss
        self.rect.x = int(self.x)
        self.y += self.speed * self.y_nap * self.yy / self.ss
        self.rect.y = int(self.y)

    def portal_open(self):
        # начальное открытие портала, выяснение положения и запуск проверок положения
        pygame.mixer.Sound.play(self.sound_portal_open)
        construction_list = pygame.sprite.spritecollide(self, construction_group, False)
        self.construction = construction_list[0]
        if self.construction.color == 'black':
            self.active = False
            self.position = 0
            return
        if self.construction.group == 'wr':
            self.position = 1
            self.portal_adjustment_walls(self.construction.group, self.image_list[0])
        elif self.construction.group == 'f':
            self.position = 2
            self.portal_adjustment_floor_ceiling(self.construction.group, self.image_list[1])
        elif self.construction.group == 'wl':
            self.position = 3
            self.portal_adjustment_walls(self.construction.group, self.image_list[2])
        elif self.construction.group == 'c':
            self.position = 4
            self.portal_adjustment_floor_ceiling(self.construction.group, self.image_list[3])
        elif self.construction.group == 'p':
            self.position_on_platform()

    def portal_adjustment_walls(self, group, image):
        # подстраивание портала под вертикальную конструкцию
        hit_flag = False
        for i in self.construction.interval_list:
            if i[0] <= self.rect.y <= i[1] or i[0] <= self.rect.y + self.rect.h <= i[1]:
                hit_flag = True
                interval = i
                break
        if hit_flag:
            if interval[1] - interval[0] >= HEIGHT_PORTAL:
                if group == 'wr':
                    self.rect.x = self.construction.rect.x
                elif group == 'wl':
                    self.rect.x = self.construction.rect.x + \
                                  self.construction.rect.w - WIDTH_PORTAL
                self.image = image
                self.rect.w = WIDTH_PORTAL
                self.rect.h = HEIGHT_PORTAL
                if self.rect.y - HEIGHT_PORTAL // 2 < interval[0]:
                    self.rect.y = interval[0]
                    self.portal_construction_other_portal()
                elif self.rect.y + HEIGHT_PORTAL // 2 > interval[1]:
                    self.rect.y = interval[1] - HEIGHT_PORTAL
                    self.portal_construction_other_portal()
                else:
                    self.rect.y -= HEIGHT_PORTAL // 2
                    if self.color == 'blue' and \
                            pygame.sprite.spritecollideany(self, yellow_portal_group) \
                            and yellow_portal.active:
                        self.portal_other_portal_wall(interval, yellow_portal.rect.y)
                    elif self.color == 'yellow' and \
                            pygame.sprite.spritecollideany(self, blue_portal_group) \
                            and blue_portal.active:
                        self.portal_other_portal_wall(interval, blue_portal.rect.y)
                if not self.active:
                    self.position = 0
                    return
                self.opened = True
            else:
                self.active = False
                self.position = 0
        else:
            self.active = False
            self.position = 0

    def portal_adjustment_floor_ceiling(self, group, image):
        # подстраивание портала под горизонтальную конструкцию
        hit_flag = False
        for i in self.construction.interval_list:
            if i[0] <= self.rect.x <= i[1] or i[0] <= self.rect.x + self.rect.w <= i[1]:
                hit_flag = True
                interval = i
                break
        if hit_flag:
            if interval[1] - interval[0] >= HEIGHT_PORTAL:
                if group == 'f':
                    self.rect.y = self.construction.rect.y
                elif group == 'c':
                    self.rect.y = self.construction.rect.y + \
                                  self.construction.rect.h - WIDTH_PORTAL
                self.image = image
                self.rect.w = HEIGHT_PORTAL
                self.rect.h = WIDTH_PORTAL
                if self.rect.x - HEIGHT_PORTAL // 2 < interval[0]:
                    self.rect.x = interval[0]
                    self.portal_construction_other_portal()
                elif self.rect.x + HEIGHT_PORTAL // 2 > interval[1]:
                    self.rect.x = interval[1] - HEIGHT_PORTAL
                    self.portal_construction_other_portal()
                else:
                    self.rect.x -= HEIGHT_PORTAL // 2
                    if self.color == 'blue' and \
                            pygame.sprite.spritecollideany(self, yellow_portal_group) \
                            and yellow_portal.active:
                        self.portal_other_portal_floor_ceiling(interval, yellow_portal.rect.x)
                    elif self.color == 'yellow' and \
                            pygame.sprite.spritecollideany(self, blue_portal_group) \
                            and blue_portal.active:
                        self.portal_other_portal_floor_ceiling(interval, blue_portal.rect.x)
                if not self.active:
                    self.position = 0
                    return
                self.opened = True
            else:
                self.active = False
                self.position = 0
        else:
            self.active = False
            self.position = 0

    def portal_construction_other_portal(self):
        # сдвиг портала при взаимодейтсвии с конструкцией, на которой он не открыт, в соотвествии с положением другого
        # портала
        if self.color == 'blue' and pygame.sprite.spritecollideany(self, yellow_portal_group) and \
                yellow_portal.active:
            self.active = False
        elif self.color == 'yellow' and pygame.sprite.spritecollideany(self, blue_portal_group) and \
                blue_portal.active:
            self.active = False

    def portal_other_portal_wall(self, interval, y_2):
        # сдвиг портала при взаимодейтсвии с другим порталом на вертикальных поверхностях
        if y_2 < self.rect.y + HEIGHT_PORTAL // 2 < y_2 + HEIGHT_PORTAL:
            self.active = False
        else:
            if self.rect.y + HEIGHT_PORTAL // 2 <= y_2 and interval[0] <= y_2 - HEIGHT_PORTAL:
                self.rect.y = y_2 - HEIGHT_PORTAL
            elif self.rect.y + HEIGHT_PORTAL // 2 >= y_2 + HEIGHT_PORTAL and \
                    interval[1] >= y_2 + 2 * HEIGHT_PORTAL:
                self.rect.y = y_2 + HEIGHT_PORTAL
            else:
                self.active = False

    def portal_other_portal_floor_ceiling(self, interval, x_2):
        # сдвиг портала при взаимодейтсвии с другим порталом на горизонтальных поверхностях
        if x_2 < self.rect.x + HEIGHT_PORTAL // 2 < x_2 + HEIGHT_PORTAL:
            self.active = False
        else:
            if self.rect.x + HEIGHT_PORTAL // 2 <= x_2 and interval[0] <= x_2 - HEIGHT_PORTAL:
                self.rect.x = x_2 - HEIGHT_PORTAL
            elif self.rect.x + HEIGHT_PORTAL // 2 >= x_2 + HEIGHT_PORTAL and \
                    interval[1] >= x_2 + 2 * HEIGHT_PORTAL:
                self.rect.x = x_2 + HEIGHT_PORTAL
            else:
                self.active = False

    def position_on_platform(self):
        # выяснение положения портала на платформе
        dx1 = self.rect.x - self.construction.rect.x
        dx2 = self.construction.rect.x + self.construction.rect.w - self.rect.x - self.rect.w
        dy1 = self.rect.y - self.construction.rect.y
        dy2 = self.construction.rect.y + self.construction.rect.h - self.rect.y - self.rect.h
        dmin = min(dx1, dx2, dy1, dy2)
        if dx2 == dmin:
            self.position = 3
            self.construction.interval_list = self.construction.interval_list_3
            self.portal_adjustment_walls('wl', self.image_list[2])
        elif dx1 == dmin:
            self.position = 1
            self.construction.interval_list = self.construction.interval_list_1
            self.portal_adjustment_walls('wr', self.image_list[0])
        elif dy2 == dmin:
            self.position = 4
            self.construction.interval_list = self.construction.interval_list_4
            self.portal_adjustment_floor_ceiling('c', self.image_list[3])
        elif dy1 == dmin:
            self.position = 2
            self.construction.interval_list = self.construction.interval_list_2
            self.portal_adjustment_floor_ceiling('f', self.image_list[1])


def reinit_groups():  # Обнуление всего, инициализация групп
    global all_sprites, wall_left_group, wall_right_group, floor_group, ceiling_group, construction_group, \
        platform_group, door_group, wire_group, button_group, background_group, cube_group, player_group, \
        cursor_group, cube_in_level, blue_portal_group, yellow_portal_group
    walking_event = 25
    pygame.time.set_timer(walking_event, 100)
    svobod_pad_event = 24
    pygame.time.set_timer(svobod_pad_event, 25)
    pfly_event = 26
    pygame.time.set_timer(pfly_event, 1)
    door_event = 23
    pygame.time.set_timer(door_event, 1)
    player_group = pygame.sprite.Group()
    blue_portal_group = pygame.sprite.Group()
    yellow_portal_group = pygame.sprite.Group()
    cursor_group = pygame.sprite.Group()
    cube_group = pygame.sprite.Group()
    background_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    wall_left_group = pygame.sprite.Group()
    wall_right_group = pygame.sprite.Group()
    floor_group = pygame.sprite.Group()
    ceiling_group = pygame.sprite.Group()
    construction_group = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    wire_group = pygame.sprite.Group()
    button_group = pygame.sprite.Group()
    background_group = pygame.sprite.Group()


def load_level(): # Загрузка уровня из файла
    global all_sprites, wall_left_group, wall_right_group, floor_group, ceiling_group, \
        construction_group, platform_group, door_group, wire_group, button_group, \
        cube_in_level, player, cube, blue_portal, yellow_portal, cursor, background_group
    # Чтение файла
    file_level = open('data/save.txt', encoding='utf8')
    num_level = int(file_level.read().split()[0])
    name_file = 'data/level_{}.txt'.format(str(num_level))
    file_objects = open(name_file, encoding='utf8')
    lines = file_objects.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split()

    # Загрузка окна и фона
    size = int(lines[0][0]), int(lines[0][1])
    width, height = size[0], size[1]
    screen = pygame.display.set_mode(size)
    background = pygame.sprite.Sprite()
    background_group.add(background)
    background_image = load_image("background_image.jpg")
    background.image = pygame.transform.scale(background_image, (size[0], size[1]))
    background.rect = background.image.get_rect()
    background.rect.x = 0
    background.rect.y = 0

    # Загрузка стен, потолка и пола
    for k in range(4):
        interval = []
        i = 6
        while i < len(lines[k + 1]):
            cnt = int(lines[k + 1][i])
            i += 1
            for j in range(cnt):
                left = int(lines[k + 1][i])
                i += 1
                right = int(lines[k + 1][i])
                i += 1
                interval.append((left, right))
        if k == 0:
            wall_left = WallFloorCelling(int(lines[k + 1][0]), int(lines[k + 1][1]),
                                         int(lines[k + 1][2]), int(lines[k + 1][3]),
                                         lines[k + 1][4], lines[k + 1][5], interval)
            wall_left_group.add(wall_left)
        elif k == 1:
            wall_right = WallFloorCelling(int(lines[k + 1][0]), int(lines[k + 1][1]),
                                          int(lines[k + 1][2]), int(lines[k + 1][3]),
                                          lines[k + 1][4], lines[k + 1][5], interval)
            wall_right_group.add(wall_right)
        elif k == 2:
            ceiling_group.add(WallFloorCelling(int(lines[k + 1][0]), int(lines[k + 1][1]),
                                               int(lines[k + 1][2]), int(lines[k + 1][3]),
                                               lines[k + 1][4], lines[k + 1][5], interval))
        else:
            floor = WallFloorCelling(int(lines[k + 1][0]), int(lines[k + 1][1]),
                                     int(lines[k + 1][2]), int(lines[k + 1][3]),
                                     lines[k + 1][4], lines[k + 1][5], interval)
            floor_group.add(floor)

    # Загрузка платформ
    cnt_platforms = int(lines[5][0])
    for k in range(cnt_platforms):
        interval = [[], [], [], []]
        i, now_inter = 5, 0
        while i < len(lines[k + 6]):
            cnt = int(lines[k + 6][i])
            i += 1
            for j in range(cnt):
                left = int(lines[k + 6][i])
                i += 1
                right = int(lines[k + 6][i])
                i += 1
                interval[now_inter].append((left, right))
            now_inter += 1
        Platform(int(lines[k + 6][0]), int(lines[k + 6][1]), int(lines[k + 6][2]),
                 int(lines[k + 6][3]), lines[k + 6][4], interval[0],
                 interval[1], interval[2], interval[3])

    # Дозагрузка всего остального
    if num_level == 1:
        cube_in_level = False
        player = Player(20, 430)
        cube = Cube(0, 0)
    elif num_level == 2:
        cube_in_level = True
        door_1 = Platform(706, height - 120, 0, 0, '',
                          [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], 'door', 1)
        button_1 = Button(400, height - 50, door_1,
                          [Wire(425, 869, 'hor'),
                           Wire(525, 869, 'hor'),
                           Wire(625, 869, 'hor')], 0, True)
        door_2 = Platform(160, 340, 0, 0, '',
                          [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], 'door', 2)
        button_2 = Button(width - 750, 410, door_2,
                          [Wire(width - 720, 418, 'hor'), Wire(width - 680, 378, 'ver'),
                           Wire(width - 680, 278, 'ver'), Wire(width - 680, 178, 'ver'),
                           Wire(width - 720, 138, 'hor'), Wire(width - 720, 138, 'hor'),
                           Wire(width - 820, 138, 'hor'), Wire(width - 920, 138, 'hor'),
                           Wire(width - 1020, 138, 'hor'), Wire(width - 1120, 138, 'hor'),
                           Wire(width - 1220, 138, 'hor'), Wire(width - 1320, 138, 'hor'),
                           Wire(width - 1378, 178, 'ver'), Wire(width - 1378, 240, 'ver')], 0, True)
        button_3 = Button(400, 610, door_2,
                          [Wire(340, 617, 'hor'), Wire(240, 617, 'hor'),
                           Wire(140, 617, 'hor'), Wire(40, 617, 'hor'),
                           Wire(-20, 577, 'ver'), Wire(-20, 479, 'ver'),
                           Wire(-20, 440, 'ver'), Wire(40, 400, 'hor'),
                           Wire(80, 400, 'hor')], 1, True)
        player = Player(20, 800)
        cube = Cube(270, 800)
    elif num_level == 3:
        cube_in_level = False
        player = Player(150, 870)
        cube = Cube(0, 0)
    elif num_level == 4:
        cube_in_level = True
        hameleon = Platform(550, 20, 40, 560, '', [(20, 580)],
                            [(0, 0)], [(0, 0)], [(550, 570)], 'hameleon', 1)
        button_wire_list = [Wire(590, -20, 'hor'), Wire(690, -20, 'hor'),
                            Wire(790, -20, 'hor'), Wire(890, -20, 'hor'),
                            Wire(990, -20, 'hor'), Wire(1090, -20, 'hor'),
                            Wire(1190, -20, 'hor'), Wire(1230, 40, 'ver'),
                            Wire(1230, 140, 'ver'), Wire(1190, 180, 'hor')]
        button = Button(1155, 188, hameleon, button_wire_list, 0)
        cube = Cube(21, 320)
        player = Player(150, 670)

    # Запуск главного цикла
    return game_cycle(screen, size, num_level, floor, wall_left, wall_right)


def game_cycle(screen, size, level_number, floor, wall_left, wall_right):  # игровой цикл
    global all_sprites, wall_left_group, wall_right_group, floor_group, ceiling_group, construction_group, \
        platform_group, door_group, wire_group, button_group, player, cube, blue_portal, yellow_portal, cursor, \
        speed_vertical, speed_horizontal, speed_vertical_cube, speed_horizontal_cube, speed_ver_rez, speed_hor_rez, \
        speed_ver_rez_cube, speed_hor_rez_cube, player_left_cube, player_right_cube, background_group
    # декоративные элементы окна
    pygame.display.set_caption('Portal 2D')
    pygame.display.set_icon(pygame.image.load('data/icon.gif'))
    # объявление некоторых переменных
    blue_portal = Portal('blue')
    yellow_portal = Portal('yellow')
    WIDTH_SCREEN = size[0]
    running = True
    speed_vertical = speed_horizontal = 0
    speed_vertical_cube = 1
    speed_horizontal_cube = 0
    speed_ver_rez = speed_hor_rez = 0
    speed_ver_rez_cube = speed_hor_rez_cube = 0
    player_left_cube = player_right_cube = 0
    flag_stand = True
    flag_stand_cube = True
    # изменение курсора
    cursor_image = load_image('cursor.png', colorkey=-1)
    cursor_image = pygame.transform.scale(cursor_image, (50, 50))
    cursor = pygame.sprite.Sprite(cursor_group)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()
    pygame.mouse.set_visible(False)
    go_sound = pygame.mixer.Sound('data/go_sound.wav')
    go_sound.set_volume(0.05)
    groups = [platform_group, button_group, cube_group]
    win_flag = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                # курсор находится не в левом углу изображения, а в середине
                cursor.rect.left = event.pos[0] - 25
                cursor.rect.top = event.pos[1] - 25
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # запуск синего портала
                    blue_portal.click_mouse(event.pos[0] - 25, event.pos[1] - 25,
                                            player.rect.left, player.rect.top)
                elif event.button == 3:
                    # запуск оранжевого портала
                    yellow_portal.click_mouse(event.pos[0] - 25, event.pos[1] - 25,
                                              player.rect.left, player.rect.top)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                # взятие куба в руки
                if pygame.sprite.spritecollideany(player, cube_group) and cube.position:
                    if player.rect.top + HEIGHT_CHELL // 2 + 10 > cube.rect.y:
                        # если куб справа
                        if player.rect.left < cube.rect.left:
                            cube.rect.left = player.rect.left + WIDTH_CHELL - 25
                            cube.rect.top = player.rect.top + 6
                            player_right_cube = 70
                            for button in button_group:
                                button.interaction_cube('n')
                                if button.activated:
                                    button.disable_button()
                                    dop = button.rect.y - player.rect.top - HEIGHT_CHELL + 9
                                    player.rect.top += dop
                                    cube.rect.top += dop
                            cube.position = False
                        else:
                            # если слева
                            cube.rect.left = player.rect.left - WIDTH_CUBE + 25
                            cube.rect.top = player.rect.top + 6
                            player_left_cube = 70
                            player_right_cube = 70
                            for button in button_group:
                                button.interaction_cube('n')
                                if button.activated:
                                    button.disable_button()
                                    dop = button.rect.y - player.rect.top - HEIGHT_CHELL + 9
                                    player.rect.top += dop
                                    cube.rect.top += dop
                            cube.position = False
                elif not cube.position:
                    # отпускание куба
                    speed_vertical_cube = speed_vertical
                    speed_horizontal_cube = speed_horizontal
                    cube.position = True
                    speed_vertical_cube = 1
                    player_left_cube = player_right_cube = 0
            if event.type == walking_event and pygame.key.get_pressed()[97]:
                # движение влево с учетом взаимодействий
                pygame.mixer.Sound.play(go_sound)
                dop_step = STEP
                player.rect.left -= player_left_cube
                # учет стен
                if pygame.sprite.spritecollideany(player, wall_left_group):
                    player.rect.left += player_left_cube
                    dop_step = player.rect.left - player_left_cube - wall_left.rect.w + 25
                    if dop_step > STEP:
                        dop_step %= STEP
                else:
                    # учет платформ, куба, кнопки
                    player.rect.left += player_left_cube
                    indi_break = False
                    for group in groups:
                        if indi_break:
                            break
                        for i in group:
                            player.rect.left -= player_left_cube
                            if not pygame.sprite.spritecollideany(i, player_group):
                                player.rect.left += player_left_cube
                                continue
                            else:
                                player.rect.left += player_left_cube
                            dop_step = i.interaction('l')
                            if dop_step is None:
                                dop_step = STEP
                                continue
                            else:
                                indi_break = True
                                break
                if not cube.position:
                    cube.rect.left -= dop_step
                for button in button_group:
                    button.interaction('n')
                player.rect.left -= dop_step
                # обновление изображения спрайта
                if player.rect.left + WIDTH_CHELL // 2 - pygame.mouse.get_pos()[0] > 0:
                    player.update(False, False)
                else:
                    player.update(False, True)
            # движение вправо
            elif event.type == walking_event and pygame.key.get_pressed()[100]:
                pygame.mixer.Sound.play(go_sound)
                dop_step = STEP
                if not player_left_cube:
                    player.rect.left += player_right_cube
                    # учет стен
                if pygame.sprite.spritecollideany(player, wall_right_group):
                    if not player_left_cube:
                        player.rect.left -= player_right_cube
                    if not player_left_cube:
                        dop_step = WIDTH_SCREEN - wall_right.rect.w - (
                                player.rect.left + player_right_cube + WIDTH_CHELL - 25)
                    else:
                        dop_step = WIDTH_SCREEN - wall_right.rect.w - (
                                player.rect.left + WIDTH_CHELL - 25)
                    if dop_step > STEP:
                        dop_step %= STEP
                else:
                    # учет платфом, куба, кнопок
                    if not player_left_cube:
                        player.rect.left -= player_right_cube
                    indi_break = False
                    for group in groups:
                        if indi_break:
                            break
                        for i in group:
                            player.rect.left += player_right_cube
                            if not pygame.sprite.spritecollideany(i, player_group):
                                player.rect.left -= player_right_cube
                                continue
                            else:
                                player.rect.left -= player_right_cube
                            dop_step = i.interaction('r')
                            if dop_step is None:
                                dop_step = STEP
                                continue
                            else:
                                indi_break = True
                                break
                if not cube.position:
                    cube.rect.left += dop_step
                for button in button_group:
                    button.interaction('n')
                player.rect.left += dop_step
                # обновление изображения спрайта
                if player.rect.left + WIDTH_CHELL // 2 - pygame.mouse.get_pos()[0] > 0:
                    player.update(True, False)
                else:
                    player.update(True, True)
            # обнуление горизонтальной скорости при встрече мтен
            if speed_horizontal < 0 and pygame.sprite.spritecollideany(player, wall_left_group):
                player.rect.x = wall_left.rect.x - 4
                speed_horizontal = 0
            if speed_horizontal > 0 and pygame.sprite.spritecollideany(player, wall_right_group):
                player.rect.x = wall_right.rect.x - 81
                speed_horizontal = 0
            # присваивание вертикальной скорости для прыжка
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and \
                    (pygame.sprite.collide_mask(player, floor) or not flag_stand):
                flag_stand = True
                speed_vertical = -15
            # событие открытия и закрытия двери и активирования соответственных проводов
            if event.type == door_event:
                for i in button_group:
                    if i.control_thing.activated_list[i.thing_arg]:
                        for j in i.wire_list:
                            j.wire_on()
                    else:
                        for j in i.wire_list:
                            j.wire_off()
                    if i.control_thing.activated_list == [True] * i.control_thing.activated_list_len:
                        i.control_thing.thing_on()
                    else:
                        i.control_thing.thing_off()
            # событие падения или прыжка. Изменяет положение перса/куба и их скорость
            if event.type == svobod_pad_event:
                # учет взаимодействия с полом
                if not pygame.sprite.collide_mask(player, floor) and speed_vertical >= 0:
                    if floor.rect.y - player.rect.top - HEIGHT_CHELL < speed_vertical and not \
                            (player.rect.left + WIDTH_CHELL - 25 < floor.rect.x or player.rect.left >
                             floor.rect.x + floor.rect.w):
                        if not cube.position:
                            cube.rect.top += floor.rect.y - player.rect.top - HEIGHT_CHELL + 5
                        player.rect.top += floor.rect.y - player.rect.top - HEIGHT_CHELL + 5
                    # учет взаимодействия с платформами, кубом, кнопками
                    elif not pygame.sprite.collide_mask(player, floor):
                        dop_flag = False
                        dop = speed_vertical
                        for group in groups[0:1]:
                            for i in group:
                                dop = i.interaction('n')
                                if dop is None:
                                    dop = speed_vertical
                                    dop_flag = False
                                    continue
                                else:
                                    dop_flag = True
                                    break
                        if not cube.position:
                            cube.rect.top += dop
                        player.rect.top += dop
                        if not speed_vertical:
                            flag_stand = False
                        for group in groups[0:1]:
                            for i in group:
                                flag_stand = i.stand_or_not_stand()
                                if not flag_stand:
                                    break
                        if flag_stand:
                            speed_vertical += 1
                        if not dop_flag:
                            dop_flag = False
                            dop = speed_vertical
                            for group in groups[1:2]:
                                for i in group:
                                    dop = i.interaction('n')
                                    if dop is None:
                                        dop = speed_vertical
                                        dop_flag = False
                                        continue
                                    else:
                                        dop_flag = True
                                        break
                            if not dop_flag and cube.position:
                                dop_flag = False
                                dop = speed_vertical
                                for group in groups[2:3]:
                                    for i in group:
                                        dop = i.interaction('n')
                                        if dop is None:
                                            dop = speed_vertical
                                            dop_flag = False
                                            continue
                                        else:
                                            dop_flag = True
                                            break
                            if dop_flag:
                                if not cube.position:
                                    cube.rect.top += dop
                                player.rect.top += dop
                            if not speed_vertical:
                                flag_stand = False
                # прыжок(или вылет из поратала) с учетом взаимодействия с платформами, кубом, кнопками
                elif speed_vertical < 0:
                    dop = abs(speed_vertical)
                    for group in groups[0:1]:
                        for i in group:
                            dop = i.interaction('v')
                            if dop is None:
                                dop = abs(speed_vertical)
                                continue
                            else:
                                break
                    if not cube.position:
                        cube.rect.top -= dop
                    player.rect.top -= dop
                    speed_vertical += 1
                # зануление скоростей, если персонаж взаимодействует с полом
                elif pygame.sprite.collide_mask(player, floor):
                    speed_vertical = 0
                    speed_horizontal = 0
                # учет взаимодействия куба с полом
                if not pygame.sprite.collide_mask(cube, floor) and speed_vertical_cube >= 0 and \
                        cube.position:
                    if floor.rect.y - cube.rect.top - HEIGHT_CUBE < speed_vertical_cube:
                        cube.rect.top += floor.rect.y - cube.rect.top - HEIGHT_CUBE + 5
                    # учет взаимодействия куба с платформами, персонажем, кнопками
                    elif not pygame.sprite.collide_mask(cube, floor):
                        dop_flag = False
                        dop = speed_vertical_cube
                        for group in groups[0:1]:
                            for i in group:
                                dop = i.interaction_cube('n')
                                if dop is None:
                                    dop = speed_vertical_cube
                                    dop_flag = False
                                    continue
                                else:
                                    dop_flag = True
                                    break
                        cube.rect.top += dop
                        if not speed_vertical_cube:
                            flag_stand_cube = False
                        indi_break = False
                        for group in groups[0:2] + [player_group]:
                            if indi_break:
                                break
                            for i in group:
                                flag_stand_cube = i.stand_or_not_stand_cube()
                                if not flag_stand_cube:
                                    indi_break = True
                                    break
                        if flag_stand_cube:
                            speed_vertical_cube += 1
                        if not dop_flag:
                            dop_flag = False
                            dop = speed_vertical_cube
                            for group in groups[1:2]:
                                for i in group:
                                    dop = i.interaction_cube('n')
                                    if dop is None:
                                        dop = speed_vertical_cube
                                        dop_flag = False
                                        continue
                                    else:
                                        dop_flag = True
                                        break
                            if not dop_flag:
                                dop = player.interaction_cube('n')
                                if dop is None:
                                    dop = speed_vertical_cube
                                    dop_flag = False
                                else:
                                    dop_flag = True
                            if dop_flag:
                                cube.rect.top += dop
                            if not speed_vertical_cube:
                                flag_stand_cube = False
                # вылет из портала вверх с учетом взаимодействия с другими объектами
                elif speed_vertical_cube < 0:
                    dop = abs(speed_vertical_cube)
                    indi_break = False
                    for group in groups[0:1] + [player_group]:
                        if indi_break:
                            break
                        for i in group:
                            dop = i.interaction_cube('v')
                            if dop is None:
                                dop = abs(speed_vertical_cube)
                                continue
                            else:
                                indi_break = True
                                break
                    cube.rect.top -= dop
                    speed_vertical_cube += 1
                # зануление скоростей персонажа при взаимодействии с полом
                elif pygame.sprite.collide_mask(cube, floor):
                    speed_vertical_cube = 0
                    speed_horizontal_cube = 0
                # учет горизонтального полета(вылет из портала) куба и персонажа и их
                # взаимодействий с другими объектами
                indi_right_left = 'Саня Логинов'
                indi_right_left_cube = 'Саня Логинов'
                for group in groups[0:3]:
                    for i in group:
                        if speed_horizontal > 0:
                            indi_right_left = 'r'
                            dop = i.interaction('r', step=speed_horizontal)
                            if dop is None:
                                dop = abs(speed_horizontal)
                            else:
                                break
                        elif speed_horizontal < 0:
                            indi_right_left = 'l'
                            dop = i.interaction('l', step=abs(speed_horizontal))
                            if dop is None:
                                dop = abs(speed_horizontal)
                            else:
                                break
                if indi_right_left == 'r':
                    if not cube.position:
                        cube.rect.left += dop
                    player.rect.left += dop
                elif indi_right_left == 'l':
                    if not cube.position:
                        cube.rect.left -= dop
                    player.rect.left -= dop
                if cube.position:
                    for group in groups[0:2] + [player_group]:
                        for i in group:
                            if speed_horizontal_cube > 0:
                                indi_right_left_cube = 'r'
                                dop = i.interaction_cube('r', step=speed_horizontal)
                                if dop is None:
                                    dop = abs(speed_horizontal_cube)
                                else:
                                    break
                            elif speed_horizontal_cube < 0:
                                indi_right_left_cube = 'l'
                                dop = i.interaction_cube('l', step=abs(speed_horizontal_cube))
                                if dop is None:
                                    dop = abs(speed_horizontal_cube)
                                else:
                                    break
                    if indi_right_left_cube == 'r':
                        cube.rect.left += dop
                    elif indi_right_left_cube == 'l':
                        cube.rect.left -= dop
            # изменение изображений персонажа
            if not pygame.key.get_pressed()[97] and not pygame.key.get_pressed()[100]:
                if pygame.mouse.get_pos()[0] < player.rect.left + WIDTH_CHELL // 2:
                    player.normal(False)
                else:
                    player.normal(True)
            # запуск метода полёта порталов
            if not pygame.sprite.spritecollideany(blue_portal, construction_group) and \
                    event.type == pfly_event and blue_portal.active and not blue_portal.opened:
                blue_portal.portal_fly()
            if not pygame.sprite.spritecollideany(yellow_portal, construction_group) and \
                    event.type == pfly_event and yellow_portal.active and not yellow_portal.opened:
                yellow_portal.portal_fly()
            # запуск метода открытия порталов
            if pygame.sprite.spritecollideany(blue_portal, construction_group) and \
                    not blue_portal.opened and blue_portal.active:
                blue_portal.portal_open()
            if pygame.sprite.spritecollideany(yellow_portal, construction_group) and not \
                    yellow_portal.opened and yellow_portal.active:
                yellow_portal.portal_open()
            # начальная проверка прохождения через портал для куба, пресонажа и персонажа, держащего куб
            if blue_portal.active and yellow_portal.active and blue_portal.opened and \
                    yellow_portal.opened:
                if not cube.position:
                    if (pygame.sprite.spritecollideany(cube, blue_portal_group) or
                        cube.touch_check(blue_portal)) \
                            and (blue_portal.position == 1 or blue_portal.position == 3):
                        player.passing_through_portal('blue', 'cube')
                    if (pygame.sprite.spritecollideany(cube, yellow_portal_group) or
                        cube.touch_check(yellow_portal)) \
                            and (yellow_portal.position == 1 or yellow_portal.position == 3):
                        player.passing_through_portal('yellow', 'cube')
                else:
                    if pygame.sprite.spritecollideany(cube, blue_portal_group) or \
                            cube.touch_check(blue_portal):
                        cube.passing_through_portal('blue')
                    if pygame.sprite.spritecollideany(cube, yellow_portal_group) or \
                            cube.touch_check(yellow_portal):
                        cube.passing_through_portal('yellow')
                if pygame.sprite.spritecollideany(player, blue_portal_group):
                    player.passing_through_portal('blue')
                if pygame.sprite.spritecollideany(player, yellow_portal_group):
                    player.passing_through_portal('yellow')
            # учет взаимодействия персонажа с потолком
            if pygame.sprite.spritecollideany(player, ceiling_group) and speed_vertical < 0:
                speed_vertical = 0
            # ограничение скорочтей
            if speed_vertical > 100:
                speed_vertical = 100
            if speed_vertical_cube > 100:
                speed_vertical_cube = 100
        # выход из цикла при проходе через дверь
        if player.rect.x + WIDTH_CHELL < 25 or player.rect.x > WIDTH_SCREEN - 25:
            win_flag = True
            running = False
        screen.fill(pygame.Color("orange"))
        # прорисовка спрайтов
        background_group.draw(screen)
        door_group.draw(screen)
        all_sprites.draw(screen)
        wire_group.draw(screen)
        button_group.draw(screen)
        if blue_portal.active:
            blue_portal_group.draw(screen)
        if yellow_portal.active:
            yellow_portal_group.draw(screen)
        if cube_in_level:
            cube_group.draw(screen)
        player_group.draw(screen)
        if pygame.mouse.get_focused():
            cursor_group.draw(screen)
        pygame.display.flip()
    pygame.quit()
    return win_flag