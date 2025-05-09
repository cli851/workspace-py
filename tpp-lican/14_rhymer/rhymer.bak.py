#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-05-09
Purpose: Rock the Casbah
"""

import argparse
import io
from pydash import flatten


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    parser.add_argument('-w',
                        '--wordlist',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='../inputs/words.txt',
                        help='Wordlist to verify authenticity')

    return parser.parse_args()


# --------------------------------------------------
def stemmer(word):
    word = word.lower()
    vowel_pos = list(map(word.index, filter(lambda c: c in word, 'aeiou')))
    if vowel_pos:
        first_vowel = min(vowel_pos)
        return (word[:first_vowel], word[first_vowel:])
    else:
        return (word, '')


def stemmer3(word):
    """Return leading consonants (if any), and 'stem' of word"""

    word = word.lower()
    pos = list(
        filter(lambda v: v >= 0,
               map(lambda c: word.index(c) if c in word else -1, 'aeiou')))
    if pos:
        first = min(pos)
        return (word[:first], word[first:])
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
    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    dict_words = read_wordlist(args.wordlist)

    def is_dict_word(word):
        return word.lower() in dict_words if dict_words else True

    start, rest = stemmer(args.word)
    if rest:
        print('\n'.join(
            sorted(
                filter(is_dict_word,
                       [p + rest for p in prefixes if p != start]))))
    else:
        print(f'Cannot rhyme "{args.word}"')


def main():
    """Make a jazz noise here"""
    # test_stemmer()
    # test_read_wordlist()
    # solution1()
    solution3()


# --------------------------------------------------
if __name__ == '__main__':
    main()
