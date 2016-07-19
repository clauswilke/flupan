from __future__ import print_function


def generate_generic():
    '''
    This function generates functional chunks of passaging annotations
    '''


    siat = ["SIAT", "S", "MDCKSIAT"]
    #Check source on MK, should b monkey?
    mdck = ["MDCK", "M", "MK"]
    unknowncell = ["C", "X"]
    rhmk = ["RHMK", "RMK", "R", "PRHMK", "RII"]
    tmk = ["TMK"]
    vero = ["VERO", "V"]
    #check source on NC meaning eggs
    egg = ["NC", "AL", "ALLANTOIC", "EGG", "E", "AM", "AMNIOTIC"]
    pigcell = ["PTHYR"]
    chickcell = ["SPFCK", "CK", "PCK"]
    unknown = ["UNKNOWN", "P"]
    only_number = [""]
    rmix = ["R_MIX", "RMIX"]

    minkcell = ["MV_1_LU", "MV1_LU", "MV1_LUNG"]

    caninecell = siat + mdck
 
    monkeycell = rhmk + tmk + vero
    all_cells = caninecell + monkeycell + unknowncell + chickcell + rmix + minkcell

    all_passages = caninecell + monkeycell + egg + unknown + pigcell + unknowncell + chickcell + rmix + only_number + minkcell




  
    single_pass = {}
    for num in ["0","1","2","3","4","5","6","7", "8", "9", "10", "X", ""]:
       for passage in all_passages:
          for sep in ["", "_"]:
              #forbidden combos         
              if passage =="X" and num == "X":
                 continue
              if num == "" and sep=="_":
                 continue 
              if num== "" and sep == "" and passage =="":
                 continue
              if sep == "_" and num == "X":
                 continue

              if passage=="" and num=="":
                 continue
              #if passage in all_cells and num in ["6","7", "8", "9", "10"]:
              #   continue

              #if num != "" and passage == "P":
              #   continue

              #annotate specific passage category
              specific_passage = ""
              general_passage= ""
              if passage in caninecell:

                  if passage in siat:
                       specific_passage = "SIAT"


                  elif passage in mdck:
                       specific_passage = "MDCK"


                  general_passage = "CANINECELL"
              elif passage in monkeycell:

                  if passage in rhmk:
                      specific_passage = "RHMK"

                  elif passage in tmk:
                      specific_passage = "TMK"

                  elif passage in vero:
                      specific_passage = "VERO"
                  general_passage = "MONKEYCELL"

              elif passage in minkcell:
                   specific_passage = "MV1LU"
                   general_passage = "MINKCELL"


              elif passage in chickcell:
                   specific_passage = "CK"
                   general_passage = "CHICKCELL"

              elif passage in rmix:
                   specific_passage = "RMIX"
                   general_passage = "RMIX"

              elif passage in unknowncell: 
                   specific_passage = "UNKNOWNCELL"
                   general_passage = "UNKNOWNCELL"

              elif passage in unknown: 
                   specific_passage = "UNKNOWN"
                   general_passage = "UNKNOWN"

              elif passage in egg: 
                   specific_passage = "EGG"
                   general_passage = "EGG" 
              
              elif passage in only_number:
                   specific_passage = "None"
                   general_passage = "None" 

              passage_construct = "".join([passage,sep,num])
              if num == "" or num=="X":
                 num_passages=None
              else:
                 num_passages=num
              annot =  [general_passage, specific_passage, num_passages]
              single_pass[passage_construct]=annot

              #single_pass.append({passage_construct:annot})

    #print(single_pass)
    print(len(single_pass))
    return single_pass



def generate_unpassaged():
    unpassaged = ["ORIGINAL_SPECIMEN_UNCULTURED_IN_VTM","OR", "ORIGINAL", "P0", "ISOLATED_DIRECTLY_FROM_HOST_NO", "CLINICAL_SPECIMEN", "NO", "LUNG_1", "LUNG"]
    unpass_dict = {}
    annot  = ["UNPASSAGED", "UNPASSAGED", "0"]

    for desc in unpassaged:
        unpass_dict[desc] = annot
    #print(unpass_dict)
    return unpass_dict


def generate_nonconventional():

    uncon_dict = {}
 
    with open("nonstandard_passages.txt", "r") as nonstandard:
        for line in nonstandard.readlines():
            i = line.rstrip("\n").split(",")
            uncon_dict[i[0]] = i[1:]
 

    #for i in ["1","2","3","4", "5"]:
    #    annot =["CANINECELL", "MDCK", i]    
        #passage = "P" + i + "_MDCK"
        #uncon_dict[passage] = annot 


    #annot =["CANINECELL", "MDCK", "X"]    
    #uncon_dict["ND_MDCK"] = annot 

    #annot =["EGG", "EGG", "X"]    
    #uncon_dict["EGG_LOT_FT2187"] = annot 


    with open("unknown_passages.txt", "r") as completely_unknown:
        annot = ["None", "None", "None"]
        for passage in completely_unknown.readlines():
            uncon_dict[passage.rstrip("\n")] = annot




    #print(unpass_dict)
    return uncon_dict


def merge_dicts(*dict_args):
   '''
   from stackoverflow.com/a/26853961
   given any number of dicts, shallow copy and
   merge into a new dict
   '''
   result = {}
   for dictionary in dict_args:
      result.update(dictionary)
   return result





if __name__ == "__main__":
    pass1 = generate_generic()
    #pass2 = second_pass(pass1)
    unpass = generate_unpassaged()
    uncon = generate_nonconventional()
    #pass2 = second_pass(pass1)
    print(pass1)
    print(uncon)
    full_list = merge_dicts(pass1, unpass, uncon) 
    print(full_list)
    for f in full_list.keys():
       print(f, full_list[f])

    with open("passage_lookup.txt", "w") as outfile:
         outfile.write(str(full_list))
    #for annotation in full_list:
        #print(annotation)
        #print(annotation.values())








