import pygame
from pygame.locals import *
import pygame.freetype
import random
import time
import math

# init game
pygame.init()
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

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Zombie Smash")
clock = pygame.time.Clock()

mouse_pos = (0, 0)
pygame.mouse.set_visible(False)
font = pygame.font.Font(None, FONT_SIZE)


background_image = pygame.image.load("img/bg.png").convert_alpha()
background_image = pygame.transform.scale(background_image, [SCREEN_WIDTH, SCREEN_HEIGHT])

hammer = []
for i in range(1, 3):
    img = pygame.image.load("img/hammer{}.png".format(i))
    img = pygame.transform.scale_by(img, 0.5)
    hammer.append(img)
hammer_img = hammer[0]
hammer_rect = hammer_img.get_rect()    



class Zombie(pygame.sprite.Sprite):
    init_x = 0
    init_y = 0
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/zombie.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.init_x = x
        self.init_y = y

        self.appear_time = random.randint(1000, 4000)
        self.disappear_time = random.randint(1000, 4000)
        self.last_appear_time = pygame.time.get_ticks()


    def get_clicked(self):
        self.rect.x = -1000
        current_time = pygame.time.get_ticks()
        self.last_appear_time = current_time
        self.disappear_time = random.randint(1000, 1500)
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_appear_time > self.appear_time:
            # Make sprite disappear
            self.rect.x = -1000  # Move sprite off-screen
            if current_time - self.last_appear_time > self.appear_time + self.disappear_time:
                # Reset sprite position after disappear_time
                self.rect.x = self.init_x
                self.rect.y = self.init_y
                self.last_appear_time = current_time
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

text = f"score: {hit} miss: {miss}"
while running:
    # quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                hammer_img = hammer[1]
                clicked_sprites = [sprite for sprite in all_sprites if sprite.rect.collidepoint(event.pos)]
                if not clicked_sprites:
                    miss +=1
                else:
                    for sprite in clicked_sprites:
                        sprite.get_clicked()
                        hit += 1
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                hammer_img = hammer[0]
            
        mouse_pos = pygame.mouse.get_pos()
        hammer_rect.center = (mouse_pos[0], mouse_pos[1])
    # if pygame.time.get_ticks() % 1500 == 0:
    text = f"score: {hit} miss: {miss}"
    screen.blit(background_image, (0, 0))
    screen.blit(hammer_img, hammer_rect)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.x = 10
    text_rect.y = 10
    screen.blit(text_surface, text_rect)
    all_sprites.update()


    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
print(hit)
pygame.quit()
