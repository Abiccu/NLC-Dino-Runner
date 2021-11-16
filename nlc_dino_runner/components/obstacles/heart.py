from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART
X_POS = 20
Y_POS = 30


class Heart(Sprite):

    def __init__(self):
        self.image = HEART
        self.list_hearts = [self.image, self.image, self.image, self.image, self.image]
        self.heart_rect = self.image.get_rect()
        self.heart_rect.x = 20
        self.heart_rect.y = 20

    def update(self):
        pass

    def draw(self, screen):
        for heart in self.list_hearts:
            heart.screen.blit(self.image(self.heart_rect.x, self.heart_rect.y))