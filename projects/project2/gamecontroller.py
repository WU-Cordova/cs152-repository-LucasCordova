from time import sleep
from typing import List
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit

class GameController:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.history: List[Grid] = []

    def run(self) -> None:
        

        print("Press 'q' to quit.")

        kbhit = KBHit()

        while True:
            self.grid.display()
            sleep(1)
            if kbhit.kbhit():
                key =kbhit.getch()

                if key == 'q':
                    print("you hit quit")
                    return
            
            self.history.append(self.grid)
            self.grid = self.grid.next_generation()


