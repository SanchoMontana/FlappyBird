import pygame                                                          
from Bird import Bird                                                         
from Pipe import Pipe                                                                  
# Common pipe colors
red = (200, 0, 0)
green = (0, 200, 0)
blue = (100, 0, 200)

# Initialization
pygame.init()                                                                   
background = pygame.image.load("res/forest.jpg")  # Loading the background.
ball = pygame.image.load("res/smallbird.bmp")  # This loads the player.
pygame.mouse.set_visible(False) 
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 900
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
background = pygame.transform.scale(background, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
rect = background.get_rect()

clock = pygame.time.Clock()
FPS = 100 # Frames per second.  --- Faster, yet smaller moving increments

pipes = []
elapsed_time = 0
prev_click = 0
player = Bird(DISPLAY_HEIGHT, ball.get_rect()[3], prev_click)
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
    distance += 1
    rect[0] = -distance
    gameDisplay.blit(background, (rect[0] % DISPLAY_WIDTH, rect[1]))
    gameDisplay.blit(background, (rect[0] % DISPLAY_WIDTH - DISPLAY_WIDTH, rect[1]))

    # Moving the player.
    player.fall()
    player.prev_click = player.time
    player.time += 1
    gameDisplay.blit(ball, (50, player.position))

    # Pipe logic.
    if elapsed_time % (FPS) == 0:
        pipes.insert(0, Pipe(gameDisplay, DISPLAY_HEIGHT, DISPLAY_WIDTH, 4, (20, 130, 200)))
    for pipe in pipes:
        pipe.move()
        if pipe.x_pos < -pipe.width:
            del pipe
            del pipes[-1]

    # Frame by frame updating.
    pygame.display.update()
    clock.tick(FPS/2)
    
    elapsed_time += 1

quit()


