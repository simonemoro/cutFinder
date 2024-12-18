# cutFinder

This program is used to quantify single-strand breaks detected by GLOE-Seq. 
(DOI: 10.1016/j.molcel.2020.03.027) 

## USAGE

cutFinder.py [-h] [-S SAMFILE] [-a ALIGNMENT] [-r REFERENCE] [-n NAME]


The following arguments must be provided for the script to function:
- **SAM file** for a specific strand alignment (either top or bottom strand) 
- **Strand alignment** (specify 'BS' (bottom strand) or 'TS' (top strand))
- **Reference** sequence of the opposite strand


## REQUIREMENTS

Python v3.10.10 (pandas v2.2.3)
