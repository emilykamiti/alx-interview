#!/usr/bin/python3
"""Determine the fewest number of coins needed to meeet a given amount total"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of coin values.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, num_coins = 0, 0
    cpy_total_amount = total
    len_coins = len(coins)

    while(i < len_coins and cpy_total_amount > 0):
        if (cpy_total_amount - coins[i]) >= 0:
            cpy_total_amount -= coins[i]
            num_coins += 1
        else:
            i += 1

    check = cpy_total_amount > 0 and num_coins > 0
    return -1 if check or num_coins == 0 else num_coins
