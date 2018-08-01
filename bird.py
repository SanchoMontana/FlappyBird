import pygame, sys
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

time = 0
currentVerticalPos = 450
gravity = 1.09

# Image init:
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

# Main loop:
game_exit = False
while not game_exit:
    print(currentVerticalPos)
    # Event handling.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time = 0
    
    distance += 2
    # Moving Background
    rect[0] = -distance
    gameDisplay.blit(background, (rect[0] % DISPLAY_WIDTH, rect[1]))
    gameDisplay.blit(background, (rect[0] % DISPLAY_WIDTH - DISPLAY_WIDTH, rect[1]))

    if currentVerticalPos > DISPLAY_HEIGHT:
        sys.exit()
    currentVerticalPos += time - 15
                            # Middle-ish of screen
    gameDisplay.blit(ball, (450, currentVerticalPos))
        
    pygame.display.update()
    clock.tick(FPS)
    time += 1
    

quit()
