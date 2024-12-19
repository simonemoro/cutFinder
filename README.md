# cutFinder

This program is used to quantify single-strand breaks detected by GLOE-Seq (DOI: 10.1016/j.molcel.2020.03.027).

## USAGE
```bash
cutFinder.py [-h] [-S SAMFILE] [-a ALIGNMENT] [-r REFERENCE] [-n NAME]

options:
  -h, --help            show this help message and exit
  -S SAMFILE, --samFile SAMFILE
                        SAM file name and location
  -a ALIGNMENT, --alignment ALIGNMENT
                        Strand alignment. Specify 'BS' (bottom strand) or 'TS' (top strand)
  -r REFERENCE, --reference REFERENCE
                        Text file with reference sequence. If -a BS, provide the top strand. If -a TS, provide the bottom strand
  -n NAME, --name NAME  CSV file output name (default: Sample_1)

```

The following arguments must be provided for the script to function:
- **SAM file** for a specific strand alignment (either top or bottom strand) 
- **Strand alignment** (specify 'BS' (bottom strand) or 'TS' (top strand))
- **Reference** sequence of the opposite strand. Reference must be provided in the 5' --> 3' orientation


## REQUIREMENTS

Python v3.10.10 (pandas v2.2.3)
