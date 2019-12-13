#Imports
import pygame
import random
import math
pygame.init()

#The window
screen = pygame.display.set_mode((1400, 750))


class DoubleGunIcon(pygame.sprite.Sprite):
    def __init__(self, coins):
        pygame.sprite.Sprite.__init__(self)

        if coins < 40:
            self.updateGrayDoubleGun()
        elif coins >= 40:
            self.updateReadyDoubleGun()
            

    def updateGrayDoubleGun(self):
        self.image = pygame.image.load("Sprites/Upgrades/DoubleGunsGray.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 430

    def updateReadyDoubleGun(self):
        self.image = pygame.image.load("Sprites/Upgrades/DoubleGuns.PNG")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 430

    
