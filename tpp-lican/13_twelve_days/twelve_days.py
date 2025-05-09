#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-09
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number  of days to sing(default: 12)',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile, mode="w", encoding="utf-8"',
                        metavar='string',
                        type=argparse.FileType("wt"),
                        default=sys.stdout)
    args = parser.parse_args()
    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    return args


# --------------------------------------------------
def verse(day):
    """create a verse"""
    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]
    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]
    lines = [
        f'On the {ordinal[day - 1]} day of Christmas,',
        f'My true love gave to me,'
    ]
    lines.extend(reversed(gifts[:day]))
    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()

    return '\n'.join(lines)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    verses = map(verse, range(1, args.num + 1))
    print('\n\n'.join(verses), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
