#!/usr/bin/python3
''' Solves the N-QUEENS Challenge '''

import argparse
from time import sleep
from datetime import datetime as dt


def board(width: int, queens: list):
    bo = [[' ' for i in range(width)] for j in range(width)]

    for i in queens:
        bo[i[0]][i[1]] = 'Q'

    for j in bo:
        print('\t\t\t\t', [*j], '\n')

    print()
    sleep(0.2)


def check(index, inits):
    ''' this solves the N_QUEENS challenge recursively '''
    covered = []
    up, down, right = inits[index], inits[index], inits[index]

    for i in range(len(inits), 0, -1):
        up = [up[0] - 1, up[1] + 1]
        down = [down[0] + 1, down[1] + 1]
        right = [right[0], right[1] + 1]
        covered.extend([up, right, down])

    return covered


def run(index):
    ''' run recursively '''
    covered = []
    for i in range(index):
        covered += check(i, inits)

    pos = [i for i in range(width) if i not in [i[0] for i in inits[:index]]]

    for i in pos:
        inits[index][0] = i
        if inits[index] in covered:
            continue

        if index == width - 1:
            if args.verbose:
                board(width, inits)

            combo.append([[j[1], j[0]] for j in inits])
            return

        run(index + 1)


if __name__ == "__main__":
    try:
        parser = argparse\
            .ArgumentParser(description='Solves the N-Queens puzzle.')
        parser.add_argument('N', type=int,
                            help='Size of the board (N must be at least 4)')
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='Enable verbose output')
        args = parser.parse_args()

        width = int(args.N)
        if width < 4:
            print('N must be at least 4'), exit(1)

        inits, combo = [[width - 1, i] for i in range(width)], []
        then = dt.now()

        print("\n\t Started... \n\n \t Crunching possibilities... \n")

        run(0), print("\t Finished in {}".format(dt.now() - then))

        print("\n\t Patterns found: {}\n".format(len(combo)))
        [print("\t {}".format(i)) for i in combo]

    except ValueError:
        print('N must be a number'), exit(1)
