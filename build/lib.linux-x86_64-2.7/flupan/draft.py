Columns for passaging annotations

passaged? transfer? single serial gen_cell cell_type rh_cell rh_cell_type species total_passages 


Should this be an r package?
Or a python package?

Lookup_table
ID type round total_rounds transfer passaged?

rhMK2_SIAT1 monkey 1 3 TRUE TRUE
rhmk2_siat1 monkey 2 3 TRUE TRUE
rhmk2_siat1 SIAT1 3 3 TRUE TRUE
unpassaged unpassaged 0 0 FALSE FALSE

class passages():
```
```


def select_passages(self, FASTA, desired_passage, max_desired_total_rounds=NA, exclude_transfer=FALSE, exclude_multi_condition=TRUE):
```
Takes seqrecords with passage annotations
Returns seqrecords with desired parameters
desired_passage : The specific passage condition desired

```
    assert type(FASTA)==seqrecord
    assert desired_passage in ["siat", "nonsiat, "cell", "unpassaged", "egg", "monkey", "rhmk", "vero", "passaged", "unclassified"]
    assert type(transfer)==bool
    assert type(exclude=multi_condition)==bool
    if max_rounds != NA:
        assert type(max_rounds)==integer


def exclude_passages(self, FASTA, unwanted_passage, exclude_total_rounds, exclude_transfer=FALSE):
    assert type(FASTA)==seqrecord
    assert unwanted_passage in ["siat", "nonsiat, "cell", "unpassaged", "egg", "monkey", "rhmk", "vero", "passaged", "unclassified"]
    assert type(transfer)==bool
    if unwanted_rounds != NA:
        assert type(unwanted_rounds)==integer


CL
    


check it's a FASTA
check each arg
      


def Specialized_parsing():
```
helper_function using regular expression to 
```





get_passaging_distribution(by=species, rounds)
'''
returns a dictionary of counts of each passage type 
'''



```

```




