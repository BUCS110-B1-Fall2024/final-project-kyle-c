from src.player import Player
from src.bullet import Bullet
from src.enemy import Enemy
from src.enemybullet import EnemyBullet
import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ENEMY_SHOOT_RATE = 1500  # Time between each enemy's shot (in ms)
ENEMY_COUNT = 3
START_LIVES = 3
ENEMY_RESPAWN_COUNT = 3  # Maximum number of enemies on the screen at once
ENEMY_SPEED_INCREMENT = 0.5  # Increase the speed of enemies after each level
ENEMY_SHOOT_SPEED_DECREMENT = 50  # Increase shooting speed (decrease time between shots)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Game clock
clock = pygame.time.Clock()

# Load font for scoring and lives
font = pygame.font.SysFont("Arial", 24)
game_over_font = pygame.font.SysFont("Arial", 48)
start_menu_font = pygame.font.SysFont("Arial", 36)

# The Player and Enemy classes would be implemented elsewhere (not shown here for brevity)


class Controller:
    def __init__(self):
        """
        Initializes the game, sets up the player, enemies, and other resources required to run the game.
        """
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self.enemies = pygame.sprite.Group()
        for i in range(ENEMY_COUNT):
            enemy = Enemy(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, 200), 2, ENEMY_SHOOT_RATE)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        self.lives = START_LIVES
        self.score = 0
        self.level = 1
        self.game_over = False
        self.game_started = False
        self.running = True

    def draw_lives_score_level(self):
        """
        Draws the lives, score, and level on the screen.
        """
        lives_text = font.render(f"Lives: {self.lives}", True, WHITE)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        level_text = font.render(f"Level: {self.level}", True, WHITE)
        screen.blit(lives_text, (10, 10))
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))
        screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 10))

    def level_up(self):
        """
        Handles the level-up process by increasing the level, decreasing the enemy shoot rate, and increasing enemy speed.
        """
        self.level += 1
        global ENEMY_SHOOT_RATE, ENEMY_COUNT, enemies, all_sprites

        ENEMY_SHOOT_RATE = max(500, ENEMY_SHOOT_RATE - ENEMY_SHOOT_SPEED_DECREMENT)
        enemy_speed = 2 + (self.level * ENEMY_SPEED_INCREMENT)

        if self.level > 1:
            ENEMY_COUNT = 3 + (self.level - 1) * 2

        enemy_width = 50
        enemy_height = 30
        cols = SCREEN_WIDTH // enemy_width
        rows = (ENEMY_COUNT // cols) + 1
        x_offset = 10
        y_offset = 10

        self.enemies.empty()

        for row in range(rows):
            for col in range(cols):
                if len(self.enemies) < ENEMY_COUNT:
                    x_pos = col * (enemy_width + x_offset)
                    y_pos = row * (enemy_height + y_offset)
                    if x_pos + enemy_width <= SCREEN_WIDTH and y_pos + enemy_height <= SCREEN_HEIGHT:
                        enemy = Enemy(x_pos, y_pos, enemy_speed, ENEMY_SHOOT_RATE)
                        self.all_sprites.add(enemy)
                        self.enemies.add(enemy)

    def game_over_screen(self):
        """
        Displays the "Game Over" screen with instructions to quit or restart.
        """
        game_over_text = game_over_font.render("GAME OVER", True, WHITE)
        restart_text = font.render("Press 'Q' to Quit", True, WHITE)

        screen.fill(BLACK)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()

    def start_menu(self):
        """
        Displays the start menu with instructions to start the game or quit.
        """
        start_text = start_menu_font.render("Space Invaders", True, WHITE)
        instructions_text = font.render("Press 'Enter' to Start or 'Q' to Quit", True, WHITE)

        screen.fill(BLACK)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()

    def handle_events(self):
        """
        Handles all events like key presses and quitting the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.game_over and self.game_started:
                    self.player.shoot()
                elif event.key == pygame.K_RETURN and not self.game_started:
                    self.start_game()
                elif event.key == pygame.K_q:
                    self.running = False
                elif event.key == pygame.K_r and self.game_over:
                    self.start_game()

    def start_game(self):
        """
        Starts or restarts the game.
        """
        self.game_started = True
        self.game_over = False
        self.lives = START_LIVES
        self.score = 0
        self.level = 1
        self.all_sprites.empty()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.enemies.empty()
        for i in range(ENEMY_COUNT):
            enemy = Enemy(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, 200), 2, ENEMY_SHOOT_RATE)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def game_loop(self):
        """
        Main game loop to handle the game logic and render frames.
        """
        while self.running:
            clock.tick(60)  # FPS limit
            self.handle_events()

            if self.game_started and not self.game_over:
                self.all_sprites.update()

                for bullet in self.bullets:
                    hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, True)
                    for enemy in hit_enemies:
                        bullet.kill()
                        self.score += 10

                for enemy_bullet in self.enemy_bullets:
                    if pygame.sprite.collide_rect(enemy_bullet, self.player):
                        enemy_bullet.kill()
                        self.lives -= 1
                        self.player.hit()
                        if self.lives == 0:
                            self.game_over = True

                if len(self.enemies) == 0:
                    self.level_up()

                screen.fill(BLACK)
                self.all_sprites.draw(screen)
                self.draw_lives_score_level()
                pygame.display.flip()

            elif not self.game_started:
                self.start_menu()
            else:
                self.game_over_screen()

        pygame.quit()
