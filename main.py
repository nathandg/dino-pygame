import pygame
import random

from Dino import Dino
from Scenario import Scenario
from FloorObstacle import FloorObstacle
from SkyObstacle import SkyObstacle

class DinoGame:
    def __init__(self):
        # Configs
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 700
        self.INITIAL_VELOCITY = 7

        pygame.init()
        pygame.mixer.init()

        # Screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Dino Game')
        pygame.font.init()

        # Background
        self.background_image = pygame.image.load('assets/imgs/background.png')
        self.background_size = self.background_image.get_size()

        # Sounds
        self.game_over_sound = pygame.mixer.Sound('assets/sounds/game_over.mp3')
        self.jump_sound = pygame.mixer.Sound('assets/sounds/jump.mp3')
        self.mini_sound = pygame.mixer.Sound('assets/sounds/mini.mp3')

        # Objects
        self.dino = Dino()
        self.scenario = Scenario(self.screen, self.background_image, self.background_size, self.INITIAL_VELOCITY)
        self.obstacles = pygame.sprite.Group()
        self.font = pygame.font.Font(None, 36)

        # Variables
        self.score = 0
        self.velocity = self.INITIAL_VELOCITY
        self.min_space_obstacle = 0

    def run(self):
      
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dino.jump()
                        self.jump_sound.play()
                    elif event.key == pygame.K_DOWN:
                        self.dino.mini_size()
                        self.mini_sound.play()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.dino.normal_size()


            # Create obstacles
            if self.min_space_obstacle >= random.randint(90, 150) - self.velocity:
                random_number = random.randint(0, 1000)
                if random_number <= 150:
                    self.min_space_obstacle = 30
                    obstacle = FloorObstacle(self.SCREEN_WIDTH)
                    self.obstacles.add(obstacle)
                elif random_number <= 200:
                    self.min_space_obstacle = 0
                    obstacle = SkyObstacle(self.SCREEN_WIDTH)
                    self.obstacles.add(obstacle)
            else:
                self.min_space_obstacle += 1
            
            # Remove obstacles
            for obstacle in self.obstacles:
                if obstacle.rect.x < -obstacle.rect.width:
                    self.obstacles.remove(obstacle)

            # Increase velocity
            if self.score % 650 == 0:
                self.velocity += 1

            # Update
            self.scenario.update(self.velocity)
            self.dino.update()
            self.obstacles.update(self.velocity)

            # Check collision
            if self.dino.collide(self.obstacles):
                game_over_text = self.font.render('Game Over', True, (255, 255, 255))
                self.screen.blit(game_over_text, (self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2))
                score_text = self.font.render(f'Pontuação: {self.score // 60}', True, (255, 255, 255))
                self.screen.blit(score_text, (self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 + 50))
                pygame.display.flip()
                self.game_over_sound.play()
                pygame.time.wait(int(self.game_over_sound.get_length() * 500))
                return

            # Draw background
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.scenario.background, (self.scenario.background_x, 0))
            self.screen.blit(self.scenario.background, (self.scenario.background_x + self.scenario.background_width, 0))

            # Draw player
            self.screen.blit(self.dino.image, (self.dino.rect.x, self.dino.rect.y))

            # Draw obstacles
            self.obstacles.draw(self.screen)

            # Draw score
            time_text = self.font.render(
                f'Pontuação: {self.score // 60}', True, (255, 255, 255))
            self.screen.blit(time_text, (self.SCREEN_WIDTH - 200, 5))

            pygame.display.flip()
            self.score += 1
            
if __name__ == '__main__':
  
  while True:
    game = DinoGame()
    game.run()
    pygame.quit()