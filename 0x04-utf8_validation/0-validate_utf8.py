#!/usr/bin/python3
""" Validates if a given data set represents a valid UTF-8 encoding. """


def validUTF8(data):
    """Validates if a given data set is a valid UTF-8 encoding.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    no_bytes = 0
    for num in data:
        mask = 1 << 7
        if no_bytes == 0:
            while mask & num:
                no_bytes += 1
                mask >>= 1
            if no_bytes == 0:
                continue
            if no_bytes == 1 or no_bytes > 4:
                return False
        else:
            if num >> 6 != 0b10:
                return False
        no_bytes -= 1
    return no_bytes == 0
