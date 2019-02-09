#Class for default gun
#Written  by John on 1/31/2019


#Car class code
#started by John Sullivan on 1/29/2019

import pygame
import random
import math
pygame.init()

#Code for the actual window itself
screen = pygame.display.set_mode((1600, 820))

#Car Class (Player)
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car7.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.gun = gun
        self.dx = 12
        self.dy = 12
        self.rect.center = (400, 400)
        self.carImgUp = pygame.image.load("car7.png")
        self.carImgDown = pygame.image.load("carDown.png")
        self.carImgLeft = pygame.image.load("carLeft.png")
        self.carImgRight = pygame.image.load("carRight.png")
        self.carImgRightUp = pygame.image.load("carRU.png")
        self.carImgRightDown = pygame.image.load("carRD.png")
        self.carImgLeftUp = pygame.image.load("carLU.png")
        self.carImgLeftDown = pygame.image.load("carLD.png")

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

#Gun Default Class
class gunDefault(pygame.sprite.Sprite):
    def __init__(self, startingX, startingY, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (20, 35))
        self.rect = self.image.get_rect()
        self.rect.centerx = startingX
        self.rect.centery = startingY
        self.dy = -15
        self.gun = gun

        #right
        r = 15

        #left
        l = -15

        #down
        d = 15

    def update(self):
        self.rect.centery += self.dy
        if self.rect.bottom < 0:
            self.dy = 0
            self.gun.remove(self)

    def left(self):
        self.rect.centery += l
        if self.rect.centerx < 0:
            l = 0
            self.gun.remove(self)

#Zombie ONE code
class ZombieOne(pygame.sprite.Sprite):
    def __init__(self, car):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("z1D.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.speed = 5

        self.reset()

    def update(self, player):
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        self.rect.x -= dx * self.speed
        self.rect.y -= dy * self.speed

        #left
        if dx > 0 and dy < dx:
            self.image = pygame.image.load("z1L.png")
            self.image = self.image.convert()
            self.image = pygame.transform.scale(self.image, (80, 80))
        #right
        if dx < 0 and dy > dx:
            self.image = pygame.image.load("z1R.png")
            self.image = self.image.convert()
            self.image = pygame.transform.scale(self.image, (80, 80))

        #up
        if dx < .02 and dx > -.02 and dy > 0:
            self.image = pygame.image.load("z1U.png")
            self.image = self.image.convert()
            self.image = pygame.transform.scale(self.image, (80, 80))

        #down
        if dx < .02 and dx > -.02 and dy < 0:
            self.image = pygame.image.load("z1D.png")
            self.image = self.image.convert()
            self.image = pygame.transform.scale(self.image, (80, 80))


    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
    
    #Background Code (TO DO!!!)
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

#Screen that pops up when you die
def DeathScreen():
    deathFont = pygame.font.SysFont("Comic Sans MS", 50)
    
    message = (
        "YOU DIED!"
        )
    message = deathFont.render(message, 1, (255, 255, 0))
    
    screen.blit(message, (100, 30))

    pygame.display.flip()

#MAIN FUNCTION (Will separate into a game() function later)
def main():
    
    #This code sets up the screen and fills the background with a color
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

    #This list will store the zombie sprites that are on the screen (for multiples)
    ZombieOneList = []
    for z in range(7):
        zombieOne = ZombieOne(car)
        ZombieOneList.append(zombieOne)

    #Necessary for collisions with zombie
    zombieGRP = pygame.sprite.Group(ZombieOneList)

    #Keeps track of time, duh.
    clock = pygame.time.Clock()

    #Variable to keep game running if person doesn't quit.
    donePlaying = False

    #Necessary for respawning enemies
    respawn = 0
    
    #Game loop!
    while donePlaying == False:
        clock.tick(30)
        respawn += 1
        pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                donePlaying = True

        
        #This identifies what key is being pressed and associates some action
        # with it. 
        key = pygame.key.get_pressed()

        #Car Controls
        if key[pygame.K_LEFT] and key[pygame.K_UP]:
            car.leftUP()
        elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:
            car.leftDOWN()
        elif key[pygame.K_RIGHT] and key[pygame.K_UP]:
            car.rUP()
        elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
            car.rDOWN()
        elif key[pygame.K_LEFT]:
            car.left()
        elif key[pygame.K_RIGHT]:
            car.right()
        elif key[pygame.K_UP]:
            car.up()
        elif key[pygame.K_DOWN]:
            car.down()
            

        #Shoot default gun
        if key[pygame.K_SPACE]:
            car.shootGun()


        #collision handling for shooting zombies
        gunCollided = pygame.sprite.groupcollide(zombieGRP, gunGRP, False, True)
        if gunCollided:
            for z in gunCollided:
                z.reset()

        #collision handling for zombie attacking player
        carCollided = pygame.sprite.groupcollide(zombieGRP, spriteGRP, False, False)
        if carCollided:
            donePlaying = True
        for z in carCollided:
            z.reset()
        
        #Draws the sprites
        spriteGRP.clear(screen, backDrop)
        gunGRP.clear(screen, backDrop)
        zombieGRP.clear(screen, backDrop)

        spriteGRP.update()
        gunGRP.update()
        zombieGRP.update(car)

        zombieGRP.draw(screen)
        spriteGRP.draw(screen)
        gunGRP.draw(screen)
        
        pygame.display.flip()

    pygame.mouse.set_visible(True)
    
    #When dead 
    if donePlaying == True:
        DeathScreen()

if __name__ == "__main__":
    main()
