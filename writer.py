from enum import StrEnum


class ANSI(StrEnum):
    NO_STYLE = '\033[0m'
    SAVE_POS = '\033[s'
    REST_POS = '\033[u'


class Writer:
    def save_pos():
        print(ANSI.SAVE_POS)

    def draw(grid):
        print(ANSI.REST_POS)
        for row in grid:
            for it in row:
                print(it.color, 'X', sep='', end='')
            print()
        print(ANSI.NO_STYLE)
