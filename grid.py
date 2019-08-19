import random
import numpy as np
import pygame

WHITE = (255, 255, 255)

class Grid:
    def __init__(self, size, cell_size):
        self.width = size[0]
        self.height = size[1]
        self.cell_size = cell_size
        self._grid = np.zeros((self.width, self.height), dtype=np.int8)
        
    def randomize(self):
        for y in range(self.height):
            for x in range(self.width):
                self._grid[y][x] = random.randint(0, 1)

    def update(self):
        _grid_next_generation = np.zeros((self.width, self.height), dtype=np.int8)
        for y in range(self.height):
            for x in range(self.width):
                _grid_next_generation[y][x] = self._should_survive((x, y), self._get_neighbours_number((x, y)))

        self._grid = _grid_next_generation

    def _get_neighbours_number(self, cell_coords):
        neighbours_number = 0
        for coords in self._get_neighbours_coords(cell_coords):
            if self.is_in_range(coords):
                neighbours_number += self.is_alive(coords)

        return neighbours_number

    def _get_neighbours_coords(self, cell_coords):
        neighbours_coords = [(x, y) \
            for x in range(cell_coords[0]-1, cell_coords[0]+2) \
            for y in range(cell_coords[1]-1, cell_coords[1]+2)]
        neighbours_coords.remove(cell_coords)

        return iter(neighbours_coords)

    def is_in_range(self, coords):
        return coords[0] >= 0 and coords[0] < self.width and coords[1] >= 0 and coords[1] < self.height

    def is_alive(self, cell_coords):
        return self._grid[cell_coords[1]][cell_coords[0]]

    def _should_survive(self, cell_coords, neighbours_number):
        return (neighbours_number == 3) or (self.is_alive(cell_coords) and neighbours_number == 2)

    def _draw_cell(self, surface, cell_coords):
        pygame.draw.rect(surface, WHITE, (cell_coords[0] * self.cell_size[0],
            cell_coords[1] * self.cell_size[1], *self.cell_size))

    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if self.is_alive((x, y)):
                    # Draw only alive cells
                    self._draw_cell(surface, (x, y))

    def get_corresponding_coords(self, coords):
        return (coords[0]//self.cell_size[0], coords[1]//self.cell_size[1])

    def invert_cell_state(self, cell_coords):
        self._grid[cell_coords[1]][cell_coords[0]] = int(not self._grid[cell_coords[1]][cell_coords[0]])
