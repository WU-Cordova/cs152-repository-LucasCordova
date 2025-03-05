from __future__ import annotations
import random

from datastructures.array2d import Array2D
from projects.project2.cell import Cell


class Grid:
    def __init__(self, rows: int=10, cols: int=10):
        self.grid: Array2D[Cell] = Array2D.empty(rows, cols, data_type=Cell)

        self.rows = rows
        self.cols = cols

        for row in range(rows):
            for col in range(cols):
                self.grid[row][col].is_alive = random.choice([True, False])


    def display(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end='')
            print()
        print()
    
    def get_neighbors(self, row, col) -> int:
        count = 0

        if col < self.cols and self.grid[row][col + 1].is_alive: # right
            count += 1
        # the rest of the 7 cases


        return count
    
    def next_generation(self) -> Grid:
        next_grid = Grid(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                num_neighbors = self.get_neighbors(row, col)
                next_state = self.grid[row][col].next_state(num_neighbors)
                next_grid[row][col].is_alive = next_state

        return next_grid
    
    def __eq__(self, value):
        if isinstance(value, Grid) and self.rows == value.rows and self.cols == value.cols:
            return self.grid == value.grid
        return False