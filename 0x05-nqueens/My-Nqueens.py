#!/usr/bin/python3
''' This module contains the verbose capable version of the alx task
    This module contains everything to help visualize the process
    of solving the challenge. To enable verbose, run the program like this:

      ./0-nqueens.py 5 -v          # 5 is the number of queens
 '''

from datetime import datetime as dt
from time import sleep
import argparse


class Queen:
    ''' A Queen class for all the necessary methods. '''

    def __init__(self, y: int, x: int) -> None:
        ''' This initiates a queen '''
        self.y = y
        self.x = x

    def sees(self, width: int) -> list:
        ''' Returns the squares a queen sees '''

        squares = []
        col = [[i, self.x] for i in range(0, width)]
        row = [[self.y, i] for i in range(0, width)]

        # Left diagonal
        if self.y != 0:
            row_index = self.x
            for i in range(self.y - 1, -1, -1):
                if row_index == 0:
                    break
                row_index -= 1  # we're traversing back
                squares.append([i, row_index])

        row_index = self.x
        for i in range(self.y + 1, width):
            if row_index == width - 1:
                break
            row_index += 1  # we're going forward now
            squares.append([i, row_index])

        # Rigth diagonal
        if self.x + 1 != width:
            row_index = self.x
            for i in range(self.y - 1, -1, -1):
                if row_index == width - 1:
                    break
                row_index += 1
                squares.append([i, row_index])

        row_index = self.x
        for i in range(self.y + 1, width):
            if row_index == 0:
                break
            row_index -= 1
            squares.append([i, row_index])

        all = []
        for i in squares + col + row:
            if i not in all:
                all.append(i)

        return all

    def __str__(self):
        return "Queen {} is on row {}".format(self.x, self.y)

    def to_list(self):
        return [self.y, self.x]

    def move(self):
        self.y -= 1


def is_safe(queen: Queen, queens: list, width: int) -> bool:
    ''' Checks if the Queen is on a safe square '''
    covered = [j for i in queens for j in i.sees(width)]

    return True if queen.to_list() not in covered else False


def board(width: int, queens: list):
    bo = [[' ' for i in range(width)] for j in range(width)]

    for i in [i.to_list() for i in queens]:
        bo[i[0]][i[1]] = 'Q'

    for j in bo:
        print('\t\t\t\t', [*j], '\n')

    print()


def run(queens, index, width):
    ''' shifts the coordinates recursively '''
    queen = queens[index]
    queen.y = width

    while queen.y != 0:
        queen.move()
        if index == width - 1:
            if check_pattern(queens) and args.verbose:
                board(width, queens)
                sleep(1)

        else:
            run(queens, index + 1, width)


def check_pattern(queens):
    ''' checks for a potential pattern '''
    for i in range(1, width):
        if not is_safe(queens[i], queens[:i], width):
            return False
        else:
            if queens[i] == queens[width - 1]:
                patterns.append([[i.x, i.y] for i in queens])
                print(patterns[-1], '\n')
                return True


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="N-Queens Solver")
        parser.add_argument("-v", "--verbose", action="store_true",
                            help="increase output verbosity")
        parser.add_argument("N", type=int, help="size of the board")
        args = parser.parse_args()

        if args.verbose:
            print("Verbose mode is on \n")

        then = dt.now()
        width = int(args.N)
        if width < 4:
            print('N must be at least 4'), exit(1)

        queens = [Queen(width - 1, i) for i in range(width)]
        patterns = []

        run(queens, 0, width)
        print("\nFinished in {}\n".format(dt.now() - then))
        print("Patterns found: {}".format(len(patterns)))

    except ValueError:
        print('N must be a number'), exit(1)
