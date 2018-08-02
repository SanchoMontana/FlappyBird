import random
import pygame
class Pipe:
    
    def __init__(self, gameDisplay,  DISPLAY_HEIGHT, DISPLAY_WIDTH, speed, color = [0, 200, 0]):
        self.gameDisplay = gameDisplay
        self.height = random.randint(int(DISPLAY_HEIGHT / 10), int(DISPLAY_HEIGHT / 10 * 7))
        self.width = DISPLAY_WIDTH / 10
        self.x_pos = DISPLAY_WIDTH
        self.speed = speed * 2
        self.color = color
        self.glare = [self.color[0] + 70 if self.color[0] < 185 else 255, self.color[1] + 70 if self.color[1] < 185 else 255, self.color[2] + 70 if self.color[2] < 185 else 255]
        self.shadow = [self.color[0] - 70 if self.color[0] > 70 else 0, self.color[1] - 70 if self.color[1] > 70 else 0, self.color[2] - 70 if self.color[2] > 70 else 0]
        self.outline = (0, 0, 0)
        self.gap = DISPLAY_HEIGHT / 4 
        self.DISPLAY_HEIGHT = DISPLAY_HEIGHT
        

    def move(self):
        self.x_pos -= self.speed
 
        pygame.draw.rect(self.gameDisplay, self.color, (self.x_pos, 0, self.width, self.DISPLAY_HEIGHT-self.height - self.gap))
        pygame.draw.rect(self.gameDisplay, self.glare, (self.x_pos + 10, 0, 50, self.DISPLAY_HEIGHT-self.height - self.gap))
        pygame.draw.rect(self.gameDisplay, self.shadow, (self.x_pos + self.width - 20, 0, 20, self.DISPLAY_HEIGHT-self.height - self.gap))
        pygame.draw.rect(self.gameDisplay, self.outline, (self.x_pos, 0, self.width, self.DISPLAY_HEIGHT-self.height - self.gap), 2)
        
        pygame.draw.rect(self.gameDisplay, self.color, (self.x_pos - self.width / 6, self.DISPLAY_HEIGHT-self.height - self.gap - 65, self.width * 4 / 3, 65))
        pygame.draw.rect(self.gameDisplay, self.glare, (self.x_pos - self.width / 6 + 10, self.DISPLAY_HEIGHT-self.height - self.gap - 65, 60, 65))
        pygame.draw.rect(self.gameDisplay, self.shadow, (self.x_pos - self.width / 6 + self.width * 4 / 3 - 30 , self.DISPLAY_HEIGHT-self.height - self.gap - 65, 30, 65))
        pygame.draw.rect(self.gameDisplay, self.outline, (self.x_pos - self.width / 6, self.DISPLAY_HEIGHT-self.height - self.gap - 65, self.width * 4 / 3, 65), 2)
 
        pygame.draw.rect(self.gameDisplay, self.color, (self.x_pos, self.DISPLAY_HEIGHT-self.height, self.width, self.height))
        pygame.draw.rect(self.gameDisplay, self.glare, (self.x_pos + 10, self.DISPLAY_HEIGHT-self.height, 50, self.height))
        pygame.draw.rect(self.gameDisplay, self.shadow, (self.x_pos + self.width - 20, self.DISPLAY_HEIGHT-self.height, 20, self.height))
        pygame.draw.rect(self.gameDisplay, self.outline, (self.x_pos, self.DISPLAY_HEIGHT-self.height, self.width, self.height), 2)
 
        pygame.draw.rect(self.gameDisplay, self.color, (self.x_pos - self.width / 6, self.DISPLAY_HEIGHT-self.height, self.width * 4 / 3, 65))
        pygame.draw.rect(self.gameDisplay, self.glare, (self.x_pos - self.width / 6 + 10, self.DISPLAY_HEIGHT-self.height, 60, 65))
        pygame.draw.rect(self.gameDisplay, self.shadow, (self.x_pos - self.width / 6 + self.width * 4 / 3 - 30 , self.DISPLAY_HEIGHT-self.height, 30, 65))
        pygame.draw.rect(self.gameDisplay, self.outline, (self.x_pos - self.width / 6, self.DISPLAY_HEIGHT-self.height, self.width * 4 / 3, 65), 2)
