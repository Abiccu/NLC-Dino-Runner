import random
from nlc_dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):

    def __init__(self):
        self.index = random.randint(0, 1)
        super().__init__(self.image, self.index)
        self.rect.y = 250