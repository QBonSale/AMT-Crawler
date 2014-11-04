import re
import os

path = os.getcwd()
for f in os.listdir(path):
  if os.path.isfile(os.path.join(path,f))==True:
  	t = re.search(r'(\d\d-\d\d)_(\d\d-\d\d)',f)
  	if t:
	  	newname = t.group(2) + "_" + t.group(1) + "_2014.json"
	  	os.rename(os.path.join(path,f),os.path.join(path,newname))
