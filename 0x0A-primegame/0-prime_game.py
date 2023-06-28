#!/usr/bin/python3
""" Determines the winner of a prime game."""


def isWinner(x, nums):
    """Returns the number of rounds to be played"""

    def is_prime(n):
        """Checks if number is prime"""

        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if x <= 0 or not nums:
        return None

    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None
