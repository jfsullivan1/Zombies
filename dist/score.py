#Score and Health class, written by john Sullivan

#Imports
import pygame
import random
import math
pygame.init()

#Code for the actual window itself
screen = pygame.display.set_mode((1200, 750))

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.font = pygame.font.Font("Fonts/csnpwdt NFI.otf", 50)

    def update(self):
                        
        self.text = "Score: %d" % (self.score)
        self.image = self.font.render(self.text, 1, (255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 630
        
