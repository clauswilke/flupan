#!/usr/bin/env python3
from __future__ import print_function
from unittest import TestCase
import sys
sys.path.append('/home/claire2/flupan/src')
import flupan


class test_flupan(TestCase):
  
    def __init__(self):
        pass
 
    def test1(self):
        test_annot = pp.parse_passage("Mdcksiat2_E8")
        print(test_annot)    
        self.assertTrue(isinstance(test_annot, list))

    def test2(self):
        test_annot = pp.parse_passage("Mdcksiat2_E8")
        print(test_annot)    
        self.assertTrue(test_annot == ['Mdcksiat2_E8', 'MDCKSIAT2_E8', 'MDCKSIAT2_E8', 'CANINECELL+EGG', 'SIAT+EGG', 'exactly', '10'])
      

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

