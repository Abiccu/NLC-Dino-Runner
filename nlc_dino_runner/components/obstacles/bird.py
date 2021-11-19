
import random
from nlc_dino_runner.components.obstacles.obstacle import Obstacle
from nlc_dino_runner.utils.constants import BIRD


class Birds(Obstacle):

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.index)
        self.rect.y = 250
        self.index = 0

    def draw(self,screen):
        if self.index >= 5:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)



#class Bird(Obstacle):

    #def __init__(self):
        #self.index = random.randint(0, 1)
        #super().__init__(self.image, self.index)
        #self.rect.y = 250
        #velocidad aleatoria
#self.speedy = random.randrange(1, 10