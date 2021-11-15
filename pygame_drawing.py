# Pygame_Drawing
# Author: Candice
# 9 November 2021

# Get introduced to Pygame and draw objects on screen

import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
LIGHT_BLUE  = (  205, 255, 249)
PINK  = ( 255, 182, 193)
DARK_PINK = (205, 131, 152)
GRASS_GREEN = (139, 193, 116)
SUN_YELLOW = (255, 255, 117)
CRIMSON = (167, 29, 49)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # ----------MAIN LOOP
    while not done:
        # Make space for the event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ---------- CHANGE ENVIRONMENT
        # ---------- DRAW THE ENVIRONMENT
        screen.fill(WHITE)      # Fill with background colour
        # for i in range(10):
        # pygame.draw.rect(screen, WHITE, [100+i*10, 100+i*10, 75, 30])

        screen.fill(LIGHT_BLUE)
        pygame.draw.rect(screen, BLACK, [19, 267, 202, 202])
        pygame.draw.polygon(screen, BLACK, [[120, 179], [60, 270], [180, 270]], 92)
        pygame.draw.rect(screen, CRIMSON, [20, 267, 200, 200])
        pygame.draw.polygon(screen, CRIMSON, [[120, 180], [60, 270], [180, 270]], 90)
        pygame.draw.rect(screen, BLACK, [0, 466, 800, 160])
        pygame.draw.rect(screen, GRASS_GREEN, [0, 467, 800, 160])
        pygame.draw.circle(screen, BLACK, [420, 355], 10)
        pygame.draw.rect(screen, WHITE, [70, 340, 100, 120])

        # CLOUD 1 OUTLINE
        pygame.draw.ellipse(screen, BLACK, [99, 89, 72, 32], 30)
        pygame.draw.ellipse(screen, BLACK, [109, 119, 102, 42], 50)
        pygame.draw.ellipse(screen, BLACK, [69, 109, 92, 32], 50)
        pygame.draw.ellipse(screen, BLACK, [129, 94, 102, 42], 50)
        pygame.draw.ellipse(screen, BLACK, [189, 119, 52, 24], 50)
        # CLOUD 1
        pygame.draw.ellipse(screen, WHITE, [100, 90, 70, 30], 30)
        pygame.draw.ellipse(screen, WHITE, [110, 120, 100, 40], 50)
        pygame.draw.ellipse(screen, WHITE, [70, 110, 90, 30], 50)
        pygame.draw.ellipse(screen, WHITE, [130, 95, 100, 40], 50)
        pygame.draw.ellipse(screen, WHITE, [190, 120, 50, 22], 50)

        # CLOUD 2 OUTLINE
        pygame.draw.ellipse(screen, BLACK, [399, 39, 82, 62], 30)
        pygame.draw.ellipse(screen, BLACK, [409, 69, 112, 62], 50)
        pygame.draw.ellipse(screen, BLACK, [369, 69, 62, 32], 50)
        pygame.draw.ellipse(screen, BLACK, [429, 44, 112, 62], 50)
        pygame.draw.ellipse(screen, BLACK, [489, 69, 92, 44], 50)
        pygame.draw.ellipse(screen, BLACK, [494, 84, 52, 44], 50)
        # CLOUD 2
        pygame.draw.ellipse(screen, WHITE, [400, 40, 80, 60], 30)
        pygame.draw.ellipse(screen, WHITE, [410, 70, 110, 60], 50)
        pygame.draw.ellipse(screen, WHITE, [370, 70, 60, 30], 50)
        pygame.draw.ellipse(screen, WHITE, [430, 45, 110, 60], 50)
        pygame.draw.ellipse(screen, WHITE, [490, 70, 90, 42], 50)
        pygame.draw.ellipse(screen, WHITE, [495, 85, 50, 42], 50)

        # SUN
        pygame.draw.circle(screen, BLACK, [700, 100], 51)
        pygame.draw.circle(screen, SUN_YELLOW, [700, 100], 50)

        # EARS
        pygame.draw.circle(screen, DARK_PINK, [380, 355], 10)
        pygame.draw.circle(screen, DARK_PINK, [420, 355], 10)
        pygame.draw.circle(screen, PINK, [380, 355], 5)
        pygame.draw.circle(screen, PINK, [420, 355], 5)

        # LEGS
        pygame.draw.rect(screen, DARK_PINK, [505, 430, 10, 45])
        pygame.draw.rect(screen, DARK_PINK, [480, 430, 10, 45])
        pygame.draw.rect(screen, DARK_PINK, [455, 430, 10, 45])
        pygame.draw.rect(screen, DARK_PINK, [430, 430, 10, 45])

        for i in range(10):
            # TAIL
            pygame.draw.rect(screen, DARK_PINK, [500 + i * 7, 370 + i * 7, 9, 9])
            pygame.draw.rect(screen, PINK, [500 + i * 7, 370 + i * 7, 7, 7])

        # BODY
        pygame.draw.circle(screen, DARK_PINK, [400, 400], 44)
        pygame.draw.circle(screen, DARK_PINK, [470, 400], 59)
        pygame.draw.circle(screen, PINK, [470, 400], 55)
        pygame.draw.circle(screen, PINK, [400, 400], 40)

        # MOUTH
        pygame.draw.circle(screen, BLACK, [400, 410], 12)
        pygame.draw.circle(screen, RED, [400, 410], 10)
        pygame.draw.rect(screen, PINK, [380, 400, 40, 10])
        pygame.draw.rect(screen, PINK, [390, 390, 20, 10])
        pygame.draw.rect(screen, BLACK, [390, 410, 20, 2])

        # EYES
        pygame.draw.circle(screen, BLACK, [381, 389], 9)
        pygame.draw.circle(screen, BLACK, [417, 389], 9)
        pygame.draw.circle(screen, WHITE, [381, 389], 7)
        pygame.draw.circle(screen, WHITE, [417, 389], 7)
        pygame.draw.circle(screen, BLACK, [381, 389], 5)
        pygame.draw.circle(screen, BLACK, [417, 389], 5)

        # NOSE
        pygame.draw.circle(screen, BLACK, [398, 402], 1)
        pygame.draw.circle(screen, BLACK, [402, 402], 1)

        # Update the screen
        pygame.display.flip()
        # ----------CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()

