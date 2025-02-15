import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Create a transparent surface
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)  # Draw the asteroid as a circle on the surface
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))  # Position the rect 
        self.velocity = velocity if velocity is not None else pygame.math.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroid_group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.copy().rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.copy().rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

# creating new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity1)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity2)

# adding them to the asteroid_group
        asteroid_group.add(asteroid1)
        asteroid_group.add(asteroid2)


    