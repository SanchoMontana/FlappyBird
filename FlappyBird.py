import pygame                                                                   
from Bird import Bird                                                           
                                                                                
pygame.init()                                                                   
ball = pygame.image.load("res/ball.bmp") # This loads the player into existance.
pygame.mouse.set_visible(False)                                                 
                                                                                
DISPLAY_WIDTH = 1200                                                            
DISPLAY_HEIGHT = 900                                                            
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))          
background = pygame.image.load("res/forest.jpg")                                
background = pygame.transform.scale(background, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
rect = background.get_rect()                                                    
                                                                                
clock = pygame.time.Clock()                                                     
FPS = 50 # Frames per second.                                                   
                                                                                
player = Bird(DISPLAY_HEIGHT / 2)                                               
                                                                                
distance = 0                                                                    
# Main loop:                                                                    
game_exit = False                                                               
while not game_exit:                                                            
    # Event handling.                                                           
    for event in pygame.event.get():                                            
        if event.type == pygame.QUIT:                                           
            game_exit = True                                                    
        if event.type == pygame.KEYDOWN:                                        
            if event.key == pygame.K_SPACE:                                     
                player.jump()                                                   
                                                                                
    # Moving Background.                                                        
    distance += 2                                                               
    rect[0] = -distance                                                         
    gameDisplay.blit(background, (rect[0] % DISPLAY_WIDTH, rect[1]))            
    gameDisplay.blit(background, (rect[0] % DISPLAY_WIDTH - DISPLAY_WIDTH, rect[1]))
                                                                                
    # Moving the player.                                                        
    player.fall()                                                               
    player.time += 1                                                            
    gameDisplay.blit(ball, (50, player.position))                               
                                                                                
    # Frame by frame updating.                                                  
    pygame.display.update()                                                     
    clock.tick(40)                                                              
                                                                                
                                                                                
quit()
