import pygame
pygame.init()

PINK  = ( 255, 182, 193)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
LIGHT_BLUE  = (  180, 215, 234)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "DVD Screen Saver"

class Dvdimage:
    """Represents a dvd image on screen
    
    Attributes:
        x, y: coordinates of top left corner
        width: width of image in pixels
        height: height of image in pixels
        img: visual representation of our Dvdimage
        colour: 3-tuple of (r, g, b)
        x-vel: x velocity in pixels/second
        y-vel: y velocity in pixels/second
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 180
        self.height = 180
        self.img = pygame.image.load("./images/dvdimage.png")
        self.bg = pygame.image.load("./images/dvdimagebackground.png")
        self.x_vel = 5
        self.y_vel = 3

    def rect(self) -> pygame.rect:
        """Returns a pygame.rect the represents a dvd_image"""
        return[self.x, self.y, self.width, self.height]

    def update(self) -> None:
        """Updates the Dvdimage with every tick"""
        # Update the x-coordinate
        self.x += self.x_vel
        # If Dvdimage is too far to the left

        # Update the y-coordinate
        self.y += self.y_vel
        # If Dvdimage is too far to the right
        if self.x + self.width > SCREEN_WIDTH:
            # Keep the object inside the canvas
            self.x = SCREEN_WIDTH - self.width
            # Set the velocity to the negative
            self.x_vel = -self.x_vel
        # If Dvdimage is too far to the left
        if self.x < 0:
            # Keep the object inside the canvas
            self.x = 0
            # Set the velocity to the negative
            self.x_vel = -self.x_vel

        # If Dvdimage is too far top
        if self.y + self.height > SCREEN_HEIGHT:
            # Keep the object inside the canvas
            self.y = SCREEN_HEIGHT - self.height
            # Set the velocity to the negative
            self.y_vel = -self.y_vel
        # If Dvdimage is too far down
        if self.y < 0:
            # Keep the object inside the canvas
            self.y = 0
            # Set the velocity to the negative
            self.y_vel = -self.y_vel


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
        screen.fill(LIGHT_BLUE)
        screen.blit(dvd_image.bg, (0, 0))
        screen.blit(dvd_image.bg, (0, SCREEN_HEIGHT / 2))
        screen.blit(dvd_image.bg, (SCREEN_WIDTH / 2, 0))
        screen.blit(dvd_image.bg, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        # Fill with background colour
        # .blit9(<surface/image>, coords)
        screen.blit(dvd_image.img, (dvd_image.x, dvd_image.y))

        # Update the screen
        pygame.display.flip()
        # ----------CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()