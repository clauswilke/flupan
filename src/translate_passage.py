#!/usr/bin/env python
from __future__ import print_function
import sys
sys.path.append('/home/claire2/flupan/src')

import flupan
import argparse


def parse_file(infile):
    with open(infile, "r") as passageIDs:
            for ID in passageIDs.readlines():
                 annotation = pp.parse_passage(ID) 
                 #print(annotation)
                 return annotation
def parse_passage(passage):
    annotation = pp.parse_passage(passage) 
    return annotation 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A tool to parse influenza passaging annotations')
    parser.add_argument('-f', '--infile', action='store', help = 'A files of passage IDs, ex M1 S4, one per line', required=False)
    parser.add_argument('-p', '--passage',  action='store', help = 'A single passage ID to be parsed, ex. E4', required=False)
    parser.add_argument('-o', '--outfile', action='store', help = 'An outfile to store output', required=False, default='interpreted_passage.txt')

    args = parser.parse_args()
    pp = flupan.PassageParser()

    if not args.infile and not args.passage:
        sys.exit("No arguments, either provide a file (-f) or single passage identifier (-p)")
        s
    if args.infile and args.passage:
        sys.exit("please provide either a text file of passages or a single passage ID, but not both")
       
 

    if args.infile:
        annotation = parse_file(args.infile)

    if args.passage:
        annotation = parse_passage(args.passage)
        print(",".join(annotation))

    if args.outfile:
        with open(args.outfile, "w") as outf:
             outf.write(",".join(annotation) + "\n")








'''
class test_flupan():
  
    def __init__(self):
        pass
 
    def test1(self):
        test_annot = pp.parse_passage("Mdcksiat2_E8")
        print(test_annot)    
        assert isinstance(test_annot, list)

    def test2(self):
        test_annot = pp.parse_passage("Mdcksiat2_E8")
        print(test_annot)    
        assert test_annot == ['Mdcksiat2_E8', 'MDCKSIAT2_E8', 'SIAT2_E8', 'CANINECELL+EGG', 'SIAT+EGG', 'exactly', '10']
      

    def test3(self):
        with open("test_passageIDs1.txt", "r") as passageIDs:
            with open("output_test_passageIDs1.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    print(ID) 
                    annotation = pp.parse_passage(ID) 
                    print(annotation)
                    outfile.write(",".join(annotation) + "\n")

    def test4(self):
        with open("test_passageIDs2.txt", "r") as passageIDs:
            with open("output_test_passageIDs2.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    print(ID) 
                    annotation = pp.parse_passage(ID) 
                    print(annotation)
                    outfile.write(",".join(annotation) + "\n")




if __name__ == "__main__":

    pp = flupan.PassageParser()
    pp.parse_passage("m 1")

    tf = test_flupan() 
    tf.test1()
    tf.test2()
    tf.test3()
    tf.test4()
'''
