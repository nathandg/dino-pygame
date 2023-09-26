import pygame
import random

class SkyObstacle(pygame.sprite.Sprite):
  def __init__(self, screen_width):
    super().__init__()
    
    self.images = [
      pygame.image.load('assets/imgs/fireball.png'),
      pygame.image.load('assets/imgs/plane.png'), 
    ]
    self.image = random.choice(self.images)
    
    self.real_space = pygame.Surface((200, 60))
    self.real_space.fill((255, 0, 0))
    # self.image.blit(self.real_space, (0, 0))
    self.rect = self.real_space.get_rect()
    
    self.rect.x = screen_width
    self.rect.y = 360
  
  def update(self, velocity):
    self.rect.x -= velocity