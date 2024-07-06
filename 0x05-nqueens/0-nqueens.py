#!/usr/bin/python3
''' This module contains a program to solve the N-QUEENS puzzle '''

from time import sleep
import sys


patterns = []


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
        return "Queen {} is on row {}".format(self.x + 1, self.y + 1)

    def to_list(self):
        return [self.y, self.x]

    def move(self):
        self.y -= 1


def is_safe(queen: Queen, queens: list, width: int) -> bool:
    ''' Checks if the Queen is on a safe square '''

    covered = [j for i in queens for j in i.sees(width)]

    return True if len(queens) == 0 or queen.to_list() not in covered else False


def board(width: int, queens: list):
    bo = [[' ' for i in range(width)] for j in range(width)]

    for i in [i.to_list() for i in queens]:
        bo[i[0]][i[1]] = 'Q'

    for j in bo:
        print('\t\t\t\t', [*j], '\n')

    print()


def safe_shift(queen: Queen, queens: list, index: int, width: int) -> bool:
    ''' This moves a queen upward in a safe square '''

    if queen.y == 0:
        if len(queens) == 0:
            print(*patterns, sep='\n\n')
            exit(0)

        else:
            queen.y = width - 1
            index -= 1
            return safe_shift(queens[index], queens[:index], index, width)

    queen.move()

    while not is_safe(queen, queens[:index], width):
        if queen.y == 0:
            queen.y = width - 1
            index -= 1
            return safe_shift(queens[index], queens[:index], index, width)

        queen.move()

    return index

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N'), exit(1)

    try:
        if int(sys.argv[1]) < 4:
            print('N must be at least 4'), exit(1)

        width = int(sys.argv[1])

        queens = [Queen(width - 1, i) for i in range(width)]

        current = 1
        # shifting = 0  # queen to check for all preceding queens possibilities

        while True:
            ''' To be documented '''

            # board(width, queens)  # print the board
            # sleep(2)

            queen = queens[current]
            if current == 0:
                for i in range(1, width):
                    queens[i].y = width - 1

                queen.move()
                current += 1
                continue

            while not is_safe(queen, queens[:current], width):
                if queen.y == 0:
                    break
                queen.move()
                # board(width, queens)

            if not is_safe(queen, queens[:current], width):
                current = safe_shift(queen, queens[:current], current, width)

            if is_safe(queen, queens[:current], width) and queen == queens[width - 1]:                
                print("Found combination!", '\n')
                print(*[i.to_list() for i in queens], '\n')
                patterns.append([[i.x, i.y] for i in queens])

            current = current + 1 if current < width - 1 else 0

    except ValueError:
        print('N must be a number')
        exit(1)
