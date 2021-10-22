'''
https://younglinux.info/pygame/mouse
Напишите код в котором имитируется полет снаряда (пусть его роль сыграет круг) в место клика мышью.
Снаряд должен вылетать из нижнего края окна и лететь вверх, т. е. изменяться должна только координата y.
Пока летит один, другой не должен появляться. Когда снаряд достигает цели, должен имитировать взрыв, например,
в этом месте прорисовываться квадрат.
'''
import pygame

WIDTH = 360
HEIGHT = 480
FPS = 40
R = 20

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
points = []
running = True

while running:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.circle(sc, RED, i.pos, R)
                coordinats = [i.pos[0], i.pos[1]]
                points.append(coordinats)
            elif i.button == 3:
                pygame.quit()
                running = False


    if points:
        sc.fill((0, 0, 0))
        start_point = points[0]
        pygame.draw.circle(sc, BLUE, start_point, R)
        start_point[1] -= 10
        pygame.display.update()
        pygame.display.flip()
        if start_point[1] <= 2 * R:
            sc.fill((0, 0, 0))
            pygame.draw.rect(sc, GREEN, (start_point[0] - R, start_point[1] - 2 * R, 2 * R, 2 * R))
            pygame.display.update()
            pygame.display.flip()
            del points[0]
            clock.tick(5)

    clock.tick(FPS)
