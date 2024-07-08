#!/usr/bin/python3
""" Minimum Operations Module."""


def minOperations(n):
    """
    minOperations - calculates the fewest number of operations
    """
    str = 'H'
    operations = 0
    factor = 2
    if n < 0:
        return 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

    return operations
