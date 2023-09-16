import pygame
import sys
import random

from Dino import Dino
from Scenario import Scenario
from FloorObstacle import FloorObstacle
from SkyObstacle import SkyObstacle

#CONFIGS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
INITIAL_VELOCITY = 6

pygame.init()
pygame.mixer.init()

#Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dino Game')
pygame.font.init()

#Load images
background_image = pygame.image.load('assets/imgs/background.png')
background_size = background_image.get_size()

#Load sounds
game_over_sound = pygame.mixer.Sound('assets/sounds/game_over.mp3')
jump_sound = pygame.mixer.Sound('assets/sounds/jump.mp3')
mini_sound = pygame.mixer.Sound('assets/sounds/mini.mp3')

dino = Dino()
scenario = Scenario(screen, background_image, background_size, INITIAL_VELOCITY)
obstacles = pygame.sprite.Group()
font = pygame.font.Font(None, 36)

score = 0
velocity = INITIAL_VELOCITY
min_space_obstacle = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        dino.jump()
        jump_sound.play()
      elif event.key == pygame.K_DOWN:
        dino.mini_size()
        mini_sound.play()
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        dino.normal_size()
  
  
  # Create obstacles
  if min_space_obstacle >= 90:
    random_number = random.randint(0, 500)
    if random_number <= 50:
      min_space_obstacle = 30
      obstacle = FloorObstacle(SCREEN_WIDTH)
      obstacles.add(obstacle)
    elif random_number <= 100:
      min_space_obstacle = 0
      obstacle = SkyObstacle(SCREEN_WIDTH)
      obstacles.add(obstacle)
  else:
      min_space_obstacle += 1
      
  if score % 650 == 0:
    velocity += 1
           
  # Update
  scenario.update(velocity)
  dino.update()
  obstacles.update(velocity)
  
  # Check collision
  if dino.collide(obstacles):
    # Display game over
    game_over_text = font.render('Game Over', True, (255, 255, 255))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    #Display score
    score_text = font.render(
      f'Pontuação: {score // 60}', True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()
    game_over_sound.play()
    pygame.time.wait(int(game_over_sound.get_length() * 1000))
    pygame.quit()
  
  # Clear screen
  screen.fill((0, 0, 0))

  # Desenha o cenário
  screen.blit(scenario.background, (scenario.background_x, 0))
  screen.blit(scenario.background, (scenario.background_x + scenario.background_width, 0))

  # Desenha o jogador
  screen.blit(dino.image, (dino.rect.x, dino.rect.y))
  
  # Desenha os obstáculos
  obstacles.draw(screen)
  
  # Renderiza a pontuação
  time_text = font.render(
    f'Pontuação: {score // 60}', True, (255, 255, 255))
  screen.blit(time_text, (SCREEN_WIDTH - 200, 5))

  pygame.display.flip()
  score += 1