class Controller:
    def __init__(self):
        """
        Initializes the game objects and resources.
        Sets up the screen, ships, enemies, etc.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.ship = Ship(400, 500, "ship_image.png")
        self.enemies = [Enemy(100, 100, "enemy_image.png"), Enemy(200, 100, "enemy_image.png")]
        self.bullets = []

    def mainloop(self):
        """
        Main game loop. Handles events, updates models, and redraws frames.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Handle key events (movement and shooting)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.ship.move_right()
                    elif event.key == pygame.K_SPACE:
                        bullet = self.ship.shoot()
                        self.bullets.append(bullet)

            # Update models (move bullets, enemies, etc.)
            for bullet in self.bullets:
                bullet.move_up()
            
            for enemy in self.enemies:
                enemy.move_down()

            # Redraw the screen
            self.screen.fill((0, 0, 0))  # Fill with black
            self.screen.blit(pygame.image.load(self.ship.img_file), (self.ship.x, self.ship.y))

            for bullet in self.bullets:
                pygame.draw.rect(self.screen, (255, 0, 0), (bullet.x, bullet.y, 5, 10))

            for enemy in self.enemies:
                self.screen.blit(pygame.image.load(enemy.img_file), (enemy.x, enemy.y))

            # Display the next frame
            pygame.display.flip()

# Entry point for the program
if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
