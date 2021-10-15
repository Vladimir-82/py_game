'''
https://younglinux.info/pygame/key
'''

import pygame

FPS = 30
W, H = 800, 500

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

v = 0
h = W // 2

RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"

play = True

motion = STOP


while play:

    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                motion = STOP


    pygame.display.update()
    sc.fill((0, 0, 0))

    pygame.draw.circle(sc, (100, 10, 200), (h, v), 50)
    v += 30
    if v == 500:
        break

    if motion == LEFT:
        h -= 20
    elif motion == RIGHT:
        h += 20

    clock.tick(FPS)