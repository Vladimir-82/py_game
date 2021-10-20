'''
https://younglinux.info/pygame/key
'''

import pygame

FPS = 20
W, H = 500, 900
RES = 900, 950

R = 50

level_50 = H
level_150 = H
level_250 = H
level_350 = H
level_450 = H
levels = [level_50, level_150, level_250, level_350, level_450]

pygame.init()
sc = pygame.display.set_mode(RES)
sc.fill((200, 200, 200))
game_sc = pygame.Surface((W, H))

score = 0

main_font = pygame.font.Font('font/font.ttf', 25)
font = pygame.font.Font('font/font.ttf', 15)
title_tetris = main_font.render("Tetris for Downs", True, pygame.Color('darkorange'))
score_show = main_font.render("SCORE", True, pygame.Color('darkorange'))

clock = pygame.time.Clock()

v = 0
h = W // 2

UP = 'to the UP'
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
DOWN = 'down'

RUNNING, PAUSE = 0, 1
state = RUNNING



play = True
animation = []
motion = STOP


while play:
    clock.tick(FPS)
    sc.blit(game_sc, (0, 0))
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
    game_sc.fill((0, 0, 0))
    if animation:
        for anim in animation:
            pygame.draw.circle(game_sc, (255, 0, 0), anim, R)


    pygame.draw.circle(game_sc, (100, 10, 200), (h, v), R)
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

    if v >= (level_50 - R) and h == 50:
        animation.append([h, level_50 - R])
        level_50 = level_50 - 2 * R
        v = 0
    elif v >= (level_150 - R) and h == 150:
        animation.append([h, level_150 - R])
        level_150 = level_150 - 2 * R
        v = 0
    elif v >= (level_250 - R) and h == 250:
        animation.append([h, level_250 - R])
        level_250 = level_250 - 2 * R
        v = 0
    elif v >= (level_350 - R) and h == 350:
        animation.append([h, level_350 - R])
        level_350 = level_350 - 2 * R
        v = 0
    elif v >= (level_450 - R) and h == 450:
        animation.append([h, level_450 - R])
        level_450 = level_450 - 2 * R
        v = 0




    if [50, 850] in animation and [150, 850] in animation and [250, 850] in animation and [350, 850] in animation and [450, 850] in animation:

        animation.remove([50, 850])
        animation.remove([150, 850])
        animation.remove([250, 850])
        animation.remove([350, 850])
        animation.remove([450, 850])

        for i in animation:
            i[1] = i[1] + 100

        level_50 = level_50 + 2 * R
        level_150 = level_150 + 2 * R
        level_250 = level_250 + 2 * R
        level_350 = level_350 + 2 * R
        level_450 = level_450 + 2 * R

        score += 100

    sc.blit(title_tetris, (570, 10))
    sc.blit(score_show, (570, 50))

    clock.tick(FPS)



