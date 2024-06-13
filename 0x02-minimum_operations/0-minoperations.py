#!/usr/bin/python3
''' This defines functions '''

import math


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


def minOperations(n):
    ''' Calculates the minimum number of operations needed to
        copy "n" number of H characters in a file using
        Copy all and Paste operations '''

    if not n or type(n) is not int or n == 0 or n == 1:
        return 0

    if is_prime(n):
        return n

    else:

        # First of all, let's find all the possible factors of n
        factors = []
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:  # Avoid duplicates for perfect squares
                    factors.append(n // i)
        factors.sort()

        # Now let's divide n to get the factors that completely divide it
        steps = []
        for i in factors:

            while n % i == 0:
                if n == 0:
                    break

                steps.append(i)
                n = n / i

        '''
            Amazingly, the number of minimum operations needed are the sum of
            the factors that completely divide the number. So, in the case
            where n is 6, the operations will be 2 + 3.

            1. Copy all (H), Paste -> (HH).

            2. Copy all (HH), Paste -> (HHHH), -> Paste (HHHHHH).

            As you can see, the operations are 5, in short 2 + 3!!
        '''

        return int(math.fsum(steps))
