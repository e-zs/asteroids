import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen):
        pygame.draw.circle(screen, GOLD, (self.x, self.y), self.radius, width=2)
    
    def update(dt):
        super().position += super().velocity * dt