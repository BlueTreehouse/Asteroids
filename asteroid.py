import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Create a transparent surface
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)  # Draw the asteroid as a circle on the surface
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))  # Position the rect 

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    