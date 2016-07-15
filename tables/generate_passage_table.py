from __future__ import print_function


def generate_generic():
    siat = ["SIAT", "S"]
    mdck = ["MDCK", "M", "MK"]
    uncategorized_cell = ["C", "X"]
    rhmk = ["RHMK", "RMK", "R", "PRHMK", "RII"]
    tmk = ["TMK"]
    #vero = ["VERO", "V"]
    vero= []
    egg = ["NC", "SPFCK", "EGG", "E", "AM", "AMNIOTIC"]
    unknown = ["UNKNOWN", "P"]


    cell = siat + mdck + uncategorized_cell
 
    monkeycell = rhmk + tmk# + vero

    all_passages = cell + monkeycell + egg + unknown


    prefix = ["", "PASSAGE", "PASSAGE_DETAILS"]
    suffix = ["PASSAGE"]


  
    single_pass = []
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
              if passage in cell and num in ["6","7", "8", "9", "10"]:
                 continue
              if passage in monkeycell and num in ["7", "8", "9", "10"]:
                 continue

              if num != "" and passage == "P":
                 continue

              #annotate specific passage category
              if passage in siat:
                   specific_passage = "SIAT"

              elif passage in mdck:
                   specific_passage = "MDCK"

              elif passage in rhmk:
                   specific_passage = "RHMK"

              elif passage in tmk:
                   specific_passage = "TMK"

              elif passage in vero:
                   specific_passage = "VERO"

              elif passage in monkeycell + cell + egg + uncategorized_cell + unknown:
                   specific_passage = "NA"

              #annotate general passage category
              if passage in cell:
                   general_passage = "CELL"

              elif passage in monkeycell:
                   general_passage = "MONKEY"

              elif passage in egg:
                   general_passage = "EGG"

              elif passage in unknown:
                   general_passage = "UNKNOWN" 
              
 
              
              passage_construct = "".join([passage,sep,num])
              if num == "" or num=="X":
                 num_passages="NA"
              else:
                 num_passages=num
              annot =  [general_passage, specific_passage, num_passages]
              single_pass.append({passage_construct:annot})

    print(single_pass)
    print(len(single_pass))
    return single_pass



def generate_unpassaged():
    unpassaged = ["OR", "ORIGINAL", "P0", "ISOLATED_DIRECTLY_FROM_HOST_NO_PASSAGE"]
    unpass_list = []
    for desc in unpassed:
        unpass_list.append([desc, "UNPASSAGED", "NA", "NA"])

    print(unpass_list)
    return unpass_list


def generate_nonconventional():

   print("holder")


def second_pass(first_pass):
    double_pass = []
    for condition1_dict in first_pass:
       for condition2_dict in first_pass:
           condition1 = condition1_dict.keys()[0]
           condition2 = condition2_dict.keys()[0]

           condition1_annot = condition1_dict[condition1]
           condition2_annot = condition2_dict[condition2]
           
 

           for sep in ["", "_"]:
                passage_construct=condition1 + sep + condition2
                double_pass.append({passage_construct:[condition1_annot, condition2_annot]})
                #print(passage_construct)
    #print(double_pass)
    print(len(double_pass))




if __name__ == "__main__":
    pass1 = generate_generic()
    pass2 = second_pass(pass1)
    



