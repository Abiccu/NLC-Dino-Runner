from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS
from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.utils.constants import BIRD
import pygame


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        elif len(self.obstacles) == 2
            self.obstacles.append(Birt(BIRD)

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.menu_final()
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

