#Written by john sullivan

import pygame
import random
import math
import time
pygame.init()

#.py imports
from carSprite import Vehicle
from zombieSprite import ZombieOne
from gunSprite import gunDefault
from backGround import BackGround
from score import Score
from health import Health
from titleScreen import titleScreen
from obstacle import obstacleOne
from coinDrop import coinDrop
from coinCount import Coins
from pauseScreen import pauseScreen


#Code for the actual window itself
screen = pygame.display.set_mode((1200, 750))

def gameScreen():
    #This code sets up the screen and fills the background with a color
    pygame.display.set_caption("Zombies")
    backDrop = pygame.Surface(screen.get_size())
    backDrop.fill((0, 0, 0))
    screen.blit(backDrop, (0,0))

        
    #Necessary for gun collisions
    gunGRP = pygame.sprite.Group()
    
    #This assigns the car sprite to a variable (for ease of use)
    car = Vehicle(gunGRP)
    
    #This assigns the gun sprite to a variable (for ease of use)
    #gun = gunDefault(car) <---- this is obviously not being used rn

    #Sets the initial speed for later changing of the zombies
    speed = 0
    
    #This is necessary for collisions later on
    spriteGRP = pygame.sprite.Group(car)

    #Obstacle car
    obstacle1 = obstacleOne()
    obstacleGRP = pygame.sprite.Group(obstacle1)

    #This list will store the zombie sprites that are on the screen (for multiples)
    ZombieOneList = []
    for z in range(7):
        speed = random.randrange(5, 15)
        zombieOne = ZombieOne(car, speed, obstacle1)
        ZombieOneList.append(zombieOne)
        
    #Coins
    coinList = []
    

    #Necessary for collisions with zombie
    zombieGRP = pygame.sprite.Group(ZombieOneList)

    #Keeps track of time, duh.
    clock = pygame.time.Clock()

    #Variable to keep game running if person doesn't quit.
    donePlaying = False

    #Necessary for respawning enemies
    respawn = 0

    #Counts seconds in the game (for doing stuff with time, who knows)
    seconds = 0

    #Timer for the gun
    gunTimer = 0

    #Coin counter
    coinCt = Coins()
    coinCtGRP = pygame.sprite.Group(coinCt)
    
    #Background
    road = BackGround()
    roadGRP = pygame.sprite.Group(road)

    #Scoreboard 
    score = Score()
    scoreGRP = pygame.sprite.Group(score)

    #Health bar
    health = Health()
    healthGRP = pygame.sprite.Group(health)

    
    #Game loop!
    while donePlaying == False:
        clock.tick(30)
        respawn += 1
        seconds += 1
        gunTimer += 1
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                donePlaying = True
            
                
                    

        
        #This identifies what key is being presses and associates some action
        # with it. 
        key = pygame.key.get_pressed()

        #Car Controls (movement)
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
            
        #Car shooting gun
        if key[pygame.K_SPACE]:
            if seconds % 6 == 0:
                car.shootGun()

        #Pause
        if key[pygame.K_ESCAPE]:
            pauseScreen()

        #These x,y variables will store a dead zombie's position.
        #This will be used for coins dropping at that location.
        currX = 0
        currY = 0
        #collision handling for shooting zombies
        gunCollided = pygame.sprite.groupcollide(zombieGRP, gunGRP, False, True)
        if gunCollided:
            score.score += 10
            for z in gunCollided:
                currX = z.getX()
                currY = z.getY()
                if seconds % 3 == 0:
                    coinList.append(coinDrop(currX, currY))
                z.reset()
        coinGRP = pygame.sprite.Group(coinList)         

        #collision handling for coins
        coinCollide = pygame.sprite.groupcollide(coinGRP, spriteGRP, True, False)
        if coinCollide:
            coinCt.coins += 1
            for c in coinCollide:
                c.reset()
            
            

        #collision handling for zombie attacking player
        carCollided = pygame.sprite.groupcollide(zombieGRP, spriteGRP, False, False)
        if carCollided:
            health.health -= 10
            if health.health <= 0:
                seconds = 0
                donePlaying = True
        for z in carCollided:
            z.reset()


        #Collision for obstacles
        carCrash = pygame.sprite.groupcollide(obstacleGRP, spriteGRP, False, False)
        if carCrash:
            health.health /= 101
            if health.health <= 0:
                seconds = 0
                donePlaying = True
        for c in carCrash:
            c.reset()

        #Zombie and obstacle collision handling
        zombieObst = pygame.sprite.groupcollide(zombieGRP, obstacleGRP, False, False)
        if zombieObst:
            for z in zombieObst:
                z.updateObst(obstacle1)
            
        
        #Draws the sprites to the screen
        roadGRP.clear(screen,backDrop)
        spriteGRP.clear(screen, backDrop)
        gunGRP.clear(screen, backDrop)
        coinGRP.clear(screen,backDrop)
        coinCtGRP.clear(screen,backDrop)
        obstacleGRP.clear(screen, backDrop)
        zombieGRP.clear(screen, backDrop)
        scoreGRP.clear(screen, backDrop)
        healthGRP.clear(screen, backDrop)

        roadGRP.update()
        spriteGRP.update()
        gunGRP.update()
        coinGRP.update()
        coinCtGRP.update()
        obstacleGRP.update()
        zombieGRP.update(car)
        scoreGRP.update()
        healthGRP.update()
    
        roadGRP.draw(screen)
        obstacleGRP.draw(screen)
        zombieGRP.draw(screen)
        coinGRP.draw(screen)
        coinCtGRP.draw(screen)
        spriteGRP.draw(screen)
        gunGRP.draw(screen)
        scoreGRP.draw(screen)
        healthGRP.draw(screen)
        
        #see dirty rect animation
        pygame.display.flip()

    pygame.mouse.set_visible(True)
    return score.score
