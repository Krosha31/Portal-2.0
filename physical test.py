import pygame
import os
import time

HEIGHT_SPRITE = WIDTH_SPRITE = 100
pygame.init()
WIDTH = HEIGHT = 700
size = WIDTH, HEIGHT
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

    def update(self):
        if self.curse:
            self.cur_frame = (self.cur_frame + 1) % len(self.right_frames)
            self.image = self.right_frames[self.cur_frame]
        else:
            self.cur_frame = (self.cur_frame + 1) % len(self.left_frames)
            self.image = self.left_frames[self.cur_frame]

    def normal(self):
        self.cur_frame = 3
        if self.curse:
            self.image = self.right_frames[self.cur_frame]
        else:
            self.image = self.left_frames[self.cur_frame]


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__(floor_group, all_sprites)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.image, pygame.Color(color), (0, 0, w, h))


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__(wall_group, all_sprites)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.image, pygame.Color(color), (0, 0, w, h))


class Ceiling(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__(ceiling_group, all_sprites)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.image, pygame.Color(color), (0, 0, w, h))


player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
floor_group = pygame.sprite.Group()
ceiling_group = pygame.sprite.Group()
cursor_group = pygame.sprite.Group()

Wall(0, 0, 20, HEIGHT, 'gray')
Ceiling(0, 0, WIDTH, 20, 'gray')
Wall(WIDTH - 20, 0, 20, HEIGHT, 'gray')
floor = Floor(0, HEIGHT - 20, WIDTH, 20, 'gray')
player = Player()

cursor_image = load_image('cursor.png', colorkey=-1)
cursor_image = pygame.transform.scale(cursor_image, (50, 50))
cursor = pygame.sprite.Sprite(cursor_group)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()
pygame.mouse.set_visible(False)
walking_event = 25
pygame.time.set_timer(walking_event, 100)

running = True
clock = pygame.time.Clock()
clock_svobod_pad = pygame.time.Clock()
boost_g = 3
speed_vertical = 0
flag_jump = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cursor.rect.topleft = event.pos
        if event.type == walking_event and pygame.key.get_pressed()[97]:
                player.rect.left -= 10
                player.curse = False
                player.update()
        elif event.type == walking_event and pygame.key.get_pressed()[100]:
                player.rect.left += 10
                player.curse = True
                player.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and flag_jump:
                player.rect.top -= 100
        if not pygame.key.get_pressed()[97] and not pygame.key.get_pressed()[100]:
            player.normal()
    if not pygame.sprite.spritecollideany(player, floor_group):
        speed_vertical += boost_g * clock_svobod_pad.tick() / 1000
        flag_jump = False
    else:
        speed_vertical = 0
        flag_jump = True
    dop_y = player.rect.top
    if floor.rect.y - player.rect.top - HEIGHT_SPRITE < speed_vertical:
        player.rect.top += floor.rect.y - player.rect.top - HEIGHT_SPRITE + 5
    else:
        player.rect.top += speed_vertical
    clock.tick(1000)
    screen.fill(pygame.Color("white"))
    if pygame.mouse.get_focused():
        cursor_group.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()