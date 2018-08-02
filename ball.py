import pygame, sys, random
from Pipe import Pipe
pygame.init()
pygame.mouse.set_visible(False)
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 700
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
FPS = 100 # Frames per second.
background = pygame.image.load("res/forest.jpg")
background = pygame.transform.scale(background, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
back = background.get_rect()
distance = 0

click_time = 0
time = 0
currentVerticalPos = DISPLAY_HEIGHT / 2

h_b_r = 230
speed = 2

rectangleObjectList = []
black = 0, 0, 0
prev_click = 0
# Image init:

ball = pygame.image.load("res/smallbird.bmp")
ballrect = ball.get_rect()

def displayRectangles():
    for rect in rectangleObjectList:
        h = rect.pipe_height
        w = rect.pipe_width
        x = rect.x_pos
        gap_pos = h_b_r + h

        # This is where the rectangles/pipe get drawn
        # Top:
        pygame.draw.rect(gameDisplay, black, [x, 0, w, h])
        # Bottom:
        pygame.draw.rect(gameDisplay, black, [x, gap_pos, w, DISPLAY_HEIGHT - gap_pos])

# Main loop:
while True:
    game_exit = False
    while not game_exit:
        # Event handling.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    click_time = 0
        
        distance += 1
        # Moving Background
        back[0] = -distance
        gameDisplay.blit(background, (back[0] % DISPLAY_WIDTH, back[1]))
        gameDisplay.blit(background, (back[0] % DISPLAY_WIDTH - DISPLAY_WIDTH, back[1]))

        if currentVerticalPos > DISPLAY_HEIGHT:
            sys.exit()
            #game_exit = True
        if time % (FPS) == 0:
            rectangleObjectList.append(Pipe(DISPLAY_HEIGHT, DISPLAY_WIDTH, speed))

        # iterate each rect object
        for rect in rectangleObjectList:
            rect.move()
            if rect.x_pos < -rect.pipe_width:   
                rectangleObjectList.pop(0)
        displayRectangles()

        currentVerticalPos += click_time - 20 + (prev_click * 1.3)
        #print(click_time)
                                # Middle-ish of screen
        gameDisplay.blit(ball, (450, currentVerticalPos))
            
        pygame.display.update() 
        clock.tick(FPS)
        prev_click = click_time
        click_time += 1
        time += 1

        #print(rectangleObjectList)

quit()
