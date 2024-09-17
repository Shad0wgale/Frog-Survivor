import pygame

class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font_size = 64
        self.button_font_size = 32
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.title_font = pygame.font.Font(None, self.title_font_size)
        self.button_font = pygame.font.Font(None, self.button_font_size)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def display(self):
        # Title screen loop
        while True:
            self.screen.fill(self.black)  # Fill screen with black

            # Render the title text
            title_text = self.title_font.render("My Awesome Game", True, self.white)
            title_rect = title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 100))
            self.screen.blit(title_text, title_rect)

            # Render the start button text
            start_text = self.button_font.render("Press ENTER to Start", True, self.white)
            start_rect = start_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 50))
            self.screen.blit(start_text, start_rect)

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()  # Close the game
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # If Enter is pressed, start the game
                        return

            # Update the display
            pygame.display.update()