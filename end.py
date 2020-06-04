import pygame

pygame.init()

size = width, height = 1600, 800
screen = pygame.display.set_mode(size)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            indi = True
            screen.fill(pygame.Color('blue'))
            r = 0
            xypos = event.pos
            pygame.draw.circle(screen, color, xypos, r, w)
        if event.type == plus and indi:
            r += 1
            pygame.draw.circle(screen, color, xypos, r, w)
    pygame.display.flip()
pygame.quit()