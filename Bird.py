class Bird:
    def __init__(self, DISPLAY_HEIGHT, BIRD_HEIGHT):
        self.prev_click = 0
        self.DISPLAY_HEIGHT = DISPLAY_HEIGHT
        self.BIRD_HEIGHT = BIRD_HEIGHT
        self.position = DISPLAY_HEIGHT / 2
        self.prev_position = self.position
        self.time = 0

    def jump(self):
        self.time = 0

    def fall(self):
        self.prev_position = self.position
        self.position += self.time - 20 + (self.prev_click * 1.7)
        if self.position > self.DISPLAY_HEIGHT - self.BIRD_HEIGHT:
            self.position = self.DISPLAY_HEIGHT - self.BIRD_HEIGHT
        if self.position < -self.BIRD_HEIGHT - 50:
            self.position = -self.BIRD_HEIGHT - 50 

