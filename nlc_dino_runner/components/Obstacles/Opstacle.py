from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import SCREEN_WIDTH

class Obstacles(Sprite):

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rec.x -= 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)