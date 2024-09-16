import pygame
from player import Player
from map import GameMap
from config import Config
from camera import Camera

class Game:
    def __init__(self):
        pygame.init()
        
        # Load settings and create objects
        self.settings = Config()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        self.player = Player(name="Miles")
        self.game_map = GameMap(self.settings.map_width, self.settings.map_height, "grass.png")
        self.camera = Camera(self.settings.screen_width, self.settings.screen_height)
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Player movement
            keys = pygame.key.get_pressed()
            moving = False

            if keys[pygame.K_a]:
                self.player.move(-5, 0, self.game_map, "left")
                moving = True

            if keys[pygame.K_d]:
                self.player.move(5, 0, self.game_map, "right")
                moving = True

            if keys[pygame.K_w]:
                self.player.move(0, -5, self.game_map)
                moving = True

            if keys[pygame.K_s]:
                self.player.move(0, 5, self.game_map)
                moving = True

            if not moving:
                self.player.transition("idle")
            
            # Update camera
            camera_x, camera_y = self.camera.update(self.player, self.game_map)
            
            # Draw everything
            self.screen.fill((0, 0, 0))
            self.game_map.draw(self.screen, camera_x, camera_y)
            self.player.update()
            self.player.draw(self.screen, camera_x, camera_y)
            
            # Update Display
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
