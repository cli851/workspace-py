#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n',
                    '--name',
                    default='World',
                    help='name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
