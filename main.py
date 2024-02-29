'''
Beach by Sakura Girl | https://soundcloud.com/sakuragirl_official
Music promoted by https://www.chosic.com/free-music/all/
Creative Commons CC BY 3.0
https://creativecommons.org/licenses/by/3.0/
'''

import pygame
from pygame.locals import *
import pygame.freetype
import random
import time
import sys
import math

# init game
pygame.init()
pygame.mixer.init()
# screen_info = pygame.display.Info()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

COL = 4
ROW = 4
FONT_SIZE = 30

hit = 0
miss = 0
bgm = pygame.mixer.Sound("music/sakura_girl.mp3")
hammer_click = pygame.mixer.Sound("music/punch.wav")
hammer_hit = pygame.mixer.Sound("music/punch2.wav")
bgm.set_volume(0.35)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Zombie Smash")
clock = pygame.time.Clock()

mouse_pos = (0, 0)
pygame.mouse.set_visible(False)
font = pygame.font.Font(None, FONT_SIZE)
bgm_channel = pygame.mixer.Channel(0)
hammer_click_channel = pygame.mixer.Channel(1)
hammer_hit_channel = pygame.mixer.Channel(2)
bgm_channel.set_volume(0.3)  # Adjust volume to 50%

bgm_channel.play(bgm ,loops = -1)

hammer_click_channel.set_volume(0.85)
hammer_hit_channel.set_volume(1)

background_image = pygame.image.load("img/bg.png").convert_alpha()
background_image = pygame.transform.scale(background_image, [SCREEN_WIDTH, SCREEN_HEIGHT])

hammer = []
for i in range(1, 3):
    img = pygame.image.load("img/hammer{}.png".format(i))
    img = pygame.transform.scale_by(img, 0.5)
    hammer.append(img)
hammer_img = hammer[0]
hammer_rect = hammer_img.get_rect()    

fi_img = pygame.image.load('img/zombie.png').convert_alpha()
fi_img = pygame.transform.scale_by(fi_img, 0.25)

se_img = pygame.image.load('img/zombie_after.png').convert_alpha()
se_img = pygame.transform.scale_by(se_img, 0.25)

class Zombie(pygame.sprite.Sprite):
    init_x = 0
    init_y = 0




    def __init__(self, x, y):
        super().__init__()
        self.image = fi_img

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.init_x = x
        self.init_y = y

        self.appear_time = random.randint(1000, 4000)
        self.disappear_time = 1500
        self.last_appear_time = pygame.time.get_ticks()

        #self.delay = 150
     #   self.get_hit = 0
    def get_clicked(self):
        current_time = pygame.time.get_ticks()
       # self.get_hit = current_time
        hammer_hit_channel.play(hammer_hit, loops = 0)
        self.image = se_img
      #  alpha = int(max(0, min(255, 255 - (255 / self.delay) * 150)))
       # self.image.set_alpha(alpha)
        #if current_time - self.get_hit >= self.delay:
            #self.rect.x = -1000
        self.last_appear_time = current_time
        #
     #   self.disappear_time = random.randint(1000, 1500)
           # self.image = fi_img




    def update(self):
        current_time = pygame.time.get_ticks()
        '''alpha = int((math.sin(self.appear_time / 1000.0) + 1) * 255) % 255
        print(alpha)
        self.image.set_alpha(alpha)'''
        if current_time - self.last_appear_time > self.appear_time:
            # Make sprite disappear
            self.rect.x = -1000  # Move sprite off-screen
           # self.image = fi_img
            if current_time - self.last_appear_time > self.appear_time + self.disappear_time:
                # Reset sprite position after disappear_time
                self.image.set_alpha(255)
                self.image = fi_img
                self.rect.x = self.init_x
                self.rect.y = self.init_y
                self.last_appear_time = current_time
                self.appear_time = random.randint(1000, 4000)
        '''else:
            # Make sprite appear
            self.rect.x = self.init_x  # Reset sprite position'''


all_sprites = pygame.sprite.Group()
zombie1 = Zombie(350, 210)
zombie2 = Zombie(490, 300)
zombie3 = Zombie(550, 420)
zombie4 = Zombie(265, 340)
zombie5 = Zombie(360, 500)
zombie6 = Zombie(175, 480)
zombie7 = Zombie(550, 600)
zombie8 = Zombie(240, 625)

all_sprites.add(zombie1)
all_sprites.add(zombie2)
all_sprites.add(zombie3)
all_sprites.add(zombie4)
all_sprites.add(zombie5)
all_sprites.add(zombie6)
all_sprites.add(zombie7)
all_sprites.add(zombie8)
# game loop
running = True
clock = pygame.time.Clock()

gameTimer = 60000

text = f"score: {hit} miss: {miss} time: {pygame.time.get_ticks()}"
while pygame.time.get_ticks() <= gameTimer:
    # quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            hammer_click_channel.play(hammer_click, loops=0)
            if event.button == 1:
                hammer_img = hammer[1]
                clicked_sprites = [sprite for sprite in all_sprites if sprite.rect.collidepoint(event.pos)]
                if not clicked_sprites:
                    miss +=1
                else:
                    for sprite in clicked_sprites:
                #        sprite.get_hit = pygame.time.get_ticks()
                        sprite.get_clicked()
                        hit += 1
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                hammer_img = hammer[0]
            
        mouse_pos = pygame.mouse.get_pos()
        hammer_rect.center = (mouse_pos[0], mouse_pos[1])
    # if pygame.time.get_ticks() % 1500 == 0:
    text = f"score: {hit} miss: {miss} time: {int(pygame.time.get_ticks()/1000)}"
    screen.blit(background_image, (0, 0))
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.x = 10
    text_rect.y = 10
    screen.blit(text_surface, text_rect)
    all_sprites.update()


    all_sprites.draw(screen)
    screen.blit(hammer_img, hammer_rect)

    pygame.display.flip()
    clock.tick(60)
pygame.mixer.music.stop()
pygame.quit()
