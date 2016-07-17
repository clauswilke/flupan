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
    
        record_strip = ID.replace("-", "")
        record_strip = re.sub('[^A-Z0-9\|]', '_', record_strip)
        record_strip = re.sub('PASSAGE_DETAILS_|_AND_|ST_PASSAGE|ND_PASSAGE|PASSAGING|_PASSAGE|_PASSAGES|_PASSAGE_|_PASSAGES_|_CELLS', '', record_strip)
        record_strip = record_strip.replace("__", "_")
        record_strip = re.sub('01', '1', record_strip)
        if len(record_strip) > 0:
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

    def reformat_annotation(self, annotation_list):

       reformatted_annotation_list = []
       for annot in annotation_list:
          reformatted_annotation_list.append(annot.replace("_", "")) 
        
          print(annot, reformatted_annotation_list)
       reformatted_annotation = "_".join(reformatted_annotation_list)
       return reformatted_annotation



    def make_annotation(self, annotation_list, lookuptable):
       '''
       This function take a list of passage IDs found in 
       the full passage ID, and then consolidates their annotations
       THIS would be the place to make a consistent format
       '''
       general_passage = ""
       specific_passage = ""
       num_passages= ""
       num_condition = "exactly"
 
       for passage in annotation_list:
            annot = lookuptable[passage]
            print(passage, annot)
            
            tmp_passage = passage.replace("_", "")
            #Consolidate the general passage info
            if general_passage == "":
                general_passage = annot[0]
            elif annot[0] in general_passage:
                general_passage = general_passage
            elif tmp_passage in ["1","2","3","4","5","6","7","9","10","11","12"]:
                general_passage = general_passage
            else:
                general_passage = "+".join([general_passage, annot[0]])
            #Consolidate the specific passage info
            if specific_passage == "":
                specific_passage = annot[1]
            elif annot[1] in specific_passage:
                specific_passage = specific_passage
            elif tmp_passage in ["1","2","3","4","5","6","7","9","10","11","12"]:
                specific_passage = specific_passage
            else:
                specific_passage = "+".join([specific_passage, annot[1]])
       
            #Add up numbers of passages
            #Some annotations don't have numbers, so can't be added
            if num_passages == "":
                try:
                   num_passages = str(eval(annot[2]))

                except:
                   #indeterminate passages happen at least once
                   num_passages = "1"
                   num_condition = "atleast"                
            else:
                try:
                   num_passages = str(eval(num_passages) + eval(annot[2])) 

                except:
                   num_condition = "atleast"                
                   num_passages = str(eval(num_passages) + 1) 

       reformatted_annotation = self.reformat_annotation(annotation_list)

       annot =  [reformatted_annotation, general_passage, specific_passage, num_condition, num_passages]
       print(annot)
       print("end function")
       return(annot)  


    def match_known_passage(self, formatted_ID):
        '''
        This function looks for known passage annotations within 
        full passage identifiers
        If the full passage can't be accounted for,
        the identifier is sent to regular expressions
        '''

        with open("../tables/passage_lookup.txt", "r") as lookuptable_txt:
           lookuptable = eval(lookuptable_txt.read())
           tmp_ID = formatted_ID
           prevlength = 100
           longest_match = ""
           matches = []
           #check for up to 5 passage rounds
           for i in [1,2,3,4, 5]:
               #while "__" in tmp_ID:
               #    tmp_ID = tmp_ID.replace("__", "_")
               for key in lookuptable.keys():
                  if key in tmp_ID:
                      if len(key) > len(longest_match):
                          longest_match = key
                          print("longest", key)
               if longest_match == "":
                   tmp_ID = tmp_ID.replace("_", "")
                   for key in lookuptable.keys():
                       if key in tmp_ID:
                           if len(key) > len(longest_match):
                               longest_match = key
                               print("longest", key)
               if len(tmp_ID)==0: 
                  continue 
               if len(tmp_ID.replace("_", "")) == 0:
                  continue     

               matches.append(longest_match)
               tmp_ID = tmp_ID.replace(longest_match, "")
               prevlength = len(tmp_ID)
               longest_match = "" 
               print(tmp_ID)
           #If the full passage can't be parsed, return None           
           if len(tmp_ID.replace("_", "")) > 1:
               annotation = ["None", "None", "None", "None", "None"]  
           else:
               #Need to get ordering of matches
               print(matches)
               match_order = []
               for match in matches:
                    match_order.append(formatted_ID.find(match))
               print(match_order)         
               ordered_matches = [x for y, x in sorted(zip(match_order, matches))]  
               print("ordering...")
               print(match_order)
               print(ordered_matches)
               print("done ordering")
               annotation = self.make_annotation(ordered_matches, lookuptable)

           #if len(matches) == 1:
           #    annotation = lookuptable[formatted_ID]
     



           #print(lookuptable)
           return annotation
         


    def regular_exp_identification(self, formatted_ID):
        print("meh")

    def parse_passage(self, ID):
        '''
        control function 
        '''
        ID = ID.rstrip("\n")
        formatted_ID = self.format_ID(ID)
        annotation =  self.match_known_passage(formatted_ID)      
        output = [ID, formatted_ID, annotation[0], annotation[1], annotation[2], annotation[3], annotation[4]] 
        return output







