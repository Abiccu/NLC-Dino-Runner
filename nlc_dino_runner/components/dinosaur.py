import pygame

from nlc_dino_runner.components.powerups.hammers import Hammers
from nlc_dino_runner.utils import text_utils_sound
from nlc_dino_runner.utils.constants import RUNNING, JUMPING, SHIELD_TYPE, DEFAULT_TYPE, DUCKING_SHIELD, \
    RUNNING_SHIELD, DUCKING, RUNNING_SHIELD, FONT_STYLE, BLACK_COLOR, JUMPING_SHIELD, HAMMER_TYPE, RUNNING_HAMMER, \
    DUCKING_HAMMER, JUMPING_HAMMER
from pygame.sprite import Sprite


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 320
    Y_POS_DUCK = 360
    JUMP_VEL = 10


# step_index es un contador para saber cuando debemos cambiar de imagen

    def __init__(self):
        #self.image = RUNNING[0]
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE:DUCKING_HAMMER}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]

        self.shield = False
        self.shield_time_up = 0
        self.show_text = False

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
# son los etados en el que estara el dinisaur, nos ayudara a definir cuando agacharse, correr y saltar
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jum_vel = self.JUMP_VEL
        self.has_powerup = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0
        self.hammer = None
        self.hammer_enabled = 0
        #self.sound_jump = SOUND_JUMP


    def update(self, user_input):
#llamamos a los metodos adecuados en cada condicional
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

# user_imput[pygame.K_DOWN(flecha abajo)nos permite detectar la tecla precionada
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            text_utils_sound.sound_play('jump.wav')
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

        if self.hammer_enabled > 0 and user_input[pygame.K_SPACE]:
            self.hammer = Hammers(self.dino_rect.x + 100, self.dino_rect.y + 50)
            self.hammer_enabled = max(self.hammer_enabled - 1, 0)
            if self.hammer_enabled == 0:
                self.update_type_to_default(HAMMER_TYPE)
        if self.hammer:
            self.hammer.update()

    #mandamos screen como un parametro para poder hacer uso de el en draw

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        if self.hammer:
            self.hammer.draw(screen)

    def run(self):
        #self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    # step_index sirve para hacer que el dinosaurio cambie de disfraz continuamente

    def duck(self):
        #self.image = RUNNING[0] if self.step_index < 5 else DUCKING[1]
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        #self.image = JUMPING
        self.image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jum_vel * 4
            self.jum_vel -= 1
        if self.jum_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jum_vel = self.JUMP_VEL

    def check_invincibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                if self.show_text:
                    font = pygame.font.Font(FONT_STYLE, 15)
                    text = font.render(f'Shield enable for {time_to_show}', True, BLACK_COLOR)
                    text_rect = text.get_rect()
                    text_rect.center = (500, 50)
                    screen.blit(text, text_rect)
            else:
                self.shield = False
                self.update_type_to_default(SHIELD_TYPE)

    def update_type_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE