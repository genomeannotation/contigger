#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys

from src.sequence import read_fasta, split_up_a_sequence, get_seq_number

MINIMUM_GAP_LENGTH = 50
infastafile = "in.fasta"
outfastafile = "out.fasta"
outgapfile = "out.gap"

def main():
    # Print picture
    with open("res/tigger.ascii", 'r') as tigger:
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
    for seq in seqs.values():
        contigs, gaps = split_up_a_sequence(seq.bases, MINIMUM_GAP_LENGTH)
        seq_number = get_seq_number(seq.header)
        # Write contigs to contig fasta file
        for i, contig in enumerate(contigs):
            outfasta.write(">contig" + seq_number + "." + str(i+1) + "\n")
            outfasta.write(contig + "\n")
        # Write gap lengths to gap file
        for i, gap in enumerate(gaps):
            outgap.write("contig" + seq_number + "." + str(i+1) + "\t" + str(len(gap)) + "\n")

    # Close contig fasta file and gap file
    outfasta.close()
    outgap.close()



###########################################

if __name__ == '__main__':
    main()
