#Class for car (Written by John Sullivan)

import pygame
import math
import random
from gunSprite import gunDefault

screen = pygame.display.set_mode((1000, 700))

#Car Class (Player)
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/car7.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (50, 80))
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
    def up(self):
        self.rect.centery -= self.dy
        self.image = self.carImgUp
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (50, 80))

    #Turn down
    def down(self):
        self.rect.centery += self.dy
        self.image = self.carImgDown
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (50, 80))

    #Turn right
    def right(self):
        self.rect.centerx += self.dx
        self.image = self.carImgRight
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 50))

    #Turn left
    def left(self):
        self.rect.centerx -= self.dx
        self.image = self.carImgLeft
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 50))


    #Right and up diagonal
    def rUP(self):
        self.rect.centerx += 10
        self.rect.centery -= 10
        self.image = self.carImgRightUp
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (90, 90))
        
    #Right and down diagonal
    def rDOWN(self):
        self.rect.centerx += 10
        self.rect.centery += 10
        self.image = self.carImgRightDown
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (90, 90))
        
    #Left and up diagonal
    def leftUP(self):
        self.rect.centerx -= 10
        self.rect.centery -= 10
        self.image = self.carImgLeftUp
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (90, 90))
        
    #Left and down diagonal
    def leftDOWN(self):
        self.rect.centerx -= 10
        self.rect.centery += 10
        self.image = self.carImgLeftDown
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (90, 90))

    
    #Shoot Gun
    def shootGun(self):
        shoot = gunDefault(self.rect.centerx, self.rect.top, self.gun)
        self.gun.add(shoot)
