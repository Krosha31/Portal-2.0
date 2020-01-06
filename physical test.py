import pygame
import os


pygame.init()

HEIGHT_CHELL = WIDTH_CHELL = 100
WIDTH_SCREEN = HEIGHT_SCREEN = 700
size = WIDTH_SCREEN, HEIGHT_SCREEN
HEIGHT_PORTAL = 100
WIDTH_PORTAL = 20
WIDTH_WIRE = HEIGHT_WIRE = 100
HEIGHT_SPHERE = WIDTH_SPHERE = 16
STEP = 20
ZERO_SPEED = 5
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
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
    global speed_horizontal
    if color == 'blue':
        if blue_portal.position == 1 or blue_portal.position == 3:
            if blue_portal.rect.y <= self.rect.y + 15 <= blue_portal.rect.y + HEIGHT_PORTAL and \
                    blue_portal.rect.y <= self.rect.y + HEIGHT_CHELL - 15 <= blue_portal.rect.y + HEIGHT_PORTAL:
                if (blue_portal.position == 1 and self.rect.x + WIDTH_CHELL > blue_portal.rect.x + 19
                    and (pygame.key.get_pressed()[100] or speed_horizontal > 0)) or \
                        (blue_portal.position == 3 and self.rect.x < blue_portal.rect.x and
                         (pygame.key.get_pressed()[97] or speed_horizontal < 0)):
                    return True
        elif blue_portal.position == 2 or blue_portal.position == 4:
            if blue_portal.rect.x <= self.rect.x + 25 <= blue_portal.rect.x + HEIGHT_PORTAL and \
                    blue_portal.rect.x <= self.rect.x + WIDTH_CHELL - 25 <= blue_portal.rect.x + HEIGHT_PORTAL:
                if (blue_portal.position == 2 and self.rect.y + HEIGHT_CHELL > blue_portal.rect.y) \
                        or (blue_portal.position == 4 and self.rect.x < blue_portal.rect.y + WIDTH_PORTAL):
                    return True
    elif color == 'yellow':
        if yellow_portal.position == 1 or yellow_portal.position == 3:
            if yellow_portal.rect.y <= self.rect.y + 15 <= yellow_portal.rect.y + HEIGHT_PORTAL and \
                    yellow_portal.rect.y <= self.rect.y + HEIGHT_CHELL - 15 <= \
                    yellow_portal.rect.y + HEIGHT_PORTAL:
                if (yellow_portal.position == 1 and self.rect.x + WIDTH_CHELL > yellow_portal.rect.x + 19
                    and (pygame.key.get_pressed()[100] or speed_horizontal > 0)) or \
                        (yellow_portal.position == 3 and self.rect.x < yellow_portal.rect.x and
                         (pygame.key.get_pressed()[97] or speed_horizontal < 0)):
                    return True
        elif yellow_portal.position == 2 or yellow_portal.position == 4:
            if yellow_portal.rect.x <= self.rect.x + 25 <= yellow_portal.rect.x + HEIGHT_PORTAL and \
                    yellow_portal.rect.x <= self.rect.x + WIDTH_CHELL - 25 <= yellow_portal.rect.x + HEIGHT_PORTAL:
                if (yellow_portal.position == 2 and self.rect.y + HEIGHT_CHELL > yellow_portal.rect.y) \
                        or (yellow_portal.position == 4 and self.rect.x < yellow_portal.rect.y + WIDTH_PORTAL):
                    return True
    return False


class Player(pygame.sprite.Sprite):
    def __init__(self, x=350, y=50):
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

    def add_frames(self):
        image0 = load_image("0_l.gif")
        image0 = pygame.transform.scale(image0, (HEIGHT_CHELL, WIDTH_CHELL))
        self.left_frames.append(image0)
        image1 = load_image("1_l.gif")
        image1 = pygame.transform.scale(image1, (HEIGHT_CHELL, WIDTH_CHELL))
        self.left_frames.append(image1)
        image2 = load_image("2_l.gif")
        image2 = pygame.transform.scale(image2, (HEIGHT_CHELL, WIDTH_CHELL))
        self.left_frames.append(image2)
        image3 = load_image("3_l.gif")
        image3 = pygame.transform.scale(image3, (HEIGHT_CHELL, WIDTH_CHELL))
        self.left_frames.append(image3)
        image4 = load_image("4_l.gif")
        image4 = pygame.transform.scale(image4, (HEIGHT_CHELL, WIDTH_CHELL))
        self.left_frames.append(image4)
        image5 = load_image("5_l.gif")
        image5 = pygame.transform.scale(image5, (HEIGHT_CHELL, WIDTH_CHELL))
        self.left_frames.append(image5)
        image6 = load_image("0_r.gif")
        image6 = pygame.transform.scale(image6, (HEIGHT_CHELL, WIDTH_CHELL))
        self.right_frames.append(image6)
        image7 = load_image("1_r.gif")
        image7 = pygame.transform.scale(image7, (HEIGHT_CHELL, WIDTH_CHELL))
        self.right_frames.append(image7)
        image8 = load_image("2_r.gif")
        image8 = pygame.transform.scale(image8, (HEIGHT_CHELL, WIDTH_CHELL))
        self.right_frames.append(image8)
        image9 = load_image("3_r.gif")
        image9 = pygame.transform.scale(image9, (HEIGHT_CHELL, WIDTH_CHELL))
        self.right_frames.append(image9)
        image10 = load_image("4_r.gif")
        image10 = pygame.transform.scale(image10, (HEIGHT_CHELL, WIDTH_CHELL))
        self.right_frames.append(image10)
        image11 = load_image("5_r.gif")
        image11 = pygame.transform.scale(image11, (HEIGHT_CHELL, WIDTH_CHELL))
        self.right_frames.append(image11)

    def update(self, curse, look):
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
        self.cur_frame = 3
        if look:
            self.image = self.right_frames[self.cur_frame]
        else:
            self.image = self.left_frames[self.cur_frame]

    def passing_through_portal(self, color):
        global speed_horizontal
        if color == 'blue':
            if chell_pass_to_portal(self, color):
                self.teleport('yellow', blue_portal.position)
        elif color == 'yellow':
            if chell_pass_to_portal(self, color):
                self.teleport('blue', yellow_portal.position)

    def teleport(self, color, position):
        global speed_vertical, speed_horizontal, speed_ver_rez, speed_hor_rez
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
        if color == 'blue':
            if blue_portal.position == 1:
                self.rect.x = blue_portal.rect.x - WIDTH_CHELL + 19
                self.rect.y = blue_portal.rect.y
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
                speed_vertical = 0
            elif blue_portal.position == 3:
                self.rect.x = blue_portal.rect.x + 1
                self.rect.y = blue_portal.rect.y
                if position == 1 and speed_horizontal == 0:
                    speed_horizontal = ZERO_SPEED
                elif position == 3:
                    if speed_horizontal != 0:
                        speed_horizontal = -speed_horizontal
                    else:
                        speed_horizontal = -ZERO_SPEED
                elif position == 2:
                    speed_horizontal = speed_vertical - 1
                elif position == 4:
                    speed_horizontal = -speed_vertical
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
                speed_horizontal = 0
        elif color == 'yellow':
            if yellow_portal.position == 1:
                self.rect.x = yellow_portal.rect.x - WIDTH_CHELL + 19
                self.rect.y = yellow_portal.rect.y
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
                speed_vertical = 0
            elif yellow_portal.position == 3:
                self.rect.x = yellow_portal.rect.x + 1
                self.rect.y = yellow_portal.rect.y
                if position == 1 and speed_horizontal == 0:
                    speed_horizontal = ZERO_SPEED
                elif position == 3:
                    if speed_horizontal != 0:
                        speed_horizontal = -speed_horizontal
                    else:
                        speed_horizontal = -ZERO_SPEED
                elif position == 2:
                    speed_horizontal = speed_vertical - 1
                elif position == 4:
                    speed_horizontal = -speed_vertical
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
                speed_horizontal = 0


class Wire(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        super().__init__(all_sprites, wire_group)
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

    def wire_on(self):
        self.image = self.image_list[1]

    def wire_off(self):
        self.image = self.image_list[0]


class WallFloorCelling(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color, group, interval_list):
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
    def __init__(self, x, y, w, h, color, interval_list_1, interval_list_2, interval_list_3, interval_list_4, type='n'):
        if type == 'n':
            super().__init__(all_sprites, construction_group, platform_group)
            if color == 'grey':
                self.image = load_image('grey.png')
            elif color == 'black':
                self.image = load_image('black.png')
        elif type == 'door':
            super().__init__(construction_group, platform_group, door_group)
            color = 'black'
            w = 19
            h = 100
            self.image = load_image('door.gif')
            self.pos = False
            self.y = y
            self.speed = 10
        self.image = pygame.transform.scale(self.image, (w, h))
        self.mask = pygame.mask.from_surface(self.image)
        self.color = color
        self.group = 'p'
        self.interval_list_1 = interval_list_1
        self.interval_list_2 = interval_list_2
        self.interval_list_3 = interval_list_3
        self.interval_list_4 = interval_list_4
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def interaction(self, side_of_movement, step=STEP):
        global speed_vertical, flag_stand, speed_horizontal, speed_ver_rez, speed_hor_rez
        if side_of_movement == 'l':
            player_left = player.rect.left - step
            if self.rect.x + self.rect.w < player_left + WIDTH_CHELL:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if player.rect.left - self.rect.x - self.rect.w + 25 >= step or not flag_stand:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return player.rect.left - self.rect.x - self.rect.w + 25
            return None
        elif side_of_movement == 'r':
            player_left = player.rect.left + step
            if self.rect.x > player_left:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if self.rect.x - player_left - WIDTH_CHELL + 40 >= STEP or not flag_stand:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return self.rect.x - player_left - WIDTH_CHELL + 40
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
                        player.rect.left + 25 > self.rect.x + self.rect.w:
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
        if player.rect.left + WIDTH_CHELL - 25 < self.rect.x or \
                player.rect.left + 25 > self.rect.x + self.rect.w or self.rect.y - player.rect.top - HEIGHT_CHELL + 9:
            return True
        else:
            return False

    def door_open(self):
        self.rect.y -= self.speed
        if self.y - self.rect.y >= self.rect.h:
            self.pos = True
            self.rect.y = self.y - self.rect.h

    def door_close(self):
        self.rect.y += self.speed
        if self.y - self.rect.y <= 0:
            self.pos = False
            self.rect.y = self.y


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, button_group)
        self.image = load_image('button.gif')
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.activated = False
        self.player_at_the_top = False

    def interaction(self, side_of_movement, step=STEP):
        global speed_vertical, flag_stand, speed_horizontal, speed_ver_rez, speed_hor_rez
        if not self.player_at_the_top:
            self.disable_button()
        if side_of_movement == 'l':
            player_left = player.rect.left - step
            if self.rect.x + self.rect.w < player_left + WIDTH_CHELL:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if player.rect.left - self.rect.x - self.rect.w + 25 >= step or not flag_stand:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return player.rect.left - self.rect.x - self.rect.w + 25
            return None
        elif side_of_movement == 'r':
            player_left = player.rect.left + step
            if self.rect.x > player_left:
                if player.rect.top + HEIGHT_CHELL < self.rect.y or \
                        player.rect.y > self.rect.y + self.rect.h:
                    return None
                else:
                    if self.rect.x - player_left - WIDTH_CHELL + 40 >= STEP or not flag_stand:
                        return None
                    speed_hor_rez = speed_horizontal
                    speed_horizontal = 0
                    return self.rect.x - player_left - WIDTH_CHELL + 40
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
                        player.rect.left + 25 > self.rect.x + self.rect.w:
                    self.player_at_the_top = False
                    return None
                elif self.rect.y - player.rect.top - HEIGHT_CHELL + 9 > speed_vertical:
                    self.player_at_the_top = False
                    return None
                else:
                    speed_ver_rez = speed_vertical
                    speed_hor_rez = speed_horizontal
                    speed_vertical = 0
                    speed_horizontal = 0
                    self.player_at_the_top = True
                    self.activate_button()
                    return self.rect.y - player.rect.top - HEIGHT_CHELL + 9
            return None

    def activate_button(self):
        global flag_door
        self.image = load_image('button_is_pressed.gif')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y + 5)
        self.activated = True
        flag_door = True

    def disable_button(self):
        global flag_door
        self.image = load_image('button.gif')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.activated = False
        flag_door = False

    def stand_or_not_stand(self):
        if player.rect.left + WIDTH_CHELL - 25 < self.rect.x or \
                player.rect.left + 25 > self.rect.x + self.rect.w or self.rect.y - player.rect.top - HEIGHT_CHELL + 9:
            return True
        else:
            return False


class Portal(pygame.sprite.Sprite):
    def __init__(self, color):
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
        self.x += self.speed * self.x_nap * self.xx / self.ss
        self.rect.x = int(self.x)
        self.y += self.speed * self.y_nap * self.yy / self.ss
        self.rect.y = int(self.y)

    def portal_open(self):
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
                    self.rect.x = self.construction.rect.x + self.construction.rect.w - WIDTH_PORTAL
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
                    if self.color == 'blue' and pygame.sprite.spritecollideany(self, yellow_portal_group) \
                            and yellow_portal.active:
                        self.portal_other_portal_wall(interval, yellow_portal.rect.y)
                    elif self.color == 'yellow' and pygame.sprite.spritecollideany(self, blue_portal_group) \
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
                    self.rect.y = self.construction.rect.y + self.construction.rect.h - WIDTH_PORTAL
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
                    if self.color == 'blue' and pygame.sprite.spritecollideany(self, yellow_portal_group) \
                            and yellow_portal.active:
                        self.portal_other_portal_floor_ceiling(interval, yellow_portal.rect.x)
                    elif self.color == 'yellow' and pygame.sprite.spritecollideany(self, blue_portal_group) \
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
        if self.color == 'blue' and pygame.sprite.spritecollideany(self, yellow_portal_group) and yellow_portal.active:
            self.active = False
        elif self.color == 'yellow' and pygame.sprite.spritecollideany(self, blue_portal_group) and blue_portal.active:
            self.active = False

    def portal_other_portal_wall(self, interval, y_2):
        if y_2 < self.rect.y + HEIGHT_PORTAL // 2 < y_2 + HEIGHT_PORTAL:
            self.active = False
        else:
            if self.rect.y + HEIGHT_PORTAL // 2 <= y_2 and interval[0] <= y_2 - HEIGHT_PORTAL:
                self.rect.y = y_2 - HEIGHT_PORTAL
            elif self.rect.y + HEIGHT_PORTAL // 2 >= y_2 + HEIGHT_PORTAL and interval[1] >= y_2 + 2 * HEIGHT_PORTAL:
                self.rect.y = y_2 + HEIGHT_PORTAL
            else:
                self.active = False

    def portal_other_portal_floor_ceiling(self, interval, x_2):
        if x_2 < self.rect.x + HEIGHT_PORTAL // 2 < x_2 + HEIGHT_PORTAL:
            self.active = False
        else:
            if self.rect.x + HEIGHT_PORTAL // 2 <= x_2 and interval[0] <= x_2 - HEIGHT_PORTAL:
                self.rect.x = x_2 - HEIGHT_PORTAL
            elif self.rect.x + HEIGHT_PORTAL // 2 >= x_2 + HEIGHT_PORTAL and interval[1] >= x_2 + 2 * HEIGHT_PORTAL:
                self.rect.x = x_2 + HEIGHT_PORTAL
            else:
                self.active = False

    def position_on_platform(self):
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


player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
wall_left_group = pygame.sprite.Group()
wall_right_group = pygame.sprite.Group()
floor_group = pygame.sprite.Group()
ceiling_group = pygame.sprite.Group()
cursor_group = pygame.sprite.Group()
construction_group = pygame.sprite.Group()
blue_portal_group = pygame.sprite.Group()
yellow_portal_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
wire_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()

wall_left = WallFloorCelling(0, 0, 20, HEIGHT_SCREEN - 120, 'grey', 'wl', [(20, HEIGHT_SCREEN - 120)])
ceiling_group.add(WallFloorCelling(0, 0, WIDTH_SCREEN, 20, 'grey', 'c', [(20, WIDTH_SCREEN - 20)]))
wall_right = WallFloorCelling(WIDTH_SCREEN - 20, 0, 20, HEIGHT_SCREEN, 'grey', 'wr', [(20, HEIGHT_SCREEN - 20)])
Platform(100, HEIGHT_SCREEN - 300, 200, 100, 'grey', [(400, 500)], [(100, 300)], [(400, 500)], [(100, 300)])
Platform(400, HEIGHT_SCREEN - 300, 200, 100, 'grey', [(400, 500)], [(400, 600)], [(400, 500)], [(400, 600)])
door = Platform(0, 580, 0, 0, '', [], [], [], [], 'door')
Wire(100, 100, 'ver')
Wire(160, 140, 'hor')
floor = WallFloorCelling(0, HEIGHT_SCREEN - 20, WIDTH_SCREEN, 20, 'grey', 'f', [(20, WIDTH_SCREEN - 20)])
floor_group.add(floor)
wall_left_group.add(wall_left)
wall_right_group.add(wall_right)
player = Player()
button = Button(500, 652)
blue_portal = Portal('blue')
yellow_portal = Portal('yellow')

cursor_image = load_image('cursor.png', colorkey=-1)
cursor_image = pygame.transform.scale(cursor_image, (50, 50))
cursor = pygame.sprite.Sprite(cursor_group)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()
pygame.mouse.set_visible(False)
walking_event = 25
pygame.time.set_timer(walking_event, 100)
svobod_pad_event = 24
pygame.time.set_timer(svobod_pad_event, 25)
pfly_event = 26
pygame.time.set_timer(pfly_event, 1)
door_event = 23
pygame.time.set_timer(door_event, 1)

pygame.mixer.music.load('data/background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

running = True
clock = pygame.time.Clock()
clock_svobod_pad = pygame.time.Clock()
boost_g = 3
speed_vertical = 0
speed_horizontal = 0
speed_ver_rez = 0
speed_hor_rez = 0
flag_jump = True
one_step = True
flag_left_step = True
flag_right_step = True
flag_stand = True
flag_door = False
go_sound = pygame.mixer.Sound('data/go_sound.wav')
go_sound.set_volume(0.05)
groups = [platform_group, button_group]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cursor.rect.left = event.pos[0] - 25
            cursor.rect.top = event.pos[1] - 25
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                blue_portal.click_mouse(event.pos[0] - 25, event.pos[1] - 25, player.rect.left, player.rect.top)
            elif event.button == 3:
                yellow_portal.click_mouse(event.pos[0] - 25, event.pos[1] - 25, player.rect.left, player.rect.top)
        if event.type == walking_event and pygame.key.get_pressed()[97]:
            pygame.mixer.Sound.play(go_sound)
            dop_step = STEP
            if pygame.sprite.spritecollideany(player, wall_left_group):
                dop_step = player.rect.left - wall_left.rect.w + 25
                if dop_step > STEP:
                    dop_step %= STEP
            else:
                for group in groups:
                    for i in group:
                        if not pygame.sprite.spritecollideany(i, player_group):
                            continue
                        dop_step = i.interaction('l')
                        if dop_step is None:
                            dop_step = STEP
                            continue
                        else:
                            break
            player.rect.left -= dop_step
            if player.rect.left + WIDTH_CHELL // 2 - pygame.mouse.get_pos()[0] > 0:
                player.update(False, False)
            else:
                player.update(False, True)
        elif event.type == walking_event and pygame.key.get_pressed()[100]:
            pygame.mixer.Sound.play(go_sound)
            dop_step = STEP
            if pygame.sprite.spritecollideany(player, wall_right_group):
                dop_step = WIDTH_SCREEN - wall_right.rect.w - player.rect.left - 80
                if dop_step > STEP:
                    dop_step %= STEP
            else:
                for group in groups:
                    for i in group:
                        if not pygame.sprite.spritecollideany(i, player_group):
                            continue
                        dop_step = i.interaction('r')
                        if dop_step is None:
                            dop_step = STEP
                            continue
                        else:
                            break
            player.rect.left += dop_step
            if player.rect.left + WIDTH_CHELL // 2 - pygame.mouse.get_pos()[0] > 0:
                player.update(True, False)
            else:
                player.update(True, True)
        if speed_horizontal < 0 and pygame.sprite.spritecollideany(player, wall_left_group):
            player.rect.x = wall_left.rect.x - 4
            speed_horizontal = 0
        if speed_horizontal > 0 and pygame.sprite.spritecollideany(player, wall_right_group):
            player.rect.x = wall_right.rect.x - 81
            speed_horizontal = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and \
                (pygame.sprite.collide_mask(player, floor) or not flag_stand):
            flag_stand = True
            speed_vertical = -15
        if event.type == door_event:
            if flag_door and not door.pos:
                door.door_open()
                for i in wire_group:
                    i.wire_on()
            if not flag_door and door.pos:
                for i in wire_group:
                    i.wire_off()
                door.door_close()
        if event.type == svobod_pad_event:
            if not pygame.sprite.collide_mask(player, floor) and speed_vertical >= 0:
                if floor.rect.y - player.rect.top - HEIGHT_CHELL < speed_vertical:
                    player.rect.top += floor.rect.y - player.rect.top - HEIGHT_CHELL + 5
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
                                    continue
                                else:
                                    dop_flag = True
                                    break
                        if dop_flag:
                            player.rect.top += dop
                        if not speed_vertical:
                            flag_stand = False
                        for group in groups[1:2]:
                            for i in group:
                                flag_stand = i.stand_or_not_stand()
                                if not flag_stand:
                                    break
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
                player.rect.top -= dop
                speed_vertical += 1
            elif pygame.sprite.collide_mask(player, floor):
                speed_vertical = 0
                speed_horizontal = 0
            indi_right_left = 'Саня Логинов'
            for group in groups[0:1]:
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
                player.rect.left += dop
            elif indi_right_left == 'l':
                player.rect.left -= dop
        if not pygame.key.get_pressed()[97] and not pygame.key.get_pressed()[100]:
            if pygame.mouse.get_pos()[0] < player.rect.left + WIDTH_CHELL // 2:
                player.normal(False)
            else:
                player.normal(True)
        if not pygame.sprite.spritecollideany(blue_portal, construction_group) and event.type == pfly_event \
                and blue_portal.active and not blue_portal.opened:
            blue_portal.portal_fly()
        if not pygame.sprite.spritecollideany(yellow_portal, construction_group) and event.type == pfly_event \
                and yellow_portal.active and not yellow_portal.opened:
            yellow_portal.portal_fly()
        if pygame.sprite.spritecollideany(blue_portal, construction_group) and not blue_portal.opened \
                and blue_portal.active:
            blue_portal.portal_open()
        if pygame.sprite.spritecollideany(yellow_portal, construction_group) and not yellow_portal.opened \
                and yellow_portal.active:
            yellow_portal.portal_open()
        if blue_portal.active and yellow_portal.active and blue_portal.opened and yellow_portal.opened:
            if pygame.sprite.spritecollideany(player, blue_portal_group):
                player.passing_through_portal('blue')
            if pygame.sprite.spritecollideany(player, yellow_portal_group):
                player.passing_through_portal('yellow')
        if pygame.sprite.spritecollideany(player, ceiling_group) and speed_vertical < 0:
            speed_vertical = 0
        if speed_vertical > 100:
            speed_vertical = 100
    if player.rect.x + WIDTH_CHELL < 25 or player.rect.x > WIDTH_SCREEN - 25:
        running = False
    screen.fill(pygame.Color("orange"))
    door_group.draw(screen)
    all_sprites.draw(screen)
    button_group.draw(screen)
    if blue_portal.active:
        blue_portal_group.draw(screen)
    if yellow_portal.active:
        yellow_portal_group.draw(screen)
    player_group.draw(screen)
    if pygame.mouse.get_focused():
        cursor_group.draw(screen)
    pygame.display.flip()
pygame.quit()