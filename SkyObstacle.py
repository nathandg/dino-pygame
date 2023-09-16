import pygame

class SkyObstacle(pygame.sprite.Sprite):
  def __init__(self, screen_width):
    super().__init__()
    
    self.image = pygame.image.load('assets/fireball.png')
    self.image = pygame.transform.scale(self.image, (300, 100))
    
    self.real_space = pygame.Surface((200, 60))
    self.real_space.fill((255, 0, 0))
    # self.image.blit(self.real_space, (0, 0))
    self.rect = self.real_space.get_rect()
    
    self.rect.x = screen_width
    self.rect.y = 360
  
  def update(self, velocity):
    self.rect.x -= velocity