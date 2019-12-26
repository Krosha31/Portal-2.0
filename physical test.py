import pygame
import os
import time

HEIGHT_CHELL = WIDTH_CHELL = 100
WIDTH_SCREEN = HEIGHT_SCREEN = 700
size = WIDTH_SCREEN, HEIGHT_SCREEN
HEIGHT_PORTAL = 80
WIDTH_PORTAL = 20
HEIGHT_SPHERE = WIDTH_SPHERE = 16
STEP = 10
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


class Player(pygame.sprite.Sprite):
    def __init__(self, x=350, y=350):
        super().__init__(player_group, all_sprites)
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
        image0 = pygame.transform.scale(image0, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.left_frames.append(image0)
        image1 = load_image("1_l.gif")
        image1 = pygame.transform.scale(image1, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.left_frames.append(image1)
        image2 = load_image("2_l.gif")
        image2 = pygame.transform.scale(image2, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.left_frames.append(image2)
        image3 = load_image("3_l.gif")
        image3 = pygame.transform.scale(image3, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.left_frames.append(image3)
        image4 = load_image("4_l.gif")
        image4 = pygame.transform.scale(image4, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.left_frames.append(image4)
        image5 = load_image("5_l.gif")
        image5 = pygame.transform.scale(image5, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.left_frames.append(image5)
        image6 = load_image("0_r.gif")
        image6 = pygame.transform.scale(image6, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.right_frames.append(image6)
        image7 = load_image("1_r.gif")
        image7 = pygame.transform.scale(image7, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.right_frames.append(image7)
        image8 = load_image("2_r.gif")
        image8 = pygame.transform.scale(image8, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.right_frames.append(image8)
        image9 = load_image("3_r.gif")
        image9 = pygame.transform.scale(image9, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.right_frames.append(image9)
        image10 = load_image("4_r.gif")
        image10 = pygame.transform.scale(image10, (HEIGHT_SPRITE, WIDTH_SPRITE))
        self.right_frames.append(image10)
        image11 = load_image("5_r.gif")
        image11 = pygame.transform.scale(image11, (HEIGHT_SPRITE, WIDTH_SPRITE))
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


class WallFloorCelling(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__(all_sprites, construction_group)
        self.image = load_image('floor.png')
        self.image = pygame.transform.scale(self.image, (w, h))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__(all_sprites, construction_group, platform_group)
        self.image = load_image('floor.png')
        self.image = pygame.transform.scale(self.image, (w, h))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def interaction_x(self, storon):
        for i in range(1, 11):
            player.rect.left += i
            if pygame.sprite.pygame.sprite.collide_mask(self, player):
                dop = pygame.sprite.pygame.sprite.collide_mask(self, player)
                player.rect.left -= i
                return dop
            player.rect.left -= i
        return False


class Portal(pygame.sprite.Sprite):
    def __init__(self, color):
        if color == 'blue':
            super().__init__(blue_portal_group)
        elif color == 'yellow':
            super().__init__(yellow_portal_group)
        self.speed = 10
        self.image_list = []
        self.add_frames(color)
        self.rect = self.image.get_rect()
        self.active = False
        self.opened = False

    def add_frames(self, color):
        if color == 'blue':
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
        elif color == 'yellow':
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
        self.image = self.image0
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
        self.opened = True
        construction_list = pygame.sprite.spritecollide(self, construction_group, False)
        if construction_list[0].group == 'wr':
            self.image = self.image_list[0]
            self.rect.x = construction_list[0].rect.x
            self.rect.y -= HEIGHT_PORTAL // 2
        elif construction_list[0].group == 'f':
            self.image = self.image_list[1]
            self.rect.y = construction_list[0].rect.y
            self.rect.x -= HEIGHT_PORTAL // 2
        elif construction_list[0].group == 'wl':
            self.image = self.image_list[2]
            self.rect.x = construction_list[0].rect.x + construction_list[0].rect.w - WIDTH_PORTAL
            self.rect.y -= HEIGHT_PORTAL // 2
        elif construction_list[0].group == 'c':
            self.image = self.image_list[3]
            self.rect.y = construction_list[0].rect.y + construction_list[0].rect.h - WIDTH_PORTAL
            self.rect.x -= HEIGHT_PORTAL // 2


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

wall_left = WallFloorCelling(0, 0, 20, HEIGHT, 'gray')
ceiling_group.add(WallFloorCelling(0, 0, WIDTH, 20, 'gray'))
wall_right = WallFloorCelling(WIDTH - 20, 0, 20, HEIGHT, 'gray')
Platform(200, HEIGHT - 180, 200, 180, 'gray')
floor = WallFloorCelling(0, HEIGHT - 20, WIDTH, 20, 'gray')
floor_group.add(floor)
player = Player()
blue_portal = Portal(0, 0, 'blue')
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

running = True
clock = pygame.time.Clock()
clock_svobod_pad = pygame.time.Clock()
boost_g = 3
speed_vertical = 0
flag_jump = True
one_step = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cursor.rect.topleft = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                blue_portal.click_mouse(event.pos[0], event.pos[1], player.rect.left, player.rect.top)
        if event.type == walking_event and pygame.key.get_pressed()[97]:
            if not pygame.sprite.pygame.sprite.collide_mask(player, wall_left):
                for i in platform_group:
                    dop = i.interaction(player.rect.left, player.rect.top)
                    if dop:
                        dop = dop[0]
                        dop_step = dop + i.rect.x - player.rect.left - 50
                        break
                    else:
                        dop_step = STEP
                player.rect.left -= dop_step
                if player.rect.left + WIDTH_CHELL // 2 - pygame.mouse.get_pos()[0] > 0:
                    player.update(False, False)
                else:
                    player.update(False, True)
        elif event.type == walking_event and pygame.key.get_pressed()[100]:
            if not pygame.sprite.pygame.sprite.collide_mask(player, wall_right):
                for i in platform_group:
                    dop = i.interaction(player.rect.left, player.rect.top)
                    if dop:
                        dop = dop[0]
                        dop_step = dop + i.rect.x - player.rect.left - 80
                        break
                    else:
                        dop_step = STEP
                player.rect.left += dop_step
                if player.rect.left + WIDTH_CHELL // 2 - pygame.mouse.get_pos()[0] > 0:
                    player.update(True, False)
                else:
                    player.update(True, True)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and pygame.sprite.collide_mask(player, floor):
            speed_vertical = -15
        if event.type == svobod_pad_event:
            if not pygame.sprite.collide_mask(player, floor) and speed_vertical >= 0:
                if floor.rect.y - player.rect.top - HEIGHT_SPRITE < speed_vertical:
                    player.rect.top += floor.rect.y - player.rect.top - HEIGHT_SPRITE + 5
                else:
                    player.rect.top += speed_vertical
            elif speed_vertical < 0:
                player.rect.top += speed_vertical
            elif pygame.sprite.collide_mask(player, floor):
                speed_vertical = 0
            speed_vertical += 1
        if not pygame.key.get_pressed()[97] and not pygame.key.get_pressed()[100]:
            if pygame.mouse.get_pos()[0] < player.rect.left + WIDTH_CHELL // 2:
                player.normal(False)
            else:
                player.normal(True)
        if not pygame.sprite.spritecollideany(blue_portal, construction_group) and event.type == pfly_event \
                and blue_portal.active and not blue_portal.opened:
            blue_portal.portal_fly()
        if pygame.sprite.spritecollideany(blue_portal, construction_group) and not blue_portal.opened \
                and blue_portal.active:
            blue_portal.portal_open()
    if pygame.sprite.spritecollideany(player, ceiling_group):
        speed_vertical = 3
    screen.fill(pygame.Color("orange"))
    construction_group.draw(screen)
    if blue_portal.active:
        blue_portal_group.draw(screen)
    if yellow_portal.active:
        yellow_portal_group.draw(screen)
    player_group.draw(screen)
    if pygame.mouse.get_focused():
        cursor_group.draw(screen)
    all_sprites.draw(screen)
    cursor_group.draw(screen)
    pygame.display.flip()
pygame.quit()