#!/usr/bin/python3
''' This module defines a function '''


def canUnlockAll(boxes):
    ''' This function checks if all boxes can be opened or not '''

    if not boxes:
        return False

    keys = set(boxes[0])
    opened_boxes = {0}

    while True:
        new_keys_found = False

        for key in list(keys):
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                keys.update(boxes[key])
                new_keys_found = True

        if len(opened_boxes) == len(boxes):
            return True

        if not new_keys_found:
            return False
