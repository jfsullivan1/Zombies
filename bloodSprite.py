#commit by Guanqiao Wang
#blood six pngs originally credit by <http://powstudios.com/> and change made by
# borix134 on <https://opengameart.org/content/blood-effect-sprite-sheet>
import pygame
from os import path

screen = pygame.display.set_mode((1400, 750))

blood_anim = {}
blood_anim['zombie'] = []
blood_dir = ('Sprites')

class bloodExp(pygame.sprite.Sprite):
    for i in range(6):
        filename = 'tile0{}.png'.format(i)
        img = pygame.image.load(path.join(blood_dir,filename)).convert_alpha()
        img_zombie =pygame.transform.scale(img,(65,65))
        blood_anim['zombie'].append(img_zombie)
        
    def __init__(self,x,y,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = blood_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 20

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(blood_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = blood_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
