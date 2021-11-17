from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART
import pygame


class Heart(Sprite):

    def __init__(self):
        self.image = HEART
        self.list_hearts = pygame.sprite.Group()
        self.list_hearts = [self.image, self.image, self.image, self.image, self.image]
        #self.heart_rect = self.image.get_rect()
        self.heart_rect.x = 20
        self.heart_rect.y = 20

    def update(self):
        pass

    def draw(self, sprite):
        #for i in range(8):
            self.list_hearts.add()

