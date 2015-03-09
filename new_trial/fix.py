import re
with open('merged.json') as fin, open('merged_fixed.json','w') as fout:
   for line in fin:
   	line = re.sub(r'("collected_time": )([^,]+)',r'\1[\2]',line)
   	fout.write(line)
# might need to manually check for outliers including 2015.
