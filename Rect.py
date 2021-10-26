'''
https://younglinux.info/pygame/rect
'''
from random import randint
import pygame as pg
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 20
W, H = 800, 800

R = W

# pg.init()
sc = pg.display.set_mode((W, H))
sc.fill((255, 255, 255))

serf_1 = pg.Surface((W//2, H//2))
serf_2 = pg.Surface((W//2, H//2))

serf_1.fill(BLACK)
serf_2.fill(BLACK)

for x, y in (0, 0), (W // 2, H // 2):
    sc.blit(serf_1, serf_1.get_rect(topleft=(x, y)))
for x, y in (W // 2, 0), (0, H // 2):
    sc.blit(serf_2, serf_2.get_rect(topleft=(x, y)))

clock = pg.time.Clock()

pg.display.update()
first_click = 'the first click'
second_click = 'the second click'
stop = 'stop'

event = stop
play = True
while play:
    clock.tick(FPS)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            play = False

        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                event = first_click

            elif i.key == pg.K_RIGHT:
                event = second_click

            elif i.key == pg.K_DOWN:
                serf_1.fill(BLACK)
                serf_2.fill(BLACK)
                for x, y in (0, 0), (W // 2, H // 2):
                    sc.blit(serf_1, serf_1.get_rect(topleft=(x, y)))
                for x, y in (W // 2, 0), (0, H // 2):
                    sc.blit(serf_2, serf_2.get_rect(topleft=(x, y)))
            elif i.key == pg.K_UP:
                play = False

        elif i.type == pg.KEYUP:
            if i.key in [pg.K_LEFT, pg.K_RIGHT]:
                event = stop

    if event == first_click:

        serf_1.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
        for x, y in (0, 0), (W // 2, H // 2):
            sc.blit(serf_1, serf_1.get_rect(topleft=(x, y)))

    elif event == second_click:
        serf_2.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
        for x, y in (W // 2, 0), (0, H // 2):
            sc.blit(serf_2, serf_2.get_rect(topleft=(x, y)))
    cir = pg.draw.circle(sc, WHITE, (W // 2, H // 2), R, R // 2 + 10)
    pg.display.update()
    clock.tick(FPS)


