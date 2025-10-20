import pygame as pg
from classes import GameSprite, Player, Ball

pg.init()

class PlayScreen():
    def __init__(self, scene):
        self.player1 = Player(None, 150, 150, 5, 50, 50, self.scene)
        self.player2 = Player(None, 400, 150, 5, 50, 50, self.scene)
        self.ball = Ball(None, 350, 350, 50, 50, 3, 3, self.scene)
        self.scene = scene
        self.point1 = 0
        self.point2 = 0
        self.max_p = 10

    def draw_all(self):
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