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
# Initial number of enemies
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

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5
        self.hit_time = 0  # Tracks when the player was last hit
        self.flash_duration = 200  # Duration for flash effect (milliseconds)
        self.is_flash = False  # Determines if the flash effect is active

    def update(self):
        # Flash effect logic: If the player is flashing, change their color temporarily
        if self.is_flash and pygame.time.get_ticks() - self.hit_time < self.flash_duration:
            self.image.fill(RED)  # Flash red when hit
        else:
            self.image.fill(GREEN)  # Normal color when not flashing
            if pygame.time.get_ticks() - self.hit_time >= self.flash_duration:
                self.is_flash = False  # Reset the flash state after duration ends
        
        # Movement logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def hit(self):
        self.hit_time = pygame.time.get_ticks()  # Set the time of the hit
        self.is_flash = True  # Activate the flash effect
        # Movement logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def hit(self):
        self.hit_time = pygame.time.get_ticks()  # Set the time of the hit
        self.is_flash = True  # Activate the flash effect
        
# Bullet class for player and enemy bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))  # Corrected this line
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
            
# Enemy class with sequential shooting logic
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, shoot_rate):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.shoot_rate = shoot_rate
        self.last_shot_time = 0  # Keep track of the last time the enemy shot

    def update(self):
        # Move enemy horizontally
        self.rect.x += self.speed
        
        # Check for screen boundaries
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed = -self.speed  # Reverse direction
            self.rect.y += 20  # Move down after hitting a boundary to simulate invader behavior

        # Check if the enemy can shoot
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_rate:  # Check if enough time has passed
            self.shoot()
            self.last_shot_time = current_time  # Update the last shot time

    def shoot(self):
        enemy_bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(enemy_bullet)
        enemy_bullets.add(enemy_bullet)
        
# Enemy Bullet class
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = 2  # Slower speed for enemy bullets

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Setup the game
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
bullets = pygame.sprite.Group()

# Initial enemies with base speed and shoot rate
enemies = pygame.sprite.Group()
for i in range(ENEMY_COUNT):
    enemy = Enemy(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, 200), 2, ENEMY_SHOOT_RATE)
    all_sprites.add(enemy)
    enemies.add(enemy)

enemy_bullets = pygame.sprite.Group()

# Game Variables
lives = START_LIVES
score = 0
level = 1  # Start at level 1

# Function to draw lives, score, and level
def draw_lives_score_level():
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(lives_text, (10, 10))
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))
    screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 10))

# Function to spawn new enemies

# Function to handle level-up
def level_up():
    global level, ENEMY_SHOOT_RATE, ENEMY_COUNT, enemies, all_sprites

    level += 1  # Increment level after completing current level
    
    # Adjust the shoot rate (decrease time between shots) and increase enemy speed
    ENEMY_SHOOT_RATE = max(500, ENEMY_SHOOT_RATE - ENEMY_SHOOT_SPEED_DECREMENT)  # Set a lower shoot rate but not below 500ms
    enemy_speed = 2 + (level * ENEMY_SPEED_INCREMENT)  # Increase enemy speed with each level
    
    # Increase the number of enemies as the level progresses
    # For example, after level 1, spawn more enemies, starting with 3 on reset
    if level > 1:
        ENEMY_COUNT = 3 + (level - 1) * 2  # Add 2 more enemies per level (you can adjust this multiplier)

    # Spawn enemies within the screen's dimensions, ensuring they fit
    enemy_width = 50
    enemy_height = 30
    cols = SCREEN_WIDTH // enemy_width  # Max number of enemies that can fit in one row
    rows = (ENEMY_COUNT // cols) + 1  # Max number of rows to fit all enemies
    x_offset = 10  # Horizontal spacing between enemies
    y_offset = 10  # Vertical spacing between enemies

    # Clear any existing enemies to avoid duplicates after level-up
    enemies.empty()

    # Spawn new enemies according to the level and count
    for row in range(rows):
        for col in range(cols):
            if len(enemies) < ENEMY_COUNT:
                x_pos = col * (enemy_width + x_offset)
                y_pos = row * (enemy_height + y_offset)

                # Ensure enemies spawn within the screen's width and height
                if x_pos + enemy_width <= SCREEN_WIDTH and y_pos + enemy_height <= SCREEN_HEIGHT:
                    enemy = Enemy(x_pos, y_pos, enemy_speed, ENEMY_SHOOT_RATE)
                    all_sprites.add(enemy)
                    enemies.add(enemy)

# Function to display the "Game Over" screen
def game_over_screen():
    game_over_text = game_over_font.render("GAME OVER", True, WHITE)
    restart_text = font.render("Press 'Q' to Quit", True, WHITE)
    
    # Display "Game Over" text and restart instructions
    screen.fill(BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

# Function to display the Start Menu
def start_menu():
    start_text = start_menu_font.render("Space Invaders", True, WHITE)
    instructions_text = font.render("Press 'Enter' to Start or 'Q' to Quit", True, WHITE)
    
    # Display start menu text
    screen.fill(BLACK)
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

# Game loop
running = True
game_over = False
game_started = False

while running:
    clock.tick(60)  # FPS limit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over and game_started:
                player.shoot()
            elif event.key == pygame.K_RETURN and not game_started:  # Start game on 'Enter'
                game_started = True
                game_over = False
                lives = START_LIVES
                score = 0
                level = 1
                all_sprites.empty()
                player = Player()
                all_sprites.add(player)
                enemies.empty()
                for i in range(ENEMY_COUNT):
                    enemy = Enemy(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, 200), 2, ENEMY_SHOOT_RATE)
                    all_sprites.add(enemy)
                    enemies.add(enemy)
            elif event.key == pygame.K_q:  # Quit the game on 'Q'
                running = False
            elif event.key == pygame.K_r and game_over:  # Restart game on 'R'
                game_started = True
                game_over = False
                lives = START_LIVES
                score = 0
                level = 1
                all_sprites.empty()
                player = Player()
                all_sprites.add(player)
                enemies.empty()
                for i in range(ENEMY_COUNT):
                    enemy = Enemy(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, 200), 2, ENEMY_SHOOT_RATE)
                    all_sprites.add(enemy)
                    enemies.add(enemy)

    if game_started and not game_over:
        all_sprites.update()

        # Handle collisions between player bullets and enemies
        for bullet in bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, True)
            for enemy in hit_enemies:
                bullet.kill()
                score += 10

        # Handle collisions between enemy bullets and player
        for enemy_bullet in enemy_bullets:
            if pygame.sprite.collide_rect(enemy_bullet, player):
                enemy_bullet.kill()
                lives -= 1
                player.hit()  # Trigger hit effect when player is hit by enemy bullet
                if lives == 0:
                    game_over = True

        # Respawn new enemies after level-up
        if len(enemies) == 0:  # All enemies defeated
            level_up()
        
        # Draw the background
        screen.fill(BLACK)

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score, lives, and level
        draw_lives_score_level()

        pygame.display.flip()  # Update screen
    elif not game_started:
        # Show start menu
        start_menu()
    else:
        # Show game over screen
        game_over_screen()
    
# Quit pygame
pygame.quit()
