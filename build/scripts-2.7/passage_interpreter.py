import __future__ 
import re
import sys
import logging



class PassageParser:
    def __init__(self, nth_passage=None): 

        #The raw input ID
        self.original = ""

        #Input ID, capitalized, spec characters removed
        self.plainformat = ""
 
        #Try to get plainformat ID into consistent format
        self.coercedformat = ""
 
        #Convenience list of annotations for a passage
        self.summary = []    

        #The minimum number of passage round that occurred. Could be higher
        #Ex. SIAT3_EGG had to have been passaged at least 4 times
        self.min_passages = None

        #If possible to determine, the exact total annotated rounds of passaging
        self.total_passages = None

        #If requested, get the identity of the nth passage
        self.nth_passage = None

        #The species/general type of the passages
        #Ex. CANINECELL, MONKEYCELL
        self.general_passages= []

        #More specific type of passage, if known
        #["MDCK", "RHMK"], etc.
        self.specific_passages = []

        #The order of specific passages
        #Ex. [[1, 'SIAT'], [2, 'SIAT'], [3, 'EGG'], [4, 'EGG']]
        self.passage_series = []
      
    def spec_char_strip(self, ID):
        ''' 
        Replaces special characters with underscores
        Compresses redundant series of underscores with a single underscore
        Replaces uninformative words 
        ''' 
        # Because- most always appears between a passage type and # of rounds    
        # Replace with no space 
        # Ex. EGG-4 -> EGG4
        record_strip = ID.replace("-", "")

        #Replace things that aren't alphanumeric with an underscore
        record_strip = re.sub('[^A-Z0-9\|]', '_', record_strip)

        #Remove not useful words
        record_strip = re.sub('PASSAGE_DETAILS_|_AND_|ST_PASSAGE|ND_PASSAGE|PASSAGING|_PASSAGE|_PASSAGES|_PASSAGE_|_PASSAGES_|_CELLS', '', record_strip)
        #Get rid
        while "__" in record_strip:
            record_strip = record_strip.replace("__", "_")

        #01 just means 1 - Maybe put back in
        #record_strip = re.sub('01', '1', record_strip)
        if len(record_strip) > 0:
            #Get rid of leading and trailing underscores
            if record_strip[0] == "_":
                record_strip = record_strip[1:]
            if record_strip[-1] == "_":
                record_strip = record_strip[:-1]

        return record_strip

    def format_ID(self, ID):
        '''
        Gets passage annotation into a consistent format for lookup
        Asserts that ID is a string
        '''

        assert type(ID)==str
        uppercase_ID = ID.upper()
        formatted_ID = self.spec_char_strip(uppercase_ID)
        

        return formatted_ID

    def reformat_annotation(self, annotation_list):
        '''
        This function coerces the most common passage IDs into a more standard format
        Removes underscores which occur inside a single annotation
        Once a set of passaging annotation standards are released, this 
        will be the function to make old annotations consistent with them
        '''
 
        reformatted_annotation_list = []
        with open("tables/coerce_format.txt", "r") as replacements_file:
             
            replacements = replacements_file.readlines()
            for annot in annotation_list:
                 for replacement in replacements:
                    rep_list = replacement.split(" ")
                    annot = annot.replace(rep_list[0], rep_list[1].rstrip("\n"))                    
                    print("reformatting")
            
                 reformatted_annotation_list.append(annot) 
                 
            print(annot, reformatted_annotation_list)
        reformatted_annotation = "_".join(reformatted_annotation_list)
        return reformatted_annotation



    def make_annotation(self, annotation_list, lookuptable):
       '''
       This function takes a list of passage IDs found in 
       the full passage ID, and then consolidates their annotations 
       It needs the dictionary from lookup_table.txt as a reference to 
       lookup annotations
       '''
       concat_general_passage = ""
       concat_specific_passage = ""
       cumulative_num_passages= ""
       num_condition = "exactly"
       assert type(annotation_list)== list
       assert type(lookuptable) == dict
       for passage in annotation_list:
            annot = lookuptable[passage]
            print(passage, annot)
            
            tmp_passage = passage.replace("_", "")
            #Consolidate the general passage summary
 
            if annot[0] == None:
                concat_general_passage = ""

            #If it's the first passage in the list
            elif concat_general_passage == "":
                concat_general_passage = annot[0]

            #If the passage has already occured, don't change anything
            elif annot[0] in concat_general_passage:
                concat_general_passage = concat_general_passage

            #If the ID is just a number, assume it was in the passage condition of
            #the previous ID. 
            #Ex. EGG5_1 = EGG6 essentially. 
            elif tmp_passage in ["1","2","3","4","5","6","7","9","10","11","12"]:
                concat_general_passage = concat_general_passage
            else:
                concat_general_passage = "+".join([concat_general_passage, annot[0]])

            #Consolidate the specific passage summary
            #Same idea as above 

            if annot[1] == None:
                concat_specific_passage = ""
 
            elif concat_specific_passage == "":
                concat_specific_passage = annot[1]
            elif annot[1] in concat_specific_passage:
                concat_specific_passage = concat_specific_passage
            elif tmp_passage in ["1","2","3","4","5","6","7","9","10","11","12"]:
                concat_specific_passage = concat_specific_passage
            else:
                concat_specific_passage = "+".join([concat_specific_passage, annot[1]])
       
            #Add up numbers of passages
            #Some annotations don't have numbers, so can't be added
            if cumulative_num_passages == "":
                try:
                   cumulative_num_passages = str(eval(annot[2]))

                except:
                   #indeterminate passages happen at least once
                   cumulative_num_passages = "1"
                   cumulative_num_condition = "atleast"                
            else:
                try:
                   cumulative_num_passages = str(eval(cumulative_num_passages) + eval(annot[2])) 

                except:
                   #if any passage has an indeterminate number of rounds,
                   #it happened at least once
                   cumulative_num_condition = "atleast"                
                   cumulative_num_passages = str(eval(cumulative_num_passages) + 1) 
 
       self.general_passages = concat_general_passage.split("+")
       assert type(self.general_passages) == list

       self.specific_passages = concat_specific_passage.split("+")
       assert type(self.specific_passages) == list
       reformatted_annotation = self.reformat_annotation(annotation_list)
       assert type(reformatted_annotation) == str
       self.coercedformat = reformatted_annotation
       self.min_passages = eval(cumulative_num_passages)
       #If any of  passage doesn't have a number, can't get exact total 
       if  num_condition == "atleast":
            self.total_passages = None
       #Can only get total number of rounds if there's an exact count
       elif num_condition == "exactly":
            self.total_passages = eval(cumulative_num_passages)

       annot =  [reformatted_annotation, concat_general_passage, concat_specific_passage, num_condition, cumulative_num_passages]
       print(annot)
       return(annot)  




    def get_nth_passage(self, n):
        '''
        Get the type of the nth round of passaging
        '''
        #If an n is provided by user...
        if n != None:
            #If a passage series could be determined by get_series()...
            if self.passage_series is not []:
               for entry in self.passage_series:  
                    #Get the nth passage
                    if entry[0] == n:
                        self.nth_passage = entry[1]


    def get_series(self, annotation_list, lookuptable):
       '''

       Get a series of passage rounds, 
       EGG2_M1 => [1, EGG], [2,EGG], [3,MDCK], etc.
       Setup for getting the nth passage function
       '''
       prev_annot = ""
       prev_i = 0
       for passage in annotation_list:
            annot = lookuptable[passage]
            #If any annot[2] (num_passage) is not a number,
            #will cause exception and just return nothing
            try: 
                #num passages
                print(annot[2]) 
                #for round in number of passages that occur
                for i in range(1, eval(annot[2])+1):

                   #If there's a passage type, use it
                   if annot[1] != None:
                        self.passage_series.append([ i + prev_i, annot[1]])
                        prev_annot = annot[1]

                   #Else, if the previous annotation's passage type isn't empty, 
                   #use previous annotation
                   elif prev_annot != "":
                        self.passage_series.append([i + prev_i, prev_annot])
                #Keep track of cumulative number of rounds    
                prev_i = eval(annot[2])
            except:
                return
                                   




    def match_known_passage(self, formatted_ID):
        '''
        This function looks for known passage annotations within 
        ihe formatted input passage identifiers
        If the full passage can't be accounted for,
        Nones are returned
        '''
 
        #Start logging
        log = open("passage_interpreter.out", "a")
        sys.stdout = log

        

        with open("tables/passage_lookup.txt", "r") as lookuptable_txt:

           #Read the {passage:annotation} file as a literal dictionary
           lookuptable = eval(lookuptable_txt.read())

           tmp_ID = formatted_ID
           longest_match = ""
           matches = []
           print("Input ID", formatted_ID)
           #Searches for up to different 5 passage rounds
           for i in [1,2,3,4, 5]:
               #find the longest known passage in input passage ID
               for key in lookuptable.keys():
                  if key in tmp_ID:
                      if len(key) > len(longest_match):
                          longest_match = key
                          print("longest match", key)
               #If no match, try getting rid of underscores
               if longest_match == "":
                   tmp_ID = tmp_ID.replace("_", "")
                   for key in lookuptable.keys():
                       if key in tmp_ID:
                           if len(key) > len(longest_match):
                               longest_match = key
                               print("longest match", key)
               #If the full passage ID is accounted for
               if len(tmp_ID)==0: 
                  continue 
               #The full passage ID is accounted for if only _ 's are left
               if len(tmp_ID.replace("_", "")) == 0:
                  continue     
               #Make list of matches
               matches.append(longest_match)

               #Get rid of current match to search rest of ID for more matches            
               tmp_ID = tmp_ID.replace(longest_match, "")
               longest_match = "" 
               print("current ID", tmp_ID)
           #If the full passage can't be parsed, return None           


           #If full passage can't be accounted for, return Nones
           if len(tmp_ID.replace("_", "")) > 1:
               annotation = ["None", "None", "None", "None", "None"]  

           else:
               #Need to get ordering of matches within input ID
               print(matches)
               match_order = []
               for match in matches:
                    match_order.append(formatted_ID.find(match))
               print(match_order)     

               #Get matches are in the same order as they appear in the ID    
               ordered_matches = [x for y, x in sorted(zip(match_order, matches))]  
               print("ordering matches...")
               print("initial order", match_order)
               print("final order", ordered_matches)
               print("done ordering")
               annotation = self.make_annotation(ordered_matches, lookuptable)
               annot_series = self.get_series(ordered_matches, lookuptable)  


           #if len(matches) == 1:
           #    annotation = lookuptable[formatted_ID]
     

           #stop logging
           sys.stdout = sys.__stdout__
           return annotation
         


    def parse_passage(self, ID, n = None):
        '''
        control function 
        '''
        ID = ID.rstrip("\n")
   
        #Store input ID
        self.original = ID

        #If there is no annotation, return default values
        if ID == "":
            return self

        #Make the ID all caps, remove special characters
        formatted_ID = self.format_ID(ID)

        #Store plain format
        self.plainformat = formatted_ID
      
        #Match a formatted ID to its composite passage types
        annotation =  self.match_known_passage(formatted_ID)
      
        #Convenience output list
        output = [ID, formatted_ID, annotation[0], annotation[1], annotation[2], annotation[3], annotation[4]] 
        self.summary = output

        #Optional retrieval of the nth passage a sequence went through
        self.get_nth_passage(n)

        return self        







