#!/usr/bin/env python
import __future__ 
from flupan import passage_interpreter
import unittest


class test_flupan(unittest.TestCase):
    def test1(self):
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
             

    def test3(self):
        pp = passage_interpreter.PassageParser()
        p = pp.parse_passage("")
        print(vars(p))
        print p.nth_passage
        self.assertTrue(p.original == "")
        self.assertTrue(p.plainformat == "")
        self.assertTrue(p.coercedformat == "")
        self.assertTrue(p.summary == [])

        self.assertTrue(p.min_passages == None)
        self.assertTrue(p.total_passages == None)
        self.assertTrue(p.nth_passage == None)
        self.assertTrue(p.general_passages== [])
        self.assertTrue(p.specific_passages == [])
        self.assertTrue(p.passage_series == []) 
        self.assertTrue(p.summary == [])
             


       

    def test4(self):
        pp = passage_interpreter.PassageParser()
        with open("tests/test_passageIDs1.txt", "r") as passageIDs:
            with open("tests/output_test_passageIDs1.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    print("asdf")
                    print(ID)
                    input_ID = ID.replace("\n", "") 
                    quick_annotation = pp.parse_passage(input_ID).summary 
                    print(quick_annotation)
                    outfile.write(",".join(quick_annotation) + "\n")

    def test5(self):
        pp = passage_interpreter.PassageParser()
        with open("tests/test_passageIDs2.txt", "r") as passageIDs:
            with open("tests/output_test_passageIDs2.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    print(ID) 
                    quick_annotation = pp.parse_passage(ID).passage_series
                    print(quick_annotation)
                    #outfile.write(str(",".join(quick_annotation)) + "\n")
     

    

if __name__ == "__main__":

    pp = flupan.PassageParser()
    pp.parse_passage("m 1")

    tf = test_flupan() 
    #tf.test1()
    #tf.test2()
    #tf.test3()
    #tf.test4()

