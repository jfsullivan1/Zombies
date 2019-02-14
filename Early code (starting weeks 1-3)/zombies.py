#John Sullivan CSC305
#Zombie Game (Name TBD)
#Started on 1/28/2019

import pygame
import random
pygame.init()

screenWidth = 800
screenLength = 640
screen = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("zombies.py")
#myFont = pygame.font.SysFont("Comic Sans MS", 20)
if not pygame.mixer:
    print ("Sound error!")
else:
    pygame.mixer.init()


rgb = (250,0,0)
x = 50
y = 50
width = 40
height = 60
vel = 5

#backDrop = pygame.Surface(screen.get_size())
#backDrop.fill((0,0,0))
char = pygame.image.load("car7.jpg")
screen.blit(char, (0,0))
keepGoing = True
clock = pygame.time.Clock()
while keepGoing == True:
    clock.tick(30)
    
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            keepGoing = False
    #screen.blit(backDrop, (0,0))
    #pygame.display.flip()
    
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and x > 0:
        x -= vel
    if key[pygame.K_RIGHT] and x < screenWidth - 200:
        x += vel
    if key[pygame.K_UP] and y > 2:
        y -= vel
    if key[pygame.K_DOWN] and y < screenLength + height + 30:
        y += vel

    screen.fill(rgb)
    pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))
    pygame.display.update()

class Vehicle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car7.jpg")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

    def updatePosition(self):
        carX, carY = pygame.mouse.get_pos()
        self.rect.center = (carX, 680)

#def main():
   
   

#if __name__ == "__main__": 
     #main()

pygame.quit()
    
