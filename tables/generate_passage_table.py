from __future__ import print_function


def generate_generic():
    '''
    This function generates functional chunks of passaging annotations
    '''


    siat = ["SIAT", "S"]
    mdck = ["MDCK", "M", "MK"]
    unknowncell = ["C", "X"]
    rhmk = ["RHMK", "RMK", "R", "PRHMK", "RII"]
    tmk = ["TMK"]
    #vero = ["VERO", "V"]
    vero= []
    egg = ["NC", "SPFCK", "EGG", "E", "AM", "AMNIOTIC"]
    pigcell = ["PTHYR"]
    unknown = ["UNKNOWN", "P"]


    caninecell = siat + mdck
 
    monkeycell = rhmk + tmk# + vero
    all_cells = caninecell + monkeycell + unknowncell

    all_passages = caninecell + monkeycell + egg + unknown + pigcell + unknowncell




  
    single_pass = {}
    for num in ["1","2","3","4","5","6","7", "8", "9", "10", "X", ""]:
       for passage in all_passages:
          for sep in ["", "_"]:
              #forbidden combos         
              if passage =="X" and num == "X":
                 continue
              if num == "" and sep=="_":
                 continue 
              if sep == "_" and num == "X":
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

              elif passage in pigcell:
                   specific_passage = "PTHYR"
                   general_passage = "PIGCELL"

              elif passage in unknowncell: 
                   specific_passage = "UNKNOWNCELL"
                   general_passage = "UNKNOWNCELL"

              elif passage in unknown: 
                   specific_passage = "UNKNOWN"
                   general_passage = "UNKNOWN"

              elif passage in egg: 
                   specific_passage = "EGG"
                   general_passage = "EGG" 
              
              passage_construct = "".join([passage,sep,num])
              if num == "" or num=="X":
                 num_passages="UNKNOWN"
              else:
                 num_passages=num
              annot =  [general_passage, specific_passage, num_passages]
              single_pass[passage_construct]=annot

              #single_pass.append({passage_construct:annot})

    #print(single_pass)
    print(len(single_pass))
    return single_pass



def generate_unpassaged():
    unpassaged = ["OR", "ORIGINAL", "P0", "ISOLATED_DIRECTLY_FROM_HOST_NO_PASSAGE", "CLINICAL_SPECIMEN"]
    unpass_dict = {}
    annot  = ["UNPASSAGED", "UNPASSAGED", "0"]

    for desc in unpassaged:
        unpass_dict[desc] = annot
    #print(unpass_dict)
    return unpass_dict


def generate_nonconventional():
 
   egg2 = [""]
   print("holder")


def second_pass(single):
    double_pass = {}
    for key1 in single.keys():
       for key2 in single.keys():
           for sep in ["", "_"]:
                passage_construct=key1 + sep + key2
                if single[key1][0] == single[key2][0]:
                    general_passage = single[key1][0]
                else:
                    general_passage = "_".join([single[key1][0], single[key2][0]])

                if single[key1][1] == single[key2][1]:
                    specific_passage = single[key1][1]
                else:
                    specific_passage = "_".join([single[key1][1], single[key2][1]])

                try:
                    num_passages = str(eval(single[key1][2]) + eval(single[key2][2]))               
                    if eval(num_passages) > 11:
                        continue
                except Exception as e:
                    num_passages = "_".join([single[key1][2], single[key2][2]])


                               
                annot =  [general_passage, specific_passage, num_passages]

                double_pass[passage_construct]=annot
    print(len(double_pass))
  
    return double_pass

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
    #pass2 = second_pass(pass1)
    print(pass1)
    #count=0

    #for key in pass2:
    #    if count < 150:
    #       print(key, pass2[key])
    #    count = count + 1
    #print(len(pass2))

   #final_dict = dict(j for i in full_list for j in i.items())
    #final_dict = {k: v for d in full_list for k, v in d.items()}
    #final_dict =     #print(final_dict)
    full_list = merge_dicts(pass1, unpass) 
    #print(full_list)
    with open("passage_lookup.txt", "w") as outfile:
         outfile.write(str(full_list))
    #for annotation in full_list:
        #print(annotation)
        #print(annotation.values())








