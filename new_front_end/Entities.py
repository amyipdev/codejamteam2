import pygame as p


class Entity:
    skin = None
    pos_x = 0
    pos_y = 0
    height = 0
    width = 0

    def __init__(self, pos_x, pos_y, height, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width


class Player(Entity):
    skin = p.image.load("assets/sprite sheet.png")
    skin = p.transform.scale(skin, (skin.get_width() / 2, skin.get_height() / 2))
    lives = 3
    coins = 0

    def __init__(self, pos_x, pos_y, height, width, lives):
        super().__init__(pos_x, pos_y, height, width)
        self.lives = lives


class Tile(Entity):
    skin = p.image.load("assets/")
