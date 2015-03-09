with open('merged_fixed.json') as fin, open('merged_valid.json','w') as fout:
   for line in fin:
		l = line.split("],")	
		nl = []
		nl.append(l[0])
		nl.append(l[3])
		nl.append(l[4])
		nl.append(l[7])
		nl.append(l[9])
		nl = "],".join(nl)
		nl += "]},\n"
		if '"expected_minutes_cost": ["0"]' not in nl:
			fout.write(nl)
# need manually delete the last comma and add a ']'
# may cause incorrect syntax by outliers.
