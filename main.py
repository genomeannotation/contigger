#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys

from src.sequence import read_fasta

def main():
    # Print picture
    with open("tigger.ascii", 'r') as tigger:
        for line in tigger:
            sys.stderr.write(line)
    pass







###########################################

if __name__ == '__main__':
    main()
