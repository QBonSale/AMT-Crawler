"""
Created on Thu Jul 3, 2014

@author: McQB
"""
import re
import os

records = []
path = os.getcwd()
flist = os.listdir(path)
flist.sort()
with open("merged.json",'w') as fout:
	for f in flist:
		if ".json" in f:
			with open(f) as fin:
				print 'Processing %s' %f
			  for line in fin:
		      m = re.search(r'"groupid": \["(.*?)"',line)
		      if m:
		     		groupid = m.group(1)
		      if groupid in records:
		      	continue
		      else:
		      	records.append(groupid)
		      	line = re.sub(r'(^\[)|(\]$)','',line)
		      	fout.write(line)
# need to manually add a pair of "[]" to the beginning and end of the merged file
