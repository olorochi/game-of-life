import time
import os
from game import Game
from writer import Writer


DELAY = 0.5

os.system('cls' if os.name == 'nt' else 'clear')
game = Game()
Writer.draw(game)

while (True):
    time.sleep(DELAY)
    game.pos.x += 1
    game.update()
    Writer.draw(game)
