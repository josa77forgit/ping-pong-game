import pygame as pg

pg.init()

class GameSprite(pg.sprite.Sprite):
    ''' класс для создания объектов
    '''
    def __init__(self, image, x, y, step, sizeV, sizeH, scene):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (sizeV, sizeH))
        self.mask = pg.mask.from_surface(self.image)
        self.step = step
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scene = scene

    def update(self):
        self.draw()

    def draw(self):
        self.scene.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    up = None
    down = None

    def go(self):
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_UP] and self.rect.y > self.scene.get_height:
            self.rect.y -= self.step
        if key_pressed[pg.K_DOWN] and self.rect.y < self.scene.get_height:
            self.rect.y += self.step

    def go2(self):
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_W] and self.rect.y > self.scene.get_height:
            self.rect.y -= self.step
        if key_pressed[pg.K_S] and self.rect.y < self.scene.get_height:
            self.rect.y += self.step

    def select_btn(self, up, down):
        self.up = up
        self.down = down

    def update(self):
        self.go()
        self.draw()

    def update2(self):
        self.go2()
        self.draw()

# key_pressed = pg.key.get_pressed()
# print(pg.K_UP)