from __future__ import print_function
import sys
sys.path.append('/home/claire2/flupan/src')
import flupan


#def single_test():
    #infile = "reduced_gisaid_sequences.fasta"
    #test_fasta = SeqIO.parse(infile, "fasta")
    #print type(test_fasta)
   
def test1():
    with open("test_passageIDs1.txt", "r") as passageIDs:
        with open("test_conversion1.txt", "w") as outfile:
            for ID in passageIDs.readlines():
                print(ID) 
                annotation = pp.parse_passage(ID) 
                print(annotation)
                outfile.write(",".join(annotation) + "\n")

def test2():
    with open("test_passageIDs2.txt", "r") as passageIDs:
        with open("test_conversion2.txt", "w") as outfile:
            for ID in passageIDs.readlines():
                print(ID) 
                annotation = pp.parse_passage(ID) 
                print(annotation)
                outfile.write(",".join(annotation) + "\n")




if __name__ == "__main__":

    pp = flupan.PassageParser()
    pp.parse_passage("m 1")
 
    test1()
    test2()

