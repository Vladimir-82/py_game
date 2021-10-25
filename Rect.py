'''
https://younglinux.info/pygame/rect
'''
from random import choice
import pygame as pg
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
collors =[BLACK, RED, GREEN, BLUE]
FPS = 20
W, H = 800, 800

R = 0.8 * W

pg.init()
sc = pg.display.set_mode((W, H))
sc.fill((255, 255, 255))

serf_1 = pg.Surface((W//2, H//2))
serf_2 = pg.Surface((W//2, H//2))

col_1 = choice(collors)


clock = pg.time.Clock()



pg.display.update()
# surf.set_alpha(200)
# cir = pg.draw.circle(sc, WHITE, (W//2, H//2), R)

play = True
while play:
    clock.tick(FPS)

    for i in pg.event.get():
        if i.type == pg.K_SPACE:
            play = False
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_F1:
                col_1 = choice(collors)
                serf_1.fill(col_1)
                for x, y in (0, 0), (W // 2, H // 2):
                    sc.blit(serf_1, serf_1.get_rect(topleft=(x, y)))

            elif i.key == pg.K_F2:
                col_2 = choice(collors)
                while col_2 == col_1:
                    col_2 = choice(collors)
                serf_2.fill(col_2)
                for x, y in (W // 2, 0), (0, H // 2):
                    sc.blit(serf_2, serf_2.get_rect(topleft=(x, y)))
            elif i.key == pg.K_KP0:
                pass
