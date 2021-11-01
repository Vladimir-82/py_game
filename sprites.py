'''
В модуле pygame.sprite есть ряд функций для проверки коллизий спрайтов.
Одна из них spritecollideany() проверяет, столкнулся ли конкретный спрайт с любым из спрайтов из группы.
Функция принимает первым аргументом спрайт, чья коллизия проверяется, вторым – группу.

Измените программу выше так, чтобы машинки появлялись чаще. Добавьте спрайт, который "едет"
навстречу всем другим и управляется стрелками влево и вправо на клавиатуре.
Цель игры – не допустить столкновения. Если оно происходит, то программа завершается.
'''
from random import randint
import pygame as pg
import sys
import time

pg.init()
pg.time.set_timer(pg.USEREVENT, 500)

RIGHT = "to the right"
LEFT = "to the left"
UP = "to the up"
DOWN = "to the down"
STOP = "stop"

motion = None
W = 500
H = 639
W_, H_ = 1100, 659
WHITE = (255, 255, 255)
MAIN_FONT = (100, 150, 200)


CARS = ('car1.png', 'car2.png', 'car3.png')


# для хранения готовых машин-поверхностей
CARS_SURF = []

# надо установить видео режим
# до вызова image.load()
sc_main = pg.display.set_mode((W_, H_))
sc = pg.Surface((W, H))
sc_main.fill(MAIN_FONT)

info_font = pg.font.Font('font/font.ttf', 50)
font_name = pg.font.Font('font/font.ttf', 80)
text_name = font_name.render('ТАЧКИ', True, (255, 0, 0))
place = text_name.get_rect(center=(850, 60))

score_show = info_font.render("SCORE", True, pg.Color('darkorange'))
score_place = score_show.get_rect(center=(850, 200))
title_record = info_font.render("Record", True, pg.Color('gold'))
record_place = title_record.get_rect(center=(850, 400))

main_font = pg.font.Font('font/font.ttf', 80)
game_over = main_font.render("GAME OVER", True, pg.Color('green'))
game_over_place = game_over.get_rect(center=(W_//2, H_//2))

bg = pg.image.load('FONT.jpg').convert_alpha()
score = 0



def get_record():
    try:
        with open('record_cars') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_cars', 'w') as f:
            f.write('0')


def set_record(record, score):
    rec = max(int(record), score)
    with open('record_cars', 'w') as f:
        f.write(str(rec))

for i in range(len(CARS)):
    CARS_SURF.append(
        pg.image.load(CARS[i]).convert_alpha())


class Car(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(
            center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = randint(1, 3)

    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()
            global score
            score += 10

class My_Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=(x, H - self.image.get_height()//2))


    def movie(self, motion):
        if motion == LEFT:
            self.rect.x -= 3
        elif motion == RIGHT:
            self.rect.x += 3
        elif motion == UP:
            self.rect.y -= 3
        elif motion == DOWN:
            self.rect.y += 3
        if self.rect.x <= 0: #ограничения
            self.rect.x = 0
        if self.rect.x >= W - self.rect.width: #ограничения
            self.rect.x = W - self.rect.width
        if self.rect.y >= H - self.rect.height: #ограничения
            self.rect.y = H - self.rect.height
        if self.rect.y <= 0: #ограничения
            self.rect.y = 0

    def boom(self):
        pg.draw.circle(sc_main, pg.Color('red'), (self.rect.x + self.rect.width, self.rect.y + self.rect.width//2), self.rect.width//3)


cars = pg.sprite.Group()
my_car = My_Car(W//2, 'car.jpg')

# добавляем первую машину,
# которая появляется сразу
# Car(randint(60, W//2), CARS_SURF[randint(0, 2)], cars) #разобраться с этой строкой

while 1:
    record = get_record()
    sc_main.blit(bg, (0, 0))
    sc_main.blit(text_name, place)
    sc_main.blit(sc, (20, 20))
    sc_main.blit(score_show, score_place)
    sc_main.blit(title_record, record_place)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Car(randint(15, W - 15),
                CARS_SURF[randint(0, 2)], cars)

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

    sc.fill(WHITE)

    sc.blit(my_car.image, my_car.rect) #тут должна быть моя машинка
    cars.draw(sc)

    if pg.sprite.spritecollideany(my_car, cars):
        my_car.boom()
        sc_main.blit(game_over, game_over_place)
        pg.display.flip()
        time.sleep(2)
        set_record(record, score)
        break

    sc_main.blit(info_font.render(str(score), True, pg.Color('red')), (840, 250))
    sc_main.blit(info_font.render(str(record), True, pg.Color('gold')), (840, 450))

    pg.display.update()



    pg.time.delay(20)

    cars.update()
    my_car.movie(motion)