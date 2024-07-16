#!/usr/bin/python3

import sys
import signal

total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}


def print_msg(dict_sc, total_file_size):
    """
    Printing data
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


def handle_interrupt(signal, frame):
    """
    Handle keyboard interrupt (CTRL+C)
    """
    print_msg(dict_sc, total_file_size)
    sys.exit(0)


# Set up signal handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parsed_line = line.split()
        if len(parsed_line) < 7:
            continue

        counter += 1
        # file size is the last element
        total_file_size += int(parsed_line[-1])
        code = parsed_line[-2]  # status code is the second to last element

        if code in dict_sc:
            dict_sc[code] += 1

        if counter == 10:
            print_msg(dict_sc, total_file_size)
            counter = 0

finally:
    print_msg(dict_sc, total_file_size)
