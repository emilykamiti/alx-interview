def isWinner(x, nums):
    def is_prime(n):
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
            wins['Maria'] += 1
        else:
            wins['Ben'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None

result = isWinner(10000, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Winner:", result)
