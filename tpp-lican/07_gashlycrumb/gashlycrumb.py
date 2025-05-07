#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-07
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def solution1():
    args = get_args()
    lookup = {}
    for line in args.file:
        lookup[line[0].upper()] = line.rstrip()
    for letter in args.letter:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


def solution2():
    args = get_args()
    lookup = {line[0].upper(): line.rstrip() for line in args.file}
    for letter in args.letter:
        print(lookup.get(letter.upper(), f'I do not know "{letter}".'))


def main():
    """Make a jazz noise here"""
    # solution1()
    solution2()


# --------------------------------------------------
if __name__ == '__main__':
    main()
