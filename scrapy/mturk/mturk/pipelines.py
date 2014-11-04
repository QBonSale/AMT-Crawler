# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class MturkPipeline(object):

    def process_item(self, item, spider):
    	s1 = "".join(item['title'])
    	s2 = "".join(item['description'])
    	s = s1 + s2
	m = re.search(r"(\d)+( |-)(H|h)ours?",s)
    	if m:
		t=60*int(m.group(1))
    		m = re.search(r"(\d+)( )+((M|m)in(utes?)?)", s)
		if m:
			t+=int(m.group(1))
		t=str(t)
    	else:
    		m = re.search(r"((\d|-|or| )+)( |-)((M|m)in(utes?)?)", s)
		if m:
			t=m.group(1)
		else:
			t='0'
    	item['expected_minutes_cost'] = [t]
    	return item

