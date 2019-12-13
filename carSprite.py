#Class for car (Written by John Sullivan)

import pygame
import math
import random
from gunSprite import gunDefault
from gunSprite import gunRight
from gunSprite import gunLeft
from particle import ParticleEmitter

screen = pygame.display.set_mode((1200, 750))

#Car Class (Player)
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, gun):
        pygame.sprite.Sprite.__init__(self)
        #Initital Car Image
        self.image = pygame.image.load("Sprites/Car/CarGun.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 130))
        self.rect = self.image.get_rect()
        self.gun = gun
        #Car Speed
        self.dx = 10
        self.dy = 10
        #Starting Location
        self.rect.center = (400, 400)
        #Other Car Sprites
        #Default Cars
        self.carImgUp = pygame.image.load("Sprites/Car/CarGun.png")
        self.carImgRightUp = pygame.image.load("Sprites/Car/CarGunUR.png")
        self.carImgLeftUp = pygame.image.load("Sprites/Car/CarGunUL.png")
        #Shielded Cars
        self.carShieldUp = pygame.image.load("Sprites/Car/CarGunShield.png")
        self.carShieldRightUp = pygame.image.load("Sprites/Car/CarGunShieldUR.png")
        self.carShieldLeftUp = pygame.image.load("Sprites/Car/CarGunShieldUL.png")
        #Double Gun Cars
        self.carDGUp = pygame.image.load("Sprites/Car/CarDoubleGun.png")
        self.carDGUL = pygame.image.load("Sprites/Car/CarDoubleGunUL.png")
        self.carDGUR = pygame.image.load("Sprites/Car/CarDoubleGunUR.png")
        #Double Gun Shield Cars
        self.carShieldDGUp = pygame.image.load("Sprites/Car/CarGunShieldDG.png")
        self.carShieldDGUL = pygame.image.load("Sprites/Car/CarGunShieldDGUL.png")
        self.carShieldDGUR = pygame.image.load("Sprites/Car/CarGunShieldDGUR.png")

        self.particleEmitter = ParticleEmitter(self.rect.x, self.rect.y)

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
        if self.rect.right < screen.get_width() - 250:
            self.rect.centerx += self.dx
            self.image = self.carImgRightUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105, 165))

    #Turn left
    def left(self):
        #Boundary constraint
        if self.rect.left >= 0:
            self.rect.centerx -= self.dx
            self.image = self.carImgLeftUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105, 165))


    #Right and up diagonal
    def rUP(self):
        #Boundary constraint
        if self.rect.right < screen.get_width() - 250 and self.rect.top >= 0:
            self.rect.centerx += 10
            self.rect.centery -= 10
            self.image = self.carImgRightUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105, 165))
        
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
            self.image = pygame.transform.scale(self.image, (105, 165))
        
    #Left and down diagonal
    def leftDOWN(self):
        #Boundary constraint
        if self.rect.left >= 0 and self.rect.bottom < screen.get_height():
            self.rect.centerx -= 10
            self.rect.centery += 10
            self.image = self.carImgUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))


    #####################################################################
#############      SHIELDED UPGRADE (SPRITES)    ####################
#####################################################################

    #Not moving on the screen, Shielded
    def deafultUpShielded(self):
        self.image = self.CarShieldUp
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,130))

    #Moving up, Shielded    
    def upShielded(self):
        if self.rect.top >= 0:
            self.rect.centery -= self.dy
            self.image = self.carShieldUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))
        
    #Moving Down, Shielded
    def downShielded(self):
        if self.rect.bottom < screen.get_height():
            self.rect.centery += self.dy
            self.image = self.carShieldUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))

    #Moving Right, Shielded
    def rightShielded(self):
        if self.rect.right < screen.get_width() - 250:
            self.rect.centerx += self.dx
            self.image = self.carShieldRightUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105,165))

    #Moving Left, Shielded
    def leftShielded(self):
        if self.rect.left >= 0:
            self.rect.centerx -= self.dx
            self.image = self.carShieldLeftUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105,165))

    #Moving Right and Up, Shielded
    def rUPShielded(self):
        if self.rect.right < screen.get_width() - 250 and self.rect.top >= 0:
            self.rect.centerx += self.dx
            self.rect.centery -= self.dy
            self.image = self.carShieldRightUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105,165))
        
    #Moving Right and Down, Shielded
    def rDOWNShielded(self):
        if self.rect.right < screen.get_width() - 10 and self.rect.bottom < screen.get_height():
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
            self.image = self.carShieldRightUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105,165))
        
    #Moving Left and Up, Shielded
    def leftUPShielded(self):
        if self.rect.left >= 0 and self.rect.top >= 0:
            self.rect.centerx -= self.dx
            self.rect.centery -= self.dy
            self.image = self.carShieldLeftUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105,165))
        
    #Moving Left and Down, Shielded
    def leftDOWNShielded(self):
        if self.rect.left >= 0 and self.rect.bottom < screen.get_height():
            self.rect.centerx -= self.dx
            self.rect.centery += self.dy
            self.image = self.carShieldLeftUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (105,165))

#####################################################################
##############    DUAL GUN UPGRADE (SPRITES)   ######################
#####################################################################

#Not moving on the screen, double gun
    def defaultUpDG(self):
        self.image = self.carDGUp
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,130))

    #Moving up, double gun    
    def upDG(self):
        if self.rect.top >= 0:
            self.rect.centery -= self.dy
            self.image = self.carDGUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))

    #Moving Down, double gun
    def downDG(self):
        if self.rect.bottom < screen.get_height():
            self.rect.centery += self.dy
            self.image = self.carDGUp
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 130))

    #Moving Right, double gun
    def rightDG(self):
        if self.rect.right < screen.get_width() - 250:
            self.rect.centerx += self.dx
            self.image = self.carDGUR
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (120,155))

    #Moving Left, double gun
    def leftDG(self):
        if self.rect.left >= 0:
            self.rect.centerx -= self.dx
            self.image = self.carDGUL
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (120,155))

    #Moving Right and Up, double gun
    def rUPDG(self):
        if self.rect.right < screen.get_width() - 250 and self.rect.top >= 0:
            self.rect.centerx += self.dx
            self.rect.centery -= self.dy
            self.image = self.carDGUR
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (120,155))

    #Moving Right and Down, double gun
    def rDOWNDG(self):
        if self.rect.right < screen.get_width() - 10 and self.rect.bottom < screen.get_height():
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
            self.image = self.carDGUR
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (120,155))

    #Moving Left and Up, double gun
    def leftUPDG(self):
        if self.rect.left >= 0 and self.rect.top >= 0:
            self.rect.centerx -= self.dx
            self.rect.centery -= self.dy
            self.image = self.carDGUL
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (120,155))

    #Moving Left and Down, double gun
    def leftDOWNDG(self):
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy
        self.image = self.carDGUL
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (120,155))

#####################################################################
##############    DUAL GUN Shielded UPGRADE   #######################
#####################################################################
#Not moving on the screen, double gun
    def defaultUpShieldDG(self):
        self.image = self.carShieldDGUp
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,130))

    #Moving up, double gun    
    def upShieldDG(self):
        self.rect.centery -= self.dy
        self.image = self.carShieldDGUp
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 130))

    #Moving Down, double gun
    def downShieldDG(self):
        self.rect.centery += self.dy
        self.image = self.carShieldDGUp
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 130))

    #Moving Right, double gun
    def rightShieldDG(self):
        self.rect.centerx += self.dx
        self.image = self.carShieldDGUR
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (105,165))

    #Moving Left, double gun
    def leftShieldDG(self):
        self.rect.centerx -= self.dx
        self.image = self.carShieldDGUL
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (105,165))

    #Moving Right and Up, double gun
    def rUPShieldDG(self):
        self.rect.centerx += self.dx
        self.rect.centery -= self.dy
        self.image = self.carShieldDGUR
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (105,165))

    #Moving Right and Down, double gun
    def rDOWNShieldDG(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        self.image = self.carShieldDGUR
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (105,165))

    #Moving Left and Up, double gun
    def leftUPShieldDG(self):
        self.rect.centerx -= self.dx
        self.rect.centery -= self.dy
        self.image = self.carShieldDGUL
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (105,165))

    #Moving Left and Down, double gun
    def leftDOWNShieldDG(self):
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy
        self.image = self.carShieldDGUL
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (105,165))

    #Shoot Gun
    def shootGun(self):
        shoot = gunDefault(self.rect.centerx, self.rect.top, self.gun)
        self.gun.add(shoot)

    #Shoot Guns
    #Added
    def shootBoth(self):
        shootL = gunLeft(self.rect.centerx,self.rect.top, self.gun)
        self.gun.add(shootL)
        shootR = gunRight(self.rect.centerx,self.rect.top, self.gun)
        self.gun.add(shootR)
