import pygame
import random

class FloorObstacle(pygame.sprite.Sprite):
  def __init__(self, screen_width):
    super().__init__()
    
    self.images = [
      pygame.image.load('assets/imgs/obstacle1.png'),
      pygame.image.load('assets/imgs/obstacle2.png'),
      pygame.image.load('assets/imgs/obstacle3.png'),
    ]
    self.image = random.choice(self.images)
    
    self.real_space = pygame.Surface((90, 150))
    self.real_space.fill((255, 0, 0))
    # self.image.blit(self.real_space, (10, 0))
    self.rect = self.real_space.get_rect()
    
    self.rect.x = screen_width
    self.rect.y = 450
  
  def update(self, velocity):
    self.rect.x -= velocity
