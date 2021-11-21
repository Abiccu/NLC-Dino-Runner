import pygame
from nlc_dino_runner.utils.constants import IMG_DIR

def sound_play(name_sound):
    path = IMG_DIR + str("/") + name_sound
    background_sound = pygame.mixer.Sound(path)
    pygame.mixer.Sound.play(background_sound)