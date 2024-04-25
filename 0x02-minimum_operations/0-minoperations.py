#!/usr/bin/python3
"""method that calculates the fewest number of operations
needed to result in exactly n H characters in the file"""


def minOperations(n):
    """this method calculates the minimum number
    of operations to achieve n 'H' characters"""
    if n == 1:
        return 1
    prev_power_2 = 1 << (n.bit_length() - 1) - 1
    if prev_power_2 == 0:
        return 0
    return 1 + minOperations(n - prev_power_2)
