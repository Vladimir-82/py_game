'''
https://younglinux.info/pygame/font
'''

import pygame as pg
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FPS = 60
W, H = 800, 800
clock = pg.time.Clock()

pg.init()
sc = pg.display.set_mode((W, H))
sc.fill(WHITE)

rect1 = pg.Rect((0, 0, 200, 200))
rect2 = pg.Rect((100, 100, 30, 30))

font_danger = pg.font.Font(None, 50)
text_danger = font_danger.render('DANGER', True, (255, 0, 0))
place = text_danger.get_rect(center = (W//2, H//2))

play = True
while play:
    clock.tick(FPS)
    sc.fill(WHITE)
    pg.draw.rect(sc, RED, rect1)


    if pg.mouse.get_focused():
        pos = pg.mouse.get_pos()
        obj = pg.draw.rect(sc, BLACK, (pos[0], pos[1], 20, 20))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            play = False

    if rect1.contains(obj):
        sc.blit(text_danger, place)



    pg.display.update()
    clock.tick(FPS)