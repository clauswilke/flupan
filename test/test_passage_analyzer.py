import sys
sys.path.append('/home/claire2/flupan/src')
import PassageAnalyzer


def test():
    from Bio import SeqIO
    infile = "reduced_gisaid_sequences.fasta"
    test_fasta = SeqIO.parse(infile, "fasta")
    print type(test_fasta)
    pa = PassageAnalyzer.PassageParser()
    pa.format_fasta(test_fasta)
    

if __name__ == "__main__":
    test()



