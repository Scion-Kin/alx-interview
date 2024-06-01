#!/usr/bin/python3
''' defines a function that returns the pascal triangle '''


def pascal_triangle(n):
    ''' returns the pascal's triangle for a given range '''

    if n == 0:
        return []

    if n == 1:
        return [[1]]

    grand_list = [[1], [1, 1]]

    if n == 2:
        return grand_list

    for i in range(3, n + 1):
        row = []

        prev = grand_list[-1]
        row.append(1)

        for i in range(1, len(prev)):
            row.append(prev[i - 1] + prev[i])

        row.append(1)

        grand_list.append(row)

    return grand_list
