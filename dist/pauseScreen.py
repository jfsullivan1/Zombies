#Pause function

import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((1200, 750))

def pauseScreen():
    pauseFont = pygame.font.SysFont("dutch", 80)
    pauseText = "Paused. Esc to resume."
    pauseText = pauseFont.render(pauseText, 1, (0, 215, 0))

    stillPaused = True
    clock = pygame.time.Clock()
    
    while stillPaused:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.blit(pauseText, (100, 250))

        pygame.display.flip()
