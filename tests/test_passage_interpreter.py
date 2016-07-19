#!/usr/bin/env python
import __future__ 
import unittest
import sys
sys.path.append('/home/claire2/flupan/src')
from flupan import passage_interpreter


class test_flupan(unittest.TestCase):
  
 
    def test1(self):
        #mods = [m.__name__ for m in sys.modules.values() if m]
        #print(mods)
        pp = passage_interpreter.PassageParser()
        p = pp.parse_passage("Mdcksiat2_E8")
        print(p)
        print(p.summary)    
        self.assertTrue(p.summary, list)

    def test2(self):

        pp = passage_interpreter.PassageParser()
        p = pp.parse_passage("Mdcksiat2_E3", 3)
        print(vars(p))
        self.assertTrue(p.original == "Mdcksiat2_E3")
        self.assertTrue(p.plainformat == "MDCKSIAT2_E3")
        self.assertTrue(p.coercedformat == "SIAT2_E3")
        self.assertTrue(p.summary == ['Mdcksiat2_E3', 'MDCKSIAT2_E3', 'SIAT2_E3', 'CANINECELL+EGG', 'SIAT+EGG', 'exactly', '5'])

        self.assertTrue(p.min_passages == 5)
        self.assertTrue(p.total_passages == 5)
        self.assertTrue(p.nth_passage == 'EGG')
        self.assertTrue(p.general_passages== ["CANINECELL", "EGG"])
        self.assertTrue(p.specific_passages == ["SIAT", "EGG"])
        self.assertTrue(p.passage_series == [[1, 'SIAT'], [2, 'SIAT'], [3, 'EGG'], [4, 'EGG'], [5, 'EGG']]) 
        self.assertTrue(p.summary == ['Mdcksiat2_E3', 'MDCKSIAT2_E3', 'SIAT2_E3', 'CANINECELL+EGG', 'SIAT+EGG', 'exactly', '5'])
             


    '''
    def test3(self):

        pp = flupan.PassageParser()
        with open("tests/test_passageIDs1.txt", "r") as passageIDs:
            with open("tests/output_test_passageIDs1.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    print(ID) 
                    annotation = pp.parse_passage(ID) 
                    print(annotation)
                    outfile.write(",".join(annotation) + "\n")

    def test4(self):
        pp = flupan.PassageParser()
        with open("tests/test_passageIDs2.txt", "r") as passageIDs:
            with open("tests/output_test_passageIDs2.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    print(ID) 
                    annotation = pp.parse_passage(ID) 
                    print(annotation)
                    outfile.write(",".join(annotation) + "\n")

    '''


if __name__ == "__main__":

    pp = flupan.PassageParser()
    pp.parse_passage("m 1")

    tf = test_flupan() 
    #tf.test1()
    #tf.test2()
    #tf.test3()
    #tf.test4()

