# flupan
Python library to parse influenza passaging annotations

# Installation

from within the flupan directory:

```python
python setup.py install 
```



# Usage
Flupan 






Example 
```python

>>import flupan

>>pp = flupan.PassageParser()
>>pp.parse_passage("m 1")

['m 1', 'M_1', 'M1', 'CELL', 'MDCK', 'exactly', '1']

>>pp.parse_passage("e 1/m3")

['e 1/m3 + 2', 'E_1_M3_2', 'E1_M3_2, 'EGG+CANINECELL', 'EGG + MDCK', 'exactly', '6']


```


#Passage annotation interpretation

A single number that follows a previous passage type is given the identity of the previous passage type






