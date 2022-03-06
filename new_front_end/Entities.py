import pygame as p
import Quantities as q, GameState


class Entity:
    skin = None
    pos_x = 0
    pos_y = 0
    vel_x = 0
    vel_y = 0
    height = 0
    width = 0

    def __init__(self, pos_x, pos_y, height, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width

    def update(self):
        return


class Player(Entity):
    skin = p.image.load("assets/mario.png")
    skin = p.transform.scale(skin, (q.SQ_SIZE, q.SQ_SIZE * 2))
    lives = 3
    coins = 0
    in_air = False

    def __init__(self, pos_x, pos_y, height, width, lives):
        super(Player, self).__init__(pos_x, pos_y, height, width)
        self.lives = lives

    def update(self):
        in_air = GameState.ground_col(self)

        if in_air or self.vel_y < 0:
            self.vel_y += q.GRAVITY / q.FPS
            self.pos_y += self.vel_y / q.FPS
        else:
            self.vel_y = 0
        if self.vel_x != 0:
            sign = (self.vel_x / abs(self.vel_x))
            self.vel_x = sign * min(q.MAX_X_SPEED, abs(self.vel_x + q.GROUND_FRICTION / q.FPS))
            self.pos_x += self.vel_x / q.FPS


class Tile(Entity):

    def __init__(self, tile_type):
        super(Tile, self).__init__()

        if tile_type == "ground":
            self.skin = p.image.load("assets/ground_tile.png")
        elif tile_type == "ground":
            self.skin = p.image.load("assets/mario.png")

        self.skin = p.transform.scale(self.skin, (q.SQ_SIZE, q.SQ_SIZE))


class Enemy(Entity):

    def __init__(self, pos_x, pos_y, height, width):
        super(Enemy, self).__init__()


