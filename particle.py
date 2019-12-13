import pygame
import math
import random

class ParticleEmitter():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.deadParticles = []
        self.maxParticles = 10

    def newParticle(self, offsetx, offsety, color, xvel, yvel, ttl):
        p = None
        if len(self.deadParticles) > 0:
            p = self.deadParticles.pop()
            p.x = offsetx
            p.y = offsety
            p.color = color
            p.xvel = xvel
            p.yvel = yvel
            p.ttl = ttl
            p.timeAlive = 0
            p.alive = True
        else:
            p = Particle(offsetx, offsety, color, xvel, yvel, ttl)
        self.particles.append(p)

    def update(self):
        if(random.randint(0,10) > 5):
            self.newParticle(self.x, self.y, (96, 91, 86), random.uniform(-5,5), 7, random.uniform(1,10))
        for p in self.particles:
            p.update()
            if not p.alive:
                self.particles.remove(p)
                self.deadParticles.append(p)

    def draw(self,surface):
        for p in self.particles:
            pygame.draw.circle(surface, p.color, (int(p.x),int(p.y)), int(2 * (p.ttl - p.timeAlive)))

class Particle():
    def __init__(self, x, y, color, xvel, yvel, ttl):
        self.x = x
        self.y = y
        self.color = color
        self.xvel = xvel
        self.yvel = yvel
        self.ttl  = ttl
        self.timeAlive = 0
        self.alive = True

    def update(self):
        self.x += self.xvel
        self.y += self.yvel
        self.timeAlive += 1

        if self.timeAlive >= self.ttl:
            self.alive = False
            return
