import pygame

class GameMap:
    def __init__(self, width, height, tile_image_path):
        # Load the tile image
        self.tile_image = pygame.image.load(tile_image_path)
        self.tile_width, self.tile_height = self.tile_image.get_size()
        
        # Create a large surface that represents your map
        self.surface = pygame.Surface((width, height))
        self.width = width
        self.height = height
        
        # Tile the map surface with the tile image
        for x in range(0, width, self.tile_width):
            for y in range(0, height, self.tile_height):
                self.surface.blit(self.tile_image, (x, y))

    def draw(self, screen, camera_x, camera_y):
        # Draw the visible part of the map on the screen
        screen.blit(self.surface, (-camera_x, -camera_y))
