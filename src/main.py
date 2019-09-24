import os
import pygame
from grid import Grid

WINDOW_SIZE = (800, 800)
FPS = 10
DESIRED_DELTA_TIME = 1 / FPS

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway's Game of Life")

grid = Grid((100, 100), (WINDOW_SIZE[0]//100, WINDOW_SIZE[1]//100))

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
LABEL_FONT = pygame.font.SysFont("arial black", 20)
LABEL_POSITION = (4, 4)

running = True
editing = True
generation = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.key == pygame.K_RETURN:
                editing = False
        if event.type == pygame.MOUSEBUTTONUP and editing:
            mouse_coords = pygame.mouse.get_pos()
            cell_coords = grid.get_corresponding_coords(mouse_coords)
            if grid.is_in_range(cell_coords):
                grid.invert_cell_state(cell_coords)

    if not editing:
        generation += 1
        grid.update()

    window.fill(COLOR_BLACK)
    grid.draw(window)

    if editing:
        intructions_label = LABEL_FONT.render("Press 'Enter' to run the simulation", 10, COLOR_RED)
        window.blit(intructions_label, LABEL_POSITION)
    else:
        generation_label = LABEL_FONT.render(f"Generation {generation}", 10, COLOR_RED)
        window.blit(generation_label, LABEL_POSITION)

    pygame.display.flip()

pygame.quit()
