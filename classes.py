import pygame as pg
from random import random

pg.init()

class GameSprite(pg.sprite.Sprite):
    ''' класс для создания и расположения объектов.
    создаем маски.
    '''
    def __init__(self, image, x, y, step, sizeV, sizeH, scene_size, scene):
        super().__init__()
        self.image = pg.transform.smoothscale(pg.image.load(image).convert_alpha(), (sizeV, sizeH))
        self.mask = pg.mask.from_surface(self.image)
        self.step = step
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scene = scene
        self.scene_size = scene_size

    def update(self):
        self.draw()

    def draw(self):
        ''' отрисовка объектов класса
        '''
        self.scene.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    ''' класс для создания двух ракеток-игроков. 
    Наследуется от GameSprite, тоесть уже
    имеет созданный объект.
    '''
    up = None
    down = None

    def go(self):
        ''' передвижение вниз-вверх 1-ой ракетки
        '''
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_UP] and self.rect.y > self.scene_size.top:
            self.rect.y -= self.step
        if key_pressed[pg.K_DOWN] and self.rect.y < self.scene_size.bottom-self.rect.height:
            self.rect.y += self.step

    def go2(self):
        ''' передвижение вниз-вверх 2-ой ракетки
        '''
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_w] and self.rect.y > self.scene_size.top:
            self.rect.y -= self.step
        if key_pressed[pg.K_s] and self.rect.y < self.scene_size.bottom-self.rect.height:
            self.rect.y += self.step

    def select_btn(self, up, down):
        self.up = up
        self.down = down

    def update(self):
        ''' отрисовка и движение первой ракетки
        '''
        self.go()
        self.draw()

    def update2(self):
        ''' отрисовка и движение второй ракетки
        '''
        self.go2()
        self.draw()

# key_pressed = pg.key.get_pressed()
# print(pg.K_UP)


class Ball(GameSprite):
    ''' класс для создания мяча. Наследуется от GameSprite,
    уже имеет созданный объект.
    '''
    def __init__(self, image, x, y, sizeV, sizeH, step_x, step_y, scene_size, scene, step=None):
        super().__init__(image, x, y, step, sizeV, sizeH, scene_size, scene)
        self.step_x = 1
        self.step_y = 1
        self.x = x
        self.y = y
        self.ball_group = pg.sprite.Group()
        self.ball_group.add(self)

    def go_ball(self, player, player2):
        ''' отвечает за передвижение мяча.
        Для оптимизации передвижения добавлен цикл
        for, помогает передвигать мяч на 1 пиксель
        с нормальной скоростью.
        '''
        for i in range(3):
            self.collide_player(player)
            self.collide_player(player2)
            self.rect.x += self.step_x
            self.rect.y += self.step_y

    def collide_walls(self):
        ''' отвечает за отскакивание мяча от нижней
        и верхней стенки поля.
        '''
        if self.rect.y > self.scene_size.bottom-self.rect.height*1.4:
            self.step_y *= -1
        if self.rect.y < self.scene_size.top+self.rect.height/2:
            self.step_y *= -1

    def collide_right(self):
        ''' возвращает True
        в случае столкновения мяча с правой стеной окна.
        '''
        if self.rect.x > self.scene.get_width()-self.rect.width:
            self.x = 350
            self.y = 350
            return True

    def collide_left(self):
        ''' возвращает True
        в случае столкновения мяча с левой стеной окна.
        '''
        if self.rect.x < 0:
            self.x = 350
            self.y = 350
            return True

    def collide_player(self, player):
        ''' отвечает за отскок мяча от ракеток.
        '''
        if pg.sprite.spritecollide(player, self.ball_group, False, pg.sprite.collide_mask):
            self.step_x *= -1
            self.rect.x += self.step_x*20
            # self.step_x = 1 + random()
            # self.step_y = 1 + random()
        # if pg.sprite.collide_rect(self, player):
        #     self.step_x *= -1

class Text():
    ''' класс для создания и отрисовки текста засчёт модуля font.
    '''
    def __init__(self, x, y, size, color, scene):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.scene = scene

    def txt(self, text):
        self.text = pg.font.Font(None, self.size).render(text, True, self.color)

    def draw_txt(self):
        self.scene.blit(self.text, (self.x, self.y))