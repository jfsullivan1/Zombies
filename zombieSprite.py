#Class for zombie enemy (Written by John Sullivan)

import pygame
import math
import random

screen = pygame.display.set_mode((1600, 820))

#Zombie ONE code
class ZombieOne(pygame.sprite.Sprite):
    def __init__(self, car):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/z1D.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.speed = 5

        self.reset()

    def update(self, player):
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        self.rect.x -= dx * self.speed
        self.rect.y -= dy * self.speed

        #left
        if dx > 0 and dy < dx:
            self.image = pygame.image.load("Sprites/z1L.png")
            self.image = self.image.convert()
            self.image = pygame.transform.scale(self.image, (80, 80))
        #right
        if dx < 0 and dy > dx:
            self.image = pygame.image.load("Sprites/z1R.png")
            self.image = self.image.convert()
            self.image = pygame.transform.scale(self.image, (80, 80))

        #up
        if dx < .02 and dx > -.02 and dy > 0:
            self.image = pygame.image.load("Sprites/z1U.png")
            self.image = self.image.convert()
            self.image = pygame.transform.scale(self.image, (80, 80))

        #down
        if dx < .02 and dx > -.02 and dy < 0:
            self.image = pygame.image.load("Sprites/z1D.png")
            self.image = self.image.convert()
            self.image = pygame.transform.scale(self.image, (80, 80))


    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
    
