#!/usr/bin/python3
"""The player that cannot make a move loses the game."""


def isWinner(x, nums):
    """
    returns:
        the name of the player that won the most rounds,
        if both players play optimally,
        or None, if the winner cannot be determined
    """
    if not nums or x < 1:  # if nums is empty or x is less than 1
        return None
    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i*i, n + 1, i):
            sieve[j] = False  # set the value to False (not prime)

    sieve[0] = sieve[1] = False
    count = 0  # initialize count to 0 (Maria's score)
    for i in range(len(sieve)):
        if sieve[i]:
            count += 1
        sieve[i] = count  # set the value to the count of primes

    player1 = 0
    for n in nums:  # loop through the nums list and count Maria's wins
        player1 += sieve[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"  # Maria wins
    return "Beiin"  # Ben wins
