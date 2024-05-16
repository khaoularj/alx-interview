#!/usr/bin/python3
"""The N Queens puzzle is a classic problem in which
the goal is to place N non-attacking queens on an N×N chessboard.
This means no two queens can be in the same row, column, or diagonal.
The objective is to write a program that finds and prints
all possible solutions for a given N."""
import sys


def safe_place(board, row, column):
    """function to check if a queen exist in the same columnumn"""
    for index in range(row):
        if board[index] == column:
            return False

    for index, key in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[index] == key:
            return False

    for index, key in zip(range(row, -1, -1), range(column, len(board))):
        if board[index] == key:
            return False

    return True


def solve_n_queens(number):
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * number
    results = []

    def helper_function(row):
        if row == number:
            results.append([[i, board[i]] for i in range(number)])
            return

        for column in range(number):
            if safe_place(board, row, column):
                board[row] = column
                helper_function(row + 1)
                board[row] = -1

    helper_function(0)
    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    results = solve_n_queens(N)
    for res in results:
        print(res)
