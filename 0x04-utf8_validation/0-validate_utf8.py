#!/usr/bin/python3
''' This defines a function '''


def recur(li):
    ''' Handles execution with recursion '''

    continue_indicators = {194: 2, 229: 3, 240: 4, 250: 5}

    if len(li) == 0:
        return True

    if li[0] < 128:
        return recur(li[1:])

    if li[0] not in continue_indicators:
        return False

    if len(li) < continue_indicators[li[0]]:
        return False

    for i in li[1:continue_indicators[li[0]] + 1]:
        if i < 128 or i > 191:
            return False

    return recur(li[continue_indicators[li[0]]:])


def validUTF8(data):
    ''' This validates if a sequence in a list is UTF-8 compliant '''

    return recur(data) if len(data) > 0 else False
