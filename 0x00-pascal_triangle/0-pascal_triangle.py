#!/usr/bin/python3
"""function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """this function returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    i = 1

    while i < n:
        prev_row = triangle[-1]
        new_row = [1]
        j = 1
        while j < i:
            new_row.append(prev_row[j - 1] + prev_row[j])
            j += 1
        new_row.append(1)
        triangle.append(new_row)
        i += 1

    return triangle
