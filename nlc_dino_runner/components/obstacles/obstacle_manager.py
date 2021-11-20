from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS
from nlc_dino_runner.components.obstacles.bird import Birds
from nlc_dino_runner.utils.constants import BIRD
import random

import pygame


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.random = random.randint(1,2)

    def update(self, game):
        if len(self.obstacles) == 0:
            if self.random == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Birds(BIRD))

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

    def reset_obstacles(self):
        self.obstacles = []

