from front_end.code.entities.Creature import Creature


class Player(Creature):
    coins = 0

    def __init__(self, image_file):
        self.image = image_file
