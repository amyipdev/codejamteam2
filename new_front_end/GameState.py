import pygame as p
import Entities, Quantities as q


class GameState:
    ground = []
    t_ground = p.transform.scale(p.image.load("assets/ground_tile.png"), (q.SQ_SIZE, q.SQ_SIZE))
    ip = ""
    port = 0
    room = ""
    pid = -1

    def __init__(self):
        for n in range(q.DIMENSION): self.ground.append([0 for n in range(q.DIMENSION - 3)] + [1 for n in range(3)])
        print(self.ground)

    def draw(self, screen, entities):
        self.draw_map(screen)
        for entity in entities:
            screen.blit(entity.skin, p.Rect(entity.pos_x, entity.pos_y, entity.height, entity.width))

    def draw_map(self, screen):
        for x in range(q.DIMENSION):
            for y in range(q.DIMENSION):
                if self.ground[x][y] != 0:
                    screen.blit(self.t_ground, p.Rect(q.SQ_SIZE * x - x, q.SQ_SIZE * y, q.SQ_SIZE, q.SQ_SIZE))

    def update(self, entities):
        for n in range(len(entities)):
            entity = entities[n]
            entity.update()


def ground_col(entity) -> bool:
    return not entity.pos_y > q.WINDOW_HEIGHT - q.SQ_SIZE * 2.65 - entity.height
