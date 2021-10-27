import pygame
import sys
RIGHT = "to the right"
LEFT = "to the left"
UP = "to the up"
DOWN = "to the down"
STOP = "stop"
H, W = 800, 800
h, w = H//2, W//2
sc = pygame.display.set_mode((W, H))
sc.fill((100, 150, 200))

car_surf = pygame.image.load('car.jpg').convert()
car_surf.set_colorkey((255, 255, 255))
car_rect = car_surf.get_rect(center=(h, w))
sc.blit(car_surf, car_rect)
pygame.display.update()

motion = STOP

sc.fill((100, 150, 200))
# поворачиваем на 45 градусов
# rot = pygame.transform.rotate(car_surf, 45)
# rot_rect = rot.get_rect(center=(H//2, W//2))
# sc.blit(rot, rot_rect)
# pygame.display.update()


while 1:
    sc.fill((100, 150, 200))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
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

    car_rect = car_surf.get_rect(center=(h, w))
    sc.blit(car_surf, car_rect)
    if motion == LEFT:
        h -= 2
        rot = pygame.transform.rotate(car_surf, 90)
        rot_rect = rot.get_rect(center=(h, w))
        car_rect = rot_rect

        sc.blit(rot, rot_rect)


    elif motion == RIGHT:
        h += 2
    elif motion == UP:
        w -= 2
    elif motion == DOWN:
        w += 2

    pygame.display.update()
    pygame.time.delay(20)
