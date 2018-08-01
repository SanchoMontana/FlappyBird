import random
class Pipe:
    def __init__(self, DISPLAY_HEIGHT, DISPLAY_WIDTH, speed):
        self.pipe_height = random.randint(int(DISPLAY_HEIGHT / 10), int(DISPLAY_HEIGHT / 3))
        self.pipe_width = DISPLAY_WIDTH / 10
        self.x_pos = DISPLAY_WIDTH
        self.speed = speed * 2

    def move(self):
        self.x_pos -= self.speed

    
