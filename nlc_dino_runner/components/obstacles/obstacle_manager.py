from nlc_dino_runner.components.obstacles.cactus import Cactus
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
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(Birds(BIRD))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                if not game.player.shield:
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000

                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
        #for obstacle in self.obstacles:
            #obstacle.update(self.obstacles)
            #if game.player.dino_rect.colliderect(obstacle.rect):
                #if game.player.shield:
                    #self.obstacles.remove(obstacle)
                #else:
                    #pygame.time.delay(500)
                    #game.playing = False
                    #game.death_count += 1
                    #break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            obstacle.update(self.obstacles)


    def reset_obstacles(self):
        self.obstacles = []

