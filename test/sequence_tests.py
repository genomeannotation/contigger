#!/usr/bin/env python

import unittest
import io
from src.sequence import Sequence, read_fasta, split_up_a_sequence, get_seq_number

class TestSequence(unittest.TestCase):

    def test_to_fasta(self):
        sequence = Sequence("foo_seq", "GATTACA")
        fasta = sequence.to_fasta()
        expected = ">foo_seq\nGATTACA\n"
        self.assertEquals(expected, fasta)

    def test_read_fasta_with_line_breaks(self):
        line_breaks = io.StringIO('>seq_1\nGATTACAGATTACAGATTACAGATTACA\nGATTACAGATTACAGATTACAGATTACA\n' +
                                 '>seq_2\nNNNNNNNNGATTACAGATTACAGATTAC\nANNNNNNNNNNN')

        seqs = read_fasta(line_breaks)
        self.assertEquals(2, len(seqs))
        self.assertEquals('NNNNNNNNGATTACAGATTACAGATTACANNNNNNNNNNN', seqs["seq_2"].bases)

    def test_read_fasta_without_line_breaks(self):
        no_line_breaks = io.StringIO('>seq_1\nGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACA\n' +
                                    '>seq_2\nNNNNNNNNGATTACAGATTACAGATTACANNNNNNNNNNN')
        seqs = read_fasta(no_line_breaks)
        self.assertEquals(2, len(seqs))
        self.assertEquals('seq_1', seqs["seq_1"].header)
        self.assertEquals('GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACA', seqs["seq_1"].bases)
        self.assertEquals('seq_2', seqs["seq_2"].header)
        self.assertEquals('NNNNNNNNGATTACAGATTACAGATTACANNNNNNNNNNN', seqs["seq_2"].bases)
        
    def test_split_up_a_sequence(self):
        testseq = "GATTACAnnNNACTACTnnnNNNGANAGA"
        expected_contigs = ["GATTACA", "ACTACT", "GANAGA"]
        expected_gaps = ["nnNN", "nnnNNN"]
        contigs, gaps = split_up_a_sequence(testseq, 4)
        self.assertEqual(contigs, expected_contigs)
        self.assertEqual(gaps, expected_gaps)

    def test_get_seq_number(self):
        header = "Scaffold00073"
        expected = "00073"
        actual = get_seq_number(header)
        self.assertEqual(expected, actual)

##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSequence))
    return suite

if __name__ == '__main__':
    unittest.main()
