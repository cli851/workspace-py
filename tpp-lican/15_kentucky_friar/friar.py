#!/usr/bin/env py
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-09
Purpose: Rock the Casbah
"""

import argparse
import os.path
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='A positional argument')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def fry(word):
    if word.lower() == 'you':
        return word[0] + "'all"

    if word.endswith('ing'):
        if any(map(lambda c: c.lower() in 'aeiouy', word[:-3])):
            return word[:-1] + "'"

    return word


# --------------------------------------------------
def test_fry():
    """Test fry"""

    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('your') == 'your'
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    test_fry()
    for line in args.text.splitlines():
        print(''.join(map(fry, re.split(r'(\W+)', line.rstrip()))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
