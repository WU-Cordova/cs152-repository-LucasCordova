from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit

class GameController:
    def __init__(self, grid: Grid) -> None:
        print("from the constuctor")
        self.grid = grid

    def run(self) -> None:
        self.grid.display()
    