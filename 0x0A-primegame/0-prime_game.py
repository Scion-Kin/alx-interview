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

    primes = [i for i in range(max(nums)) if is_prime(i)]
    M, B = 0, 0

    for i in range(2, x):
        num = nums[i]
        nprimes = [i for i in primes if i <= num]
        M = M + 1 if len(nprimes) - 1 % 2 == 0 else M + 0
        B += B + 1 if len(nprimes) % 2 == 0 else B + 0

    return 'Maria' if M > B else None if M == B else "Ben"
