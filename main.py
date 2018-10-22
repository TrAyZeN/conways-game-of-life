import pygame
import os
import math
import numpy as np

# set the position of the window
window_pos_x = 100
window_pos_y = 100
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (window_pos_x, window_pos_y)

# Set the height and width of the screen
screen_size = (1600, 900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Conway's Game of life")

# cells measure 10 by 10 and are separated by 1 px
width = round(screen_size[0] / (10+1))      # set number of cells for the width
height = round(screen_size[1] / (10+1))     # set number of cells for the height


def intialize(width, height):
    """Initialize the game engine and return a blank grid"""
    
    pygame.init()
    grid = np.array([[0 for x in range(width)] for y in range(height)], dtype=np.int8)      # Create a blank grid
    return grid


def update(grid):
    """Compare each cells with their neighbours and update the board"""

    grid_next_generation = np.array([[0 for k in range(width+2)]], dtype=np.int8)

    for y in range(1, height+1):
        line = np.array([[0]], dtype=np.int8)
        for x in range(1, width+1):
            neighbours = 0 - grid[y][x]

            for i in range(y-1, y+2):
                for j in range(x-1, x+2):
                    if grid[i][j] == 1:
                        neighbours += 1

            if (neighbours == 3) or (grid[y][x] == 1 and neighbours == 2):
                line = np.append(line, [[1]], axis=1)
                pygame.draw.rect(screen, (255, 255, 255), [(x-1) * (10+1) + 1, (y-1) * (10+1) + 1, 10, 10])
            else:
                line = np.append(line, [[0]], axis=1)
                pygame.draw.rect(screen, (0, 0, 0), [(x-1) * (10+1) + 1, (y-1) * (10+1) + 1, 10, 10])

        line = np.append(line, [[0]], axis=1)
        grid_next_generation = np.append(grid_next_generation, line, axis=0)
    grid_next_generation = np.append(grid_next_generation, [[0 for k in range(width+2)]], axis=0)
    # grid = grid_next_generation
    return grid_next_generation


grid = intialize(width+2, height+2)
font = pygame.font.SysFont("arial black", 20)
done = False
play = False
turn = 0

# selection loop
while not done:
    pygame.time.Clock().tick(60)
    screen.fill((58, 58, 58))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play = True
                    done = True
                if event.key == pygame.K_RETURN:
                    play = True
                    done = True
            if event.type == pygame.MOUSEBUTTONUP:
                click_coords = pygame.mouse.get_pos()
                click_x = math.floor((click_coords[0]+10) / 11)
                click_y = math.floor((click_coords[1]+10) / 11)
                try:
                    grid[click_y][click_x] = int(not(grid[click_y][click_x]))
                except IndexError:
                    print("Click on the grid please")

    for y in range(1, height+1):
        for x in range(1, width+1):
            if grid[y][x] == 1:
                pygame.draw.rect(screen, (255, 255, 255), [(x-1) * (10+1) + 1, (y-1) * (10+1) + 1, 10, 10])
            else:
                pygame.draw.rect(screen, (0, 0, 0), [(x-1) * (10+1) + 1, (y-1) * (10+1) + 1, 10, 10])

    pygame.display.flip()

# play loop
while play:
    pygame.time.Clock().tick(5)
    screen.fill((58, 58, 58))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play = False

    turn += 1
    grid = update(grid)

    label = font.render("Generation: " + str(turn), 10, (255, 0, 0))
    screen.blit(label, (4, 4))

    pygame.display.flip()

pygame.quit()
