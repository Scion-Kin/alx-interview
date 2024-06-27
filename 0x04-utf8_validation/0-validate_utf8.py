#!/usr/bin/python3
''' This defines a function '''


def validUTF8(data):
    ''' This validates if a sequence in a list is UTF-8 compliant '''

    # Mask values for checking the bytes
    def is_continuation_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]

        if (byte & 0b10000000) == 0:  # 1-byte character (0xxxxxxx)
            i += 1
            continue
        elif (byte & 0b11100000) == 0b11000000:
            # 2-byte character (110xxxxx 10xxxxxx)
            num_bytes = 2

        elif (byte & 0b11110000) == 0b11100000:
            # 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
            num_bytes = 3

        elif (byte & 0b11111000) == 0b11110000:
            # 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
            num_bytes = 4

        else:
            # Invalid first byte
            return False

        # Check if there are enough continuation bytes
        if i + num_bytes > len(data):
            return False

        # Check continuation bytes
        for j in range(1, num_bytes):
            if not is_continuation_byte(data[i + j]):
                return False

        i += num_bytes

    return True
