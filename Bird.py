class Bird:
    def __init__(self, DISPLAY_HEIGHT, BIRD_HEIGHT):
        self.DISPLAY_HEIGHT = DISPLAY_HEIGHT
        self.BIRD_HEIGHT = BIRD_HEIGHT
        self.position = DISPLAY_HEIGHT / 2
        self.time = 0

    def jump(self):
        self.time = 0

    def fall(self):
        self.position += 2 * (self.time - 10)
        if self.position > self.DISPLAY_HEIGHT - self.BIRD_HEIGHT:
            self.position = self.DISPLAY_HEIGHT - self.BIRD_HEIGHT
        if self.position < -self.BIRD_HEIGHT - 50:
            self.position = -self.BIRD_HEIGHT - 50
