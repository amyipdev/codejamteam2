import pygame as p
import pygame.font

import GameState, Entities
import Quantities as q

import requests as r

local_player = Entities.Player(100, 100, 100, 100, 3)


def initialize():
    q.ENTITIES.append(local_player)


def main():
    initialize()
    p.init()
    screen = p.display.set_mode((q.WINDOW_WIDTH, q.WINDOW_HEIGHT))
    p.display.set_caption("Mario!")
    clock = p.time.Clock()
    gs = GameState.GameState()
    intro = True
    running = True
    bstr = ""
    font = pygame.font.SysFont(None, 48)
    imgb = font.render("Game data in form ip:port:gameid", True, (0x0, 0x0, 0x0))
    rectb = imgb.get_rect()
    imgc = font.render("0000 for new game", True, (0x0,0x0,0x0))
    rectc = imgc.get_rect()
    rectb.topleft = (20, 20)
    rectc.topleft = (20, 60)
    while intro:
        screen.fill(p.Color("white"))
        img = font.render(bstr, True, (0x0, 0x0, 0x0))
        rect = img.get_rect()
        rect.topleft = (20, 100)
        cursor = p.Rect(rect.topright, (3, rect.height))
        rect.size = img.get_size()
        cursor.topleft = rect.topright

        for e in p.event.get():
            if e.type == p.QUIT: running = intro = False
            elif e.type == p.KEYDOWN:
                if e.key == p.K_BACKSPACE:
                    if len(bstr)>0:
                        bstr = bstr[:-1]
                elif e.key == p.K_RETURN:
                    intro = False
                    print(bstr)
                else:
                    bstr += e.unicode
        clock.tick(q.FPS)
        screen.blit(imgb, rectb)
        screen.blit(imgc, rectc)
        screen.blit(img, rect)
        p.display.flip()

    while running:
        screen.fill((0x89, 0xcf, 0xf0))

        for e in p.event.get():
            if e.type == p.QUIT: running = False
            elif (e.type == p.KEYDOWN):
                if (e.key == p.K_UP and (not GameState.ground_col(local_player))):
                    local_player.vel_y -= q.DELTA_Y_VELOCITY
    #            elif (e.key == p.K_DOWN):
    #                if GameState.ground_col(local_player.pos_y):
    #                    local_player.pos_y = local_player.pos_y + q.DELTA_Y
                elif (e.key == p.K_RIGHT):
                    local_player.vel_x += q.DELTA_X_VELOCITY
                elif (e.key == p.K_LEFT):
                    local_player.vel_x -= q.DELTA_X_VELOCITY

        gs.update(q.ENTITIES)
        gs.draw(screen, q.ENTITIES)
        clock.tick(q.FPS)
        p.display.flip()



#def load_images():
#    IMAGES.append(p.transform.scale(Entities, (SQ_SIZE, SQ_SIZE)))

main()