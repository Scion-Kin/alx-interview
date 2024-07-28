#!/usr/bin/python3
''' This defines a function '''


def makeChange(coins, total):
    ''' This returns the lowest amount of coin flips
        needed to make change for a given total '''

    coins = sorted(coins)
    coins.reverse()

    def recur(coins, coin, total, count=0):
        ''' This solves the problem recursively '''

        if total == 0:
            return count

        if total < 0 or total - coin < 0:
            nextcoin = coins.index(coin) + 1
            if nextcoin == len(coins):
                return -1

            return recur(coins, coins[nextcoin], total - coins[nextcoin],
                         count + 1)

        return recur(coins, coin, total - coin, count + 1)

    all = []
    for i in coins:
        try:
            all.append(recur(coins, i, total))

        except RecursionError:
            pass

    all = [i for i in all if i != -1]

    return 0 if total <= 0 else min(all) if len(all) != 0 else -1
