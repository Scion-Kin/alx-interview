#!/usr/bin/python3
''' This defines a function '''


def makeChange(coins, total):
    ''' This returns the lowest total of coin flips
        needed to make change for a given total '''

    if total <= 0:
        return 0

    # This table will store the answer to our sub problems
    dp = [total + 1] * (total + 1)

    '''
    The answer to making change with minimum coins for 0
    will always be 0 coins no matter what the coins we are
    given are
    '''
    dp[0] = 0

    # Solve every subproblem from 1 to total
    for i in range(1, total + 1):
        # For each coin we are given
        for j in range(0, len(coins)):
            # If it is less than or equal to the sub problem total
            if coins[j] <= i:
                # Try it. See if it gives us a more optimal solution
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    '''
    dp[total] has our answer. If we do not have an answer then dp[total]
    will be total + 1 and hence dp[total] > total will be true. We then
    return -1.

    Otherwise, dp[total] holds the answer
    '''

    return -1 if dp[total] > total else dp[total]
