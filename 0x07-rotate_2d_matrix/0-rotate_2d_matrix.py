#!/usr/bin/python3
''' This defines a function '''

from time import sleep


def rotate_2d_matrix(matrix):
    ''' This prints a 90 degree rotated version of the given matrix '''

    grand = [[] for i in matrix]

    for j in range(len(matrix)):
        for i in range(len(matrix) - 1, -1, -1):
            grand[j].append(matrix[i][j])

    for i in range(len(matrix)):
        matrix[i] = grand[i]
