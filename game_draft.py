import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = (175, 140, 155)

SCREEN_WIDTH  = 1600
SCREEN_HEIGHT = 1200
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Game Draft"

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
        self.rect.x, self.rect.y = (
            (SCREEN_WIDTH)/2,
            (SCREEN_HEIGHT)
        )
        self.x_vel = 0
        self.y_vel = 0
        self.grav = 0.4

    def rect(self) -> pygame.rect:
        """Returns a pygame.rect the represents a dvd_image"""
        return[self.x, self.y, self.width, self.height]

    def left(self):
        self.x_vel = -5
    def right(self):
        self.x_vel = 5
    def stop(self):
        self.x_vel = 0
    def up(self):
        if self.rect.bottom == SCREEN_HEIGHT:
            self.y_vel = -12

    # def gravity(self):



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

# class Cloud(pygame.sprite.Sprite):
#     """Describes a platform
#
#     Attributes:
#         image: Surface that is the visual
#             representation of our Block
#         rect: numerical representation of
#             our Block [x, y, width, height]
#     """
#     def __init__(self):
#         platforms = [
#             [150, 20, 1100, 600],
#             [150, 20, 900, 1600],
#             [150, 20, 600, 1100],
#             [150, 20, 400, 700],
#             [150, 20, 1000, 1700],
#             [150, 20, 800, 500]
#         ]


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

        self.vel_y = 5

    def update(self):
        self.rect.y -= self.vel_y

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    platforms = []

    # Create groups to hold sprites
    all_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

    # Create player block
    player = Player()
    # Add the player to all_sprites group
    all_sprites.add(player)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left()
                if event.key == pygame.K_RIGHT:
                    player.right()
                if event.key == pygame.K_UP:
                    player.up()
                if event.key == pygame.K_SPACE:
                    if len(bullet_sprites) < 8:
                        bullet = Bullet(player.rect.midtop)

                    bullet_sprites.add(bullet)
                    all_sprites.add(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.x_vel < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.x_vel > 0:
                    player.stop()



        # ----------- CHANGE ENVIRONMENT

        # Update the location of all sprites
        all_sprites.update()
        for bullet in bullet_sprites:
            if bullet.rect.y < 0:
                bullet.kill()

        # ----------- DRAW THE ENVIRONMENT
        #screen.fill(BGCOLOUR)      # fill with bgcolor
        screen.blit(pygame.image.load("./images/blue_mountains.jpg"), (0, 0))

        # for platform in platforms:
        #     pygame.draw.rect(screen, WHITE, cloud.platform)

        # Draw all sprites
        all_sprites.draw(screen)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()