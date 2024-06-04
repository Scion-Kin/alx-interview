#!/usr/bin/python3
''' This module defines a function '''


def canUnlockAll(boxes):
    ''' This functions checks if all boxes can be opened or not '''

    if not boxes:
        return False

    keys = set(boxes[0])
    boxes[0] = 'opened'

    while True:
        if len(keys) == 0 and len([i for i in boxes if i != 'opened']) > 0:
            return False

        elif len(keys) == 0 and len([i for i in boxes if i != 'opened']) == 0:
            return True

        elif len([i for i in boxes if i == 'opened']) == len(boxes):
            return True

        else:
            box_found = False
            for key in keys:
                if boxes[key] != 'opened':
                    box_found = True
                    keys.update([i for i in boxes[key] if i < len(boxes)
                                 and i != 0])
                    boxes[key] = 'opened'
                    keys.remove(key)
                    break

            if not box_found:
                ''' We break the function here since,
                if the not box was found matching the keys in the set,
                the loop would run forever pointlessly '''

                return False
