import pygame
# (fron)desde que carpetas debe importar las costantes
from nlc_dino_runner.utils.constants import (
    TITTLE,
    ICON,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BG,
    FPS,
    RUNNING,
    IMG_DIR,
    WHITE
)
from nlc_dino_runner.components.cloud import Cloud
from nlc_dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.utils import text_utils, text_utils_sound
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.playing = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x_pos_bg = 0
        self.y_pos_bg = 400
        self.game_speed = 15
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.player_heart_manager = PlayerHeartManager()
        self.cloud = Cloud()
        self.points = 0
        self.RUNING = True
        self.death_count = 0
        self.white = WHITE
        self.counter = 0

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1
        score_element, score_element_rec = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rec)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()



    def print_menu_elements(self):
        half_width = SCREEN_WIDTH // 2
        half_height = SCREEN_HEIGHT // 2
        if self.points >= 1:
            text_element, text_element_rec = text_utils.get_centared_message("Press any key to restart")
            self.screen.blit(text_element, text_element_rec)
            text_element, text_element_rec = text_utils.get_centared_message("Death Coundt :" + str(self.death_count),height=half_height + 50)
            self.screen.blit(text_element, text_element_rec)
        else:
            text_element, text_element_rec = text_utils.get_centared_message("Press any key to start")
            self.screen.blit(text_element, text_element_rec)
        self.screen.blit(ICON, (half_width - 40, half_height - 150))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()


    def run(self):
        self.points = 0
        self.obstacle.reset_obstacles()
        self.playing = True
        self.create_components()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        self.running = True
        text_utils_sound.sound_play('mixkit-ominous-drums-227.wav')
        while self.running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.cloud.update(self.game_speed)


    def draw(self):
        self.clock.tick(FPS)
        self.screen_update()
        self.screen.fill((self.white))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.score()
        self.cloud.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def screen_update(self):
        self.counter += 1
        if self.counter == 1000:
            self.white = (71, 71, 71)
        if self.counter == 2000:
            self.counter = 0
            self.white = (255, 255, 255)

    def draw_background(self):
        image_with = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_with:
            self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def create_components(self):
        self.obstacle.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)
        self.player_heart_manager.recet_hearts()