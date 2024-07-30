#!/usr/bin/python3
''' This defines a function '''


def island_perimeter(grid):
    ''' Returns the perimeter of an island '''

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                indices = [j - 1, j + 1, i - 1, i + 1]

                for k in indices[:2]:
                    if k == -1 or k > len(grid[i]) - 1:
                        count += 1
                        continue

                    if grid[i][k] == 0:
                        count += 1

                for k in indices[2:]:
                    if k == -1 or k > len(grid) - 1:
                        count += 1
                        continue

                    if grid[k][j] == 0:
                        count += 1

    return count
