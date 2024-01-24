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

hit = 0
miss = 0

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Zombie Smash")
clock = pygame.time.Clock()

mouse_pos = (0, 0)
pygame.mouse.set_visible(False)

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
    ZOMBIE_HEIGHT = 50
    ZOMBIE_WIDTH = 50

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/zombie.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.creation_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.creation_time > 1500:
            all_sprites.remove()

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])


all_sprites = pygame.sprite.Group()

# game loop
running = True
while running:
    # quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                hammer_img = hammer[1]
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                hammer_img = hammer[0]
            
        mouse_pos = pygame.mouse.get_pos()
        hammer_rect.center = (mouse_pos[0], mouse_pos[1])
    # if pygame.time.get_ticks() % 1500 == 0:
    
    zombie = Zombie(335, 220)
    all_sprites.add(zombie)

    screen.blit(background_image, (0, 0))
    screen.blit(hammer_img, hammer_rect)
    
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
