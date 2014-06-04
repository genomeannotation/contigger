#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys

from src.sequence import Sequence, read_fasta, split_up_a_sequence, get_seq_number

MINIMUM_GAP_LENGTH = 50
infastafile = "in.fasta"
outfastafile = "out.fasta"
outgapfile = "out.gap"

def decontig():
    # Open scaffold fasta file for writing
    #outfasta = open(infastafile, 'w')
    # Open input fasta file and read it
    with open("decontig/contig.fasta", "r") as fasta:
    #with open("example/output.fasta", "r") as fasta:
        seqs = read_fasta(fasta)
    # Open input gap file and read it
    with open("decontig/contig.gap", "r") as gap:
    #with open("example/output.gap", "r") as gap:
        gaps = {}
        for line in gap:
            if not line:
                continue
            columns = line.strip().split('\t')
            if len(columns) < 2:
                continue
            gaps[columns[0]] = int(columns[1])
    if not seqs:
        sys.stderr.write("Found nothing in that fasta file, what are you trying to pull?")
        exit()

    # Separate sequences by end 
    contigs = {}
    for header, seq in seqs.items():
        split_header = header.split(".")
        number = split_header[-1]
        merged_header = ".".join(split_header[:-1])
        if merged_header in contigs:
            contigs[merged_header].append(header)
        else:
            contigs[merged_header] = [header]

    # Put scaffolds together
    with open("out.fasta", "w") as outfasta:
        for header, contig_headers in contigs.items():
            header_num = header[6:] # Strip beginning contig
            scaffold = Sequence("Scaffold"+header_num, "")
            for contig_header in sorted(contig_headers):
                scaffold.bases += seqs[contig_header].bases
                if contig_header in gaps:
                    scaffold.bases += ("N"*gaps[contig_header])
            outfasta.write(">"+scaffold.header+"\n")
            outfasta.write(scaffold.bases+"\n")
        
    # Close contig fasta file and gap file
    outfasta.close()

###############################################################################

def main():
    # Print picture
    with open("res/tigger.ascii", 'r') as tigger:
        for line in tigger:
            sys.stderr.write(line)

    decontig()
    exit()
    
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
            outfasta.write(">Contig" + seq_number + "." + str(i+1) + "\n")
            outfasta.write(contig + "\n")
        # Write gap lengths to gap file
        for i, gap in enumerate(gaps):
            outgap.write("Contig" + seq_number + "." + str(i+1) + "\t" + str(len(gap)) + "\n")

    # Close contig fasta file and gap file
    outfasta.close()
    outgap.close()



###########################################

if __name__ == '__main__':
    main()
