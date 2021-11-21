from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils import text_utils_sound
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from nlc_dino_runner.components.obstacles.bird import Birds
from nlc_dino_runner.utils.constants import BIRD
from nlc_dino_runner.components.obstacles.large_cactus import LargeCactus
import random

import pygame


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.num = random.randint(0, 2)
            if self.num == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.num == 1:
                self.obstacles.append(Birds(BIRD))
            elif self.num == 2:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.hammer is not None and game.player.hammer.rect.colliderect(obstacle.rect):
                game.player.hammer.kill()
                self.obstacles.pop()
            else:
                obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000
                    else:
                        self.obstacles.remove(obstacle)
                        pygame.time.delay(500)
                        game.playing = False
                        text_utils_sound.sound_play('mixkit-arcade-retro-changing-tab-206.wav')
                        break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

