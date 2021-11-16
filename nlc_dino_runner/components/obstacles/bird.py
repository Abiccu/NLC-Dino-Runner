import random
from nlc_dino_runner.components.obstacles.obstacle import Obstacle
from nlc_dino_runner.utils.constants import BIRD


class Birds(Obstacle):

    def __init__(self, image):
        self.index = random.randint(0, 1)
        super().__init__(image, self.index)
        self.rect.y = 250