from random import choice
from enum import StrEnum


class Color(StrEnum):
    BLACK = '\033[30m'
    # RED = '\033[31m'
    # GREEN = '\033[32m'
    # YELLOW = '\033[33m'
    # BLUE = '\033[34m'
    # MAGENTA = '\033[35m'
    # CYAN = '\033[36m'
    WHITE = '\033[37m'
    # DEFAULT = '\033[0m'


class Cell:
    def __init__(self, color):
        self.color = color

    def alive(self):
        return self.color != Color.BLACK


class Game:
    def __init__(self, x, y):
        colors = list(Color)
        self.grid = [
                [Cell(choice(colors)) for _ in range(x)] for _ in range(y)
            ]
        self.update()

    def update(self):
        for y, row in enumerate(self.grid):
            for x, it in enumerate(row):
                n = self.count_cell_neighbors(x, y)
                if (n == 2):
                    pass
                elif (n == 3):
                    it.color = Color.WHITE
                else:
                    self.cell_die(x, y)

    def count_cell_neighbors(self, x, y):
        n = 0
        for i in range(y - 1, y + 1):
            for j in range(x - 1, x + 1, 2 if i == y else 1):
                if (self.grid[i][j].alive()):
                    n += 1

        return n

    def cell_die(self, x, y):
        self.grid[y][x] = Cell(Color.BLACK)
