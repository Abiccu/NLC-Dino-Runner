import pygame
from nlc_dino_runner.components.game import Game
# si e nombre del modulo que esta corriendo es el main
#__mame__ nos da el nombre del modulo
if __name__ == "__main__":
    game = Game()
    game.execute()


