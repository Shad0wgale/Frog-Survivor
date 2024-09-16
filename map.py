import pygame
import pytmx

class GameMap:
    def __init__(self, tmx_path):
        """
        Initialize the game map with tile data from a Tiled TMX file.
        :param tmx_path: Path to the Tiled map TMX file
        """
        # Load the TMX map using pytmx
        self.tmx_map = pytmx.load_pygame(tmx_path)
        
        # Extract map properties
        self.width = self.tmx_map.width * self.tmx_map.tilewidth
        self.height = self.tmx_map.height * self.tmx_map.tileheight
        self.tile_width = self.tmx_map.tilewidth
        self.tile_height = self.tmx_map.tileheight
        
        # Create a surface for the map
        self.surface = pygame.Surface((self.width, self.height))
        
        # Draw the map using tilesets and layers
        self._draw_map()

    def _draw_map(self):
        """
        Draw all layers of tiles on the map surface.
        """
        for layer in self.tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, tile in layer:
                    tile_image = self.tmx_map.get_tile_image_by_gid(tile)
                    if tile_image:
                        self.surface.blit(tile_image, (x * self.tile_width, y * self.tile_height))

    def draw(self, screen, camera_x, camera_y):
        """
        Draw the visible part of the map on the screen.
        :param screen: The pygame display surface
        :param camera_x: X position of the camera
        :param camera_y: Y position of the camera
        """
        screen.blit(self.surface, (-camera_x, -camera_y))

# Example usage
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # Initialize the GameMap with your TMX file path
    game_map = GameMap("path_to_your_map.tmx")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Draw the map
        game_map.draw(screen, 0, 0)  # Adjust camera_x and camera_y as needed
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
