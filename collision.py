def collided(playerRect, pipeList):
    for pipe in pipeList:
        if pipe.x_pos < playerRect[0] + playerRect[2] and pipe.x_pos + pipe.width > playerRect[0]:
            if pipe.height > playerRect[1] or pipe.height + pipe.gap < playerRect[1] + playerRect[3]:
                return True
    return False
