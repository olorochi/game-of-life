import time
from game import Game
from writer import Writer


GRID_HEIGHT = 40
GRID_WIDTH = 80

game = Game(GRID_WIDTH, GRID_HEIGHT)
Writer.draw(game.grid)

while (True):
    time.sleep(1)
    game.update()
    Writer.draw(game.grid)
