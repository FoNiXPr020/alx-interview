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
    for byte in data:
        if skip > 0:
            skip -= 1
            continue
        if byte >> 5 == 0b111:
            if byte >> 4 == 0b1110:
                skip = 1
            elif byte >> 3 == 0b11110:
                skip = 2
            elif byte >> 2 == 0b111110:
                skip = 3
            else:
                return False
            if len(data) - len(data[data.index(byte):]) < skip:
                return False
            for i in range(1, skip):
                if data[i + data.index(byte)] >> 6 != 0b10:
                    return False
        elif byte >> 7 != 0:
            return False
    return True
