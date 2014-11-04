with open('data/merged_simplified.json') as fin:
	count=0
	for line in fin:
		if '"expected_minutes_cost": ["0"]' not in line:
			count+=1
	print"number of valid data is ",count
