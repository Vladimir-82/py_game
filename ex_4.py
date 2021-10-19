'''
https://younglinux.info/pygame/key
'''

import pygame

FPS = 20
W, H = 500, 900
R = 50

level_50 = H
level_150 = H
level_250 = H
level_350 = H
level_450 = H

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
    v += 5



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

    if v >= (level_50 - R) or v >= (level_150 - R) or v >= (level_250 - R) or v >= (level_350 - R) or v >= (level_450 - R):
        if h == 50:
            animation.append((h, level_50 - R))
            level_50 = level_50 - 2 * R

        elif h == 150:
            animation.append((h, level_150 - R))
            level_150 = level_150 - 2 * R

        elif h == 250:
            animation.append((h, level_250 - R))
            level_250 = level_250 - 2 * R

        elif h == 350:
            animation.append((h, level_350 - R))
            level_350 = level_350 - 2 * R

        elif h == 450:
            animation.append((h, level_450 - R))
            level_450 = level_450 - 2 * R
        v = 0

        if (50, 850) in animation and (150, 850) in animation and (250, 850) in animation and (350, 850) in animation and (350, 850) in animation:

            animation.remove((50, 850))
            animation.remove((150, 850))
            animation.remove((250, 850))
            animation.remove((350, 850))
            animation.remove((450, 850))



    print(animation)


    clock.tick(FPS)



