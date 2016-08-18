#!/usr/bin/env python
import __future__ 
import sys
import flupan
import unittest


class test_flupan(unittest.TestCase):
    
    def test1(self):
        '''
        Test of summary
        '''
        pp = flupan.PassageParser()
        p = pp.parse_passage("Mdcksiat2_E8")
        self.assertTrue(p.summary, list)
    
    def test2(self):
        '''
        Test example case
        '''

        pp = flupan.PassageParser()
        p = pp.parse_passage("Mdcksiat2_E3", 3)
        #print(vars(p))
        self.assertTrue(p.original == "Mdcksiat2_E3")
        self.assertTrue(p.plainformat == "MDCKSIAT2_E3")
        self.assertTrue(p.coerced_format == "S2_E3")
        self.assertTrue(p.summary == ['Mdcksiat2_E3', 'MDCKSIAT2_E3', 'S2_E3', 'CANINECELL+EGG', 'SIAT+EGG', 'exactly', '5'])
        self.assertTrue(p.ordered_matches) == ['MDCKSIAT2', 'E3']
        self.assertTrue(p.min_passages == 5)
        self.assertTrue(p.total_passages == 5)
        self.assertTrue(p.nth_passage == 'EGG')
        self.assertTrue(p.general_passages== ["CANINECELL", "EGG"])
        self.assertTrue(p.specific_passages == ["SIAT", "EGG"])
        self.assertTrue(p.passage_series == [[1, 'SIAT'], [2, 'SIAT'], [3, 'EGG'], [4, 'EGG'], [5, 'EGG']]) 
        self.assertTrue(p.summary == ['Mdcksiat2_E3', 'MDCKSIAT2_E3', 'S2_E3', 'CANINECELL+EGG', 'SIAT+EGG', 'exactly', '5'])
             

    def test3(self):
        '''
        Test an empty passage annotation
        '''
        pp = flupan.PassageParser()
        p = pp.parse_passage("")
        self.assertTrue(p.original == "")
        self.assertTrue(p.plainformat == "")
        self.assertTrue(p.coerced_format == "")
        self.assertTrue(p.summary == [])

        self.assertTrue(p.min_passages == None)
        self.assertTrue(p.total_passages == None)
        self.assertTrue(p.nth_passage == None)
        self.assertTrue(p.general_passages== [])
        self.assertTrue(p.specific_passages == [])
        self.assertTrue(p.passage_series == []) 
        self.assertTrue(p.summary == [])
             


    def test4(self):
        '''
        Check a a longer list of passage IDs
        and write an outfile of the summary test
        These passage IDs are already partially formatted
        '''        

        with open("tests/test_passageIDs1.txt", "r") as passageIDs:
            with open("tests/output_test_passageIDs1.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    pp = flupan.PassageParser()
                    input_ID = ID.replace("\n", "") 
                    full_annotation = pp.parse_passage(input_ID)
                    quick_annotation = full_annotation.summary
                    outfile.write(",".join(quick_annotation) + "\n")

    def test5(self):
        '''
        Check another list of passage IDs
        and write an outfile
        '''
        with open("tests/test_passageIDs2.txt", "r") as passageIDs:
            with open("tests/output_test_passageIDs2.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    pp = flupan.PassageParser()
                    quick_annotation = pp.parse_passage(ID).summary
                    outfile.write(str(",".join(quick_annotation)) + "\n")
    def test6(self):
        '''
        Check a completely unformatted list of passage IDs
        and write an outfile of input passage and the coerced format passage
        '''        

        with open("tests/test_unformatted_passage_IDs.txt", "r") as passageIDs:
            with open("tests/output_test_unformatted_passageIDs.txt", "w") as outfile:
                for ID in passageIDs.readlines():
                    pp = flupan.PassageParser()
                    input_ID = ID.replace("\n", "") 
                    full_annotation = pp.parse_passage(input_ID)
                    outstring = full_annotation.original + "\t" + full_annotation.coerced_format+ "\n"
                    outfile.write(outstring)
 
    def test7(self):
        '''
        Test a nonsense passage annotation
        '''
        pp = flupan.PassageParser()
        p = pp.parse_passage("asdk?&~EE8")
        self.assertTrue(p.original == "asdk?&~EE8")
        self.assertTrue(p.plainformat == "ASDK_EE8")
        self.assertTrue(p.coerced_format == "")
        self.assertTrue(p.summary == ['asdk?&~EE8', 'ASDK_EE8', 'None', 'None', 'None', 'None', 'None'])

        self.assertTrue(p.min_passages == None)
        self.assertTrue(p.total_passages == None)
        self.assertTrue(p.nth_passage == None)
        self.assertTrue(p.general_passages== [])
        self.assertTrue(p.specific_passages == [])
        self.assertTrue(p.passage_series == []) 
    

if __name__ == "__main__":
    pass 

