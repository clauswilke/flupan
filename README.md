flupan
=========
Python library to parse influenza passaging annotations.

### About
Influenza virus is frequency passaged prior to being sequenced. These growth conditions are recorded as shorthand passaging annotations. However, these passages are often inconsistent and not easily machine readable. This library takes individual passage history strings (Ex. M1_S3) and returns an object containing its interpretation. 

### Influenza passaging annotations 

 - Each portion of a passage history string ex. M3 refers to the type of passage and the number of rounds of passage. In the annotion M3, M refers to MDCK cells, and 3 signifies the strain was passaged 3 times. 

 - These portions are strung together into a full passage history, ex. M1_S2. This strain was passaged once in MDCK cells then twice in SIAT1 cells.  
 
 - A "/" as in S1/S1 can mean the strain was transferred to a different lab and repassaged. 

 - A "+" as in S2+3 can mean that a strain was repassaged in the previous condition after some type of break. In S2+3, the strain was initially passaged twice in SIAT1 cells and later passaged 3 more times in SIAT1 cells.



### Installation
flupan can be directly installed with [sudo permission] from pypi

```bash
pip install flupan 
```

or 

```bash
easy_install install flupan
```
Alternatively, flupan can also be installed from source. 

```bash
git clone https://github.com/clauswilke/flupan.git
cd flupan
python setup.py install
#or 
sudo python setup.py install
#or 
python setup.py install --user   
```

There are several recommended tests, which can be run using
```bash
[sudo] python setup.py test
```

There will always be passage annotations which aren't currently covered by this packaged. If you find any, please submit them under the Issues tab, and we'll add them in. Alternatively, special cases can be locally appended to the passage lookup tables (see section 'Custom passage annotations' below) : [https://github.com/clauswilke/flupan/issues](https://github.com/clauswilke/flupan/issues)


### Package usage

```python

>>import flupan

>> p = flupan.PassageParser().parse_passage("m 1") #passage annotation to be parsed
>> p.summary #A quick summary of the passage interpretation

['m 1', 'M_1', 'M1', 'CELL', 'MDCK', 'exactly', '1']

>>pp.parse_passage("e 1/m3", 4)
>>p.original #The input passage
e 1/mdck3 

>>p.plain_format #The input passage capitalized w/ special characters removed 
E_1_MDCK3

>>p.coerced_format #Standardized format where each passage is separated by an underscore
#And common passage IDs are shortened
#This step is currently useful for common annotations, but can return nonsense for parse uncommon or weirdly formatted passages
E1_M3

>>p.ordered_passages #Each round of passaging in a list
["E1", "M3"]

>>p.general_passages #The broad categories of the passage types
["EGG", "CANINECELL"]

>>p.specific_passages #More specific categories of the passage types (if known)
["EGG", "MDCK"]

>>p.total_passages  #The total rounds of passaging, if it can be determined
4

>>p.min_passages # At least this many rounds occurred (useful for passage IDs without numbers of rounds annotated)
4

>>p.passage_series #An ordered list of each round of passaging
[[1, 'EGG'], [2,'MDCK'], [3,'MDCK'], [4, 'MDCK']]


>>p.summary  #A quick listing of passage features
['e 1/mdck3', 'E_1_MDCK3', 'E1_M3, 'EGG+CANINECELL', 'EGG + MDCK', 'exactly', '4']
# 1. original input, 2. standardized input, 3. coerced format input, 4. general passage type(s), 5. specific passage type(s), 6. qualifier for number of passages, 7. number of passages


```

### Command line usage

$ translate_passage  

usage: translate_passage [-h] [-f INFILE] [-p PASSAGE] [-o OUTFILE]

A command line tool to parse influenza passaging annotations

optional arguments:
  -h, --help            show this help message and exit
  -f INFILE, --infile INFILE
                        A files of passage IDs, ex M1 S4, one per line
  -p PASSAGE, --passage PASSAGE
                        A single passage ID to be parsed, ex. E4
  -o OUTFILE, --outfile OUTFILE
                        An outfile to store output

ex.
```bash
$ translate_passage -p 'm2 + rhmk1'
m2 + rhmk1,M2_RHMK1,M2_R1,CANINECELL+MONKEYCELL,MDCK+RHMK,exactly,


```

### Passage ID interpretation

A single number that follows a previous passage type is given the identity of the previous passage type
Ex. Mdck3 + 2 is interpreted to have gone through 5 MDCK passages


X following a passage type, ex. MX means an unknown number of passages. X alone ex. X2 means an unknown cell culture. 

### Passage assignments


    #### CANINECELL passages
         
    - SIAT passage = ["SIAT", "S", "MDCKSIAT"] 
    - MDCK passage = ["MDCK", "M", "MK"]
    - UNKNOWNCELL passage = ["C", "X"]
    #### MONKEYCELL passages
    - RHMK = ["RHMK", "RMK", "R", "PRHMK", "RII"]
    - TMK = ["TMK"]
    - VERO = ["VERO", "V"]
    #### EGG passages
    - EGG  = ["AL", "ALLANTOIC", "EGG", "E", "AM", "AMNIOTIC"]
    #### PIGCELL passages
    - PTHYR = ["PTHYR"]
    #### CHICKCELL passages
    -chickcell = ["SPFCK", "CK", "PCK"]
    #### UNKNOWN passages
    - unknown = ["UNKNOWN", "P", "", "NC"]
    #### R-MIX passage
    - RMIX = ["R_MIX", "RMIX"]
    #### MINKCELL passage
    - MINKCELL = ["MV_1_LU", "MV1_LU", "MV1_LUNG"]

    CANINECELL = SIAT + MDCK

    MONKEYCELL = RHMK + TMK + VERO

    ALL_CELLS = CANINECELL + MONKEYCELL + UNKNOWNCELL + CHICKCELL + RMIX + MINKCELL

    ALL_PASSAGES = CANINECELL + MONKEYCELL + EGG + UNKNOWN + PIGCELL + UNKNOWNCELL + CHICKCELL + RMIX +  MINKCELL

### Custom passage annotations

If a passage ID hasn't been observed in the flupan database or can't be parsed, it is given empty annotations. 

There are two ways to add in custom annotations:

 1. Custom annotations can be added to nonstandard_passages_input.txt followed by running generate_passage_table.py. This will add append custom annotations to passage_lookup.txt 

 2. Add directly to passage_lookup.txt. Warning: Running generate_passage_table.py will overwrite any changes made directly to passage_lookup.txt.  

 3. Custom passage categories can be added to the generate_passage_table.py script to generate passage annotations from scratch

Custom passage annotation should be written 1 per line in the form:

passage,general_type, specific_type,number_of_rounds
ex. MDCK3,CANINECELL,MDCK,3 


### Tables
Tables use in flupan are stored in src/tables

passage_lookup.txt: lookup table generated by running generate_passage_table.py. Concatenation of generated passage annotations, nonstandard_passages_input.txt, and unknown_passages_input.txt annotations. Required by flupan. 

nonstandard_passages_input.txt: Table of custom passage annotations

unknown_passages_input.txt: Table of uninterpretable passage IDs.

coerce_format.txt: Table of passage key words and simplified versions ex. SIAT S. Required by flupan











