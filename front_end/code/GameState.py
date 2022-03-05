import pygame as p
import entities.Player

class GameState():

    entities = []

    def __init__(self):
        p1 = entities.Player.Player()
        entities.append(p1)


    def draw(self):
        for entity in entities:
            entity.draw()



