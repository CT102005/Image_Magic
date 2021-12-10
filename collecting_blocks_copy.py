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
        hp: describe how much
            health our player has
        """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()
        # Create the image of the block
        self.image = pygame.image.load("./images/NPC_Timmie.png")
        self.image = pygame.transform.scale(self.image, (24, 44))
        # Based on the image, create a rectangle for the block
        self.rect = self.image.get_rect()
        # Initial health points
        self.hp = 250

    def hp_remaining(self) -> float:
        """Return the percent of health remaining"""
        return self.hp / 250

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
        self.image = pygame.transform.scale(self.image, (60, 54))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )

        # Define the initial velocity
        self.x_vel = random.choice([-4, -3, 3, 4])
        self.y_vel = random.choice([-4, -3, 3, 4])

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

class Bullet(pygame.sprite.Sprite):
    """Bullet
    Attributes:
        image: visual representation
        rect: mathematical representation (hit box)
        vel_y: y velocity in px/sec
    """
    def __init__(self, coords: tuple):
        """
        Arguments:
            coords: tuple of (x,y) to represent initial location
        """
        super().__init__()

        self.image = pygame.Surface((5, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        # Set the middle of the bullet to be at coords
        self.rect.center = coords

        self.vel_y = 3

    def update(self):
        self.rect.y -= self.vel_y

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    global enemy
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_enemies = 15
    score = 0
    time_start = time.time()
    time_invincible = 5      # Seconds
    game_state = "running"
    endgame_cooldown = 5       # Seconds
    time_ended = 0.0

    endgame_messages = {
        "win": "Congratulations, you have collected the pigeons!", "lose": "Sorry, they got you and the pigeons. Play again."
    }

    font = pygame.font.SysFont("Arial", 25)


    score = 0

    pygame.mouse.set_visible(False)

    # Create groups to hold sprites
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

    # Create player block
    player = Player()
    # Add the player to all_sprites group
    all_sprites.add(player)

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
            if event.type == pygame.KEYDOWN:
                # We can't create a bullet when:
                    # Initial cooldown
                    # When there are three on the screen
                if len(bullet_sprites) < 3 and time.time() - time_start > time_invincible:

                    # Create a bullet
                    bullet = Bullet(player.rect.midtop)

                    # TODO: Add it to the allsprites group
                    bullet_sprites.add(bullet)
                    all_sprites.add(bullet)


        # End-game Listener
        # Indicate to draw a message

        # SET THE TIME THAT THE GAME WAS WON

        # TODO: LOSE CONDITION - Player's hp goes below 0
        if player.hp_remaining() <= 0:
            game_state = "lose"
            time.time(5) #TODO: fix this bug
            done = True
            print("GAME OVER")

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - player.rect.width / 2
        player.rect.y = mouse_pos[1] - player.rect.height / 2

        all_sprites.update()

        # Check all collisions between the player and all blocks


        # Check all collisions between the player and all enemies
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)


        # Set a time for invincibility at the beginning of the

                # if len(enemies_collided) > 1:

        # mouse_pos = player.rect.x) + 3, player.rect.y

        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        for enemy in enemies_collided:
        # TODO Add in last time collided
            print(f"Enemy Collided!")

        for bullet in bullet_sprites:
            if bullet.rect.y < 0:
                bullet.kill()


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

        if time.time() - time_start < time_invincible:
            screen.blit(font.render("The traveller has spawned a bunch of tornadoes!", True, BLACK), (100, 100))
            screen.blit(font.render("You must collect all the pigeons before they die!", True, BLACK), (100, 130))
            screen.blit(font.render("The traveller has spawned a bunch of tornadoes!", True, BLACK), (102, 102))
            screen.blit(font.render("You must collect all the pigeons before they die!", True, BLACK), (102, 132))
            screen.blit(font.render("The traveller has spawned a bunch of tornadoes!", True, BLACK), (101, 102))
            screen.blit(font.render("You must collect all the pigeons before they die!", True, BLACK), (101, 132))
            screen.blit(font.render("The traveller has spawned a bunch of tornadoes!", True, BLACK), (102, 101))
            screen.blit(font.render("You must collect all the pigeons before they die!", True, BLACK), (102, 131))
            screen.blit(font.render("The traveller has spawned a bunch of tornadoes!", True, WHITE), (101, 101))
            screen.blit(font.render("You must collect all the pigeons before they die!", True, WHITE), (101, 131))
        # Draw a health bar
        # Draw the background rectangle
        pygame.draw.rect(screen, NAVY_BLUE, [580, 5, 215, 20])

        # Draw the foreground rectangle which represents the remaining health
        life_remaining = 215 - (215 * player.hp_remaining())
        pygame.draw.rect(screen, GREEN, [580, 5, life_remaining, 20])

        # If we've won, draw the text on the screen
        if game_state == "won":
            screen.blit(
                font.render(endgame_messages["win"], True, BLACK), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        if game_state == "lose":
            screen.blit(
                font.render(endgame_messages["lose"], True, BLACK), (100 / 2, SCREEN_HEIGHT / 2))


        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()