#Main and death screen (Written by john sullivan)

import pygame
import random
import math
pygame.init()

#.py imports
from carSprite import Vehicle
from zombieSprite import ZombieOne
from gunSprite import gunDefault

#Code for the actual window itself
screen = pygame.display.set_mode((1600, 820))

#Screen that pops up when you die
def DeathScreen():
    deathFont = pygame.font.SysFont("Comic Sans MS", 50)
    
    message = (
        "YOU DIED!"
        )
    message = deathFont.render(message, 1, (255, 255, 0))
    
    screen.blit(message, (100, 30))

    #This is necessary, dont ask why
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
        
        #Draws the sprites to the screen
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
        pygame.quit()
if __name__ == "__main__":
    main()
