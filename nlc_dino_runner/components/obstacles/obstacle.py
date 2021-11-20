from nlc_dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite


class Obstacle(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.index = 0

    def update(self, obstacles):
        self.rect.x -= 20
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        if self.index >= 10:
            self.index = 0

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

    # def __init__(self, image, index):
    # self.image = image
    # self.index = index
    # self.rect = self.image[self.index].get_rect()
    # self.rect.x = SCREEN_WIDTH

    # def update(self, obstacles):
    # self.rect.x -= 20
    # if self.rect.x < -self.rect.width:
    # obstacles.pop()
    # pop se usa para sacar de  nuestra lista

    # def draw(self, screen):
    # screen.blit(self.image[self.index], self.rect)
