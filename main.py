import time
import os
import sys
import tty
import threading
from enum import StrEnum
from game import CHUNK_X, CHUNK_Y, Point, Game
from queue import Queue
from event import Event, EventType, InputEvent


DELAY = 0.5


class ANSI(StrEnum):
    NO_STYLE = '\033[0m'
    HOME = '\033[H'


def getch():
    fd = sys.stdin.fileno()
    tty.setcbreak(fd)
    ch = sys.stdin.read(1)
    return ch


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


def draw(game):
    print(ANSI.HOME, end='')
    half_y = CHUNK_Y // 2
    half_x = CHUNK_X // 2
    for y in range(game.pos.y - half_y, game.pos.y + half_y):
        for x in range(game.pos.x - half_x, game.pos.x + half_x):
            print(game[Point(x, y)].color, 'X', sep='', end='')
        print()
    print(ANSI.NO_STYLE, end='')


os.system('clear')
events = Queue()
game = Game(events)
for fn in [input_thr, update_thr]:
    thr = threading.Thread(target=fn)
    thr.start()

while True:
    ev = events.get()
    if (ev.type == EventType.INPUT):
        game.pos += ev.vec
        draw(game)
    elif (ev.type == EventType.UPDATE):
        game.get_update()
    else:  # EventType.UPDATED
        draw(game)
