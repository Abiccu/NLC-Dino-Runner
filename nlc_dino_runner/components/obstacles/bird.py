
import random
from nlc_dino_runner.components.obstacles.obstacle import Obstacle
from nlc_dino_runner.utils.constants import BIRD


class Birds(Obstacle):

    def __init__(self, image):
        self.image = BIRD[0]
        self.type = 0
        self.index = 0
        super().__init__(image, self.index)
        self.rect.y = 240
        self.index = 0

    def draw(self,screen):
        if self.index >= 5:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)

    def run(self, image):
        # self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        while self.index < 0:
            self.image = BIRD[0] if self.index < 5 else BIRD[1]
            super().__init__(image, self.index)
            self.rect.y = 240
            self.index = 0
            self.index += 1

#class Bird(Obstacle):LO BORE [self.type][self.step_index // 5]

    #def __init__(self):
        #self.index = random.randint(0, 1)
        #super().__init__(self.image, self.index)
        #self.rect.y = 250
        #velocidad aleatoria
#self.speedy = random.randrange(1, 10