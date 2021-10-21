'''
Напишите код в котором имитируется полет снаряда (пусть его роль сыграет круг) в место клика мышью.
Снаряд должен вылетать из нижнего края окна и лететь вверх, т. е. изменяться должна только координата y.
Пока летит один, другой не должен появляться. Когда снаряд достигает цели, должен имитировать взрыв, например,
в этом месте прорисовываться квадрат.
'''
import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
pygame.mixer.init()
sc = screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                weapon = pygame.draw.circle(sc, RED, i.pos, 5)
                # horisontal, vertical = i.pos[0], i.pos[1]
                pygame.display.update()
                # vertical += 5
    pygame.display.flip()

pygame.quit()