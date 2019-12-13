#Pause function

import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((1400, 750))

def pauseScreen():
    pauseFont = pygame.font.SysFont("dutch", 80)
    pauseText = "Paused. Spacebar to resume."
    pauseText = pauseFont.render(pauseText, 1, (0, 215, 0))

    stillPaused = True
    clock = pygame.time.Clock()
    
    while stillPaused:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False
            if event.type == pygame.QUIT:
                return True

        screen.blit(pauseText, (100, 250))

        pygame.display.flip()
