#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-08
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles (default: 10)',
                        metavar='number',
                        type=int,
                        default=10)
    args = parser.parse_args()
    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args


def verse(bottle):
    next_bottle = bottle
    next_bottle = next_bottle - 1
    s1 = '' if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    num_text = 'No more' if next_bottle == 0 else next_bottle
    return '\n'.join([
        f'{bottle} bottle{s1} of beer on the wall,',
        f'{bottle} bottle{s1} of beer,',
        f'Take one down, pass it around,',
        f'{num_text} bottle{s2} of beer on the wall!'
    ])


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
