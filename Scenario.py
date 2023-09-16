import pygame

class Scenario:
  def __init__(self, screen, image, size, velocity):
    self.screen = screen
    self.velocity = velocity
    self.background = image
    self.background_x = 0
    self.background_width = size[0]
    self.background_height = size[1]
    self.time_elapsed = 0
    
  def update(self, velocity):
    self.velocity = velocity
        
    self.background_x -= self.velocity
    if self.background_x <= -self.background_width:
      self.background_x = 0