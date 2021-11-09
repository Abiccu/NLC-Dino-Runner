import pygame
# (fron)desde que carpetas debe importar las costantes
from nlc_dino_runner.utils.constants import (
    TITTLE,
    ICON,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BG,
    FPS
)
from nlc_dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        #llamamos a pygame y a su metodo init para inicializar y cuando llamaemos recien se va mostrar
        #pygame.display.set_caption es un metodo que ya tiene pygame para configurar el titulo de la ventana
        pygame.init()
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.playing = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # pygame.display.set_mode llamamos un metodo de pygame que recibe el tamaño de la ventana
        #set_icon recibe una superficie como parametro
        self.x_pos_bg = 0
        self.y_pos_bg = 400
        self.game_speed = 20
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle = ObstacleManager()
# (run) va a ejecutar todos los metodos que le pongamos
    def run(self):
        #cambiamos a True para que comiense a correr el juego
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
# pygame.quit() para terminar el siclo
    def events(self):
        for event in pygame.event.get():
            #QUIT event.type es lo que se va precionar y compara se sera igual a QUIT que es el icono para cerrar la ventana
            if event.type == pygame.QUIT:
                self.playing = False
        # para capturar todos los eventos es mejor crear un ciclo
        # pygame.even.get es una lista de eventos y con for estamos iterando todos esos eventos

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle.update(self)

    def draw(self):
        self.clock.tick(29)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
#pygame.display.flill el metodo flill de pygame nos sirve para llenar la superficie con un color entero(recibe una dupla)
# flip , actualiza loque se configure y se muestra en la pantalla
    # update tambien muestra en la pantalla pero selo recibe siertas partes de nuestra pantalla
    def draw_background(self):
        image_with = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_with:
            self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        # el metodo blit nos ayuda a dibujar una superficie sobre otra sperficie
        # self.screen es a pantalla y la vamos actualizando es un objeto a las que vamos agragando mas cosas