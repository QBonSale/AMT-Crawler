import datetime
import re
with open('719_822.json') as fin:
	count=0
	for line in fin:
		m = re.search(r'"time_of_expiration": \["([^"]+)',line)
		if m:
			d = m.group(1);
			d = datetime.datetime.strptime(d, "%b %d, %Y").date()
			if d <= datetime.date(2014,8,22):
				count += 1
	print"number of valid data is ",count
