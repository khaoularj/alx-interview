#!/usr/bin/python3
"""method that calculates the fewest number of operations
needed to result in exactly n H characters in the file"""


def minOperations(n):
    """this method calculates the minimum number
    of operations to achieve n 'H' characters"""
    if n == 1:
        return 0

    operations = float('inf')

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factor_operations = minOperations(i) + n // i
            operations = min(operations, factor_operations)

    return operations
