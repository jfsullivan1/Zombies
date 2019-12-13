#Imports
import pygame
import random
import math
pygame.init()

#The window
screen = pygame.display.set_mode((1400, 750))


class SpeedIcon(pygame.sprite.Sprite):
    def __init__(self, coins):
        pygame.sprite.Sprite.__init__(self)

        if coins < 20:
            self.updateGraySpeed()
        elif coins >= 20:
            self.updateReadySpeed()

    def updateGraySpeed(self):
        self.image = pygame.image.load("Sprites/Upgrades/SpeedUp.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 540

    def updateReadySpeed(self):
        self.image = pygame.image.load("Sprites/Upgrades/SpeedUpColored.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 540

    
