'''
https://younglinux.info/pygame/font
'''

import pygame as pg
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60
W, H = 800, 800
clock = pg.time.Clock()

pg.init()
sc = pg.display.set_mode((W, H))
sc.fill(WHITE)

serf_1 = pg.Surface((W//2, H//2))
serf_1.fill(BLACK)
rect_serf_1 = serf_1.get_rect()

font = pg.font.Font(None, 24)
text = font.render('PYGAMES', True, (255, 0, 0))
place = text.get_rect(center=(200, 150))

font_danger = pg.font.Font(None, 50)
text_danger = font.render('DANGER', True, (255, 0, 0))


objects = []

play = True
while play:
    clock.tick(FPS)
    sc.fill(WHITE)
    sc.blit(serf_1, (50, 50))
    for i in objects:
        sc.blit(text, i)

    if pg.mouse.get_focused():
        pos = pg.mouse.get_pos()
        sc.blit(text, pos)
        print(pos)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            play = False

        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                 objects.append(i.pos)

    if place.contains(rect_serf_1):
        sc.blit(text_danger, (50, 50))
        print('ok')
    pg.display.update()






    pg.display.update()
    clock.tick(FPS)