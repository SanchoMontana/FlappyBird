import pygame
pygame.init()
pygame.mouse.set_visible(False)
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 900
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
FPS = 50 # Frames per second.
background = pygame.image.load("res/forest.jpg")
background = pygame.transform.scale(background, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
rect = background.get_rect()
distance = 0
# Main loop:
game_exit = False
while not game_exit:
    # Event handling.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    
    distance += 2
    # Moving Background
    rect = rect.move((-distance, 0))
    gameDisplay.blit(background, (rect[0] % DISPLAY_WIDTH, rect[1]))
    gameDisplay.blit(background, (rect[0] % DISPLAY_WIDTH - DISPLAY_WIDTH, rect[1]))
    
    pygame.display.update()
    clock.tick(FPS)
    

quit()
