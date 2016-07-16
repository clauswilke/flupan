from __future__ import print_function
import re



class PassageParser:
    def __init__(self): 
        pass
  
    def spec_char_strip(self, ID):
        ''' 
        Replaces special characters with underscores
        Compresses redundant series of underscores with a single underscore
        Replaces uninformative words 
        ''' 

        record_strip = re.sub('[^A-Z0-9\|]', '_', ID)
        record_strip = re.sub('PASSAGE_DETAILS_|_AND_|ST_PASSAGE|ND_PASSAGE|PASSAGING', '', record_strip)
        record_strip = record_strip.replace("__", "_")
        if record_strip[0] == "_":
            record_strip = record_strip[1:]
        if record_strip[-1] == "_":
            record_strip = record_strip[:-1]

        return record_strip

    def format_ID(self, ID):
        '''
        Gets passage annotation into a consistent format for lookup
        '''

        assert type(ID)==str
        uppercase_ID = ID.upper()
        formatted_ID = self.spec_char_strip(uppercase_ID)
        

        return formatted_ID



    def match_known_passage(self, formatted_ID):
        with open("../tables/passage_lookup.txt", "r") as lookuptable_txt:
           lookuptable = eval(lookuptable_txt.read())

           #print(lookuptable)
           annotation = lookuptable[formatted_ID]
           return annotation
         


    def regular_exp_identification(self, formatted_ID):
        print("meh")

    def parse_passage(self, ID):
        '''
        control function 
        '''
        formatted_ID = self.format_ID(ID)
        annotation =  self.match_known_passage(formatted_ID)      
        output = [ID, formatted_ID, annotation[0], annotation[1], annotation[2]] 
        return output







