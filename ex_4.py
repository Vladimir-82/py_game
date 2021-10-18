'''
https://younglinux.info/pygame/key
'''

import pygame

FPS = 20
W, H = 500, 900
R = 50

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

v = 0
h = W // 2

UP = 'to the UP'
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
DOWN = 'down'

play = True
animation = []
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
            elif i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN


        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = STOP


    pygame.display.update()
    sc.fill((0, 0, 0))
    if animation:
        for anim in animation:
            pygame.draw.circle(sc, (255, 0, 0), anim, R)


    pygame.draw.circle(sc, (100, 10, 200), (h, v), R)
    v += 15



    if motion == LEFT:
        h -= 100
    elif motion == RIGHT:
        h += 100
    elif motion == UP:
        v -= 30
    elif motion == DOWN:
        v += 50

    if h >= W - R:
        h = W - R
    elif h <= R:
        h = R


# не получается стройка

    if v >= H - R:
        animation.append((h, H - R))
        v = 0


    clock.tick(FPS)



