import pygame
import random
import time
pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = (150, 200, 255)
RAD_RED = (255, 56, 100)
BLK_CHOCOLATE = (25, 17, 2)
NAVY_BLUE = (3, 4, 94)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Collecting Blocks"


class Player(pygame.sprite.Sprite):
    """Describes a player object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
        """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()
        # Create the image of the block
        self.image = pygame.image.load("./images/NPC_Timmie.png")
        self.image = pygame.transform.scale(self.image, (36, 81))
        # Based on the image, create a rectangle for the block
        self.rect = self.image.get_rect()
        self.lasttimecollided = 0

class Block(pygame.sprite.Sprite):
    """Describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
    """
    def __init__(self) -> None:
        """
        Arguments:

        """
        # Call the superclass constructor
        super().__init__()
        # Create the image of the block
        self.image = pygame.image.load("./images/Pigeon.png")
        self.image = pygame.transform.scale(self.image, (40, 42))

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    """The enemy sprites

    Attributes:
        image: Surface that is the visual representation
        rect: Rect (x, y, width height)
        x_vel: x velocity
        y_vel: y velocity
        """
    def __init__(self):
        """
        Arguments:

        """
        super().__init__()
        self.image = pygame.image.load("./images/tornado.png")
        self.image = pygame.transform.scale(self.image, (50, 62))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )

        # Define the initial velocity
        self.x_vel = random.choice([-3, -2, 2, 3])
        self.y_vel = random.choice([-3, -2, 2, 3])

    def update(self) -> None:
        """Calculates movement"""
        # Update the x-coordinate
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        # Constrain movement
        # X -
        if self.rect.left < 0:
            self.rect.left = 0
            self.x_vel = -self.x_vel # Bounce
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel
        # Y -
        if self.rect.top < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel # Bounce
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel



def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    global enemy
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    num_enemies = 10
    time_start = time.time()
    time_invincible = 5

    font = pygame.font.SysFont("Arial", 25)


    score = 0

    pygame.mouse.set_visible(False)

    # Create groups to hold sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # Create player block
    player = Player()
    # Add the player to all_sprites group
    all_sprites.add(player)
    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):
        # Create a block(set its parameters)
        block = Block()
        # Set a random location for the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)

        # Add the block to the block_sprites Group
        # Add the block to the all_sprites Group
        block_sprites.add(block)
        all_sprites.add(block)

    # Create enemy sprites
    for i in range(num_enemies):
        # Create an enemy
        enemy = Enemy()
        # Add it to the sprites list (enemy_sprites and all_sprites)
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)




    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        # if len(pygame.sprite.spritecollide(player, enemy_sprites, False)) > 1:
          #  done = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - player.rect.width / 2
        player.rect.y = mouse_pos[1] - player.rect.height / 2

        all_sprites.update()

        # Check all collisions between the player and all blocks
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)

        # Check all collisions between the player and all enemies
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        # Set a time for invincibility at the beginning of the
        if time.time() - time_start > time_invincible:
            for enemy in enemies_collided:
                if len(enemies_collided) > 1:
                    done = True
                    print("GAME OVER!!")


        for block in blocks_collided:
            score += 1
            print(f"Score: {score}")
        # mouse_pos = player.rect.x) + 3, player.rect.y

        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        for enemy in enemies_collided:
        # Add in lasttimecollided
            print(f"Enemy Collided!")


        # mouse_pos = player.rect.x) + 3, player.rect.y

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        # Draw the score on the screen



        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)
        )

        screen.blit(
            font.render(f"Lives left: {10 - score}", True, BLACK),
            (5, 5)
        )
        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()