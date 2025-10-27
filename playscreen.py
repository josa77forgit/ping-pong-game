import pygame as pg
from classes import GameSprite, Player, Ball

pg.init()

class PlayScreen():
    def __init__(self, scene):
        self.scene = scene
        self.player1 = Player('static/pictures/rocket.png', 100, 350, 5, 100, 200, self.scene)
        self.player2 = Player('static/pictures/rocket.png', 700, 350, 5, 100, 200, self.scene)
        self.ball = Ball('static/pictures/ball.png', 350, 350, 50, 50, 3, 3, self.scene)
        self.field = GameSprite('static/pictures/field.png', 50, 50, 0, 740, 500, self.scene)
        self.point1 = 0
        self.point2 = 0
        self.max_p = 10

    def draw_all(self):
        self.field.draw()
        self.player1.update()
        self.player2.update2()
        self.ball.draw()
        self.ball.go_ball()
        self.ball.collide_walls()
        self.ball.collide_left()
        self.ball.collide_right()
        if self.ball.collide_player(self.player1):
            self.point1 += 1
        if self.ball.collide_player(self.player2):
            self.point2 += 1