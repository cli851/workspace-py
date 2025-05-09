#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-09
Purpose: Rock the Casbah
"""

import argparse
import io
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')
    args = parser.parse_args()
    return args


# --------------------------------------------------
def stemmer(word):
    word = word.lower()
    vowel_pos = list(map(word.index, filter(lambda c: c in word, 'aeiou')))
    if vowel_pos:
        first_vowel = min(vowel_pos)
        return (word[:first_vowel], word[first_vowel:])
    else:
        return (word, '')


def test_stemmer():
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


def read_wordlist(fh):
    return set(
        flatten([line.lower().strip().split() for line in fh] if fh else [])
    )


def test_read_wordlist():
    """test"""

    assert read_wordlist(io.StringIO('foo\nbar\nfoo')) == set(['foo', 'bar'])
    assert read_wordlist(io.StringIO('foo bar\nbar foo\nfoo')) == set(
        ['foo', 'bar'])


def solution1():
    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()
    start, rest = stemmer(args.word)

    if rest:
        print('\n'.join(sorted([prefix + rest for prefix in prefixes if prefix != start])))
    else:
        print(f'Cannot rhyme "{args.word}"')


def solution3():
    return


def main():
    """Make a jazz noise here"""
    # test_stemmer()
    test_read_wordlist()
    # solution1()
    # solution3()


# --------------------------------------------------
if __name__ == '__main__':
    main()
