import pygame as pg
import sys

pg.init()
W_, H_ = 1100, 659
WHITE = (255, 255, 255)
MAIN_FONT = (100, 150, 200)
sc_main = pg.display.set_mode((W_, H_))
sc_main.fill(MAIN_FONT)


RIGHT = "to the right"
LEFT = "to the left"
UP = "to the up"
DOWN = "to the down"
STOP = "stop"

motion = STOP


class My_Car(pg.sprite.Sprite):

    def __init__(self, x, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y + self.image.get_height()//2))

    def to_the_left(self):
        sc_main.fill((100, 150, 200))
        rot = pg.transform.rotate(self.image, 90)
        rot_rect = rot.get_rect(center=(self.x, self.y))
        sc_main.blit(rot, rot_rect)
        self.x -= 2

    def to_the_right(self):
        sc_main.fill((100, 150, 200))
        rot = pg.transform.rotate(self.image, -90)
        rot_rect = rot.get_rect(center=(self.x, self.y))
        sc_main.blit(rot, rot_rect)
        self.x += 2

    def to_the_up(self):
        sc_main.fill((100, 150, 200))
        sc_main.blit(self.image, self.rect)
        self.y -= 2

    def to_the_down(self):
        sc_main.fill((100, 150, 200))
        rot = pg.transform.rotate(self.image, 180)
        rot_rect = rot.get_rect(center=(self.x, self.y))
        sc_main.blit(rot, rot_rect)
        self.y += 2



x, y = 200, 0
my_car = My_Car(x, y, 'car.jpg')
sc_main.blit(my_car.image, my_car.rect)
pg.display.update()


while 1:

    my_car = My_Car(x, y, 'car.jpg')
    sc_main.blit(my_car.image, my_car.rect)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                motion = LEFT
            elif i.key == pg.K_RIGHT:
                motion = RIGHT
            elif i.key == pg.K_UP:
                motion = UP
            elif i.key == pg.K_DOWN:
                motion = DOWN

        elif i.type == pg.KEYUP:
            if i.key in [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]:
                motion = STOP


    if motion == LEFT:
        my_car.to_the_left()
        pg.display.update()
    elif motion == RIGHT:
        my_car.to_the_right()
        pg.display.update()
    elif motion == UP:
        my_car.to_the_up()
        pg.display.update()
    elif motion == DOWN:
        my_car.to_the_down()
        pg.display.update()
