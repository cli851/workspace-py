#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n',
                    '--name',
                    default='World',
                    help='name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
