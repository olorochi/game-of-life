import time
from game import Game
from writer import Writer


GRID_HEIGHT = 40
GRID_WIDTH = 80
LIFE_CHANCE = 0.3
DELAY = 0.5

game = Game(GRID_WIDTH, GRID_HEIGHT, LIFE_CHANCE)
Writer.draw(game.grid)

while (True):
    time.sleep(DELAY)
    game.update()
    Writer.draw(game.grid)
