import pygame
from utilities import mirror_images, loadsheet, StateMachine

class Player(StateMachine):
    def __init__(self,name):
        super().__init__()
        super().__init__()
        self.name = name
        self.direction = "right"
        self.scale = 4
        
        # Control animation speed
        self.frame_delay = 2  # Delay between frames (higher value = slower)
        self.frame_counter = 0  # Counter to control frame delay
        
        self.idle_frames = loadsheet('frog/PNG/froglet_frog_green_sheet_idle.png',self.scale)
        self.walking_frames = loadsheet('frog/PNG/froglet_frog_green_sheet_walk.png',self.scale)

        # Generate mirrored frames for walking left
        self.walking_frames_left = mirror_images(self.walking_frames)
        self.idle_frames_left = mirror_images(self.idle_frames)

        self.current_frame = 0  # Track the current frame in the animation
        self.image = self.idle_frames[0]  # Default to the first idle frame
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        
    def update_animation(self):
        self.frame_counter += 1  # Increment the frame counter

        # Update frame only after the delay
        if self.frame_counter >= self.frame_delay:
            if self.current_state == "idle":
                if self.direction == "right":
                    self.image = self.idle_frames[self.current_frame % len(self.idle_frames)]
                else:
                    self.image = self.idle_frames_left[self.current_frame % len(self.idle_frames_left)]
            elif self.current_state == "walking":
                if self.direction == "left":
                    self.image = self.walking_frames_left[self.current_frame % len(self.walking_frames_left)]
                else:
                    self.image = self.walking_frames[self.current_frame % len(self.walking_frames)]
            
            self.current_frame += 1  # Move to the next frame
            self.frame_counter = 0  # Reset the frame counter
    
    def move(self, dx, dy, game_map,direction = None):
        # Move the player, but keep them within the map boundaries
        if direction is None:
            self.direction = self.direction
        else:
            self.direction = direction
        self.transition("walking")
        self.rect.x = max(0, min(self.rect.x + dx, game_map.width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + dy, game_map.height - self.rect.height))
    
    def update(self):
    # Handle state transitions and movement
        self.update_animation()
        
    def draw(self, screen, camera_x, camera_y):
        # Draw the player relative to the camera position
        
        #pygame.draw.rect(screen, (0, 0, 255), (self.rect.x - camera_x, self.rect.y - camera_y, self.rect.width, self.rect.height))
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))
