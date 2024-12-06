import pygame
import time
import random

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
