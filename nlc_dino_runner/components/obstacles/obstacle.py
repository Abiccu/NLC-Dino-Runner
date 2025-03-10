from nlc_dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite


class Obstacle(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width and obstacles:
            obstacles.pop()
        if self.index >= 10:
            self.index = 0

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)


