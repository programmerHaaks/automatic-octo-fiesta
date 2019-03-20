import pygame

GAME_NAME = "Automatic Octo Fiesta"
LOGO_LOCATION = "images/aof_logo_icon.png"
RESOLUTION = WIDTH, HEIGHT = 640, 480


def main():
    pygame.init()

    # Load and set logo
    set_logo()

    # Create a surface on screen that has RESOLUTION as size.
    screen = pygame.display.set_mode(RESOLUTION)

    # Setup ball
    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()
    ballrect.move_ip(WIDTH / 2, HEIGHT / 2)

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            # Only event to handle right now is quit.
            if event.type == pygame.QUIT:
                running = False


def set_logo():
    # Load and set logo
    logo = pygame.image.load(LOGO_LOCATION)
    pygame.display.set_icon(logo)
    pygame.display.set_caption(GAME_NAME)


if __name__ == "__main__":
    main()
