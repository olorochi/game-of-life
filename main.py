import time
from game import Game
from writer import Writer


DELAY = 0.5

game = Game(LIFE_CHANCE)
Writer.save_pos()
Writer.draw(game.grid)

while (True):
    time.sleep(DELAY)
    game.update()
    Writer.draw(game.grid)
