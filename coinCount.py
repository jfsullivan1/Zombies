#Coin counter written by john sullivan, aaron schneidereit, matt carley

import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((1400, 750))

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.coins = 0
        self.font = pygame.font.Font("Fonts/csnpwdt NFI.otf", 45)

    def update(self):

        self.text = "Coins: %d" % (self.coins)
        self.image = self.font.render(self.text, 1, (255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1300
        self.rect.centery = 700
