from nlc_dino_runner.components.obstacles.obstacle import Obstacle
import random


class LargeCactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 320
