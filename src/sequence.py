#!/usr/bin/env python

import re

class Sequence:

    def __init__(self, header="", bases=""):
        self.header = header
        self.bases = bases

    def to_fasta(self):
        result = '>' + self.header + '\n'
        result += self.bases + '\n'
        return result

####################################################

def read_fasta(io_buffer):
    header = ''
    bases = ''
    seqs = {}
    for line in io_buffer:
        if line[0] == '>':
            if len(header) > 0:
                # Save the data
                seqs[header] = Sequence(header, bases)
            header = line[1:].strip().split()[0] # Get the next header
            bases = ''
        else:
            bases += line.strip()
    # Add the last sequence
    seqs[header] = Sequence(header, bases)
    return seqs

def write_fasta(io_buffer, seqs):
    for seq in seqs.values():
        io_buffer.write(">"+seq.header+"\n"+seq.bases+"\n")

def split_up_a_sequence(seq, min_gap_len):
    """Returns a list of N contigs and N-1 gaps which comprise a sequence."""
    # Regular expression which matches 'min_gap_len' or more N's or n's
    pattern = re.compile("[Nn]{"+str(min_gap_len)+",}")
    contigs = re.split(pattern, seq)
    gaps = re.findall(pattern, seq)
    return contigs, gaps

def get_seq_number(header):
    pattern = re.compile("[0-9]+")
    m = re.search(pattern, header)
    if m:
        return m.group()
