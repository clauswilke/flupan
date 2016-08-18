flupan
=========
Python library to parse influenza passaging annotations.

# About
Influenza virus is frequency passaged prior to being sequenced. These growth conditions are recorded as shorthand passaging annotations. However, these passages are often inconsistent, and not easily machine readable. This library takes individual passage annotation strings, (Ex. M1_S3), and returns an object containing its interpretation. 


# Installation
Flupan can be directly installed with [sudo permission] from pypi

```bash
pip install flupan 
```

or 

```bash
easy_install install flupan
```

Alternatively, Flupan can also be installed from source. 

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

There will always be passage annotations which aren't currently covered by this packaged. If you find any, please submit them under the Issues tab, and we'll add them in.Alternatively, special cases can be locally appended to the /tables .txt files. : [https://github.com/clauswilke/flupan/issues](https://github.com/clauswilke/flupan/issues)


# Package usage

```python

>>from flupan import passage_interpreter

>> pp = passage_interpreter.PassageParser()
>> p = pp.parse_passage("m 1") #passage annotation to be parsed
>> p.summary #A quick summary of the passage interpretation

['m 1', 'M_1', 'M1', 'CELL', 'MDCK', 'exactly', '1']

>>pp.parse_passage("e 1/m3", 4)
>>p.original #The input passage
e 1/mdck3 

>>p.plainformat #The input passage capitalized w/ special characters removed 
E_1_MDCK3

>>p.coercedformat #Standardized format where each passage is separated by an underscore
#And common passage IDs are shortened
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

# Command line usage



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



# Passage annotation interpretation

A single number that follows a previous passage type is given the identity of the previous passage type
Ex. Mdck3 + 2 is interpreted to have gone through 5 MDCK passages


If a passage annotation hasn't been observed in the flupan database or can't be parsed, it is given "None" values. 


## Passage assignments


    #### CANINECELL passages
         
    - SIAT passage = ["SIAT", "S", "MDCKSIAT"] 

    - MDCK passage = ["MDCK", "M", "MK"]
    - UNKNOWNCELL passage = ["C", "X"]
    #### MONKEYCELL passages
    - RHMK = ["RHMK", "RMK", "R", "PRHMK", "RII"]
    - TMK = ["TMK"]
    - VERO = ["VERO", "V"]
    ####check source on NC meaning eggs
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








