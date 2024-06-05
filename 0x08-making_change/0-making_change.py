#!/usr/bin/python3
"""determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """function that returns the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    minm = [float('inf')] * (total + 1)
    minm[0] = 0

    for i in coins:
        for k in range(i, total + 1):
            if minm[k - i] + 1 < minm[k]:
                minm[k] = minm[k - i] + 1
    if minm[total] == float('inf'):
        return -1
    else:
        return minm[total]
