#!/usr/bin/python3

"""
Prime Game Module: Defines function that determines the winner after a certain
number of rounds of playing the Prime Game.
"""


def isWinner(x, nums):
    """
    Determines the winner after a certain number of rounds
    of playing the Prime Game.

    The Prime Game is a game where Maria and Ben take turns choosing a prime number
    from a set of consecutive integers starting from 1 up to and including n.
    The chosen prime number and its multiples are removed from the set.
    The player who cannot make a move loses the game.

    They play x rounds of the game, with n potentially different for each round.
    Assuming Maria always goes first and both players play optimally,
    this function determines the winner of each game.

    Args:
        x (int): The number of rounds.
        nums (list): List of n for each round.

    Returns:
        str: The name of the player that won the most rounds.
             If the winner cannot be determined, returns None.
    """
    if not nums or x < 1:
        return None

    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    for n in nums:
        primes = [i for i in range(2, n + 1) if isPrime(i)]
        if len(primes) % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == x:
        return None
    elif maria_wins * 2 > x:
        return "Maria"
    else:
        return "Ben"


if __name__ == "__main__":
    # Example usage
    print(isWinner(5, [2, 5, 1, 4, 3]))
