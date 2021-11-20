
from nlc_dino_runner.utils.constants import SMALL_CACTUS
from nlc_dino_runner.components.obstacles.obstacle import Obstacle
import random


class Cactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0, 2)
    # super() se ace referencia al metodo y atributos de su clase padre
        super().__init__(image, self.type)
        self.rect.y = 350

