"""
Add colors to strings, using ANSI escape-sequences

https://www.geeksforgeeks.org/print-colors-python-terminal/

"""

RED_ANSI = "\033[91m{some_string}\033[00m"
YELLOW_ANSI = "\033[93m{some_string}\033[00m"
BLUE_ANSI = "\033[94m{some_string}\033[00m"


def to_red(some_string):

    return RED_ANSI.format(some_string=some_string)


def to_yellow(some_string):

    return YELLOW_ANSI.format(some_string=some_string)


def to_blue(some_string):

    return BLUE_ANSI.format(some_string=some_string)
