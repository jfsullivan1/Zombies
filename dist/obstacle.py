#Written by Aaron Schneidereit and John Sullivan
#3/25/2019
#OBSTACLES for Zombie Road Game!


import pygame
import random
import math
import time
pygame.init()

#.py imports
#Code for the actual window itself
screen = pygame.display.set_mode((1200, 750))
#class definition

class obstacleOne(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/brokenCar.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (130,70))
        self.rect = self.image.get_rect()
        self.speed = 15
        self.reset()


    def update(self):
        self.rect.centery += self.speed

        if self.rect.top > screen.get_height():
            self.reset()

    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(60, screen.get_width() - 150)

        
        
