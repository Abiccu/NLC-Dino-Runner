from nlc_dino_runner.utils.constants import HEART_COUNT
from nlc_dino_runner.components.player_hearts.player_hearts import Heart


class PlayerHeartManager:
    def __init__(self):
        self.heart_count = HEART_COUNT

    def reduce_heart(self):
        self.heart_count -= 1

    def draw(self, screen):
        x_position = 20
        y_position = 20
        for counter in range(self.heart_count):
            heart = Heart(x_position, y_position)
            heart.draw(screen)
            x_position += 30

    def recet_hearts(self):
        self.heart_count = HEART_COUNT