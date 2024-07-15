#!/usr/bin/python3
''' Solves the N-QUEENS Challenge.
    I gotta say... I'm very proud of this one. This wasn't easy.
'''

import sys


def check(index, inits):
    ''' this registers attacked squares '''
    covered = []
    up, down, right = inits[index], inits[index], inits[index]

    for i in range(len(inits), 0, -1):
        up = [up[0] - 1, up[1] + 1]
        down = [down[0] + 1, down[1] + 1]
        right = [right[0], right[1] + 1]
        covered.extend([up, right, down])

    return covered


def run(index):
    ''' run recursively to find possible patterns '''
    covered = []
    for i in range(index):
        covered += check(i, inits)

    pos = [i for i in range(width) if i not in [i[0] for i in inits[:index]]]

    for i in pos:
        inits[index][0] = i
        if inits[index] in covered:
            continue

        if index == width - 1:
            combo.append([[j[1], j[0]] for j in inits])
            return

        run(index + 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N'), exit(1)

    try:
        width = int(sys.argv[1])
        if width < 4:
            print('N must be at least 4'), exit(1)

        inits, combo = [[width - 1, i] for i in range(width)], []

        run(0), print(*combo, sep='\n')

    except ValueError:
        print('N must be a number'), exit(1)
