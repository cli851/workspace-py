#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-07
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
                        help='Input text of file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel(s) allowed',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def solution1():
    args = get_args()
    text = args.text
    vowel = args.vowel
    new_text = []
    for char in text:
        if char in 'aeiou':
            new_text.append(vowel)
        elif char in 'AEIOU':
            new_text.append(vowel.upper())
        else:
            new_text.append(char)
    print(''.join(new_text))


def solution2():
    args = get_args()
    text = args.text
    vowel = args.vowel
    for c in 'aeiou':
        text = text.replace(c, vowel).replace(c.upper(), vowel.upper())
    print(text)


def solution3():
    args = get_args()
    text = args.text
    vowel = args.vowel
    trans = str.maketrans('aeiouAEIOU', vowel * 5 + vowel.upper() * 5)
    text = text.translate(trans)
    print(text)


def solution4():
    args = get_args()
    vowel = args.vowel

    def new_char(c):
        return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c

    text = ''.join(new_char(c) for c in args.text)
    print(text)


def solution5():
    args = get_args()
    vowel = args.vowel
    text = map(
        lambda c: vowel if c in 'aeiou' else vowel.upper()
        if c in 'AEIOU' else c,
        args.text)
    print(''.join(text))


def solution7():
    args = get_args()
    vowel = args.vowel

    def new_char(c):
        return vowel if c in 'aeiou' else vowel.upper() \
            if c in 'AEIOU' else c

    text = map(new_char, args.text)
    print(''.join(text))


def solution8():
    args = get_args()
    vowel = args.vowel
    text = args.text
    text = re.sub('[aeiou]', vowel, text)
    text = re.sub('[AEIOU]', vowel.upper(), text)
    print(text)


def main():
    """Make a jazz noise here"""
    # solution1()
    # solution2()
    # solution3()
    # solution4()
    # solution5()
    # solution7()
    solution8()


# --------------------------------------------------
if __name__ == '__main__':
    main()
