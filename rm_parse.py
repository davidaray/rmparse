import pandas as pd
import os

##Initialize a list
RM_OUT_LIST = []

##Open the file as a variable, RM_IN
with open('aVan_rm.out') as RM_IN:
##Skip the first three lines
	for X in range(3):
		HEADER = RM_IN.readline()
##Read in each line, remove 'kimura=' from each line, and add each line to the list you initialized.
	for LINE in RM_IN:
		LINE = LINE.replace('kimura=', '').replace('/', '\t')
		RM_OUT_LIST.append(LINE)

##Create a tmp file from the new list for use as an dataframe in pandas
NEWFILE = open('tmp.bed', 'w')
for LINE in RM_OUT_LIST:
        NEWFILE.write(LINE)
NEWFILE.close()

##Create a pandas dataframe from the tmp file, adding headers as you do so.
RM_OUT_ARRAY = pd.read_table('tmp.bed', names=['A', 'B', 'C', 'D', 'chrom', 'start', 'stop', 'E', 'strand', 'name', 'class', 'family', 'F', 'G', 'H', 'I', 'diverge'])

##Delete the tmp file
os.remove('tmp.bed')

##Calculate size, adding column to the end
RM_OUT_ARRAY['size'] = RM_OUT_ARRAY['stop'].subtract(RM_OUT_ARRAY['start'] -1)

##Rearrange the headers as you want
RM_OUT_ARRAY = RM_OUT_ARRAY[['chrom', 'start', 'stop', 'name', 'class', 'family', 'strand', 'size', 'diverge']]
#print(RM_OUT_ARRAY)

##Replace 'C' with '-' in the 'strand' column and 'kimura=' with nothing in the 'diverge' column. 
RM_OUT_ARRAY.strand = RM_OUT_ARRAY.strand.replace({'C':'-'})
#RM_OUT_ARRAY.diverge = RM_OUT_ARRAY.diverge.replace({'kimura=':''})

##Write the dataframe to a file, leaving out the headers and row names.
RM_OUT_ARRAY.to_csv('aVan_fix.bed', sep='\t', header=False, index=False)

CLUSTERED = RM_OUT_ARRAY.sort_values(['class'])
SPLITLIST = []
SPLITLIST = RM_OUT_ARRAY['class'].unique()
#print(SPLITLIST)
for SPLITVALUE in SPLITLIST:
	CLUSTEREDW = CLUSTERED[CLUSTERED['class']==SPLITVALUE]
	CLUSTEREDW.to_csv(SPLITVALUE + '_fix.bed', sep='\t', header=False, index=False)


