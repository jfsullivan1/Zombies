#Imports
import pygame
import random
import math
pygame.init()

#The window
screen = pygame.display.set_mode((1400, 750))


class FireRateIcon(pygame.sprite.Sprite):
    def __init__(self, coins):
        pygame.sprite.Sprite.__init__(self)

        if coins < 30:
            self.updateGrayFireRate()
        elif coins >= 30:
            self.updateReadyFireRate()
            

    def updateGrayFireRate(self):
        self.image = pygame.image.load("Sprites/Upgrades/FireRateGray.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 210

    def updateReadyFireRate(self):
        self.image = pygame.image.load("Sprites/Upgrades/FireRate.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 210

    
