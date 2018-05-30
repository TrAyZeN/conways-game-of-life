import pygame
import os
import math

# set the position of the window
windowX = 100
windowY = 100
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (windowX, windowY)

# Set the height and width of the screen
screenSize = (1600, 900)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Conway's Game of life")
# cells measure 10 by 10 and are separated by 1 px
w = round(screenSize[0]/(10+1)) # set number of cells for the width
h = round(screenSize[1]/(10+1)) # set number of cells for the height

def intialization(w, h):
    pygame.init()
    
    grid = [[0 for x in range(w)] for y in range(h)] # Create a blank grid
    return grid

grid = intialization(w+2, h+2)
font = pygame.font.SysFont("arial black", 20)
done = False
play = False
turn = 0

def update():
    global grid
    gridNextGen = [[0 for k in range(w+2)]]

    for y in range(1, h+1):
        line = [0]
        for x in range(1, w+1):
            neighbours = 0 - grid[y][x]

            for i in range(y-1, y+2):
                for j in range(x-1, x+2):
                    if grid[i][j] == 1:
                        neighbours += 1

            if (neighbours == 3) or (grid[y][x] == 1 and neighbours == 2):
                line.append(1)
                pygame.draw.rect(screen, (255, 255, 255), [(x-1)*(10+1)+1, (y-1)*(10+1)+1 , 10, 10])
            else:
                line.append(0)
                pygame.draw.rect(screen, (0, 0, 0), [(x-1)*(10+1)+1, (y-1)*(10+1)+1, 10, 10])
        line.append(0)
        gridNextGen.append(line)
    gridNextGen.append([0 for k in range(w+2)])
    grid = gridNextGen

while not done:
    pygame.time.Clock().tick(5)
    screen.fill((58, 58, 58))
    if not play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play = True
                    done = True
                if event.key == pygame.K_RETURN:
                    play = True
            if event.type == pygame.MOUSEBUTTONUP:
                clickCoords = pygame.mouse.get_pos()
                x = math.floor((clickCoords[0]+10)/11)
                y = math.floor((clickCoords[1]+10)/11)
                try:
                    grid[y][x] = int(not(grid[y][x]))
                except IndexError:
                    print("Click on the grid please")

        for y in range(1, h+1):
            for x in range(1, w+1):
                if grid[y][x] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), [(x-1)*(10+1)+1, (y-1)*(10+1)+1 , 10, 10])
                else:
                    pygame.draw.rect(screen, (0, 0, 0), [(x-1)*(10+1)+1, (y-1)*(10+1)+1, 10, 10])

    else:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        turn += 1
        update()

        label = font.render("Generation: " + str(turn), 10, (255,0,0))
        screen.blit(label, (4, 4))

    pygame.display.flip()

pygame.quit()
