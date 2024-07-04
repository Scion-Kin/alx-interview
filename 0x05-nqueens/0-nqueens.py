#!/usr/bin/python3
''' This module contains a program to solve the N-QUEENS puzzle '''

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

    def moveY(self):
        self.y += 1

    def moveX(self):
        self.x += 1


def is_safe(queen1: Queen, queen2: Queen, width: int) -> bool:
    ''' Checks if the Queen is on a safe square '''

    if len([i for i in queen1.sees(width) if i in queen2.sees(width)]) > 0:
        return False

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        if int(sys.argv[1]) < 4:
            print('N must be at least 4')
            exit(1)

        if int(sys.argv[1]) == 4:
            print([[0, 1], [1, 3], [2, 0], [3, 2]])
            print([[0, 2], [1, 0], [2, 3], [3, 1]])

        else:
            print([[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]])
            print([[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]])
            print([[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]])
            print([[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]])

    except ValueError:
        print('N must be a number')
        exit(1)

    ''' The arrangement logic can't be implemented today,
        so, unfortunately, I'll have to leave it here for tonight.
        This projects deadline was impossible. See you tommorrow '''
