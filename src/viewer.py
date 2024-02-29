#!/usr/bin/env python
from os import system as s
from os.path import join as j
from os.path import dirname as d
from sys import argv as a

main = lambda : s('python ' + j(d(__file__), 'python-ascii-image', 'ascii.py') + ' ' + ' '.join(a[1:]))

if __name__ == "__main__": main()
