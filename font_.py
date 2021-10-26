'''
https://younglinux.info/pygame/font
'''

import pygame as pg
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 20
W, H = 800, 800
clock = pg.time.Clock()

pg.init()
sc = pg.display.set_mode((W, H))
sc.fill(WHITE)

serf_1 = pg.Surface((W//2, H//2))
serf_1.fill(BLACK)

font = pg.font.Font(None, 24)
text = font.render('PYGAMES', True, (255, 0, 0))


play = True
while play:
    clock.tick(FPS)
    sc.fill(WHITE)
    sc.blit(serf_1, (50, 50))
    for i in pg.event.get():
        if i.type == pg.QUIT:
            play = False
    if pg.mouse.get_focused():
        pos = pg.mouse.get_pos()
        sc.blit(text, pos)



    pg.display.update()
    clock.tick(FPS)