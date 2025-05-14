#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit','-l',type=int, help='the number of lines to read')

args = parser.parse_args()
print(args)