#Class for zombie enemy (Written by John Sullivan)

import pygame
import math
import random

screen = pygame.display.set_mode((1400, 750))

#Zombie ONE code
class ZombieOne(pygame.sprite.Sprite):
    def __init__(self, car, speed, obstacle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/z1D.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.left = pygame.image.load("Sprites/z1L.png")
        self.right = pygame.image.load("Sprites/z1R.png")
        self.up = pygame.image.load("Sprites/z1U.png")
        self.down = pygame.image.load("Sprites/z1D.png")
        
        self.reset()

    def update(self, player):
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        self.rect.x -= dx * self.speed
        self.rect.y -= dy * self.speed

        #left
        if dx > 0 and dy < dx:
            self.image = self.left
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 50))
        #right
        if dx < 0 and dy > dx:
            self.image = self.right
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 50))

        #up
        if dx < .02 and dx > -.02 and dy > 0:
            self.image = self.up
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (80, 80))

        #down
        if dx < .02 and dx > -.02 and dy < 0:
            self.image = self.down
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (80, 80))

    def getX(self):
        return self.rect.x
    
    def getY(self):
        return self.rect.y

    def updateObst(self, obstacle):
        dx, dy = self.rect.x - obstacle.rect.x, self.rect.y - obstacle.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width() - 300)
    
