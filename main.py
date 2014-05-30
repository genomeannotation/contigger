#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys

from src.sequence import read_fasta

def main():
    # Print picture
    with open("tigger.ascii", 'r') as tigger:
        for line in tigger:
            sys.stderr.write(line)

    # Open contig fasta file and gap file for writing
    # Open input fasta file for reading

    # Read fasta

    # For each sequence, separate into contigs
        # Write contigs to contig fasta file
        # Write gap lengths to gap file


    # Close input fasta file
    # Close contig fasta file and gap file




###########################################

if __name__ == '__main__':
    main()
