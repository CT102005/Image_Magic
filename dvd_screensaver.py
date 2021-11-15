import pygame
pygame.init()


WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
LIGHT_BLUE  = (  0, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "DVD Screen Saver"

class Dvdimage:
    """Represents a dvd image on screen
    
    Attributes:
        x, y: coordinates of top left corner
        width: width of a rectangle in pixels
        height: height of our rectangle in pixels
        colour: 3-tuple of (r, g, b)
        x-vel: x velocity in pixels/second
        y-vel: y velocity in pixels/second
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 150
        self.height = 90
        self.colour = RED
        self.x_vel = 5
        self.y_vel = 3

    def rect(self) -> pygame.rect:
        """Returns a pygame.rect the represents a dvd_image"""
        return[self.x, self.y, self.width, self.height]

    def update(self) -> None:
        """Updates the Dvdimage with every tick"""
        # Update the x-coordinate
        self.x += self.x_vel
        # Update the y-coordinate
        self.y += self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()

    # ----------MAIN LOOP
    while not done:
        # Make space for the event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ---------- CHANGE ENVIRONMENT
        dvd_image.update()
        print(f"x: {dvd_image.x}, y: {dvd_image.y}")
        # ---------- DRAW THE ENVIRONMENT
        screen.fill(WHITE)      # Fill with background colour
        pygame.draw.rect(screen, dvd_image.colour, dvd_image.rect()) # TODO: method

        # Update the screen
        pygame.display.flip()
        # ----------CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()