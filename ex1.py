'''
https://younglinux.info/pygame/key
'''

import pygame

FPS = 10
W, H = 800, 500

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

v = 0
h = W // 2
play = True

while play:

    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                h -= 20
            elif i.key == pygame.K_RIGHT:
                h += 20


    pygame.display.update()
    sc.fill((0, 0, 0))

    pygame.draw.circle(sc, (100, 10, 200), (h, v), 50)
    v += 30
    if v == 500:
        break

    clock.tick(FPS)