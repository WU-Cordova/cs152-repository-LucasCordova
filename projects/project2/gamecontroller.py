from time import sleep
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit

class GameController:
    def __init__(self, grid: Grid):
        self.grid = grid

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
            
            self.grid = self.grid.next_generation()


