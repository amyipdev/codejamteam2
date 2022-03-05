import pygame as p
import Entities


class GameState:

    def __init__(self):
        print("hi")

    def draw(self, screen, entities):
        for entity in entities:
            screen.blit(entity.skin, p.Rect(entity.pos_x, entity.pos_y, entity.height, entity.width))
