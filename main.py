import pygame as pg 

pg.init()

clock = pg.time.Clock()
FPS = 40

window = pg.display.set_mode((840, 680))
window.fill((168, 224, 224))



game = True

while game:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
    pg.display.update()