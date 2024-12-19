# cutFinder

This program is used to quantify single-strand breaks detected by GLOE-Seq (DOI: 10.1016/j.molcel.2020.03.027).

## USAGE
```bash
cutFinder.py [-h] [-S samFile] [-a alignment] [-r reference] [-n name]

options:
  -h, --help            show this help message and exit
  -S, --samFile         SAM file name and location
  -a, --alignment       Strand alignment. Specify 'BS' (bottom strand) or 'TS' (top strand)
  -r, --reference       Text file with reference sequence. If -a BS, provide the top strand. If -a TS, provide the bottom strand.
                        Reference must be provided in the 5' --> 3' orientation
  -n, --name            CSV file output name (default: Sample_1)

```

| Option              | Description                                                            |
|---------------------|------------------------------------------------------------------------|
| `-h`, `--help`      | Show this help message and exit.                                       |
| `-S`, `--samFile`   | SAM file name and location.                                            |
| `-a`, `--alignment` | Strand alignment. Specify `'BS'` (bottom strand) or `'TS'` (top strand).|
| `-r`, `--reference` | Text file with reference sequence. If `-a BS`, provide the top strand. If `-a TS`, provide the bottom strand. Reference must be provided in the 5' → 3' orientation. |
| `-n`, `--name`      | CSV file output name (default: `Sample_1`).  



## Options

| Option                          | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| `-h`, `--help`                  | Show this help message and exit.                                            |
| `-S`, `--samFile`               | SAM file name and location.                                                 |
| `-a`, `--alignment`             | Strand alignment. Specify `'BS'` (bottom strand) or `'TS'` (top strand).    |
| `-r`, `--reference`             | Text file with reference sequence. If `-a BS`, provide the top strand. If `-a TS`, provide the bottom strand. Reference must be provided in the 5' → 3' orientation. |
| `-n`, `--name`                  | CSV file output name (default: `Sample_1`).                                 |




The following arguments must be provided for the script to function:
- **SAM file** for a specific strand alignment (either top or bottom strand) 
- **Strand alignment** (specify 'BS' (bottom strand) or 'TS' (top strand))
- **Reference** sequence of the opposite strand.


## REQUIREMENTS

Python v3.10.10 (pandas v2.2.3)
