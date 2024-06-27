#!/usr/bin/python3
''' This defines a function '''


def validUTF8(data):
    ''' This validates if a sequence in a list is UTF-8 compliant '''

    continue_indicators = {194: 2, 229: 3, 240: 4, 250: 5}

    if len(data) == 0:
        return True

    if data[0] < 128:
        return validUTF8(data[1:])

    if data[0] not in continue_indicators:
        return False

    if len(data) < continue_indicators[data[0]]:
        return False

    for i in data[1:continue_indicators[data[0]] + 1]:
        if i < 128 or i > 191:
            return False

    return validUTF8(data[continue_indicators[data[0]]:])
