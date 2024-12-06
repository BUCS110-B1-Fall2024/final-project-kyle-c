import pygame
import time


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
        
