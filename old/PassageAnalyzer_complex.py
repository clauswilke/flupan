from Bio import SeqIO
import re


#Columns for passaging annotations

#passaged? transfer? single serial gen_cell cell_type rh_cell rh_cell_type species total_passages 


'''
Lookup_table
ID type round total_rounds transfer passaged?

rhMK2_SIAT1 monkey 1 3 True True
rhmk2_siat1 monkey 2 3 True True
rhmk2_siat1 SIAT1 3 3 True True
unpassaged unpassaged 0 0 False False
'''

class PassageParser:
    def __init__(self):
   
        pass
  
    def format_fasta(self, fasta):
       '''
       Takes fasta IDs, and makes dictionary of their formatted versions
       '''
       print "whatev"


    def record_strip(self):
        record_strip = re.sub('[^A-Z0-9\|]', '_', id)
        return record_strip

    def record_to_upper(record_id):
         return record_id.upper()





    def select_passages(self, fasta, desired_passage, max_desired_total_rounds=None, exclude_transfer=False, exclude_multi_condition=True):
        '''
        Takes seqrecords with passage annotations
        Returns seqrecords with desired parameters
        desired_passage : The specific passage condition desired
        '''
        assert type(FASTA)==seqrecord
        assert desired_passage in ["siat", "nonsiat", "cell", "unpassaged", "egg", "monkey", "rhmk", "vero", "passaged", "unclassified"]
        assert type(transfer)==bool
        assert type(exclude=multi_condition)==bool
        if max_rounds != NA:
            assert type(max_rounds)==integer


    def exclude_passages(self, FASTA, unwanted_passage, exclude_total_rounds, exclude_transfer=False):
        assert type(FASTA)==seqrecord
        assert unwanted_passage in ["siat", "nonsiat", "cell", "unpassaged", "egg", "monkey", "rhmk", "vero", "passaged", "unclassified"]
        assert type(transfer)==bool
        if unwanted_rounds != NA:
            assert type(unwanted_rounds)==integer



    


      


    def Specialized_parsing():
        '''
        helper_function using regular expression to 
        '''
        print "test"




    #def get_passaging_distribution(rounds, by=species):
     #  '''
    #   returns a dictionary of counts of each passage type 
    #   '''
     #  print "testing"







