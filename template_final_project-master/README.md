
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Space Invaders >>
## CS110 B1 Final Project  << Semester 1, Year 1 >>

## Team Members

<< Kyle Coichy >>

***

## Project Description

<< Recreate the classic arcade game Space Invaders where the user will be able to control a battleship by moving it left to right. The battleship will automatically fire lasers towards enemy alien invaders and when these enemies get hit by the lasers, they get destroyed. However, the alien invaders are able to fire back at the battleship so the user must also try to dodge; if the battleship gets hit, the user loses a life. When the user loses all 3 lives, the game is over. Also as the battleship destroys enermy invaders, the users will gain score points.>>

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. << Moveable character >>
2. << Killable enemies >>
3. << Score Counter >>
4. << Number of Lives Counter >>
5. << Laser gun to shoot projectiles >>

### Classes

- << 1.Player Class

Description: This class represents the player's spaceship. It allows the spaceship to move left and right using the arrow keys and shoot bullets upwards using the spacebar.

2. Bullet Class

Description: This class represents both the player's and enemy's bullets. It handles the creation of bullets and their movement upwards or downwards.

3. Enemy Class

Description: Represents an enemy invader. It is responsible for the enemy's movement, boundary behavior, and shooting mechanics.

4. EnemyBullet Class

Description: Represents bullets fired by enemies. The bullets move downward at a slower speed compared to the player's bullets.

 >>

## ATP


| **Test Case**             | **Test Description**                                                                                     | **Test Steps**                                                                                                                                                   | **Expected Outcome**                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Test Case 1: Player Movement**    | Verify that the player's spaceship moves left and right as expected.                                    | 1. Start the game. <br> 2. Press the left arrow key. <br> 3. Verify that the spaceship moves left. <br> 4. Press the right arrow key. <br> 5. Verify that the spaceship moves right. | The player's spaceship should move left and right in response to the arrow key inputs.                         |
| **Test Case 2: Shooting Mechanism**  | Verify that the player can shoot bullets correctly.                                                      | 1. Start the game. <br> 2. Press the space bar to fire a bullet. <br> 3. Verify that a bullet is fired from the spaceship. <br> 4. Press space again to fire another bullet. | The player's spaceship should fire bullets in response to the space bar press.                                 |
| **Test Case 3: Enemy Movement**     | Ensure that the enemies move across the screen correctly.                                                | 1. Start the game. <br> 2. Wait for enemies to begin moving. <br> 3. Observe the movement pattern of the enemies. <br> 4. Verify that enemies move left and right, and down as intended. | Enemies should move horizontally across the screen and descend periodically.                                  |
| **Test Case 4: Player-Enemy Collision** | Ensure that the game correctly detects a collision between the player’s bullet and an enemy ship.       | 1. Start the game. <br> 2. Fire a bullet towards an enemy ship. <br> 3. Verify that the bullet collides with the enemy. <br> 4. Confirm that the enemy ship is destroyed. | The bullet should hit and destroy the enemy ship when they collide.                                           |
| **Test Case 5: Game Over Condition** | Verify that the game ends when the player's spaceship is hit by an enemy or when the enemies reach the bottom. | 1. Start the game. <br> 2. Allow the enemy ships to hit the player's spaceship. <br> 3. Verify that the game ends with a "Game Over" message. <br> 4. Alternatively, let the enemies reach the bottom of the screen. | The game should end and display a "Game Over" message when the player’s spaceship is hit or when enemies reach the bottom. |
| **Test Case 6: Player Score Tracking** | Verify that the player's score updates correctly when an enemy is destroyed.                              | 1. Start the game. <br> 2. Destroy an enemy by shooting it with a bullet. <br> 3. Verify that the player's score increases. <br> 4. Destroy multiple enemies and verify the score increases with each kill. | The player's score should increase by the correct amount each time an enemy ship is destroyed.                |
| **Test Case 7: Level Up Mechanism** | This test verifies that the game properly handles the level-up process when all enemies are defeated. The level-up should increase the enemy count and increase their speed. | 1. Start the game. <br> 2. Play through the initial level and defeat all enemies. <br> 3. Verify that after defeating all enemies, the level-up process occurs. <br> 4. Verify that the enemy count increases (based on the level). <br> 5. Verify that the enemy shoot rate decreases (i.e., enemies shoot faster). <br> 6. Verify that enemy speed increases (enemies should move faster). | - After defeating all enemies, the game should automatically level up. <br> - The number of enemies should increase. <br> - The enemies should shoot more frequently. <br> - The enemies should move faster as the level increases. |
