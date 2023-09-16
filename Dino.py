import pygame

class Dino(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.floor = 400
    
    self.image = pygame.image.load('assets/dino.png')
    self.image = pygame.transform.scale(self.image, (200, 200))
    
    self.real_space = pygame.Surface((140, 120))    
    # self.image.blit(self.real_space, (30, 40))
    self.rect = self.real_space.get_rect()
    
    self.rect.x = 30
    self.rect.y = self.floor
    
    self.velocity_y = 0
    self.gravity = 0.5
    self.jump_height = 13
    self.in_floor = True
    self.animation = False
    self.is_mini = False
  
  def update(self):
    if self.animation:
      self.velocity_y -= 4
      self.animation = False
    
    self.velocity_y += self.gravity
    self.rect.y += self.velocity_y
    if self.rect.y >= self.floor:
      self.rect.y = self.floor
      self.velocity_y = 0
      self.in_floor = True
      self.animation = True
  
  def jump(self):
    if self.in_floor and not self.is_mini:
      self.in_floor = False
      self.velocity_y = -self.jump_height
  
  def collide(self, obstacles):
    for obstacle in obstacles:
      if pygame.sprite.collide_rect(self, obstacle):
        return True
    return False
  
  def mini_size(self):
    self.is_mini = True
    self.image = pygame.transform.scale(self.image, (150, 150))
    self.real_space = pygame.Surface((180, 150))    
    self.floor += 50
    self.gravity = 0.8
  
  def normal_size(self):
    self.is_mini = False
    self.image = pygame.transform.scale(self.image, (200, 200))
    self.real_space = pygame.Surface((180, 150))    
    self.floor -= 50
    self.gravity = 0.5