import pygame
import random
pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY = (128, 128, 128)
BGCOLOUR = (  50, 55, 155)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Relaxing Snowscape"
FLOOR = 500

class Snowflake:
    """ Represents a singular snowflake
    Attributes:
        size: size of the radius of the snowflake in pixels
        coordinates: {x: int, y:int}
        width: width of image in pixels
        height: height of image in pixels
        colour: 3-tuple of (r, g, b)
        velocity: falling velocity in pixels per second
        colour: 3-tuple of (r, g, b)
    """
    def __init__(self):
      self.coords = [random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)]
      self.y_vel = 4
      self.colour = WHITE
      self.size = 2

    def update(self) -> None:
        # If Snowflake is too far top
        self.coords[1] += self.y_vel
        if self.coords[1] > SCREEN_HEIGHT:
            self.coords = [
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(-25, 0)
            ]
       # elif self.coords[1] > FLOOR:
        #    self.coords[1] = FLOOR
            # Keep the object inside the canvas

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_snowflakes = 500
    # Create a hundred snowflakes
    snowflakes = []

    for i in range(num_snowflakes-350):
        close_snowflake = Snowflake()
        close_snowflake.size = random.choice([4, 5])
        close_snowflake.y_vel = random.choice([1, 2])
        snowflakes.append(close_snowflake)

    for i in range(num_snowflakes - 250):
        close_snowflake = Snowflake()
        close_snowflake.size = random.choice([2, 3, 4])
        close_snowflake.y_vel = random.choice([3, 4])
        snowflakes.append(close_snowflake)

    for i in range(num_snowflakes):
        snowflakes.append(Snowflake())

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        for snow in snowflakes:
            snow.update()

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor
        pygame.draw.rect(screen, GREY, [0, 500, 800, 100])
        for snow in snowflakes:
            pygame.draw.circle(screen, snow.colour, snow.coords, snow.size)
        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()