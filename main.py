import time
import os
import threading
from game import Game, Point
from writer import Writer
from queue import Queue
from getch import getch
from event import Event, EventType, InputEvent


DELAY = 0.5


def input_thr():
    while True:
        c = getch()
        if c in ['h', 'a']:
            pt = Point(-1, 0)
        elif c in ['j', 's']:
            pt = Point(0, 1)
        elif c in ['k', 'w']:
            pt = Point(0, -1)
        elif c in ['l', 'd']:
            pt = Point(1, 0)
        else:
            continue

        events.put(InputEvent(pt))


def update_thr():
    while True:
        events.put(Event(EventType.UPDATE))
        time.sleep(DELAY)


os.system('cls' if os.name == 'nt' else 'clear')
events = Queue()
game = Game(events)
for fn in [input_thr, update_thr]:
    thr = threading.Thread(target=fn)
    thr.start()

while True:
    ev = events.get()
    if (ev.type == EventType.INPUT):
        game.pos += ev.vec
        Writer.draw(game)
    elif (ev.type == EventType.UPDATE):
        game.get_update()
    else:  # EventType.UPDATED
        Writer.draw(game)
