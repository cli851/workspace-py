#!/usr/bin/env python
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

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        bringing = ', '.join(items[:-1]) + ', and ' + items[-1]
    print(f'{temp} {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
