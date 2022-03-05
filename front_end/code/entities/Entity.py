import pygame as p


class Entity:
    xPos = 100
    yPos = 100
    image = None

    def __init__(self, image_file):
        print("hi")
        self.image = image_file

    def draw(self, screen):
        screen.blit(self.image, p.Rect(self.xPos, self.yPos, self.xPos, self.yPos))

    def update(self):
        print("hi")
