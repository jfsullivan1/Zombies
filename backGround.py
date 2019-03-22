#Scrolling background sprite
#John Sullivan  

import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode((1000, 700))

#Background Code (TO DO!!!)
class BackGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/back.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (1000, 2000))
        self.rect = self.image.get_rect()
        self.dy = 15
        self.reset()

    def update(self):
        self.rect.bottom += self.dy
        if self.rect.top >= 0:
            self.reset()

    def reset(self):
        self.rect.bottom = screen.get_height()


