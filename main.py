import pygame as pg
from playscreen import PlayScreen

pg.init()

clock = pg.time.Clock()
FPS = 60

window = pg.display.set_mode((840, 680))
window.fill((255, 158, 39))

play = PlayScreen(window)

game = True

while game:
    clock.tick(FPS)
    window.fill((255, 158, 39))
    play.draw_all()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
    pg.display.update()