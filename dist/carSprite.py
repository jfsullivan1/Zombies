#Class for car (Written by John Sullivan)

import pygame
import math
import random
from gunSprite import gunDefault

screen = pygame.display.set_mode((1200, 750))

#Car Class (Player)
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/car7.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 130))
        self.rect = self.image.get_rect()
        self.gun = gun
        self.dx = 12
        self.dy = 12
        self.rect.center = (400, 400)
        self.carImgUp = pygame.image.load("Sprites/car7.png")
        self.carImgDown = pygame.image.load("Sprites/carDown.png")
        self.carImgLeft = pygame.image.load("Sprites/carLeft.png")
        self.carImgRight = pygame.image.load("Sprites/carRight.png")
        self.carImgRightUp = pygame.image.load("Sprites/carRU.png")
        self.carImgRightDown = pygame.image.load("Sprites/carRD.png")
        self.carImgLeftUp = pygame.image.load("Sprites/carLU.png")
        self.carImgLeftDown = pygame.image.load("Sprites/carLD.png")

    #Function to make the car turn up on the screen
    #boundary constraints are to make sure the car doesn't drive off the screen
    def up(self):
        #Boundary constraint
        if self.rect.top >= 0:
            self.rect.centery -= self.dy
            self.image = self.carImgUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))

    #Turn down
    def down(self):
        #Boundary constraint
        if self.rect.bottom < screen.get_height():
            self.rect.centery += self.dy
            self.image = self.carImgUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))

    #Turn right
    def right(self):
        #Boundary constraint
        if self.rect.right < screen.get_width() - 50:
            self.rect.centerx += self.dx
            self.image = self.carImgRightUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 150))

    #Turn left
    def left(self):
        #Boundary constraint
        if self.rect.left >= 0:
            self.rect.centerx -= self.dx
            self.image = self.carImgLeftUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 150))


    #Right and up diagonal
    def rUP(self):
        #Boundary constraint
        if self.rect.right < screen.get_width() - 50 and self.rect.top >= 0:
            self.rect.centerx += 10
            self.rect.centery -= 10
            self.image = self.carImgRightUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 150))
        
    #Right and down diagonal
    def rDOWN(self):
        #Boundary constraint
        if self.rect.right < screen.get_width() - 10 and self.rect.bottom < screen.get_height():
            self.rect.centerx += 10
            self.rect.centery += 10
            self.image = self.carImgUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))
        
    #Left and up diagonal
    def leftUP(self):
        #Boundary constraint
        if self.rect.left >= 0 and self.rect.top >= 0:
            self.rect.centerx -= 10
            self.rect.centery -= 10
            self.image = self.carImgLeftUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 150))
        
    #Left and down diagonal
    def leftDOWN(self):
        #Boundary constraint
        if self.rect.left >= 0 and self.rect.bottom < screen.get_height():
            self.rect.centerx -= 10
            self.rect.centery += 10
            self.image = self.carImgUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))

    
    #Shoot Gun
    def shootGun(self):
        shoot = gunDefault(self.rect.centerx, self.rect.top, self.gun)
        self.gun.add(shoot)
