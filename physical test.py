import pygame
import os
import time


pygame.init()
WIDTH = HEIGHT = 800
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
    def __init__(self, x=50, y=50):
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
        image0 = pygame.transform.scale(image0, (100, 100))
        self.left_frames.append(image0)
        image1 = load_image("1_l.gif")
        image1 = pygame.transform.scale(image1, (100, 100))
        self.left_frames.append(image1)
        image2 = load_image("2_l.gif")
        image2 = pygame.transform.scale(image2, (100, 100))
        self.left_frames.append(image2)
        image3 = load_image("3_l.gif")
        image3 = pygame.transform.scale(image3, (100, 100))
        self.left_frames.append(image3)
        image4 = load_image("4_l.gif")
        image4 = pygame.transform.scale(image4, (100, 100))
        self.left_frames.append(image4)
        image5 = load_image("5_l.gif")
        image5 = pygame.transform.scale(image5, (100, 100))
        self.left_frames.append(image5)
        image6 = load_image("0_r.gif")
        image6 = pygame.transform.scale(image6, (100, 100))
        self.right_frames.append(image6)
        image7 = load_image("1_r.gif")
        image7 = pygame.transform.scale(image7, (100, 100))
        self.right_frames.append(image7)
        image8 = load_image("2_r.gif")
        image8 = pygame.transform.scale(image8, (100, 100))
        self.right_frames.append(image8)
        image9 = load_image("3_r.gif")
        image9 = pygame.transform.scale(image9, (100, 100))
        self.right_frames.append(image9)
        image10 = load_image("4_r.gif")
        image10 = pygame.transform.scale(image10, (100, 100))
        self.right_frames.append(image10)
        image11 = load_image("5_r.gif")
        image11 = pygame.transform.scale(image11, (100, 100))
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
        self.add(all_sprites)
        self.add(floor_group)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x, y, 20, 20)
        pygame.draw.rect(self.image, pygame.Color(color), (0, 0, w, h))


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__(wall_group, all_sprites)
        self.add(all_sprites)
        self.add(wall_group)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x, y, 20, 20)
        pygame.draw.rect(self.image, pygame.Color(color), (0, 0, w, h))


player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
floor_group = pygame.sprite.Group()
Wall(0, 0, 20, HEIGHT, 'gray')
Floor(0, 0, WIDTH, 20, 'gray')
Wall(WIDTH - 20, 0, 20, HEIGHT, 'gray')
Floor(0, HEIGHT - 20, WIDTH, 20, 'gray')
player = Player()
running = True
k = 0
time_begin = 0
indi = False
clock = pygame.time.Clock()
boost_g = 10
speed_vertical = 0
while running:
    if pygame.key.get_pressed()[276]:
        if not time_begin:
            time_begin = time.time()
        if time.time() - time_begin > 0.1:
            player.rect.left -= 10
            player.curse = False
            player.update()
    elif pygame.key.get_pressed()[275]:
        if not time_begin:
            time_begin = time.time()
        if time.time() - time_begin > 0.1:
            player.rect.left += 10
            player.curse = True
            player.update()
    else:
        time_begin = 0
        indi = True
        player.normal()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if indi:
                    player.rect.left -= 10
                    indi = False
                    player.curse = False
                    player.update()
            if event.key == pygame.K_RIGHT:
                if indi:
                    player.rect.left += 10
                    indi = False
                    player.curse = True
                    player.update()
            if event.key == pygame.K_SPACE:
                player.rect.top -= 20
    if pygame.sprite.spritecollideany(player,wall_group):
        print('ok')
    clock.tick(10)
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()