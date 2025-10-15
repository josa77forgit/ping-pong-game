import pygame as pg
from classes import GameSprite, Player

pg.init()

class PlayScreen():
    def __init__(self, scene):
        player1 = Player(None, 150, 150, 5, 50, 50, scene)
        player2 = Player(None, 400, 150, 5, 50, 50, scene)
        