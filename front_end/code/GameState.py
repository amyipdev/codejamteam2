import pygame as p
import pygame.display
from front_end.code.entities.Player import Player


class GameState:
    entities_arr = []

    def __init__(self):
        p1 = Player()
        self.entities_arr.append(p1)
        pygame.display.set_caption("Mario!")

    def draw(self):
        for entity in self.entities_arr:
            entity.draw()
