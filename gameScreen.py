#Written by john sullivan
#BGM: zombieIsComing credit by yd in <opengameart.org/content/zombies-march>
#I change zombie damage to random integer 1 to 10
# coin randomly drop 1 to 5

import pygame
import random
import math
import time
pygame.init()
from os import path



#Sound
if not pygame.mixer:
    print ("problem with sound")
else:
    pygame.mixer.init()

#load game sounds and back ground music
gunSnd = pygame.mixer.Sound("Sounds/shoot.wav")
# didn't use car sound loop, too noisy
carSnd = pygame.mixer.Sound("Sounds/car.wav")
healthUpSnd = pygame.mixer.Sound("Sounds/healthUp.wav")
pickCoinSnd = pygame.mixer.Sound("Sounds/Pickup_Coin.wav")
crashSnd = pygame.mixer.Sound("Sounds/car_crash.wav")
# not sure where to trigger play button
playSnd = pygame.mixer.Sound("Sounds/play.wav")
upgrade_success_Snd = pygame.mixer.Sound("Sounds/upgrade.wav")
#set background music after click playing
pygame.mixer.music.load("Sounds/ZombiesAreComing.ogg")
#set back ground music to lower to hear other sound effect clearly
pygame.mixer.music.set_volume(0.5)    



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
from shield import ShieldIcon
from fireRate import FireRateIcon
from doubleGun import DoubleGunIcon
from speed import SpeedIcon
from healthIcon import HealthIcon
from bloodSprite import bloodExp

#Code for the actual window itself
screen = pygame.display.set_mode((1400, 750))
#define screen title
screen_title = 'Zombie Roads V1.3'
pygame.display.set_caption(screen_title)


    
def gameScreen():
    #This code sets up the screen and fills the background with a color
    pygame.display.set_caption("Zombies")
    backDrop = pygame.Surface(screen.get_size())
    backDrop.fill((0, 0, 0))
    screen.blit(backDrop, (0,0))

    #Shielded bool
    isShieldOn = False
    #Shield timer
    shieldTimer = 0
    
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
    fireRate = 6

    #Variable for Double Guns
    dGuns = False

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

    all_sprites = pygame.sprite.Group()


    #Necessary so you don't buy 35 upgrades when you press a button
    upgradeDelay = False
    upgradeDelayTimer = 0
    
    #Coin costs
    healthCost = "x10 Coins"
    fireRateCost = "x30 Coins"
    shieldCost = "x30 Coins"
    doubleCost = "x40 Coins"
    speedCost = "x20 Coins"
    coinFont = pygame.font.SysFont("Comic Sans MS", 20)
    screen.blit(coinFont.render(healthCost, True, (0, 255, 0)), (1210, 90))
    screen.blit(coinFont.render(fireRateCost, True, (0, 255, 0)), (1210, 210))
    screen.blit(coinFont.render(shieldCost, True, (0, 255, 0)), (1210, 320))
    screen.blit(coinFont.render(doubleCost, True, (0, 255, 0)), (1210, 430))
    screen.blit(coinFont.render(speedCost, True, (0, 255, 0)), (1210, 540))

    #set background music play to loops
    pygame.mixer.music.play(loops= -1)
    
    #Game loop!
    while donePlaying == False:
        #keep loop running at right speed
        clock.tick(30)
        respawn += 1
        seconds += 1
        mouse = pygame.mouse.get_pos()
        pygame.mouse.set_visible(True)
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)

        
        #Upgrade display
        healthUpIcon = HealthIcon(coinCt.coins)
        speedUpIcon = SpeedIcon(coinCt.coins)
        shieldUpIcon = ShieldIcon(coinCt.coins)
        doubleGunUpIcon = DoubleGunIcon(coinCt.coins)
        fireRateUpIcon = FireRateIcon(coinCt.coins)
        upgradeGRP = pygame.sprite.Group(healthUpIcon, speedUpIcon, shieldUpIcon, doubleGunUpIcon, fireRateUpIcon)

        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                donePlaying = True
                
        #update
        all_sprites.update()
        car.particleEmitter.update()
                    
                
            
             
                    

        
        #This identifies what key is being presses and associates some action
        # with it. 
        key = pygame.key.get_pressed()

        #Car Controls (movement)
        if key[pygame.K_LEFT] and key[pygame.K_UP]:
            if isShieldOn == False and dGuns == False:
                car.leftUP()
            elif dGuns == True and isShieldOn == True:
                car.leftUPShieldDG()
            elif dGuns == True:
                car.leftUPDG()
            elif isShieldOn == True:
                car.leftUPShielded()
        elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:
            if isShieldOn == False and dGuns == False:
                car.leftDOWN()
            elif dGuns == True and isShieldOn == True:
                car.leftDOWNShieldDG()
            elif dGuns == True:
                car.leftDOWNDG()
            elif isShieldOn == True:
                car.leftDOWNShielded()
        elif key[pygame.K_RIGHT] and key[pygame.K_UP]:
            if isShieldOn == False and dGuns == False:
                car.rUP()
            elif dGuns == True and isShieldOn == True:
                car.rUPShieldDG()
            elif dGuns == True:
                car.rUPDG()
            elif isShieldOn == True:
                car.rUPShielded()
        elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
            if isShieldOn == False and dGuns == False:
                car.rDOWN()
            elif dGuns == True and isShieldOn == True:
                car.rDOWNShieldDG()
            elif dGuns == True:
                car.rDOWNDG()
            elif isShieldOn == True:
                car.rDOWNShielded()
        elif key[pygame.K_LEFT]:
            if isShieldOn == False and dGuns == False:
                car.left()
            elif dGuns == True and isShieldOn == True:
                car.leftShieldDG()
            elif dGuns == True:
                car.leftDG()
            elif isShieldOn == True:
                car.leftShielded()
        elif key[pygame.K_RIGHT]:
            if isShieldOn == False and dGuns == False:
                car.right()
            elif dGuns == True and isShieldOn == True:
                car.rightShieldDG()
            elif dGuns == True:
                car.rightDG()
            elif isShieldOn == True:
                car.rightShielded()
        elif key[pygame.K_UP]:
            if isShieldOn == False and dGuns == False:
                car.up()
            elif dGuns == True and isShieldOn == True:
                car.upShieldDG()
            elif dGuns == True:
                car.upDG()
            elif isShieldOn == True:
                car.upShielded()
        elif key[pygame.K_DOWN]:
            if isShieldOn == False and dGuns == False:
                car.down()
            elif dGuns == True and isShieldOn == True:
                car.downShieldDG()
            elif dGuns == True:
                car.downDG()
            elif isShieldOn == True:
                car.downShielded()

        
        
        elif key[pygame.K_1] and coinCt.coins >= 10 and upgradeDelay == False:
            #Health
            upgrade_success_Snd.play()
            upgradeDelay = True
            health.health = 100
            coinCt.coins -= 10
            healthUpSnd.play()
        elif key[pygame.K_2] and coinCt.coins >= 30 and fireRate > 1 and upgradeDelay == False:
            #Fire Rate Up
            upgrade_success_Snd.play()
            upgradeDelay = True
            if fireRate != 2:
                fireRate -= 1
            coinCt.coins -= 30
        elif key[pygame.K_3] and coinCt.coins >= 30 and upgradeDelay == False:
            #Shield Activate
            upgrade_success_Snd.play()
            upgradeDelay = True
            isShieldOn = True
            coinCt.coins -= 45
        elif key[pygame.K_4] and coinCt.coins >= 40 and upgradeDelay == False:
            #Double Guns
            upgrade_success_Snd.play()
            upgradeDelay = True
            dGuns = True
            coinCt.coins -= 60
        elif key[pygame.K_5] and coinCt.coins >= 20 and upgradeDelay == False:
            #Speed Up
            upgrade_success_Snd.play()
            upgradeDelay = True
            car.dx += 3
            car.dy += 3
            coinCt.coins -= 20

        if isShieldOn == True:
            shieldTimer += 1
        if shieldTimer >= 250:
            isShieldOn = False
            shieldTimer = 0

        if upgradeDelay == True:
            upgradeDelayTimer += 1
        if upgradeDelayTimer >= 100:
            upgradeDelay = False

        car.particleEmitter.x = car.rect.x + car.rect.width / 2
        car.particleEmitter.y = car.rect.y + car.rect.height - 10

        ###################################################
        ##################Respawns timers##################
        ###################################################

        if seconds % 1500 == 0:
            for z in range(5):
                speed = random.randrange(5, 15)
                zombieOne = ZombieOne(car, speed, obstacle1)
                ZombieOneList.append(zombieOne)
            zombieGRP = pygame.sprite.Group(ZombieOneList)
                    
        #Car shooting gun
        if key[pygame.K_SPACE] and dGuns == True:
            if seconds % fireRate == 0:
                car.shootBoth()
                gunSnd.play()
        elif key[pygame.K_SPACE]:
            if seconds % fireRate == 0:
                car.shootGun()
                gunSnd.play()

        #Pause
        if key[pygame.K_ESCAPE]:
            donePlaying = pauseScreen()
            if donePlaying == True:
                pygame.quit()
                


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
                bloodSpread = bloodExp(currX,currY,'zombie')
                all_sprites.add(bloodSpread)
                if seconds % 3 == 0:
                    coinList.append(coinDrop(currX, currY))
                z.reset()
        coinGRP = pygame.sprite.Group(coinList)




        #collision handling for coins, coin number 1 or 5, play pick up coin sound
        coinCollide = pygame.sprite.groupcollide(coinGRP, spriteGRP, True, False)
        if coinCollide:
            pickCoinSnd.play()
            coinCt.coins += random.randrange(1,5)
            for c in coinCollide:
                c.reset()
            
            

        #collision handling for zombie attacking player
        carCollided = pygame.sprite.groupcollide(zombieGRP, spriteGRP, False, False)
        if carCollided:
            if isShieldOn == False:
                health.health -= random.randrange(1,10)
            if health.health <= 0:
                seconds = 0
                donePlaying = True
        for z in carCollided:
            z.reset()


        #Collision for obstacles
        carCrash = pygame.sprite.groupcollide(obstacleGRP, spriteGRP, False, False, pygame.sprite.collide_mask)
        if carCrash:
            if isShieldOn == False:
                health.health /= 101
            if health.health <= 0:
                crashSnd.play()
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
        upgradeGRP.clear(screen, backDrop)

        roadGRP.update()
        spriteGRP.update()
        gunGRP.update()
        coinGRP.update()
        coinCtGRP.update()
        obstacleGRP.update()
        zombieGRP.update(car)
        scoreGRP.update()
        healthGRP.update()
        upgradeGRP.update(coinCt.coins)
    
        roadGRP.draw(screen)
        obstacleGRP.draw(screen)
        zombieGRP.draw(screen)
        coinGRP.draw(screen)
        coinCtGRP.draw(screen)
        car.particleEmitter.draw(screen)
        spriteGRP.draw(screen)
        gunGRP.draw(screen)
        scoreGRP.draw(screen)
        healthGRP.draw(screen)
        upgradeGRP.draw(screen)

        all_sprites.draw(screen)
        
        #see dirty rect animation
        pygame.display.flip()

    pygame.mouse.set_visible(True)
    return score.score

