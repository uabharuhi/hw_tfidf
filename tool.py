import re

#read txt and extract content column
def read_tweet_content(filename):
	#$ begin of line,only in file can search $ end of file
	#'^[0-9]+[\t]+(.+)[\t]+[0-9]+$'  wrong --> '[0-9]+[\t]+(.+)[\t]+[0-9]+'  correct
	pattern = '[0-9]+[\t]+(.+)[\t]+-?[0-9]+' 
	with open(filename) as f:
		content_list = []
		for line_n,line in enumerate(f):
			if line_n == 0:
				print('has zero')
				continue
			p = re.compile(pattern)
			m = p.search(line)
			print(line)
			content = m.group(1)
			content_list.append(content)
	return content_list



