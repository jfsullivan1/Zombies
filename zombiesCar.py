#Car class code
#started by John Sullivan on 1/29/2019

import pygame
pygame.init()

class Vehicle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car7.jpg")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.dx = 8
        self.dy = 8
        self.rect.center = (400, 400)
    def up(self):
        self.rect.centery -= self.dy
    def down(self):
        self.rect.centery += self.dy
    def right(self):
        self.rect.centerx += self.dx
    def left(self):
        self.rect.centerx -= self.dx
def main():
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Zombies")

    backDrop = pygame.Surface(screen.get_size())
    backDrop.fill((0, 0, 0))
    screen.blit(backDrop, (0,0))

    car = Vehicle()

    spriteGRP = pygame.sprite.Group(car)
    
    clock = pygame.time.Clock()

    donePlaying = False

    while donePlaying == False:
        clock.tick(30)
        pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                donePlaying = True
    
    
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            car.left()
        if key[pygame.K_RIGHT]:
            car.right()
        if key[pygame.K_UP]:
            car.up()
        if key[pygame.K_DOWN]:
            car.down()


        spriteGRP.clear(screen, backDrop)
        spriteGRP.draw(screen)
        pygame.display.flip()

    pygame.mouse.set_visible(True)

if __name__ == "__main__":
    main()
        
