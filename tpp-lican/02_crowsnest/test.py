#!/usr/bin/env python
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

file = 'crowsnest.py'
prg = 'python crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""
    assert (os.path.exists(file))


# --------------------------------------------------
def test_usage():
    """usage"""
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""
    for word in consonant_words:
        rv, out = getstatusoutput(f'{prg} {word}')
        assert rv == 0
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""
    for word in consonant_words:
        rv, out = getstatusoutput(f'{prg} {word.title()}')
        assert rv == 0
        assert out.strip() == template.format('a', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""
    for word in vowel_words:
        rv, out = getstatusoutput(f'{prg} {word}')
        assert rv == 0
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""
    for word in vowel_words:
        rv, out = getstatusoutput(f'{prg} {word.title()}')
        assert rv == 0
        assert out.strip() == template.format('an', word.title())
