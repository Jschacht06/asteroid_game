import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self,x ,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        return pygame.draw.circle(screen,"white",self.position,self.radius, LINE_WIDTH)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            vector_positive = self.velocity.rotate(angle)
            vector_negative = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid1.velocity = vector_positive*1.2
            new_asteroid2.velocity = vector_negative*1.2
            
            
    
    
