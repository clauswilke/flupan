# flupan
Python library to parse influenza passaging annotations

# Installation



# Usage







Example usage
```python

>>import flupan

>>pp = flupan.PassageParser()
>>pp.parse_passage("m 1")

['m 1', 'M_1', 'CELL', 'MDCK', '1']

```


A single number that follows a previous passage type is given the identity of the previous passage type






