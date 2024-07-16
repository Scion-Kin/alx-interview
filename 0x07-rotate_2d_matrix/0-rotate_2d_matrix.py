#!/usr/bin/python3
''' This defines a function '''


def rotate_2d_matrix(matrix):
    ''' This prints a 90 degree rotated version of the given matrix '''

    for i in range(0, len(matrix)):
        ''''''
        to = (len(matrix[i]) - 1 - i)
        if i == len(matrix) - 1:
            to = len(matrix) - 1

        for j in range(to, -1, -1):
            ''''''
            indice = len(matrix) - 1 - i
            temp = matrix[j][indice]
            matrix[j][indice] = matrix[i][j]
            matrix[i][j] = temp

            if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
                temp = matrix[j][indice]
                matrix[j][indice] = matrix[i][j]
                matrix[i][j] = temp
