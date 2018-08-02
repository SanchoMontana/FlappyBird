import random
class Pipe:
    def __init__(self, DISPLAY_HEIGHT, DISPLAY_WIDTH, speed):
        pipe_lip = int(DISPLAY_HEIGHT / 10)
        pipe_gap = int(DISPLAY_HEIGHT / 3)
        self.pipe_height = random.randint(pipe_lip, DISPLAY_HEIGHT - pipe_lip - pipe_gap)
        self.pipe_width = DISPLAY_WIDTH / 10
        self.x_pos = DISPLAY_WIDTH
        self.speed = speed * 2

    def move(self):
        self.x_pos -= self.speed

    
