#Written by john Sullivan
#Class for updating health upgrade icon

#Imports
import pygame
import random
import math
pygame.init()

#The window
screen = pygame.display.set_mode((1400, 750))


class HealthIcon(pygame.sprite.Sprite):
    def __init__(self, coins):
        pygame.sprite.Sprite.__init__(self)

        if coins < 10:
            self.updateGrayHealth()
        elif coins >= 10:
            self.updateReadyHealth()
        

    def updateGrayHealth(self):
        self.image = pygame.image.load("Sprites/Upgrades/HealthGray.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 100

    def updateReadyHealth(self):
        self.image = pygame.image.load("Sprites/Upgrades/Health.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 100

    
        
        
