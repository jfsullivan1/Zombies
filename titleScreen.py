#titlescreen.py

import pygame
import random
import math
pygame.init()
from carSprite import Vehicle
from zombieSprite import ZombieOne
from gunSprite import gunDefault
from backGround import BackGround
from score import Score
from health import Health
from helpMenu import helpScreen
from bloodSprite import bloodExp


myFont = pygame.font.Font("Fonts/csnpwdt NFI.otf", 70)
screen = pygame.display.set_mode((1400, 750))
#define screen title
screen_title = "Zombie Roads V1.3"
pygame.display.set_caption(screen_title)

def titleScreen(score):
    backDrop = pygame.Surface(screen.get_size())
    backDrop.fill((0, 0, 0))
    screen.blit(backDrop, (0,0))
    road = BackGround()
    gun = pygame.sprite.Group()
    car = Vehicle(gun)
    sprites = pygame.sprite.Group(road, car)
    

    
    text = (
        "Zombie Road\n",
        "\n",
        "Your last score was: %d" %score,
        )
    
    label = []
    for line in text:
        temp = myFont.render(line, 1, (150, 100, 100))
        label.append(temp)

    donePlaying = False
    helpClicked = False
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepGoing:
        mouse = pygame.mouse.get_pos()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 550 > mouse[0] > 350 and 550 > mouse[1] > 450:   
                    keepGoing = False
                    donePlaying = False
                if 955 > mouse[0] > 750 and 550 > mouse[1] > 450:
                    keepGoing = False
                    donePlaying = True
                if 752 > mouse[0] > 550 and 710 > mouse[1] > 600:
                    helpClicked = True
                    while helpClicked == True:
                        keepGoing, helpClicked, donePlaying = helpScreen()
                     
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
        sprites.clear(screen, backDrop)
        sprites.update()
        sprites.draw(screen)
        event = pygame.event.get()
        for i in range(len(label)):
            screen.blit(label[i], (100, 70*i))
            
        #Draw play button
        pygame.draw.rect(screen, (0,0,255),(350,450,200,100))
        screen.blit(myFont.render('PLAY', False, (0,255,0)), (371, 417))

        #Draw Quit button
        pygame.draw.rect(screen, (0,0,255),(750,450,200,100))
        screen.blit(myFont.render('QUIT', False, (0,255,0)), (790, 417))

        #Draw help button
        pygame.draw.rect(screen, (0,0,255),(551,600,200,100))
        screen.blit(myFont.render('HELP', False, (0,255,0)), (580, 570))

        #Play button mouseover reaction
        if 550 > mouse[0] > 350 and 550 > mouse[1] > 450:
                pygame.draw.rect(screen, (50,0,0),(350,450,200,100))
                screen.blit(myFont.render('PLAY', True, (0,255,0)), (371, 417))

        #Quit button mouseover reaction 
        if 955 > mouse[0] > 750 and 550 > mouse[1] > 450:
                pygame.draw.rect(screen, (50,0,0),(750,450,200,100))
                screen.blit(myFont.render('QUIT', True, (0,255,0)), (790, 417))

        #Help button mouseover reaction
        if 752 > mouse[0] > 550 and 710 > mouse[1] > 600:
                pygame.draw.rect(screen, (50,0,0),(551,600,200,100))
                screen.blit(myFont.render('HELP', True, (0,255,0)), (580, 570))

        pygame.display.flip()

    pygame.mouse.set_visible(True)
    return donePlaying
