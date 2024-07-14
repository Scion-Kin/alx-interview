#!/usr/bin/python3
''' Solves the N-QUEENS Challenge '''

import sys
from time import sleep


def board(width: int, queens: list):
    bo = [[' ' for i in range(width)] for j in range(width)]

    for i in queens:
        bo[i[0]][i[1]] = 'Q'

    for j in bo:
        print('\t\t\t\t', [*j], '\n')

    print()
    sleep(0.5)

def check(index, init):
    ''' this solves the N_QUEENS challenge recursively '''
    covered = []
    up, down, right = init[index], init[index], init[index]

    for i in range(len(init), 0, -1):
        up = [up[0] - 1, up[1] + 1]
        down = [down[0] + 1, down[1] + 1]
        right = [right[0], right[1] + 1]
        covered.extend([up, right, down])

    return covered

def run(index):
    ''' run recursively '''
    covered = []
    for i in range(index):
        covered += check(i, init)
    
    pos = [i for i in range(width) if i not in [i[0] for i in init[:index]]]

    for i in pos:
        init[index][0] = i

        if init[index] in covered:
            continue

        if index == width - 1:
            # board(width, init)
            combo.append([[j[1], j[0]] for j in init])
            return

        run(index + 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N'), exit(1)

    try:
        width = int(sys.argv[1])
        if width < 4:
            print('N must be at least 4'), exit(1)

        init = [[width - 1, i] for i in range(width)]
        combo = []

        run(0)

        print(*combo, sep='\n')
        print("\n Combinations found: {}".format(len(combo1)))

    except ValueError:
        print('N must be a number'), exit(1)
