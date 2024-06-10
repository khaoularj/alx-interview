#!/usr/bin/python3
""" function def island_perimeter(grid)"""


def island_perimeter(grid):
    """this function returns the perimeter
    of the island described in grid"""
    perimeter = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    if not grid:
        return 0
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
