#Health class written by john sullivan


#Imports
import pygame
import random
import math
pygame.init()

#Code for the window itself
screen = pygame.display.set_mode((1400, 750))

class Health(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100

        #Image loading for health bar
        self.fullHealth = pygame.image.load("Sprites/HealthFull.png")
        self.ThreeQHealth = pygame.image.load("Sprites/Health3Quarters.png")
        self.halfHealth = pygame.image.load("Sprites/HealthHalf.png")
        self.OneQHealth = pygame.image.load("Sprites/Health1Quarter.png")
        self.NoHealth = pygame.image.load("Sprites/HealthDead.png")
        
    def update(self):
        if self.health > 75:
            self.image = self.fullHealth
            self.image = pygame.transform.scale(self.image, (375, 100))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.centerx = 200
            self.rect.centery = 700
        if self.health <= 75 and self.health > 50:
            self.image = self.ThreeQHealth
            self.image = pygame.transform.scale(self.image, (375, 100))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.centerx = 200
            self.rect.centery = 700
        if self.health <= 50 and self.health > 25:
            self.image = self.halfHealth
            self.image = pygame.transform.scale(self.image, (375, 100))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.centerx = 200
            self.rect.centery = 700
        if self.health <= 25 and self.health > 0:
            self.image = self.OneQHealth
            self.image = pygame.transform.scale(self.image, (375, 100))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.centerx = 200
            self.rect.centery = 700
        if self.health <= 0:
            self.image = self.NoHealth
            self.image = pygame.transform.scale(self.image, (375, 100))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.centerx = 200
            self.rect.centery = 700
