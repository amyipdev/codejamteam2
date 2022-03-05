import pygame as p


class Entity:
    xPos = 0
    yPos = 0
    image = None

    def __init__(self, image_file):
        print("hi")
        self.image = image_file

    def draw(self, screen):
        screen.blit(self.image, p.Rect(100, 200, 100, 200))
