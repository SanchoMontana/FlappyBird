class Bird:
    def __init__(self, position):
        self.position = position
        self.time = 0

    def jump(self):
        self.time = 0

    def fall(self):
        self.position += self.time - 15
