import pygame
from game import Game
from title import TitleScreen

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Define constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Create the screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the title of the window
    pygame.display.set_caption("My Awesome Game")

    # Create and display the title screen
    title_screen = TitleScreen(screen)
    title_screen.display()

    # Initialize your Game class and run it (assumed you have a Game class)
    from game import Game
    game = Game()
    game.run()