RM_OUT_LIST = []

with open('aVan_rm.out') as RM_IN:
	for LINE in RM_IN:
		LINE.replace('kimura=', '')
		RM_OUT.append(LINE)

NEWFILE = open('aVan_rm_fix.bed', 'w')
for LINE in RM_OUT:
	NEWFILE.write(LINE)
NEWFILE.close()
