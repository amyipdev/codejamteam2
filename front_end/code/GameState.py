import pygame as p
import pygame.display
import imageio as iio

from front_end.code.entities.Player import Player


class GameState:
    entities_arr = []

    def __init__(self):
        p1 = Player(p.image.load("assets/sprite sheet.png"))
        self.entities_arr.append(p1)
        pygame.display.set_caption("Mario!")

    def key_input(self):
        for e in p.event.get():
            if e.type == p.KEYUP:
                for entity in self.entities_arr:
                    if isinstance(entity, Player):
                        entity.yPos = entity.yPos + 50
            if e.type == p.KEYDOWN:
                for entity in self.entities_arr:
                    if isinstance(entity, Player):
                        entity.yPos = entity.yPos - 50

    #            if e.type == p.QUIT:
    #                running = False

    def update(self, screen):
        for entity in self.entities_arr:
            entity.update()
            entity.draw(screen)
