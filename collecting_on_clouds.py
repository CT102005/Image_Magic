import pygame
import random
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BGCOLOUR = (175, 140, 155)
SHADOW_BLUE = (110, 130, 160)

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Game Draft"


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

        super().__init__()
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 25
        self.height = 25
        self.image = pygame.Surface([self.width, self.height])
        self.bg = pygame.image.load("./images/dvdimagebackground.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.x, self.rect.y = (SCREEN_WIDTH/2, SCREEN_HEIGHT)
        self.x_vel = 0
        self.y_vel = 0
        self.grav = 0.4

        self.cloud_list = pygame.sprite.Group()

        # TODO: cloud fall cooldown

    def rect(self) -> pygame.rect:
        """Returns a pygame.rect the represents a dvd_image"""
        return[self.x, self.y, self.width, self.height]

    def left(self):
        self.x_vel = -7

    def right(self):
        self.x_vel = 7

    def stop(self):
        self.x_vel = 0

    def up(self):
        # Check if we're on a platform
        self.rect.bottom += 2
        cloud_underneath = pygame.sprite.spritecollideany(self, self.cloud_list)
        self.rect.bottom -= 2

        if self.rect.bottom == SCREEN_HEIGHT or cloud_underneath:
            self.y_vel = -12

    def update(self) -> None:
        """Calculate movement"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Constrain movement
        # X -
        if self.rect.left < 0:
            self.rect.x = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        # Y -
        if self.rect.bottom < SCREEN_HEIGHT:
            self.y_vel += self.grav
        else:
            self.y_vel = 0

        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel

        clouds_collided = pygame.sprite.spritecollide(self, self.cloud_list, False)

        for cloud in clouds_collided:
            if self.y_vel > 0:
                self.rect.bottom = cloud.rect.top
            elif self.y_vel < 0:
                self.rect.top = cloud.rect.bottom


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
        self.width = 30
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(SHADOW_BLUE)

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()


class Cloud(pygame.sprite.Sprite):
    """Describes a platform

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
    """
    platforms = [
        [150, 20, 1100, 600],
        [150, 20, 900, 800],
        [150, 20, 600, 1100],
        [150, 20, 350, 700],
        [150, 20, 1000, 100],
        [150, 20, 800, 500],
        [150, 20, 100, 300],
        [150, 20, 300, 200],
        [150, 20, 150, 1000],
        [150, 20, 450, 900],
        [150, 20, 500, 600],
        [150, 20, 550, 300],
        [150, 20, 1100, 1000],
        [150, 20, 1400, 850],
        [150, 20, 1425, 350],
        [150, 20, 1250, 175],
        [150, 20, 1250, 500],
        [150, 20, 150, 550]
    ]

    def __init__(self, width, height):
        """Platform constructor"""
        super().__init__()

        self.image = pygame.image.load("./images/cloud.png")
        self.image = pygame.transform.scale(self.image, (150, 20))
        self.rect = self.image.get_rect()


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

        self.vel_y = 15
        self.cloud_list = pygame.sprite.Group()

    def update(self):
        self.rect.y -= self.vel_y


class AmmoBar(pygame.sprite.Sprite):
    """Represents a bar that shows how much ammunition the player has left
    Attributes:
        rect: representation of the bar
    """
    def __init__(self):
        """Arguments:"""

        super().__init__()

        self.rect = self.image.get_rect()


class Quit_Button(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        """Create a quit button

        Args:
            pos - (x, y)
        """
        super().__init__()
        self.image = pygame.image.load("./images/closebutton.jpg")
        self.image = pygame.transform.scale(self.image, (120, 45))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 75

    # Create groups to hold sprites
    all_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    cloud_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()

    # Create player block
    player = Player()

    # Font
    font_large = pygame.font.SysFont("dejavusansmono", 40)
    font_medium = pygame.font.SysFont("dejavusansmono", 30)
    font_small = pygame.font.SysFont("dejavusansmono", 25)

    # Variables
    score = 0
    winscore = 50
    t_start = pygame.time.get_ticks()
    time_won = 0

    # Create cloud block and add to the cloud sprites and all sprites list
    for c in Cloud.platforms:
        cloud = Cloud(c[0], c[1])
        cloud.rect.x, cloud.rect.y = c[2], c[3]
        cloud_sprites.add(cloud)
        all_sprites.add(cloud)

    player.cloud_list = cloud_sprites

    # Add the player to all_sprites group
    all_sprites.add(player)

    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):
        # Create a block(set its parameters)
        block = Block()
        # Set a random location for the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(1000 - block.rect.height)

        # Add the block to the block_sprites Group
        # Add the block to the all_sprites Group
        block_sprites.add(block)
        all_sprites.add(block)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER

        # Moving left and right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left()
                if event.key == pygame.K_RIGHT:
                    player.right()
                # Jumping
                if event.key == pygame.K_UP:
                    player.up()
                # Shooting
                if event.key == pygame.K_e:
                    if len(bullet_sprites) < 20:
                        bullet = Bullet(player.rect.midtop)

                    bullet_sprites.add(bullet)
                    all_sprites.add(bullet)

            # Stop when the keys are lifted
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.x_vel < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.x_vel > 0:
                    player.stop()

            # Game win
            if score >= winscore:
                for cloud in cloud_sprites:
                    cloud.kill()
                for block in block_sprites:
                    block.kill()

        # ----------- CHANGE ENVIRONMENT

        # Update the location of all sprites
        all_sprites.update()
        for bullet in bullet_sprites:
            if bullet.rect.y < 0:
                bullet.rect.y = -10
            if pygame.sprite.spritecollideany(bullet, cloud_sprites):
                bullet.rect.y = -10

            blocks_hit = pygame.sprite.spritecollide(bullet, block_sprites, True)
            if blocks_hit:
                bullet.rect.y = -10
                score += 1

        # Check if player is at the bottom
        if player.rect.bottom >= SCREEN_HEIGHT:
            # Empty all the bullets from the clip
            for bullet in bullet_sprites:
                if bullet.rect.y < -9:
                    bullet.kill()

        # Kill blocks that touch clouds
        for block in block_sprites:
            if pygame.sprite.spritecollideany(block, cloud_sprites):
                block.kill()

        # Kill blocks that touches the player
        block_collect = pygame.sprite.spritecollide(player, block_sprites, True)
        for block in block_collect:
            score += 1

        ammo = (20 - int(len(bullet_sprites)))

        if len(block_sprites) <= 50:
            if score < winscore:
                # Create 10 more blocks when there's only 40 on screen
                for i in range(10):
                    block = Block()
                    block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
                    block.rect.y = random.randrange(1000 - block.rect.height)
                    block_sprites.add(block)
                    all_sprites.add(block)

        # ----------- DRAW THE ENVIRONMENT

        # Background image
        screen.blit(pygame.image.load("./images/blue_mountains.jpg"), (0, 0))

        if score < winscore:

            # Instructions
            screen.blit(pygame.transform.scale(pygame.image.load("./images/arrowkeys.png"), (180, 90)), (1050, 300))
            screen.blit(font_medium.render("Shoot or touch the blocks to collect them", True, BLACK), (100, 100))
            screen.blit(font_medium.render("Jump on the clouds to aim at the blocks better", True, BLACK), (100, 125))
            screen.blit(font_medium.render("Jump underneath a cloud to warp through", True, BLACK), (935, 210))
            screen.blit(font_medium.render("Stay too long on a cloud and you'll fall through", True, BLACK), (900, 250))
            screen.blit(font_small.render("Press E to shoot", True, BLACK), (1065, 400))
            screen.blit(font_small.render(f"Collect {winscore} blocks to win!", True, BLACK), (300, 400))
            screen.blit(font_small.render("Touch bottom to recharge ammo", True, WHITE), (25, 1170))

        if score >= winscore:
            # If time_won is zero, set time to time_now
            if time_won == 0:
                time_won = time_now
                # Update the high score if the current score is the highest
                with open("./data/collecting_on_clouds_highscore.txt") as f:
                    high_scoretime = float(f.readline().strip())
                    print(high_scoretime)

                with open("./data/collecting_on_clouds_highscore.txt", "w") as f:

                    if time_won < high_scoretime:
                        f.write(str(time_won))
                    else:
                        f.write(str(high_scoretime))

                button = Quit_Button((SCREEN_WIDTH - 130, 10))
                all_sprites.add(button)

            # Print out time_won
            screen.blit(font_medium.render("YOU WIN!", True, BLACK), (800, 300))
            screen.blit(font_small.render(f"Time taken: {time_won} seconds", True, BLACK), (750, 330))
            screen.blit(font_small.render(f"High score: {high_scoretime} seconds", True, BLACK), (750, 360))
            screen.blit(pygame.transform.scale(pygame.image.load("./images/cake.png"), (420, 420)), (630, 380))
            screen.blit(font_small.render("Thanks for playing!", True, BLACK), (760, 800))
            screen.blit(font_small.render("Created by Candice Tsai", True, BLACK), (745, 830))

            # If user clicks in area, set done = True
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed(3)[0]:
                if (button.rect.left < mouse_pos[0] < button.rect.right) and (button.rect.top < mouse_pos[1] < button.rect.bottom):
                    done = True


        # Title
        screen.blit(font_large.render("RELAXING (KIND OF) BLOCK COLLECTING GAME", True, WHITE), (10, 10))

        # Score
        if score < winscore:
            screen.blit(font_medium.render(f"Score: {score}", True, BLACK), (1490, 15))

        # Ammo Bar
        ammo_remaining = (1.8 * ammo) - 1.8

        pygame.draw.rect(screen, WHITE, [player.rect.x - 5.2, (player.rect.y - 10.5), 36.5, 7])
        pygame.draw.rect(screen, BLUE, [player.rect.x - 5, (player.rect.y - 10), ammo_remaining, 5])

        # Stopwatch
        time_now = round(((pygame.time.get_ticks() - t_start) / 1000), 1)
        if score < winscore:
            screen.blit(font_small.render(f"Time: {time_now}", True, BLACK), (1490, 35))

        # Draw all sprites
        all_sprites.draw(screen)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
