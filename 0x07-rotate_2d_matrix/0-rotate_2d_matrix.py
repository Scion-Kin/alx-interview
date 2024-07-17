#!/usr/bin/python3
''' This defines a function '''


def rotate_2d_matrix(matrix):
    ''' This rotates a matrix to 90 degrees'''

    grand = [[] for i in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix) - 1, -1, -1):
            grand[i].append(matrix[j][i])

    for i in range(len(matrix)):
        matrix[i] = grand[i]


'''
    The solution to this problem is not literally swapping the values in
    the matrix. Rather, it is copying the indices in a new list,
    in a way that they will be rotated.
'''
