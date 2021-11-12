import pygame as pg
import sys
from random import randint

pg.init()
W, H = 600, 600
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

    def __init__(self, x, y, filename, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.add(group)


    def to_the_left(self):
        sc.fill(WHITE)
        rot = pg.transform.rotate(self.image, 90)
        rot_rect = rot.get_rect(center=(self.x, self.y))
        sc.blit(rot, rot_rect)
        self.x -= 2
        if self.x == 0:
            self.x = W - self.rect.height//2
        return self.x, self.y

    def to_the_right(self):
        sc.fill(WHITE)
        rot = pg.transform.rotate(self.image, -90)
        rot_rect = rot.get_rect(center=(self.x, self.y))
        sc.blit(rot, rot_rect)
        self.x += 2
        if self.x == W:
            self.x = self.rect.height//2
        return self.x, self.y

    def to_the_up(self):
        sc.fill(WHITE)
        sc.blit(self.image, self.rect)
        self.y -= 2
        if self.y == 0:
            self.y = H - self.rect.width//2
        return self.x, self.y

    def to_the_down(self):
        sc.fill(WHITE)
        rot = pg.transform.rotate(self.image, 180)
        rot_rect = rot.get_rect(center=(self.x, self.y))
        sc.blit(rot, rot_rect)
        self.y += 2
        if self.y == H:
            self.y = self.rect.width//2
        return self.x, self.y


class Body(Head):
    def __init__(self, x, y, filename, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)



    # def move(self):
    #     sc.fill(WHITE)
    #     Body.bode_list.append((self.x, self.y))
    #     print(Body.bode_list)
    #     if len(Body.bode_list) == 40:
    #         self.add(self.group)
    #         sc.blit(self.image, self.rect)

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

body_list = []



while 1:
    head = Head(x, y, 'head_snake.png', heads)

    # body_list.append((x, y))
    # if len(body_list) == 40:
    #     for i in body_list:
    #         body = Body(i[0], i[1], 'body.png', bodes)


    # body.move()

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

    if motion == LEFT:
        x, y = head.to_the_left()
    elif motion == RIGHT:
        x, y = head.to_the_right()
    elif motion == UP:
        x, y = head.to_the_up()
    elif motion == DOWN:
        x, y = head.to_the_down()

    for col in pg.sprite.groupcollide(heads, bushes, False, False).keys():
        sys.exit()

    for col in pg.sprite.groupcollide(heads, apples, False, True).keys():
        apple = Apple((randint(0, W)), (randint(0, H)), 'apple.png', apples)



    bushes.draw(sc)
    apples.draw(sc)
    bodes.draw(sc)
    # heads.draw(sc)

    pg.display.update()


    pg.time.delay(30)

