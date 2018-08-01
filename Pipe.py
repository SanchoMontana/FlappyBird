import pygame
import random
class Pipe:
    def __init__(self, gameDisplay,  DISPLAY_HEIGHT, DISPLAY_WIDTH, speed):
        self.gameDisplay = gameDisplay
        self.height = random.randint(int(DISPLAY_HEIGHT / 10), int(DISPLAY_HEIGHT / 3))
        self.width = DISPLAY_WIDTH / 10
        self.x_pos = DISPLAY_WIDTH
        self.speed = speed * 2
        self.green = (0, 200, 0)
        self.glare = (100, 200, 100)
        self.shadow = (0, 160, 0)
        self.outline = (0, 50, 0)
        self.gap = 230 
        self.DISPLAY_HEIGHT = DISPLAY_HEIGHT
        

    def move(self):
        self.x_pos -= self.speed
    
    
        
    
        pygame.draw.rect(self.gameDisplay, self.green, (self.x_pos, 0, self.width, self.DISPLAY_HEIGHT-self.height - self.gap))
        pygame.draw.rect(self.gameDisplay, self.glare, (self.x_pos + 10, 0, 50, self.DISPLAY_HEIGHT-self.height - self.gap))
        pygame.draw.rect(self.gameDisplay, self.shadow, (self.x_pos + self.width - 20, 0, 20, self.DISPLAY_HEIGHT-self.height - self.gap))
        pygame.draw.rect(self.gameDisplay, self.outline, (self.x_pos, 0, self.width, self.DISPLAY_HEIGHT-self.height - self.gap), 2)
        
        
        pygame.draw.rect(self.gameDisplay, self.green, (self.x_pos - self.width / 6, self.DISPLAY_HEIGHT-self.height - self.gap - 65, self.width * 4 / 3, 65))
        pygame.draw.rect(self.gameDisplay, self.glare, (self.x_pos - self.width / 6 + 10, self.DISPLAY_HEIGHT-self.height - self.gap - 65, 60, 65))
        pygame.draw.rect(self.gameDisplay, self.shadow, (self.x_pos - self.width / 6 + self.width * 4 / 3 - 30 , self.DISPLAY_HEIGHT-self.height - self.gap - 65, 30, 65))
        pygame.draw.rect(self.gameDisplay, self.outline, (self.x_pos - self.width / 6, self.DISPLAY_HEIGHT-self.height - self.gap - 65, self.width * 4 / 3, 65), 2)
        
        
        
        
        
        pygame.draw.rect(self.gameDisplay, self.green, (self.x_pos, self.DISPLAY_HEIGHT-self.height, self.width, self.height))
        pygame.draw.rect(self.gameDisplay, self.glare, (self.x_pos + 10, self.DISPLAY_HEIGHT-self.height, 50, self.height))
        pygame.draw.rect(self.gameDisplay, self.shadow, (self.x_pos + self.width - 20, self.DISPLAY_HEIGHT-self.height, 20, self.height))
        pygame.draw.rect(self.gameDisplay, self.outline, (self.x_pos, self.DISPLAY_HEIGHT-self.height, self.width, self.height), 2)
        
        
        pygame.draw.rect(self.gameDisplay, self.green, (self.x_pos - self.width / 6, self.DISPLAY_HEIGHT-self.height, self.width * 4 / 3, 65))
        pygame.draw.rect(self.gameDisplay, self.glare, (self.x_pos - self.width / 6 + 10, self.DISPLAY_HEIGHT-self.height, 60, 65))
        pygame.draw.rect(self.gameDisplay, self.shadow, (self.x_pos - self.width / 6 + self.width * 4 / 3 - 30 , self.DISPLAY_HEIGHT-self.height, 30, 65))
        pygame.draw.rect(self.gameDisplay, self.outline, (self.x_pos - self.width / 6, self.DISPLAY_HEIGHT-self.height, self.width * 4 / 3, 65), 2)
    
