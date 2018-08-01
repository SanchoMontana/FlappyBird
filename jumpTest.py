import sys, pygame
pygame.init()

size = width, height = 1300, 500
speed = [0, 0]
black = 0, 0, 0

### physics
gravity = 9.8
currentVerticalSpeed = 1
currentVerticalPosition = 500

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed[1] += (currentVerticalSpeed * gravity)
                
                
    #reverses the directions when hitting a border
    ballrect = ballrect.move(speed)
##    if ballrect.left < 0 or ballrect.right > width:
##        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
