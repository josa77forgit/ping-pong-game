import pygame as pg

pg.init()

class GameSprite(pg.sprite.Sprite):
    ''' класс для создания объектов фывапролд
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
        self.scene.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    up = None
    down = None

    def go(self):
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_UP] and self.rect.y > self.scene_size.top:
            self.rect.y -= self.step
        if key_pressed[pg.K_DOWN] and self.rect.y < self.scene_size.bottom-self.rect.height:
            self.rect.y += self.step

    def go2(self):
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_w] and self.rect.y > self.scene_size.top:
            self.rect.y -= self.step
        if key_pressed[pg.K_s] and self.rect.y < self.scene_size.bottom-self.rect.height:
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


class Ball(GameSprite):
    def __init__(self, image, x, y, sizeV, sizeH, step_x, step_y, scene_size, scene, step=None):
        super().__init__(image, x, y, step, sizeV, sizeH, scene_size, scene)
        self.step_x = 1
        self.step_y = 1
        self.ball_group = pg.sprite.Group()
        self.ball_group.add(self)

    def go_ball(self, player):
        for i in range(1):
            self.collide_player(player)
            self.rect.x += self.step_x
            self.rect.y += self.step_y

    def collide_walls(self):
        if self.rect.y > self.scene_size.bottom-self.rect.height*1.4:
            self.step_y *= -1
        if self.rect.y < self.scene_size.top+self.rect.height/2:
            self.step_y *= -1

    def collide_right(self):
        if self.rect.x > self.scene.get_width()-self.rect.width:
            return True

    def collide_left(self):
        if self.rect.x < 0:
            return True

    def collide_player(self, player):
        if pg.sprite.spritecollide(player, self.ball_group, False, pg.sprite.collide_mask):
            self.step_x *= -1
            self.rect.x += self.step_x*100
