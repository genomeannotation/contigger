#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys

from src.sequence import read_fasta, split_up_a_sequence

MINIMUM_GAP_LENGTH = 50
infastafile = "in.fasta"
outfastafile = "out.fasta"
outgapfile = "out.gap"

def main():
    # Print picture
    with open("tigger.ascii", 'r') as tigger:
        for line in tigger:
            sys.stderr.write(line)
    
    # Open contig fasta file and gap file for writing
    outfasta = open(outfastafile, 'w')
    outgap = open(outgapfile, 'w')
    # Open input fasta file and read it
    with open(infastafile, 'r') as fasta:
        seqs = read_fasta(fasta)
    if not seqs:
        sys.stderr.write("Found nothing in that fasta file, what are you trying to pull?")
        exit()

    # For each sequence, separate into contigs and gaps
    for seq in seqs:
        contigs, gaps = split_up_a_sequence(seq.bases, MINIMUM_GAP_LENGTH)
        # Write contigs to contig fasta file
        # Write gap lengths to gap file


    # Close input fasta file
    # Close contig fasta file and gap file




###########################################

if __name__ == '__main__':
    main()
