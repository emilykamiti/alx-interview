#!/usr/bin/python3
""" In this module is a function for calculating the perimeter of an island."""


def island_perimeter(grid):
    """calculating the perimeter of the island is described in the grid."""

    r = len(grid)
    c = len(grid[0])
    perimeter = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                perimeter += 4

                # cells that are adjacent
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
