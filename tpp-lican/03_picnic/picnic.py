#!/usr/bin/env python3
"""
Author : runner <runner@e15a7fd738b2>
Date   : 2025-05-03
Purpose: Rock the Casbah
"""

temp = 'You are bringing'

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args().item
    count = len(args)
    if count < 2:
        str = args[0]
    elif count == 2:
        str = ' and '.join(args)
    else:
        str = ', '.join(args[:len(args) - 1]) + ', and ' + args[len(args) - 1]
    print(f'{temp} {str}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
