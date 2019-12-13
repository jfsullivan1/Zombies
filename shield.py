#Imports
import pygame
import random
import math
pygame.init()

#The window
screen = pygame.display.set_mode((1400, 750))


class ShieldIcon(pygame.sprite.Sprite):
    def __init__(self, coins):
        pygame.sprite.Sprite.__init__(self)
        if coins < 30:
            self.updateGrayShield()
        elif coins >= 30:
            self.updateReadyShield()
            

    def updateGrayShield(self):
        self.image = pygame.image.load("Sprites/Upgrades/ShieldGray.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 320

    def updateReadyShield(self):
        self.image = pygame.image.load("Sprites/Upgrades/Shield.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1350
        self.rect.centery = 320

    
