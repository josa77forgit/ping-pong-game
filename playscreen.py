import pygame as pg
from classes import GameSprite, Player, Ball, Text

pg.init()

class PlayScreen():
    ''' класс для создания и отрисовки объектов
    на главном окне. В дальнейшем планируется
    связь self.point1/2 с очками игроков при
    столкновении мяча с левой и правой стеной.
    '''
    def __init__(self, scene):
        self.scene = scene
        self.field = GameSprite('static/pictures/field.png', 50, 50, 0, 740, 500, None, self.scene)
        self.player1 = Player('static/pictures/rockett.png', 70, 350, 5, 40, 140, self.field.rect, self.scene)
        self.player2 = Player('static/pictures/rockett.png', 670, 350, 5, 40, 140, self.field.rect, self.scene)
        self.ball = Ball('static/pictures/bal.png', 350, 350, 50, 50, 3, 3, self.field.rect, self.scene)
        self.text = Text(100, 100, 24, (242, 56, 56), self.scene)
        self.point1 = 0
        self.point2 = 0
        self.max_p = 10

    def draw_all(self):
        self.field.draw()
        self.text.txt(f'{self.point1}:{self.point2}')
        self.text.draw_txt()
        self.player1.update2()
        self.player2.update()
        self.ball.go_ball(self.player1, self.player2)
        self.ball.draw()
        self.ball.collide_walls()
        self.ball.collide_left()
        self.ball.collide_right()
        if self.ball.collide_player(self.player1):
            self.point1 += 1
        if self.ball.collide_player(self.player2):
            self.point2 += 1