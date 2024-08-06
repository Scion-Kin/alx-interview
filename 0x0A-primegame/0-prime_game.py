#!/usr/bin/python3
''' This defines functions '''


def is_prime(n):
    """Check if a number is a prime number."""

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    ''' Calculates the winner of the prime numbers game '''

    scores = {"Maria": 0, "Ben": 0}
    turns = ["Maria", "Ben"]

    if len(nums) == 0 or x == 0:
        return None

    for i in range(x):
        num = nums[i]
        primes = [i for i in range(num + 1) if is_prime(i)]
        turn = 0

        while len(primes) > -1:
            if len(primes) == 0:
                scores[turns[turn - 1]] += 1
                break

            picked = primes[0]
            primes = [i for i in primes if i % picked != 0]
            turn = 0 if turn == 1 else 1

    if scores["Maria"] == scores["Ben"]:
        return None

    return 'Maria' if scores['Maria'] > scores['Ben'] else 'Ben'
