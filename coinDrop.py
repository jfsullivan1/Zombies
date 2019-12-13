import pygame
import math
import random

screen = pygame.display.set_mode((1400, 750))

class coinDrop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/coin.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.y += 15

    def reset(self):
        self.rect.x = -200

        
