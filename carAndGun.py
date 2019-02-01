#Class for default gun
#Written  by John on 1/31/2019


#Car class code
#started by John Sullivan on 1/29/2019

import pygame
pygame.init()

#Car Class (Player)
class Vehicle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car7.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))
        self.rect = self.image.get_rect()
        self.dx = 8
        self.dy = 8
        self.rect.center = (400, 400)
    def up(self):
        self.rect.centery -= self.dy
        self.image = pygame.image.load("car7.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))
    def down(self):
        #self.rect.centery += self.dy
        self.rect.centerx -= self.dx
        self.image = pygame.image.load("carDown.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))
    def right(self):
        self.rect.centerx += self.dx
        self.image = pygame.image.load("carRight.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))
        
    def left(self):
        self.rect.centerx -= self.dx
        self.image = pygame.image.load("carLeft.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))

#Gun Default Class
class gunDefault(pygame.sprite.Sprite):
    def __init__(self, carX, carY, gunGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 12))
        self.image = self.image.convert()
        self.image.fill((211, 211, 211))
        self.rect = self.image.get_rect()
        self.rect.centerx = carX
        self.rect.centery = carY
        self.dy = -15
        self.gunGroup = gunGroup

    def update(self):
        self.rect.centery += self.dy
        if self.rect.bottom < 0:
            self.dy = 0
            self.gunGroup.remove(self)

#MAIN FUNCTION (Will separate into a game() function later)
def main():
    
    #This code sets up the screen and fills the background with a color
    screen = pygame.display.set_mode((900, 800))
    pygame.display.set_caption("Zombies")
    backDrop = pygame.Surface(screen.get_size())
    backDrop.fill((0, 0, 0))
    screen.blit(backDrop, (0,0))

    #This assigns the car sprite to a variable
    car = Vehicle()
    
    #This is necessary for collisions later on
    spriteGRP = pygame.sprite.Group(car)

    #Keeps track of time, duh.
    clock = pygame.time.Clock()

    #Variable to keep game running if person doesn't quit.
    donePlaying = False

    #Game loop!
    while donePlaying == False:
        clock.tick(30)
        pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                donePlaying = True
    
        #This identifies what key is being pressed and associates some action
        # with it. 
        key = pygame.key.get_pressed()

        #Car Controls
        if key[pygame.K_LEFT]:
            car.left()
        if key[pygame.K_RIGHT]:
            car.right()
        if key[pygame.K_UP]:
            car.up()
        if key[pygame.K_DOWN]:
            car.down()

        

        spriteGRP.clear(screen, backDrop)
        spriteGRP.draw(screen)
        pygame.display.flip()

    pygame.mouse.set_visible(True)
    #TO QUIT
    if donePlaying == True:
        pygame.quit()

if __name__ == "__main__":
    main()
