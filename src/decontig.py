#!/usr/bin/env python

from src.sequence import Sequence, read_fasta, write_fasta

def read_gaps(io_buffer):
    gaps = {}
    for line in io_buffer:
        if not line:
            continue
        columns = line.strip().split('\t')
        if len(columns) < 2:
            continue
        gaps[columns[0]] = int(columns[1])
    return gaps

def sort_contigs(seqs):
    contigs = {}
    for header, seq in seqs.items():
        split_header = header.split(".")
        number = split_header[-1]
        merged_header = ".".join(split_header[:-1])
        if merged_header in contigs:
            contigs[merged_header].append(header)
        else:
            contigs[merged_header] = [header]
    return contigs

def build_scaffolds(seqs, gaps, contigs):
    scaffolds = {}
    for header, contig_headers in contigs.items():
        header_num = header[6:] # Strip beginning contig
        scaffold = Sequence("Scaffold"+header_num, "")
        for contig_header in sorted(contig_headers):
            scaffold.bases += seqs[contig_header].bases
            if contig_header in gaps:
                scaffold.bases += ("N"*gaps[contig_header])
        scaffolds[scaffold.header] = scaffold
    return scaffolds
