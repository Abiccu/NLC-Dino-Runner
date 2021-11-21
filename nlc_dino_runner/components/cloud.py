from nlc_dino_runner.utils.constants import SCREEN_WIDTH, CLOUD, SCREEN_HEIGHT
import random
from pygame.sprite import Sprite


class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
        self.rect.y = random.randint(100, 140)

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            self.rect.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.rect.y = random.randint(50, 90)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
