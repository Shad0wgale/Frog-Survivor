class Camera:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, player, game_map):
        # Center the camera on the player
        camera_x = player.rect.x - self.screen_width // 2 + player.rect.width // 2
        camera_y = player.rect.y - self.screen_height // 2 + player.rect.height // 2

        # Keep the camera within the map boundaries
        camera_x = max(0, min(camera_x, game_map.width - self.screen_width))
        camera_y = max(0, min(camera_y, game_map.height - self.screen_height))

        return camera_x, camera_y