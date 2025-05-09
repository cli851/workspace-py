#!/usr/bin/env python
"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput

file = 'hello.py'
prg = 'python hello.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(file)


# --------------------------------------------------
# def test_runnable():
#     """Runs using python3"""
#     out = getoutput(f'python {prg}')
#     assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default"""
    out = getoutput(prg)
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_usage():
    """usage"""
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

# --------------------------------------------------
def test_input():
    """test for input"""
