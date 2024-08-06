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

    scores, turns = [0, 0], ["Ben", "Maria"]
    primes = [i for i in range(max(nums) + 1) if is_prime(i)]

    for i in range(x):
        nprimes = [j for j in primes if j <= nums[i]]
        scores[len(nprimes) % 2] += 1

    return None if scores[0] == scores[1] else turns[scores.index(max(scores))]
