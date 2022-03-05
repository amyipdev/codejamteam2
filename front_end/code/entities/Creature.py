from front_end.code.entities.Entity import Entity


class Creature(Entity):
    health = 0
    xVel = 0
    yVel = 0

    def __init__(self, image_file):
        self.image = image_file

    def update(self):
        self.xPos = 10 * self.xVel
        self.yPos = 10 * self.yVel
