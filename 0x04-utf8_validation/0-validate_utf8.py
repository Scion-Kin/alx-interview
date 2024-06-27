#!/usr/bin/python3
''' This defines a function '''


def validUTF8(data):
    ''' This validates if a sequence in a list is UTF-8 compliant '''

    continue_indicators = {194: 2, 229: 3, 240: 4}

    if len(data) == 0 or type(data) != list:
        return False

    for i in range(len(data)):
        if type(data[i]) != int:
            return False

        if data[i] < 128:
            continue

        if data[i] not in continue_indicators:
            return False

        if not data[continue_indicators[data[i]] + i]:
            return False

        for j in data[i:continue_indicators[data[i]] + i]:
            if j < 128 or j > 191:
                return False

        i += continue_indicators[data[i]] + 1

    return True
