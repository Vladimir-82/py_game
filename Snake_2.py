import pygame as pg
import sys
from random import randint

pg.init()
W, H = 800, 800
WHITE = (255, 255, 255)
MAIN_FONT = (100, 150, 200)
sc = pg.display.set_mode((W, H))
# sc = pg.Surface((W, H))
sc.fill(WHITE)


RIGHT = "to the right"
LEFT = "to the left"
UP = "to the up"
DOWN = "to the down"

motion = UP


class Head(pg.sprite.Sprite):

    def __init__(self, x, y, filename, motion, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert_alpha()
        self.motion = motion
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.add(group)

    def move(self):
        sc.fill(WHITE)
        if self.motion == LEFT:
            rot = pg.transform.rotate(self.image, 90)
            rot_rect = rot.get_rect(center=(self.x, self.y))
            sc.blit(rot, rot_rect)
            self.x -= 40
            if self.x < 0:
                self.x = W
            return self.x, self.y

        elif motion == RIGHT:
            rot = pg.transform.rotate(self.image, -90)
            rot_rect = rot.get_rect(center=(self.x, self.y))
            sc.blit(rot, rot_rect)
            self.x += 40
            if self.x > W:
                self.x = 0
            return self.x, self.y


        elif motion == UP:
            sc.blit(self.image, self.rect)
            self.y -= 40
            if self.y < 0:
                self.y = H
            return self.x, self.y

        elif motion == DOWN:
            rot = pg.transform.rotate(self.image, 180)
            rot_rect = rot.get_rect(center=(self.x, self.y))
            sc.blit(rot, rot_rect)
            self.y += 40
            if self.y > H:
                self.y = 0
            return self.x, self.y


class Body(pg.sprite.Sprite):

    def __init__(self, x, y, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        sc.blit(self.image, self.rect)

        self.add(group)



class Apple(pg.sprite.Sprite):
    def __init__(self, x, y, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)


class Troubles(pg.sprite.Sprite):
    def __init__(self, pos, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=pos)
        self.add(group)


x, y = W//2, H//2
BUSHES = ('bush_1.jpg', 'bush_2.jpg', 'bush_3.jpg')
BUSHES_SURF = []
count_troublse = 3

heads = pg.sprite.Group()

apples = pg.sprite.Group()
apple = Apple((randint(0, W)), (randint(0, H)), 'apple.png', apples)

bushes = pg.sprite.Group()
for i in range(count_troublse):
    BUSHES_SURF.append(pg.image.load(BUSHES[i]).convert_alpha())

for i in range(count_troublse):
    Troubles((randint(0, W), (randint(0, H))), BUSHES_SURF[randint(0, 1)], bushes)

bodes = pg.sprite.Group()


while 1:
    head = Head(x, y, 'head_snake.png', motion, heads)
    x, y = head.move()


    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT and motion != RIGHT:
                motion = LEFT
            elif i.key == pg.K_RIGHT and motion != LEFT:
                motion = RIGHT
            elif i.key == pg.K_UP and motion != DOWN:
                motion = UP
            elif i.key == pg.K_DOWN and motion != UP:
                motion = DOWN


    for col in pg.sprite.groupcollide(heads, bushes, False, False).keys():
        sys.exit()

    for col in pg.sprite.groupcollide(heads, apples, False, True).keys():
        apple = Apple((randint(0, W)), (randint(0, H)), 'apple.png', apples)


    bushes.draw(sc)
    apples.draw(sc)
    bodes.draw(sc)
    # heads.draw(sc)

    pg.display.update()


    pg.time.delay(300)

