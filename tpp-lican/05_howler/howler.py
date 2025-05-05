#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-05
Purpose: Rock the Casbah
"""

import argparse
import io
import os
import sys
from os import write


# --------------------------------------------------
def get_args1():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Words to mannered')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def get_args2():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def solution1():
    args = get_args1()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()


def solution2():
    args = get_args2()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()

def main():
    """Make a jazz noise here"""
    # solution1()
    solution2()


# --------------------------------------------------
if __name__ == '__main__':
    main()
