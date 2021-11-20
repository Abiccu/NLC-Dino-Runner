
import random
from nlc_dino_runner.components.obstacles.obstacle import Obstacle
from nlc_dino_runner.utils.constants import BIRD


class Birds(Obstacle):

    def __init__(self, image):
        #self.image = BIRD[0]
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 240
        self.index = 0

    def draw(self,screen):
        if self.index >= 10:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1


