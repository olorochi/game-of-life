import time
import os
import threading
from game import Game
from writer import Writer
from queue import Queue
from enum import Enum, auto


DELAY = 0.5


class EventType(Enum):
    INPUT = auto(),
    UPDATE = auto()


class Event:
    def __init__(self, evtype):
        self.type = evtype


class InputEvent(Event):
    def __init__(self, pos):
        Event.__init__(self, EventType.INPUT)
        self.pos = pos


def event_loop():
    while True:
        ev = evs.get()
        game.update()
        Writer.draw(game)


def input_thr():
    pass


def update_thr():
    while True:
        evs.put(Event(EventType.UPDATE))
        time.sleep(DELAY)


os.system('cls' if os.name == 'nt' else 'clear')
game = Game()
evs = Queue()
for fn in [event_loop, input_thr, update_thr]:
    thr = threading.Thread(target=fn)
    thr.start()
