import pygame as pg
import sys


pg.init()
size = 750, 750
screen = pg.display.set_mode(size)


def draw_background():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
        
    
def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    draw_background()
    pg.display.flip()
    

while True:
    game_loop()
