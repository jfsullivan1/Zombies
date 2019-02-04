#Class for default gun
#Written  by John on 1/31/2019


#Car class code
#started by John Sullivan on 1/29/2019

import pygame
pygame.init()

#Car Class (Player)
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car7.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))
        self.rect = self.image.get_rect()
        self.gun = gun
        self.dx = 12
        self.dy = 12
        self.rect.center = (400, 400)

    #Function to make the car turn up on the screen
    def up(self):
        self.rect.centery -= self.dy
        self.image = pygame.image.load("car7.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))

    #Turn down
    def down(self):
        self.rect.centery += self.dy
        self.image = pygame.image.load("carDown.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))

    #Turn left
    def right(self):
        self.rect.centerx += self.dx
        self.image = pygame.image.load("carRight.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))

    #Turn right
    def left(self):
        self.rect.centerx -= self.dx
        self.image = pygame.image.load("carLeft.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 120))

    #Shoot Gun
    def shootGun(self):
        shoot = gunDefault(self.rect.centerx, self.rect.top, self.gun)
        self.gun.add(shoot)

#Gun Default Class
class gunDefault(pygame.sprite.Sprite):
    def __init__(self, startingX, startingY, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (10, 25))
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

class BackGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dy = 5
        self.reset()

    def update(self):
        self.rect.bottom += self.dy
        if self.rect.top >= 0:
            self.reset()

    def reset(self):
        self.rect.bottom = screen.get_height()

#MAIN FUNCTION (Will separate into a game() function later)
def main():
    
    #This code sets up the screen and fills the background with a color
    screen = pygame.display.set_mode((1600, 820))
    pygame.display.set_caption("Zombies")
    backDrop = pygame.Surface(screen.get_size())
    backDrop.fill((0, 0, 0))
    screen.blit(backDrop, (0,0))

    gunGRP = pygame.sprite.Group()
    
    #This assigns the car sprite to a variable (for ease of use)
    car = Vehicle(gunGRP)
    
    #This assigns the gun sprite to a variable (for ease of use)
    #gun = gunDefault(car)
    
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

        #Shoot default gun
        if key[pygame.K_SPACE]:
            car.shootGun()
        

        spriteGRP.clear(screen, backDrop)
        gunGRP.clear(screen, backDrop)

        spriteGRP.update()
        gunGRP.update()
        
        spriteGRP.draw(screen)
        gunGRP.draw(screen)
        pygame.display.flip()

    pygame.mouse.set_visible(True)
    #TO QUIT
    if donePlaying == True:
        pygame.quit()

if __name__ == "__main__":
    main()
