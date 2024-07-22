#!/usr/bin/python3

"""
    Determines if a given data set represents a valid UTF-8 encoding.

    This script takes a list of integers representing bytes in the data set
    and returns a boolean indicating whether or not the data set is a valid
    UTF-8 encoding.

    Args:
        data (List[int]): list of integers representing bytes in the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
        bool: True if data is a valid UTF-8 encoding, else False.
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    A valid UTF-8 encoding is when all bytes in the data set are valid
    UTF-8 encoded characters.

    Args:
        data (List[int]): list of integers representing bytes in the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    count = 0
    for byte in data:
        if count == 0:
            if (byte >> 5) == 0b110:
                count = 1
            elif (byte >> 4) == 0b1110:
                count = 2
            elif (byte >> 3) == 0b11110:
                count = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
