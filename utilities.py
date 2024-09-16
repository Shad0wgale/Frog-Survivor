import pygame
class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            exit("oops")
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey != None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

def mirror_images(images):
    return [pygame.transform.flip(image, True, False) for image in images]

def loadsheet(path:str,scale_factor:int):
        sheet = spritesheet(path)
        frames = sheet.images_at(
            [(0, 0, 16, 20), (16, 0, 16, 20), (32, 0, 16, 20), (48, 0, 16, 20),
            (64, 0, 16, 20), (80, 0, 16, 20), (96, 0, 16, 20)], colorkey=(0, 0, 0)
        )
        frames = scale_images(frames, scale_factor)
        return frames
    
def scale_images(images, scale_factor):
    return [pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor))) for image in images]

class StateMachine:
    def __init__(self):
        # Define states
        self.states = ["idle", "walking", "running", "jumping","attacking"]
        self.current_state = "idle"  # Initial state

    def transition(self, new_state):
        # Check if the new state is valid
        if new_state in self.states:
            print(f"Transitioning from {self.current_state} to {new_state}")
            self.current_state = new_state
        else:
            print(f"Invalid transition to {new_state}")

    def get_state(self):
        return self.current_state

# Example usage
machine = StateMachine()

# Initial state
print(f"Initial state: {machine.get_state()}")  # Output: idle

# Transition to walking
machine.transition("walking")
print(f"Current state: {machine.get_state()}")  # Output: walking

# Invalid transition
machine.transition("flying")  # Output: Invalid transition

# Transition to running
machine.transition("running")
print(f"Current state: {machine.get_state()}")  # Output: running