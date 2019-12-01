"""
Do stuff with YAML files.

"""

import argparse
from argparse import RawTextHelpFormatter
import sys

from .yams import sync_two_files, perform_key_diff


def handle_cmd_options():

    usage = """
    Usage: yam_sort -s file_one file_two    """

    hp = lambda prog: RawTextHelpFormatter(prog, max_help_position=50, width=120)
    parser = argparse.ArgumentParser(description=usage, formatter_class=hp)

    parser.add_argument('-s', '--sync', nargs=2, metavar=('first', 'second'),
                        help='sort the second of two YAML files by keys in first')
    parser.add_argument('-k', '--keys', nargs=2, metavar=('first', 'second'),
                        help='diff two YAML files by keys only')
    parser.add_argument('-o', '--overwrite', action="store_true",
                        help='overwrite second file with re-sorted data')
    cmd_args = parser.parse_args()

    # You would think an empty argument list would *default* to printing help, but no...
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return cmd_args


def main():

    args = handle_cmd_options()
    # print(f"args = {args}\n")
    if args.sync:
        sync_two_files(args.sync, args.overwrite)
    elif args.keys:
        perform_key_diff(args.keys)


if __name__ == '__main__':
    main()
