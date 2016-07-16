from __future__ import print_function
import sys
sys.path.append('/home/claire2/flupan/src')
import flupan


#def single_test():
    #infile = "reduced_gisaid_sequences.fasta"
    #test_fasta = SeqIO.parse(infile, "fasta")
    #print type(test_fasta)
   
def multipleIDs_test():
    with open("test_passageIDs.txt", "r") as passageIDs:
        for ID in passageIDs.readlines():
          print(ID) 
          annotation = pp.parse_passage(ID) 
          print(annotation)

if __name__ == "__main__":

    pp = flupan.PassageParser()
    pp.parse_passage("m 1")
 
    #single_test()
    multipleIDs_test()


