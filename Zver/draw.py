import sys
import pygame

WIDTH = 600
HIGH = 600
scale = 5
p = pygame.display.set_mode((600, 600))



def start(zveri):
    pygame.init()
    p.fill((255, 255, 255))
    for i in zveri:
        i.rect = pygame.Rect(i.x, i.y, scale, scale)
        pygame.draw.rect(p, (255, 0, 0), i.rect)
    pygame.display.update()


def tick(zveri, pole):
    for i in range(0, WIDTH, scale):
        for o in range(0, HIGH, scale):
            eda = pole[o][i]['eda']
            pygame.draw.rect(p, (255 - eda * 2.5, 255 - eda * 2.5, 255 - eda * 2.5), (i, o, scale, scale))
    for i in zveri:
        i.rect.move_ip(i.x - i.rect.x, i.y - i.rect.y)
        pygame.draw.rect(p, (255, 0, 0), i.rect)
    pygame.display.update()
    for u in pygame.event.get():
        if u.type == pygame.QUIT:
            sys.exit()
