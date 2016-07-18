# flupan
Python library to parse influenza passaging annotations

# Installation

From within the flupan directory:

```python
python setup.py install 
```

# Package usage

Example 

```python

>>import flupan

>>pp = flupan.PassageParser()
>>pp.parse_passage("m 1")

['m 1', 'M_1', 'M1', 'CELL', 'MDCK', 'exactly', '1']

>>pp.parse_passage("e 1/m3")

['e 1/m3 + 2', 'E_1_M3_2', 'E1_M3_2, 'EGG+CANINECELL', 'EGG + MDCK', 'exactly', '6']

# 1. original input, 2. standardized input, 3. standardized passage, 4. general passage type(s), 5. specific passage type(s), 6. qualifier for number of passages, 7. number of passages
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

# Passage annotation interpretation

A single number that follows a previous passage type is given the identity of the previous passage type

If a passage annotation hasn't been observed in the flupan database, it is given "None" values. 


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
    - EGG  = ["NC", "AL", "ALLANTOIC", "EGG", "E", "AM", "AMNIOTIC"]
    #### PIGCELL passages
    - PTHYR = ["PTHYR"]
    #### CHICKCELL passages
    -chickcell = ["SPFCK", "CK", "PCK"]
    #### UNKNOWN passages
    - unknown = ["UNKNOWN", "P"]
    #### R-MIX passage
    - RMIX = ["R_MIX", "RMIX"]
    #### MINKCELL passage
    - MINKCELL = ["MV_1_LU", "MV1_LU", "MV1_LUNG"]

    CANINECELL = SIAT + MDCK

    MONKEYCELL = RHMK + TMK + VERO

    ALL_CELLS = CANINECELL + MONKEYCELL + UNKNOWNCELL + CHICKCELL + RMIX + MINKCELL

    ALL_PASSAGES = CANINECELL + MONKEYCELL + EGG + UNKNOWN + PIGCELL + UNKNOWNCELL + CHICKCELL + RMIX + ONLY_NUMBER + MINKCELL








