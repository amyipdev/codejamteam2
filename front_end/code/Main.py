import pygame as p
import GameState

WINDOW_WIDTH = 960 #1280
WINDOW_HEIGHT = 600 #800
WIDTH = HEIGHT = 600
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION
FPS = 30

def main():
    p.init()
    screen = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(p.Color("white"))
    p.display.set_caption("Mario Race")
    clock = p.time.Clock()
    gs = GameState.GameState()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        gs.draw(screen)
        clock.tick(FPS)
        p.display.flip()

main()