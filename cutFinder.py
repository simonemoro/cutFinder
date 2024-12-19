import sys
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-S", "--samFile", type=str, help="SAM file name and location")
parser.add_argument("-a", "--alignment", type=str, help="Strand alignment. Specify 'BS' (bottom strand) or 'TS' (top strand)")
parser.add_argument("-r", "--reference", type=str, help="Text file with reference sequence. If -a BS, provide the top strand. If -a TS, provide the bottom strand. Reference must be provided in the 5' --> 3' orientation")
parser.add_argument("-n", "--name", type=str, help="CSV file output name (default: Sample_1)")
args = parser.parse_args()

if args.samFile == None:
	print('Error: No SAM file provided. The field -S must be specified...')
        sys.exit()

samFile = args.samFile

if args.alignment == None:
        print('Error: No alignment type provided. The field -a must be specified...')
        sys.exit()

alignment = args.alignment

if args.reference == None:
        print('Error: No reference file provided. The field -r must be specified...')
        sys.exit()

ref = args.reference
reference = open(ref).read().strip()

if(args.name == None):
    name = 'Sample_1'
else:
    name = args.name


############################################################################################################
#################################### FOR BS ALIGNMENTS

if alignment == 'BS':
	output = name+'_freqs_TOP.csv'
	nucleotides_top = list(reference)
	df_top = pd.DataFrame(nucleotides_top, columns=['Nucleotide'])
	df_top['Frequency'] = 0

	with open(samFile, "r") as sam_file:
		for line in sam_file:
			if line.startswith("@"):
				continue
			columns = line.strip().split("\t")
			if columns[1] == '0' or columns[1] == '256':
				start_position = int(columns[3]) - len(reference)
				position_in_top = len(reference) - start_position
				df_top.at[position_in_top, 'Frequency'] += 1

	df_top.insert(0, 'Position', range(1, len(df_top) + 1))
	df_top.to_csv(output, index=False)


############################################################################################################
#################################### FOR TS ALIGNMENTS
if alignment == 'TS':
	output = name+'_freqs_BOTTOM.csv'
	nucleotides_bottom = list(reference[::-1])
	df_bottom = pd.DataFrame(nucleotides_bottom, columns=['Nucleotide'])
	df_bottom['Frequency'] = 0

	with open(samFile, "r") as sam_file:
		for line in sam_file:
			if line.startswith("@"):
				continue
			columns = line.strip().split("\t")
			if columns[1] == '0' or columns[1] == '256':
				start_position = int(columns[3]) - len(reference)
				position_in_bottom = start_position -1
				df_bottom.at[position_in_bottom, 'Frequency'] += 1

	df_bottom.insert(0, 'Position', range(1, len(df_bottom) + 1))
	df_bottom.to_csv(output, index=False)
