#!/usr/bin/python3
"""primegame"""


def isWinner(x, nums):
    """this function determine who the winner of each game is"""
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for current in range(2, int(max_num ** 0.5) + 1):
        if is_prime[current]:
            for multiple in range(current * current, max_num + 1, current):
                is_prime[multiple] = False

    for num in nums:
        prime_count = sum(is_prime[2:num + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
