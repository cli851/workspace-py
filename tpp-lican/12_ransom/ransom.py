#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-08
Purpose: Rock the Casbah
"""

import argparse
import os.path
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='A named string argument',
                        metavar='str',
                        type=int,
                        default=1)
    args = parser.parse_args()
    random.seed(args.seed)
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def solution1():
    args = get_args()
    ransom = []
    for char in args.text:
        ransom.append(char.upper()) if random.choice([False, True]) else ransom.append(char.lower())
    print(''.join(ransom))


# --------------------------------------------------
def solution2():
    args = get_args()
    ransom = []
    for char in args.text:
        if random.choice([False, True]):
            ransom += char.upper()
        else:
            ransom += char.lower()
    print(''.join(ransom))


def solution3():
    args = get_args()
    ransom = ''
    for char in args.text:
        if random.choice([False, True]):
            ransom += char.upper()
        else:
            ransom += char.lower()
    print(''.join(ransom))


def choose(char):
    return char.upper() if random.choice([0, 1]) else char.lower()


def solution4():
    args = get_args()
    ransom = [choose(char) for char in args.text]
    print(''.join(ransom))


def solution5():
    args = get_args()
    ransom = [char.upper() if random.choice([0, 1]) else char.lower() for char in args.text]
    print(''.join(ransom))


def solution6():
    args = get_args()
    ransom = map(lambda char: char.upper() if random.choice([0, 1]) else char.lower(),
                 args.text)
    print(''.join(ransom))


def solution7():
    args = get_args()
    ransom = map(choose, args.text)
    print(''.join(ransom))


def main():
    """Make a jazz noise here"""
    # solution1()
    # solution2()
    # solution3()
    # solution4()
    # solution5()
    # solution6()
    solution7()


# --------------------------------------------------
if __name__ == '__main__':
    main()
