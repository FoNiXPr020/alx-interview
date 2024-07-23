"""
Validates if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Validates if a given data set is a valid UTF-8 encoding.

    Args:
        data (List[int]): list of integers representing bytes in the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    skip = 0
    for i, byte in enumerate(data):
        if skip > 0:
            skip -= 1
            continue
        if not (isinstance(byte, int) and 0 <= byte <= 0x10ffff):
            return False
        if byte <= 0x7f:
            skip = 0
        elif byte >= 0b11110000:
            if (byte & 0b11100000) == 0b11100000:
                span = 3
            elif (byte & 0b11111000) == 0b11110000:
                span = 4
            else:
                return False
            if i + span > len(data):
                return False
            if not all(data[i + 1] >> 6 == 0b10 for i in range(1, span)):
                return False
            skip = span - 1
        else:
            return False
    return True
