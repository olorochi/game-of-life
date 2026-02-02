import random
from enum import StrEnum


CHUNK_Y = 40
CHUNK_X = 80
LIFE_CHANCE = 0.3

class Color(StrEnum):
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    # YELLOW = '\033[33m'
    BLUE = '\033[34m'
    # MAGENTA = '\033[35m'
    # CYAN = '\033[36m'
    WHITE = '\033[37m'


class Cell:
    def __init__(self, color):
        self.color = color

    def alive(self):
        return self.color != Color.BLACK


class Chunk:
    def __init__(self, parent):
        colors = list(Color)
        wgts = [len(colors) - 1 if c == Color.BLACK else LIFE_CHANCE for c in colors]
        self.grid = [[Cell(c) for c in random.choices(colors, wgts, k=CHUNK_X)] for _ in range(CHUNK_Y)]
        self.update()

    def get_updated(self, parent)
        # starting with all dead means we don't have to kill cells manually
        grid = [[Cell(Color.BLACK) for _ in self.grid[0]] for _ in self.grid]

        for y, row in enumerate(self.grid):
            for x, it in enumerate(row):
                color, n = self.query_cell_neighbors(x, y)
                if (n == 2 and it.alive()):
                    grid[y][x] = it
                elif (n == 3):
                    grid[y][x].color = color

        return grid

class Game:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):

    def query_cell_neighbors(self, x, y):
        colors = dict((c, 0) for c in list(Color))
        colors.pop(Color.BLACK)

        rows = range(max(y - 1, 0), min(y + 2, len(self.grid)))
        for row in rows:
            cols = range(max(x - 1, 0), min(x + 2, len(self.grid[0])), 2 if row == y else 1)
            for col in cols:
                it = self.grid[row][col]
                if (it.alive()):
                    colors[it.color] += 1

        n = sum(colors.values())
        high = max(colors.values())
        color = random.choice([c for c, v in colors.items() if v == high])
        return color, n
