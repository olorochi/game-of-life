class Writer:
    def draw(grid):
        for row in grid:
            for it in row:
                print(it.color, '█', sep='', end='')
            print()
        print('\033[0m')
