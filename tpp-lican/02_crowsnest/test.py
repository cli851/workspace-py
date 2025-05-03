#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
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
    assert(os.path.exists(prg))

# --------------------------------------------------
def test_usage():
    """usage"""



# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""



# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""



# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""
