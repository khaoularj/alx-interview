#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """this function rotate an n x n 2D matrix to 90 degrees clockwise"""
    n = len(matrix)
    index = 0
    while index < n // 2:
        j = index
        while j < n - index - 1:
            res = matrix[index][j]
            matrix[index][j] = matrix[n - 1 - j][index]
            matrix[n - 1 - j][index] = matrix[n - 1 - index][n - 1 - j]
            matrix[n - 1 - index][n - 1 - j] = matrix[j][n - 1 - index]
            matrix[j][n - 1 - index] = res
            j += 1
        index += 1
