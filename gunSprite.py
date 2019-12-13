#Class for gun (Written by John Sullivan)

import pygame
import math
import random

screen = pygame.display.set_mode((1400, 750))

#Gun Default Class
class gunDefault(pygame.sprite.Sprite):
    def __init__(self, startingX, startingY, gun):
        pygame.sprite.Sprite.__init__(self)
        self.bullet = pygame.image.load("Sprites/bullet.png")
        self.image = self.bullet
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 35))
        self.rect = self.image.get_rect()
        self.rect.centerx = startingX
        self.rect.centery = startingY
        self.dy = -15
        self.gun = gun

    def update(self):
        self.rect.centery += self.dy
        if self.rect.bottom < 0:
            self.dy = 0
            self.gun.remove(self)
#Added
class gunRight(pygame.sprite.Sprite):
    def __init__(self, startingX, startingY, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/bullet.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 35))
        self.rect = self.image.get_rect()
        self.rect.centerx = startingX + 20
        self.rect.centery = startingY
        self.dy = 15
        self.gun = gun

    def update(self):
        self.rect.centery -= self.dy
        if self.rect.bottom < 0:
            self.dy = 0
            self.gun.remove(self)

class gunLeft(pygame.sprite.Sprite):
    def __init__(self, startingX, startingY, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/bullet.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 35))
        self.rect = self.image.get_rect()
        self.rect.centerx = startingX - 20
        self.rect.centery = startingY
        self.dy = 15
        self.gun = gun

    def update(self):
        self.rect.centery -= self.dy
        if self.rect.bottom < 0:
            self.dy = 0
            self.gun.remove(self)

