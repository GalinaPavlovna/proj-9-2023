import sys
import pygame

WIDTH = 1000
HIGH = 800
p = pygame.display.set_mode((WIDTH, HIGH))

def start(zveri):
    pygame.init()
    p.fill((255, 255, 255))
    for i in zveri:
        i.rect=pygame.Rect(i.x, i.y, 3, 3)
        pygame.draw.rect(p, (255, 0, 0), i.rect)
    pygame.display.update()


def tick(zveri, pole):
    for i in range(0, WIDTH, 3):
        for o in range(0, HIGH, 3):
            eda = pole[o][i]['eda']
            pygame.draw.rect(p, (255 - eda * 2.5, 255 - eda * 2.5, 255 - eda * 2.5), (i, o, 3, 3))
    for i in zveri:
        i.rect.move_ip(i.x-i.rect.x, i.y-i.rect.y)
        pygame.draw.rect(p, (255, 0, 0), i.rect)
    pygame.display.update()
    for u in pygame.event.get():
        if u.type == pygame.QUIT:
            sys.exit()
