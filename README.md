## Problem 1: Parsing Sequence Strings

### Function a. `str` sequence -> `int` length of sequence in nucleotides

Basic idea: parse string into list of `Nucelotide` objects, detecting irregularities. Length is merely the length of the previously-parsed list. 

Implemented in `sequence_parser.sequence_str_to_len`. 


### Function b. `str` sequence -> `str` sequence type (∈ {`chimera`, `mod RNA`, `vanilla RNA`})

Idea: using parsed-string, go through it to detect irregularities. 

Implemented in `sequence_parser.sequence_str_to_product_type`. 

