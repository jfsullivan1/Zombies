 #Main and death screen (Written by john sullivan)

import pygame
import random
import math
import time
pygame.init()


if not pygame.mixer:
    print ("problem with sound")
else:
    pygame.mixer.init()


#.py imports
from carSprite import Vehicle
from zombieSprite import ZombieOne
from gunSprite import gunDefault
from backGround import BackGround
from score import Score
from health import Health
from gameScreen import gameScreen
from titleScreen import titleScreen
from obstacle import obstacleOne

#Code for the actual window itself
screen = pygame.display.set_mode((1400, 750))
#define screen title
screen_title = 'Zombie Roads V1.3'
pygame.display.set_caption(screen_title)

#Screen that pops up when you die
def DeathScreen():
    deathFont = pygame.font.Font("Fonts/csnpwdt NFI.otf", 200)
   
    message = "YOU DIED!"
    message = deathFont.render(message, 1, (255, 255, 0))
    
    screen.blit(message, (400, 200))

    #This is necessary, dont ask why
    pygame.display.flip()

def main():
    donePlaying = False
    lastHighScore = 0
    clock = pygame.time.Clock()
    seconds = 0
    while not donePlaying:
        clock.tick(30)
        donePlaying = titleScreen(lastHighScore)
        if not donePlaying:
            lastHighScore = gameScreen()
            while seconds < 200:
                DeathScreen()
                seconds += 1
            seconds = 0
        elif donePlaying == True:
            pygame.quit()

if __name__ == "__main__":
    main()

