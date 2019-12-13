#Help Screen

import pygame
import random
import math

pygame.init()

myFont = pygame.font.SysFont("Comic Sans MS", 35)
screen = pygame.display.set_mode((1400, 750))

#from backGround import BackGround


def helpScreen():
    #road = BackGround()
    #back = pygame.sprite.Group(road)
    helpBackground = pygame.image.load("Sprites/helpBack.jpg")
    helpBackground = pygame.transform.scale(helpBackground, (1200,1300))
    text = (
        "Welcome to Zombie Road",
        "",
        "To play, click the Play button on the main menu",
        "Your goal is to kill zombies with your gun and",
        "collect coins to purchase car/gun upgrades",
        "Make sure you avoid obstacles!",
        "INSTRUCTIONS:",
        "Use arrow keys to move, shoot with spacebar,",
        "use the ESC key to pause, and aim for a high score!",
        "Use the 1, 2, 3, 4 and 5 keys to purchase corresponding upgrades.",
        "The game will increasingly get harder as time goes on",
        "Good luck!"
        )

    helpIns = []
    i = 0
    for line in text:
        if i == 6:
            temp = myFont.render(line, 1, (255, 0, 0))
        elif i > 6:
            temp = myFont.render(line, 1, (0, 255, 255))
        else:
            temp = myFont.render(line, 1, (10, 10, 5))
        helpIns.append(temp)
        i += 1
        
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepGoing:
        mouse = pygame.mouse.get_pos()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False, True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True, False, False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1100 > mouse[0] > 900 and 130 > mouse[1] > 30:
                    return True, False, False
        
        #back.update()
        #back.draw(screen)
        screen.blit((helpBackground),(0, 0))

        #Draw Back button
        pygame.draw.rect(screen, (0,0,0),(900,30,200,100))
        screen.blit(myFont.render('Main Menu', False, (255,255,255)), (900, 45))
        if 1100 > mouse[0] > 900 and 130 > mouse[1] > 30:
                pygame.draw.rect(screen, (255,255,255),(900,30,200,100))
                screen.blit(myFont.render('Main Menu', True, (0,0,0)), (900, 45))
        
        for i in range(len(helpIns)):
            screen.blit(helpIns[i], (100, 55*i))

    
        pygame.display.flip()

    
    
