import pygame as p
import GameState, Entities

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 600
WIDTH = HEIGHT = 600
DIMENSION = 16
SQ_SIZE = HEIGHT / DIMENSION
FPS = 30
ENTITIES = []
DELTA_X = 10
DELTA_Y = 10

local_player = Entities.Player(100, 100, 100, 100, 3)


def initialize():
    ENTITIES.append(local_player)


def main():
    initialize()
    p.init()
    screen = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    p.display.set_caption("Mario!")
    clock = p.time.Clock()
    gs = GameState.GameState()
    running = True
    while running:
        screen.fill(p.Color("white"))

        for e in p.event.get():
            if e.type == p.QUIT: running = False
            elif (e.type == p.KEYDOWN):
                if (e.key == p.K_UP): local_player.pos_y = local_player.pos_y - DELTA_Y
                elif (e.key == p.K_DOWN): local_player.pos_y = local_player.pos_y + DELTA_Y
                elif (e.key == p.K_RIGHT): local_player.pos_x = local_player.pos_x + DELTA_X
                elif (e.key == p.K_LEFT): local_player.pos_x = local_player.pos_x - DELTA_X

        gs.draw(screen, ENTITIES)
        clock.tick(FPS)
        p.display.flip()



#def load_images():
#    IMAGES.append(p.transform.scale(Entities, (SQ_SIZE, SQ_SIZE)))

main()