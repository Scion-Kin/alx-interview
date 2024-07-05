#!/usr/bin/python3
''' This module contains a program to solve the N-QUEENS puzzle '''

from time import sleep
import sys


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

    def move(self, direction):
        self.y = self.y + 1 if direction == 'down' else self.y - 1


def is_safe(queen: Queen, queens: list, width: int) -> bool:
    ''' Checks if the Queen is on a safe square '''

    covered = [j for i in queens for j in i.sees(width)]

    return True if queen.to_list() not in covered else False


def board(width: int, queens: list):
    bo = [[' ' for i in range(width)] for j in range(width)]

    for i in queens:
        bo[i[0]][i[1]] = 'Q'

    for j in bo:
        print('\t\t\t\t', [*j], '\n')

    print('')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        if int(sys.argv[1]) < 4:
            print('N must be at least 4')
            exit(1)

        width = int(sys.argv[1])
        starting_position = [[width - 1, width - 1] for i in range(width)]

        shifted = [Queen(width - 1, i) for i in range(width)]
        #shifted[1].move('up')

        current = 0
        returning = False

        while [i.to_list() for i in shifted] != starting_position:
            ''' This loop will move every single queen on every possible
                square to check for all possible solutions
            '''
            queen = shifted[current]

            if current == 0:
                if returning:
                    if queen.y != 0:
                        queen.move('up')
                        board(width, [i.to_list() for i in shifted])

                current += 1
                continue

            left_queens = shifted[:current]
            queen.y = width - 1

            while not is_safe(queen, left_queens, width):
                if queen.y == 0:
                    break

                queen.move('up')
                board(width, [i.to_list() for i in shifted])
                sleep(2)

            returning = True
            if not is_safe(queen, left_queens, width):
                if shifted[0].y == 0:
                    break

                current = 0
                continue

            if current == width - 1:
                print([i.to_list() for i in shifted], '\n')

            current = current + 1 if current < width - 1 else 0

    except ValueError:
        print('N must be a number')
        exit(1)
